---
title: "Finding replays: list"
nav_order: 2
---

# Finding replays: `list`

```bash
heat3d-dota-replay list [--game FOLDER]
```

prints where Dota 2 saves replays and each replay there with its size. Without
a replay given, [`convert`](convert.md) converts the ones `list` shows.

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
  7123456790.dem                  121.4 MB
2 replay(s)
```

## Where replays are

Dota 2 saves the replays you download - a match's details, **Download replay**,
or Watch > Replays - to `<Dota>/game/dota/replays/<match id>.dem`. The tool
looks for Dota 2 in `--game` (the `dota 2 beta` folder or its `game\dota`), else
in every Steam library: Steam's own folder (from the registry, else
`C:\Program Files (x86)\Steam`, `~/.steam/steam` or `~/.local/share/Steam`) and
each library its `steamapps\libraryfolders.vdf` lists.

Valve keeps a public match's replay for a few weeks. To fetch one by its match
id without the game, the 3DHeat Watcher's `python -m heat3d_watch dota-replay
<match id>` downloads it through OpenDota's record of the match
([Watcher commands](https://holdi601.github.io/3DHeat-Watcher/commands.html)).
A replay anyone sends you works the same: give its path to `convert`.

## Messages and exit status

| Message | Exit | Means |
|---|---|---|
| `heat3d-dota-replay: Dota 2 not found in any Steam library: ...` | 2 | install Dota 2 through Steam, or pass `--game` |
| `<folder> (not there yet: no replay downloaded)` | 2 | Dota 2 is there, but no replay was downloaded yet |
| `0 replay(s)` | 2 | the folder has no `.dem` |
