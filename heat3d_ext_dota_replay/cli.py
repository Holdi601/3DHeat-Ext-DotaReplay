"""
heat3d-dota-replay list [--game FOLDER]                where Dota 2 saves replays, and the replays there
heat3d-dota-replay convert [REPLAY|FOLDER ...] -o OUT  each replay as 3DHeat tables in OUT

Exit status: 0 done, 1 a replay failed, 2 nothing to read (no replay found, not a
Dota 2 replay, gem-dota not installed).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .steam import steam_libraries

PROG = "heat3d-dota-replay"


def say(text: str) -> None:
    print(f"{PROG}: {text}", file=sys.stderr)


def replay_folders(game: str | None = None) -> list[Path]:
    """
    Where Dota 2 saves the replays a player downloads: `<Dota>/game/dota/replays`,
    in `--game` (the `dota 2 beta` folder or its `game/dota`) or in every Steam
    library Dota 2 is installed in.
    """
    if game:
        given = Path(game)
        for candidate in (given / "game" / "dota", given, given / "dota"):
            if (candidate / "gameinfo.gi").exists() or (candidate / "replays").is_dir():
                return [candidate / "replays"]
        return [given / "game" / "dota" / "replays"]
    out = []
    for common in steam_libraries():
        game_dir = common / "dota 2 beta" / "game" / "dota"
        if game_dir.is_dir():
            out.append(game_dir / "replays")
    return out


def replays_in(paths: list[str], game: str | None) -> tuple[list[Path], list[Path]]:
    """The replays to convert (each file given, each folder's `*.dem`), and the folders looked in."""
    folders = [Path(p) for p in paths] if paths else replay_folders(game)
    found: list[Path] = []
    for p in folders:
        if p.is_file():
            found.append(p)
        elif p.is_dir():
            found += sorted(f for f in p.glob("*.dem") if f.is_file())
    return found, folders


def cmd_list(args) -> int:
    folders = replay_folders(args.game)
    if not folders:
        say("Dota 2 not found in any Steam library: install it through Steam, or pass --game <the dota 2 beta folder>")
        return 2
    total = 0
    for folder in folders:
        found = sorted(folder.glob("*.dem")) if folder.is_dir() else []
        print(f"{folder}{'' if folder.is_dir() else ' (not there yet: no replay downloaded)'}")
        for f in found:
            print(f"  {f.name:28s} {f.stat().st_size / 1e6:8.1f} MB")
        total += len(found)
    print(f"{total} replay(s)")
    return 0 if total else 2


def cmd_convert(args) -> int:
    from . import dota_replay as d

    files, folders = replays_in(args.replay, args.game)
    if not files:
        where = ", ".join(str(f) for f in folders) or "no Dota 2 install found"
        say(f"no replay (.dem) found in {where}")
        return 2
    failed = unread = done = 0
    for path in files:
        try:
            data, doc = d.convert(path, args.out, args.hz)
        except d.Missing as e:
            say(str(e))
            return 2
        except d.FormatError as e:
            say(f"{path}: {e}")
            unread += 1
            continue
        except Exception as e:  # noqa: BLE001 - one bad replay does not stop the next
            say(f"{path}: {type(e).__name__}: {e}")
            failed += 1
            continue
        print(data)
        print(doc)
        done += 1
    if failed or (unread and done):
        return 1
    return 0 if done else 2


def main(argv: list[str] | None = None) -> int:
    try:
        import heat3d_update

        heat3d_update.startup("heat3d_ext_dota_replay")
    except Exception:  # an update check never stops a conversion
        pass
    ap = argparse.ArgumentParser(prog=PROG, description="Dota 2 replays (.dem) into 3DHeat tables")
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="command", required=True)
    game_help = "the Dota 2 folder, `dota 2 beta` or its game/dota (default: found in your Steam libraries)"

    p = sub.add_parser("list", help="where Dota 2 saves replays, and the replays there")
    p.add_argument("--game", help=game_help)
    p.set_defaults(run=cmd_list)

    p = sub.add_parser("convert", help="each replay as 3DHeat tables: <match>.parquet, .match.json and sidecars")
    p.add_argument("replay", nargs="*", help="a .dem replay or a folder of them (default: Dota 2's replays folder)")
    p.add_argument("-o", "--out", required=True, help="the folder to write to")
    p.add_argument("--game", help=game_help + "; only used without a replay")
    p.add_argument("--hz", type=float, default=7.5, help="hero samples a second (default 7.5, every fourth tick)")
    p.set_defaults(run=cmd_convert)

    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
