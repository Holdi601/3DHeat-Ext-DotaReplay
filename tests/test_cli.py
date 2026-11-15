"""The command line: where replays are found, what is converted, and the exit status - on made-up files."""

from __future__ import annotations

from pathlib import Path

from heat3d_ext_dota_replay import cli
from heat3d_ext_dota_replay import dota_replay as d


def test_the_replays_folder_is_found_in_the_steam_libraries(tmp_path, monkeypatch):
    common = tmp_path / "steamapps" / "common"
    (common / "dota 2 beta" / "game" / "dota").mkdir(parents=True)
    monkeypatch.setattr(cli, "steam_libraries", lambda: [common])
    assert cli.replay_folders() == [common / "dota 2 beta" / "game" / "dota" / "replays"]
    assert cli.replay_folders(str(tmp_path / "x")) == [tmp_path / "x" / "game" / "dota" / "replays"]


def test_list_shows_the_replays_and_says_when_there_are_none(tmp_path, monkeypatch, capsys):
    replays = tmp_path / "dota 2 beta" / "game" / "dota" / "replays"
    replays.mkdir(parents=True)
    assert cli.main(["list", "--game", str(tmp_path / "dota 2 beta")]) == 2
    (replays / "42.dem").write_bytes(d.DEMO_MAGIC + bytes(100))
    assert cli.main(["list", "--game", str(tmp_path / "dota 2 beta")]) == 0
    assert "42.dem" in capsys.readouterr().out
    monkeypatch.setattr(cli, "steam_libraries", lambda: [])
    assert cli.main(["list"]) == 2


def test_convert_reads_each_replay_into_the_folder(tmp_path, monkeypatch, capsys):
    folder = tmp_path / "replays"
    folder.mkdir()
    for name in ("1.dem", "2.dem"):
        (folder / name).write_bytes(d.DEMO_MAGIC)
    (folder / "notes.txt").write_text("not a replay")
    done = []

    def convert(path, out, hz):
        done.append((Path(path).name, Path(out), hz))
        return Path(out) / f"{Path(path).stem}.parquet", Path(out) / f"{Path(path).stem}.match.json"

    monkeypatch.setattr(d, "convert", convert)
    assert cli.main(["convert", str(folder), "-o", str(tmp_path / "out")]) == 0
    assert done == [("1.dem", tmp_path / "out", 7.5), ("2.dem", tmp_path / "out", 7.5)]
    assert "2.match.json" in capsys.readouterr().out


def test_exit_status_says_what_went_wrong(tmp_path, monkeypatch, capsys):
    out = str(tmp_path / "out")
    assert cli.main(["convert", str(tmp_path / "empty"), "-o", out]) == 2
    other = tmp_path / "x.dem"
    other.write_bytes(b"HL2DEMO\0" + bytes(32))  # a Source 1 demo
    assert cli.main(["convert", str(other), "-o", out]) == 2
    assert "not a Source 2 demo" in capsys.readouterr().err

    def missing(*a):
        raise d.Missing("pip install gem-dota (the Dota 2 replay parser, MIT)")

    monkeypatch.setattr(d, "convert", missing)
    assert cli.main(["convert", str(other), "-o", out]) == 2
    assert "gem-dota" in capsys.readouterr().err

    def broken(*a):
        raise RuntimeError("cut short")

    monkeypatch.setattr(d, "convert", broken)
    assert cli.main(["convert", str(other), "-o", out]) == 1
