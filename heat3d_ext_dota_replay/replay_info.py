"""
What a Dota 2 replay (.dem) says about its match, read without converting it.

A Source 2 demo starts with its magic (`PBDEMS2\\0`) and two little-endian
int32s: the byte offset of the DEM_FileInfo frame near the end of the file, and
that of the spawn groups. The first frame is DEM_FileHeader. Both frames are
read here and nothing else, so this stays fast on a replay of any length:

* DEM_FileHeader: the game's build (`game_version`);
* DEM_FileInfo: the demo's length (`duration_s`) and the game info the server
  writes when the match ends - match id, game mode, winner, the end time, the
  team tags and ids, and each player's name, hero, team and Steam id.

A frame is a varint command (bit 64 set: Snappy-compressed), a varint tick, a
varint size and the protobuf; the protobuf classes are Valve's, as gem ships
them. A replay still being written, or cut short, has no file info yet: its
match fields come back empty.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .dota_replay import DEMO_MAGIC, RADIANT, TEAMS, FormatError, Missing, _id_from_name, hero_display

#: EDemoCommands: the two frames read here, and the compression flag.
DEM_FILE_HEADER, DEM_FILE_INFO, DEM_IS_COMPRESSED = 1, 2, 64
#: The fixed header: magic, then the file info's and the spawn groups' offsets.
HEAD = len(DEMO_MAGIC) + 8
#: The game modes as the game names them (DOTA_GameMode); others by their enum name.
MODES = {
    "AP": "All Pick", "CM": "Captains Mode", "RD": "Random Draft", "SD": "Single Draft", "AR": "All Random",
    "INTRO": "Intro", "HW": "Diretide", "REVERSE_CM": "Reverse Captains Mode", "XMAS": "Frostivus",
    "TUTORIAL": "Tutorial", "MO": "Mid Only", "LP": "Least Played", "POOL1": "Limited Heroes", "FH": "Compendium",
    "CUSTOM": "Custom Game", "CD": "Captains Draft", "BD": "Balanced Draft", "ABILITY_DRAFT": "Ability Draft",
    "EVENT": "Event", "ARDM": "All Random Deathmatch", "1V1MID": "1v1 Solo Mid", "ALL_DRAFT": "All Pick",
    "TURBO": "Turbo", "MUTATION": "Mutation", "COACHES_CHALLENGE": "Coaches Challenge",
}  # fmt: skip


def _varint(buf: bytes, at: int) -> tuple[int, int]:
    x = s = 0
    while True:
        if at >= len(buf):
            raise FormatError("the replay ends inside a frame header")
        b = buf[at]
        at += 1
        x |= (b & 0x7F) << s
        s += 7
        if not b & 0x80 or s >= 35:
            return x, at


def _frame(f: Any, at: int, size: int) -> tuple[int, bytes] | None:
    """The frame at byte `at`: its command (compression flag cleared) and its payload, uncompressed."""
    if at < HEAD or at >= size:
        return None
    f.seek(at)
    head = f.read(15)
    command, i = _varint(head, 0)
    _tick, i = _varint(head, i)
    length, i = _varint(head, i)
    if at + i + length > size:
        return None
    f.seek(at + i)
    data = f.read(length)
    if command & DEM_IS_COMPRESSED:
        try:
            import snappy
        except ImportError as e:
            raise Missing("pip install python-snappy (compressed replay frames)") from e
        try:
            data = snappy.decompress(data)
        except Exception as e:  # noqa: BLE001 - a frame that does not unpack is not one this reader knows
            raise FormatError("a compressed frame does not unpack") from e
    return command & ~DEM_IS_COMPRESSED, data


def _parse(cls: Any, data: bytes) -> Any:
    m = cls()
    try:
        m.ParseFromString(data)
    except Exception as e:  # noqa: BLE001 - protobuf's DecodeError
        raise FormatError(f"its {cls.__name__} does not decode") from e
    return m


def _mode(number: int) -> str | None:
    if not number:
        return None
    try:
        from gem.proto.dota_shared_enums_pb2 import DOTA_GameMode

        name = DOTA_GameMode.Name(number).removeprefix("DOTA_GAMEMODE_")
    except Exception:  # noqa: BLE001 - a mode newer than the definitions
        return str(number)
    return MODES.get(name, name.replace("_", " ").title())


def info(path: Path) -> dict[str, Any]:
    """
    The match as the replay's header and file info describe it. Keys are None
    (or empty) where the replay does not say. Raises `FormatError` (a
    ValueError) for a file that is not a Dota 2 replay.
    """
    path = Path(path)
    try:
        from gem.proto import demo_pb2
    except ImportError as e:
        raise Missing("pip install gem-dota (the Dota 2 replay parser, MIT)") from e
    size = path.stat().st_size
    with path.open("rb") as f:
        head = f.read(HEAD)
        if len(head) < HEAD or head[: len(DEMO_MAGIC)] != DEMO_MAGIC:
            raise FormatError(f"{path.name} is not a Dota 2 replay (a .dem.bz2 must be unpacked first)")
        info_at = int.from_bytes(head[8:12], "little", signed=True)
        first = _frame(f, HEAD, size)
        if first is None or first[0] != DEM_FILE_HEADER:
            raise FormatError(f"{path.name} does not start with a demo file header")
        header = _parse(demo_pb2.CDemoFileHeader, first[1])
        try:
            last = _frame(f, info_at, size)
            file_info = _parse(demo_pb2.CDemoFileInfo, last[1]) if last is not None and last[0] == DEM_FILE_INFO \
                else None
        except FormatError:
            # A replay cut short or still being written: the header alone.
            file_info = None
    dota = file_info.game_info.dota if file_info is not None and file_info.HasField("game_info") else None

    players: list[dict[str, Any]] = []
    teams: list[dict[str, Any]] = []
    outcome = None
    date = mode = None
    match_id = _id_from_name(path) or None
    if dota is not None:
        match_id = int(dota.match_id) or match_id
        mode = _mode(dota.game_mode)
        if dota.end_time:
            date = datetime.fromtimestamp(dota.end_time, timezone.utc).isoformat()
        for p in dota.player_info:
            players.append({"name": p.player_name or None, "team": TEAMS.get(p.game_team, str(p.game_team)),
                            "hero": p.hero_name or None, "heroName": hero_display(p.hero_name) if p.hero_name else None,
                            "steamid": str(p.steamid) if p.steamid else None, "bot": bool(p.is_fake_client)})
        for number, tag, team_id in ((RADIANT, dota.radiant_team_tag, dota.radiant_team_id),
                                     (RADIANT + 1, dota.dire_team_tag, dota.dire_team_id)):
            teams.append({"id": TEAMS[number], "name": tag or None, "team_id": team_id or None})
        if dota.game_winner in TEAMS:
            winner = TEAMS[dota.game_winner]
            outcome = {"winner": winner, "result": f"{winner} victory"}
    version = header.build_num or header.patch_version
    return {
        "game": "Dota 2",
        "match_id": str(match_id) if match_id else None,
        "map": "dota",
        "map_title": None,
        "mode": mode,
        "date": date,
        "duration_s": round(float(file_info.playback_time), 3) if file_info is not None and file_info.playback_time
        else None,
        "players": players,
        "teams": teams,
        "outcome": outcome,
        "game_version": str(version) if version else None,
    }
