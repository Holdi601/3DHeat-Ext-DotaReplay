# Changelog

## 0.1.0

- First version, moved out of the 3DHeat Watcher (its `dota-replays` adapter and
  `dota-replay --convert` now run this tool): a Dota 2 replay (.dem) as 3DHeat
  tables - every hero's track 7.5 times a second with its state, kills, deaths,
  objectives, wards, pings, drawings and orders where they happened in
  `<match>.parquet`; every other unit in `<match>.units.parquet`; the whole
  combat log in `<match>.combatlog.parquet`; the match, the draft, the chat and
  the game's own end-of-match record in `<match>.match.json`; everything else
  the replay holds kept whole in `<match>.packets`, `.entities` and
  `.strings.parquet`. Read with gem-dota (MIT). `list` says where Dota 2 saves
  replays; `convert` without a replay converts that folder.
- Installs with one pip line from the release zip, no Git needed; a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## Docs

Where each feature is documented
([holdi601.github.io/3DHeat-Ext-DotaReplay](https://holdi601.github.io/3DHeat-Ext-DotaReplay/)):

| Feature | Page |
|---|---|
| Installing, a first run | [Before you start](docs/before-you-start.md) |
| Where replays are, getting one (`list`, `--game`) | [Finding replays: list](docs/list.md) |
| Converting (`convert` and its options), the tables, loading them in the viewer | [Converting: convert](docs/convert.md) |
| Valve's replays, gem-dota's licence | [Terms and licence](docs/terms.md) |
| Every option and column, generated | [Command reference](docs/cli-reference.md) |
| Release checklist for the docs | [Maintaining these docs](docs/maintaining.md) |
