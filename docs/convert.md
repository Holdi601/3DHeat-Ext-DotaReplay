---
title: "Converting: convert"
nav_order: 3
---

# Converting: `convert`

```bash
heat3d-dota-replay convert [<replay.dem> or <folder> ...] -o <folder> [--game FOLDER] [--hz N]
```

reads each replay and writes it as 3DHeat tables into the `-o` folder, named by
the match id. Without a replay it converts every `.dem` in Dota's replays
folder ([list](list.md) shows which). A folder given converts each `.dem` in it.
Code: [`heat3d_ext_dota_replay/dota_replay.py`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/heat3d_ext_dota_replay/dota_replay.py).

| Option | Does |
|---|---|
| `<replay.dem>` or `<folder>` | what to convert; several may be given (default: Dota's replays folder) |
| `-o`, `--out FOLDER` | where the tables go (required); made when missing |
| `--game FOLDER` | the `dota 2 beta` folder, when no replay is given and Dota 2 is in no Steam library |
| `--hz N` | hero samples a second (default 7.5, every fourth of the replay's 30 ticks) |

For each replay it prints the two main files it wrote:

```text
tables\7123456789.parquet
tables\7123456789.match.json
```

A long match takes a minute or two and about a gigabyte of memory while it is
read.

## What comes out

| File | Holds |
|---|---|
| `<match>.parquet` | the table to open: every hero 7.5 times a second while alive (position, height, health, level, facing, mana, experience, attributes, armour, speed, damage, items, the player's cursor), and every event where it happened: kills where the killer stood, deaths where the hero fell, towers, barracks, Roshan and Tormentors where they fell, wards where they were planted and where they ended, the combat log's entries about heroes, map pings, map drawings and every order (move, attack, cast, buy, ...) |
| `<match>.units.parquet` | every other unit - creeps, summons, illusions, couriers, buildings - once a second |
| `<match>.combatlog.parquet` | the whole combat log, every field |
| `<match>.match.json` | the match: teams, score, winner, every player's line, deaths, objectives, wards, the draft, the chat, everything else gem-dota extracts, the replay's own file header and info, and the game's end-of-match record (`matchDetails`, `matchMetadata`); `selfCheck` says how complete the reading was |
| `<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet` | everything else the replay holds, kept whole: every frame and network message, every entity property change, every string table entry |

Positions are Dota's world units (Hammer units): x east, y north, z up; the
playable map runs about -8200 to 8200 on both axes - the same units the Dota 2
game-state integration reports, so a replay and a live session line up. Time is
the game clock in seconds: negative before the horn, standing while paused.
Every row has a `life`: a hero's lives counted from 1, so a track ends where the
hero died. All columns: [Command reference](cli-reference.md#output).

## Loading it in the viewer

Open `<match>.parquet` in the viewer with **Files…** or drop it on the window.
Its footer tells the viewer the axes, units and columns (players as people,
teams, lives as sessions, facing as a direction), so nothing needs mapping. The
side tables open the same way when picked on their own. For the map under it in
3D, build the Dota 2 level with [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## How it was checked

On a public match's replay: kills, deaths, assists, level, last hits and denies
read from the stream match the game's own end-of-match record for all ten
players (`selfCheck.crossCheck` in the match file holds the comparison for every
replay), and every message in the packets table re-serialises byte for byte.
The tests run on made-up data only.

A new Dota patch can change the replay's entities before gem-dota follows. A
replay gem-dota cannot read to the end is converted as far as it goes and
marked `incomplete` in its match file.

## Messages and exit status

| Message | Exit | Means |
|---|---|---|
| two file names per replay | 0 | done |
| `heat3d-dota-replay: no replay (.dem) found in ...` | 2 | nothing to convert where it looked |
| `heat3d-dota-replay: <file>: <file> is not a Source 2 demo ...` | 2 | not a Dota 2 replay (a `.dem.bz2` must be unpacked first); among others that converted: 1 |
| `heat3d-dota-replay: pip install gem-dota ...` | 2 | gem-dota is not installed: `python -m pip install gem-dota` |
| `heat3d-dota-replay: <file>: <error>` | 1 | that replay failed; the others are still converted |
