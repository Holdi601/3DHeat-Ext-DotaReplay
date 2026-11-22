"""The match facts read from a replay's header and file info alone - on made-up files."""

from __future__ import annotations

import struct

import pytest

from heat3d_ext_dota_replay import dota_replay as d
from heat3d_ext_dota_replay.replay_info import info

demo_pb2 = pytest.importorskip("gem.proto.demo_pb2")


def _varint(v: int) -> bytes:
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        out.append(b | (0x80 if v else 0))
        if not v:
            return bytes(out)


def _frame(command: int, tick: int, payload: bytes) -> bytes:
    return _varint(command) + _varint(tick) + _varint(len(payload)) + payload


def demo(compress_info: bool = False, with_info: bool = True) -> bytes:
    """A demo shaped like the game's: magic, the offsets, the header frame, a packet, the file info at the end."""
    header = demo_pb2.CDemoFileHeader(demo_file_stamp="PBDEMS2", patch_version=99, map_name="start", build_num=12345,
                                      game_directory="dota")
    fi = demo_pb2.CDemoFileInfo(playback_time=2400.5, playback_ticks=72015, playback_frames=36000)
    g = fi.game_info.dota
    g.match_id = 1234567890
    g.game_mode = 22
    g.game_winner = 3
    g.end_time = 1_700_000_000
    g.radiant_team_tag = "AAA"
    g.dire_team_tag = "BBB"
    g.dire_team_id = 42
    for name, hero, team in (("Player One", "npc_dota_hero_axe", 2), ("Player Two", "npc_dota_hero_lina", 3)):
        p = g.player_info.add()
        p.player_name, p.hero_name, p.game_team, p.steamid = name, hero, team, d.STEAM64 + 1  # account 1: no real player
    body = _frame(1, 0, header.SerializeToString()) + _frame(7, 30, b"\x00" * 64)
    head_len = len(d.DEMO_MAGIC) + 8
    info_at = head_len + len(body)
    data = fi.SerializeToString()
    if compress_info:
        snappy = pytest.importorskip("snappy")
        tail = _frame(2 | 64, 72015, snappy.compress(data))
    else:
        tail = _frame(2, 72015, data)
    if not with_info:
        info_at, tail = 0, b""
    return d.DEMO_MAGIC + struct.pack("<ii", info_at, 0) + body + tail


@pytest.mark.parametrize("compress", [False, True])
def test_the_header_and_file_info_describe_the_match(tmp_path, compress):
    f = tmp_path / "replay.dem"
    f.write_bytes(demo(compress))
    r = info(f)
    assert r["map"] == "dota"
    assert r["match_id"] == "1234567890"
    assert r["mode"] == "All Pick"
    assert r["date"] == "2023-11-14T22:13:20+00:00"
    assert r["duration_s"] == pytest.approx(2400.5)
    assert r["game_version"] == "12345"
    assert [(p["name"], p["team"], p["hero"]) for p in r["players"]] == [
        ("Player One", "Radiant", "npc_dota_hero_axe"), ("Player Two", "Dire", "npc_dota_hero_lina")]
    assert r["players"][0]["heroName"] == "Axe"
    assert r["teams"] == [{"id": "Radiant", "name": "AAA", "team_id": None}, {"id": "Dire", "name": "BBB", "team_id": 42}]
    assert r["outcome"] == {"winner": "Dire", "result": "Dire victory"}


def test_a_replay_without_file_info_gives_the_header_alone(tmp_path):
    f = tmp_path / "987_1.dem"
    f.write_bytes(demo(with_info=False))
    r = info(f)
    assert r["game_version"] == "12345"
    assert r["match_id"] == "987"
    assert r["players"] == [] and r["teams"] == [] and r["outcome"] is None
    assert r["date"] is None and r["duration_s"] is None and r["mode"] is None


def test_other_files_are_refused(tmp_path):
    for name, raw in (("junk.dem", b"not a replay at all" * 10), ("source1.dem", b"HL2DEMO\0" + bytes(64)),
                      ("short.dem", b"PBD")):
        f = tmp_path / name
        f.write_bytes(raw)
        with pytest.raises(ValueError):
            info(f)
