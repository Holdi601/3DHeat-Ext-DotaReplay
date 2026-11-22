"""
The standalone app's description of this tool (app/spec.py): the Dota 2
install whose replays folder it reads, and the replay conversion as a task. A
replay reader has no maps to extract. `python -m heat3d_ext_dota_replay.standalone_spec`
runs the app from a checkout; the release executables run the same.
"""

from __future__ import annotations

from pathlib import Path

from . import __version__
from .app import paths
from .app.spec import GameSpec, Input, Replays, Spec, Task, game_folders

#: The install's folder name in a Steam library.
STEAM_FOLDER = "dota 2 beta"


def _as_root(p: Path) -> Path | None:
    """The install's top folder from it, its `game` or its `game/dota` folder."""
    for r in (p, p.parent, p.parent.parent):
        if (r / "game" / "dota" / "gameinfo.gi").is_file():
            return r
    return None


def _find(given: str | None) -> Path | None:
    if given:
        return _as_root(Path(given).expanduser())
    from .steam import steam_libraries

    for c in [*paths.steam_game_dirs(STEAM_FOLDER), *(common / STEAM_FOLDER for common in steam_libraries())]:
        root = _as_root(c)
        if root is not None:
            return root
    return None


def _replays(levels: Path) -> str:
    """Where the game saves the replays a player downloads: `game/dota/replays` in the install."""
    game = game_folders(SPEC).get("dota")
    folder = game / "game" / "dota" / "replays" if game else None
    return str(folder) if folder and folder.is_dir() else ""

def _replay_info(path: Path) -> dict:
    """`info <replay> --json`: the header only (replay_info.py)."""
    from .replay_info import info

    return info(path)


SPEC = Spec(
    id="heat3d-dota-replay",
    name="3DHeat Dota replays",
    repo="Holdi601/3DHeat-Ext-DotaReplay",
    version=__version__,
    tools={"heat3d-dota-replay": "heat3d_ext_dota_replay.cli:main"},
    default_tool="heat3d-dota-replay",
    description="Dota 2 replays (.dem) into 3DHeat tables",
    module="heat3d_ext_dota_replay.standalone_spec",
    games=[GameSpec(
        key="dota", label="Dota 2", find=_find,
        platforms=("windows-x64", "linux-x64", "macos-arm64"),
    )],
    tasks=[Task(
        "replays", "Convert replays",
        [Input("src", "Folder with .dem replays", "folder", default=_replays),
         Input("out", "Where the matches go", "folder", default=lambda levels: str(paths.data_dir() / "matches" / "dota"))],
        lambda v, levels: ["heat3d-dota-replay", "convert", v["src"], "-o", v["out"]],
        help="each replay becomes the tables of one match the viewer opens",
    )],
    min_free_gb=2.0,
    replays=Replays("dota", (".dem",), lambda r, out: ["heat3d-dota-replay", "convert", str(r), "-o", str(out)], info=_replay_info),
    notice="Not affiliated with or endorsed by Valve Corporation.",
)

if __name__ == "__main__":
    from . import update
    from .app.entry import main

    raise SystemExit(main(SPEC, apply_source=update.apply))
