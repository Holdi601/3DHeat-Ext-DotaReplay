"""The standalone spec on a synthetic Dota 2 install (tiny fake files, no game data)."""

from __future__ import annotations

import dataclasses
import json
from pathlib import Path

import pytest

from heat3d_ext_dota_replay import standalone_spec as S
from heat3d_ext_dota_replay.app import entry, spec as app_spec


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")


def install(tmp_path: Path) -> Path:
    root = tmp_path / "dota 2 beta"
    dota = root / "game" / "dota"
    (dota / "replays").mkdir(parents=True)
    (dota / "gameinfo.gi").write_text("x")
    return root


def test_find_and_replays_folder(tmp_path, monkeypatch):
    root = install(tmp_path)
    assert S._find(str(root)) == root
    assert S._find(str(root / "game" / "dota")) == root
    assert S._find(str(tmp_path / "nowhere")) is None
    monkeypatch.setattr(S, "game_folders", lambda spec: {"dota": root})
    assert S._replays(tmp_path / "levels") == str(root / "game" / "dota" / "replays")


def test_no_maps_to_extract(tmp_path, capsys):
    root = install(tmp_path)
    spec = dataclasses.replace(S.SPEC, games=[dataclasses.replace(S.SPEC.games[0], find=lambda given: root)])
    assert not spec.has_maps()
    entry.main(spec, ["status", "--json"])
    g = json.loads(capsys.readouterr().out)["games"][0]
    assert g["found"] and g["maps"] == []
    assert entry.main(spec, ["extract", "--new", "--progress-json"]) == 0
    assert json.loads(capsys.readouterr().out.splitlines()[-1]) == {"event": "done", "ok": 0, "failed": 0}


def test_task_and_tool(tmp_path):
    assert S.SPEC.version == (Path(__file__).resolve().parents[1] / "VERSION").read_text().strip()
    t = S.SPEC.tasks[0]
    assert t.argv({"src": "in", "out": "o"}, tmp_path) == ["heat3d-dota-replay", "convert", "in", "-o", "o"]
    assert t.inputs[1].default(tmp_path).endswith(str(Path("matches") / "dota"))
    assert entry.run_tool(S.SPEC, "heat3d-dota-replay", ["--help"]) == 0
    assert isinstance(app_spec.standard_checks(S.SPEC, {"dota": None}, tmp_path)[0], app_spec.Check)
