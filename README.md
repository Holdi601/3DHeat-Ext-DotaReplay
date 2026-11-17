# 3DHeat Dota Replay: Dota 2 replays as 3DHeat tables

**What is it?** This tool reads Dota 2 replays (`.dem` files) and writes what
happened in them as tables the [3DHeat](https://github.com/Holdi601/3DHeat)
viewer opens: every hero's path over the map, every kill, tower, ward, ping and
order where it happened, and the whole match.

**Why would I use it?** To see a Dota 2 match - yours or any public one - as a
heatmap and a replay on the map in 3DHeat: where a hero spent the game, where
fights happened, where wards went.

**Example:** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet` (the table to open in the viewer),
`tables/7123456789.match.json` (the match) and the side tables.

**Documentation:** [holdi601.github.io/3DHeat-Ext-DotaReplay](https://holdi601.github.io/3DHeat-Ext-DotaReplay/),
a page per command with step-by-step use and example output. Part of
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn on
a rights holder's request - on its own, without affecting the viewer or the
other tools. The tables this tool writes stay on your machine.

## Quick start for new users

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), and Dota 2 replays: in
Dota 2, open a match's details and click **Download replay**; it lands in
`...\steamapps\common\dota 2 beta\game\dota\replays\<match id>.dem`, where the
tool finds it by itself. No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt; it also
   installs gem-dota, the replay parser it reads with):

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-DotaReplay/archive/refs/tags/v0.1.0.zip
   ```

2. List the replays Dota 2 saved, then convert them (or name one `.dem`):

   ```bash
   heat3d-dota-replay list
   heat3d-dota-replay convert -o tables
   heat3d-dota-replay convert 7123456789.dem -o tables
   ```

   Dota 2 outside your Steam libraries: add `--game "<...>\dota 2 beta"`.
3. The output lands in the `-o` folder, per replay named by its match id:
   `tables\<match>.parquet` (the table to open), `tables\<match>.match.json`
   (the match, players, draft, chat) and side tables (`.units`, `.combatlog`,
   `.packets`, `.entities`, `.strings.parquet`). A long match takes a minute
   or two and about a gigabyte of memory.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There,
   **Source -> Files...**, pick `<match>.parquet` (or drop it on the Source
   panel) and click **Load file**. For the Dota 2 map in 3D under it, see
   [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota#quick-start-for-new-users).

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_dota_replay.update` does the same).

## Install from a checkout

New to the command line? Read [Before you start](https://holdi601.github.io/3DHeat-Ext-DotaReplay/before-you-start.html) first.

1. Install Python 3.10 or later.
2. `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay` (or download the
   ZIP) and open a terminal in that folder.
3. Install the command (pip also installs gem-dota, the replay parser it reads
   through) and check where your replays are:

```bash
python -m pip install -e .        # installs the heat3d-dota-replay command and gem-dota
heat3d-dota-replay list           # where Dota 2 saves replays, and the ones there
```

You should see the replays folder of your Dota 2 install and a line per replay.

## Commands

| Command | Does | Page |
|---|---|---|
| `list [--game FOLDER]` | where Dota 2 saves replays (`<Dota>/game/dota/replays`), and the replays there | [list](https://holdi601.github.io/3DHeat-Ext-DotaReplay/list.html) |
| `convert [REPLAY or FOLDER ...] -o OUT` | each replay as 3DHeat tables in `OUT`; without a replay, every one in Dota's replays folder | [convert](https://holdi601.github.io/3DHeat-Ext-DotaReplay/convert.html) |

```bash
heat3d-dota-replay convert 7123456789.dem -o tables     # one replay
heat3d-dota-replay convert -o tables                    # every replay Dota 2 saved
```

| `convert` option | Does |
|---|---|
| `-o`, `--out FOLDER` | the folder to write to (required) |
| `--game FOLDER` | the `dota 2 beta` folder, when Dota 2 is in no Steam library (also for `list`) |
| `--hz N` | hero samples a second (default 7.5: every fourth tick) |

Exit status: 0 done; 1 a replay could not be read to the end or failed; 2
nothing to read - no replay found, a file that is not a Dota 2 replay, or
gem-dota not installed (the message says which, and what to do). Every option,
as the program prints it: [Command reference](https://holdi601.github.io/3DHeat-Ext-DotaReplay/cli-reference.html).

## What comes out, and loading it

Per replay, named by its match id: `<match>.parquet`, every hero 7.5 times a
second (position, height, health, level, facing, mana, experience, items, the
player's cursor) and every event where it happened - kills, deaths, towers,
barracks, Roshan, Tormentors, wards, combat log entries about heroes, map
pings, map drawings and orders; `<match>.units.parquet`, every other unit once
a second; `<match>.combatlog.parquet`, the whole combat log;
`<match>.match.json`, the match, the players, the draft, the chat and the
game's own end-of-match record; and everything else the replay holds, kept
whole: `<match>.packets.parquet`, `<match>.entities.parquet`,
`<match>.strings.parquet`. Positions are Dota's world units, x east, y north, z
up. Open `<match>.parquet` in the viewer (**Files…** or drag and drop): its
footer tells the viewer the axes, units and columns, so nothing needs mapping.
The side tables open the same way when picked on their own. The Dota 2 map as a 3D level under it:
[3DHeat-Ext-Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).
[The tables, column by column](https://holdi601.github.io/3DHeat-Ext-DotaReplay/convert.html).

The 3DHeat Watcher runs this tool on each replay Dota 2 saves while it watches,
and on request (`python -m heat3d_watch replays dota-replays`); its
`dota-replay <match id> --convert` downloads a public match's replay and
converts it with this tool.

## Terms

3DHeat Dota Replay is not affiliated with or endorsed by Valve. Dota 2 and
related names and trademarks belong to their owners. The tool reads replay files
on your machine and talks to no server. Valve's replays are not encrypted; the
reading is done by gem-dota (MIT), a published parser ([Terms and
licence](https://holdi601.github.io/3DHeat-Ext-DotaReplay/terms.html)).

Rights holders: open an issue at
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) -
we respond quickly and remove anything on request.

## Tests

```bash
python -m pip install -e .[test]
python -m pytest
```

On made-up data only: no replay is part of this repository.

## Licence

MIT ([`LICENSE`](LICENSE)). Third-party software it uses: [`LICENSES.md`](LICENSES.md).
