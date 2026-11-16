---
title: "Replays finden: list"
nav_order: 2
lang: "de"
source: list.md
source_hash: "42b8c485dac2"
nav_exclude: true
search_exclude: true
---
# Replays finden: `list` {#finding-replays-list}

```bash
heat3d-dota-replay list [--game FOLDER]
```

zeigt, wo Dota 2 Replays speichert, und jedes Replay dort mit seiner Größe. Ohne angegebenes
Replay konvertiert [`convert`](convert.md) die Replays, die `list` zeigt.

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
  7123456790.dem                  121.4 MB
2 replay(s)
```

## Wo die Replays liegen {#where-replays-are}

Dota 2 speichert die Replays, die du herunterlädst - die Details eines Matches,
**Download replay**, oder Ansehen > Replays - unter `<Dota>/game/dota/replays/<match id>.dem`.
Das Werkzeug sucht Dota 2 in `--game` (der Ordner `dota 2 beta` oder sein `game\dota`), sonst in
jeder Steam-Bibliothek: Steams eigener Ordner (aus der Registry, sonst
`C:\Program Files (x86)\Steam`, `~/.steam/steam` oder `~/.local/share/Steam`) und jede Bibliothek,
die ihre `steamapps\libraryfolders.vdf` auflistet.

Valve bewahrt das Replay eines öffentlichen Matches einige Wochen auf. Um es anhand seiner
Match-ID ohne das Spiel zu holen, lädt `python -m heat3d_watch dota-replay <match id>` aus dem
3DHeat Watcher es über OpenDotas Aufzeichnung des Matches herunter
([Watcher-Befehle](https://holdi601.github.io/3DHeat-Watcher/commands.html)).
Ein Replay, das dir jemand schickt, funktioniert genauso: Gib seinen Pfad an `convert` weiter.

## Meldungen und Exit-Status {#messages-and-exit-status}

| Meldung | Exit | Bedeutung |
|---|---|---|
| `heat3d-dota-replay: Dota 2 not found in any Steam library: ...` | 2 | installiere Dota 2 über Steam, oder gib `--game` an |
| `<folder> (not there yet: no replay downloaded)` | 2 | Dota 2 ist da, aber es wurde noch kein Replay heruntergeladen |
| `0 replay(s)` | 2 | der Ordner enthält keine `.dem` |
