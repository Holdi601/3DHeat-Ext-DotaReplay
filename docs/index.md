---
title: Home
nav_order: 1
---

# 3DHeat Dota Replay

**What is it?** This tool reads Dota 2 replays (`.dem` files) and writes what
happened in them as tables for the [3DHeat](https://github.com/Holdi601/3DHeat)
viewer ([documentation](https://holdi601.github.io/3DHeat/)): every hero's path
over the map, every kill, tower, ward, ping and order where it happened, and
the whole match.

**Why would I use it?** To see a Dota 2 match - yours or any public one - as a
heatmap and a replay on the map: where a hero spent the game, where the fights
were, where the wards went.

**Example:** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet`, the table to open in the viewer, with the match
and the side tables beside it.

## Quick start

New to the command line? Read [Before you start](before-you-start.md) first.
You need Python 3.10 or later and a replay: download one in Dota 2 (a match's
details, **Download replay**), and it lands in Dota's replays folder. Run these
in the folder you cloned or unzipped:

```bash
python -m pip install -e .                  # installs heat3d-dota-replay and gem-dota
heat3d-dota-replay list                     # where Dota 2 saves replays, the ones there
heat3d-dota-replay convert -o tables        # every replay there, as tables
```

`list` prints Dota's replays folder and a line per replay; `convert` prints the
two files it wrote for each, `tables/<match>.parquet` and
`tables/<match>.match.json`. Open the `.parquet` in the viewer with **Files…**
or by dropping it on the window ([Converting](convert.md#loading-it-in-the-viewer)).

## Pages

| Page | What it covers |
|---|---|
| [Before you start](before-you-start.md) | Python, a terminal, a first run |
| [Finding replays: list](list.md) | where Dota 2 saves replays, getting one, what `list` prints |
| [Converting: convert](convert.md) | every option, the tables column by column, loading them, how it was checked |
| [Terms and licence](terms.md) | Valve's replays, gem-dota's licence, why this is a separate package |
| [Command reference](cli-reference.md) | every option, generated from the code |
| [Maintaining these docs](maintaining.md) | the release checklist |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- The 3DHeat Watcher runs this tool on every replay Dota 2 saves, and downloads
  public matches' replays by id: [Dota 2 replays in the Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- The Dota 2 map as a 3D level under these tables: [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## The 3DHeat tools

| Tool | What it does | Code | Docs |
|---|---|---|---|
| 3DHeat viewer | shows the data: heatmaps, race analysis, match review | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | levels and courses from a game's own files | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin: a level as one `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War Thunder replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World of Tanks replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World of Warships replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2 Sturmovik maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | the Dota 2 map as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota 2 replays as tables | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League of Legends and VALORANT replays: what they carry in the open | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
