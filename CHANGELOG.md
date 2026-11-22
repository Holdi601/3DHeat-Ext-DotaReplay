# Changelog

## 0.3.0

- Its own icon: the 3DHeat cube with a text badge for its game (letters in 3DHeat's colours), as the
  program, window, taskbar and docs icon.
- A new window: the 3DHeat look in dark and light (follows the system, switchable), the logo and
  icon, sharp at any display scaling. Four steps: find the game (each requirement with its fix),
  choose (maps ticked when there is something to do, filters, search; jobs with their fields
  inline), work (progress, time left, cancel), done (open in 3DHeat, open the output folder, and
  for a failure what went wrong and what to do, copy details, report a problem).
- No console window on Windows: the program is a window program. From a terminal it still prints
  as before; `heat3d-dota-replay-cli.cmd` beside it waits for it in a terminal and passes its exit code.
- The update offer in the same look: Update now / Later / Skip this version, and "Update
  automatically" from the dialog.
- CI draws every page and dialog of the window (on Linux under a virtual display) and checks the
  Windows build is a window program.
- `heat3d-dota-replay convert <replay>... -o <out> [--progress-json]` and `heat3d-dota-replay info <replay> --json` (what the
  replay says about its match, read from its header without converting it), the same verbs in every
  3DHeat replay reader; the old command lines work as before.

## 0.2.0

- A standalone program for Windows, Linux and macOS (no Python needed), built by CI with a `SHA256SUMS` file.
  Without arguments it opens a window: what is found and what is missing (install, disk space), and the
  conversion of a folder of replays (the game's replays folder by default), and updates. `--check --json`,
  `status --json` and `extract` answer as every 3DHeat extractor does; a replay reader has no maps.
- Updates ask first (update now / later / skip this version) unless automatic updates were chosen
  (`--auto-update`, the window's checkbox, or `HEAT3D_AUTO_UPDATE=1`).
- The install is also found in Steam libraries on Linux (native, flatpak, Steam Deck) and macOS.

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
