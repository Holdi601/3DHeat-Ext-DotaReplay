---
title: "Trovare i replay: list"
nav_order: 2
lang: "it"
source: list.md
source_hash: "42b8c485dac2"
nav_exclude: true
search_exclude: true
---
# Trovare i replay: `list` {#finding-replays-list}

```bash
heat3d-dota-replay list [--game FOLDER]
```

stampa dove Dota 2 salva i replay e ogni replay presente con la sua dimensione. Se non ne viene indicato
nessuno, [`convert`](convert.md) converte quelli che `list` mostra.

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
  7123456790.dem                  121.4 MB
2 replay(s)
```

## Dove sono i replay {#where-replays-are}

Dota 2 salva i replay che scarichi - i dettagli di una partita, **Download replay**, oppure
Watch > Replays - in `<Dota>/game/dota/replays/<match id>.dem`. Lo strumento cerca Dota 2 in
`--game` (la cartella `dota 2 beta` o la sua `game\dota`), altrimenti in ogni libreria Steam: la cartella
di Steam stessa (dal registro, altrimenti `C:\Program Files (x86)\Steam`, `~/.steam/steam` o
`~/.local/share/Steam`) e ogni libreria elencata nel suo `steamapps\libraryfolders.vdf`.

Valve conserva il replay di una partita pubblica per qualche settimana. Per recuperarne uno tramite il suo id
partita senza il gioco, il comando `python -m heat3d_watch dota-replay <match id>` del 3DHeat Watcher lo scarica
attraverso il registro della partita di OpenDota ([comandi del Watcher](https://holdi601.github.io/3DHeat-Watcher/commands.html)).
Un replay che qualcuno ti manda funziona allo stesso modo: indica il suo percorso a `convert`.

## Messaggi e stato di uscita {#messages-and-exit-status}

| Messaggio | Uscita | Significa |
|---|---|---|
| `heat3d-dota-replay: Dota 2 not found in any Steam library: ...` | 2 | installa Dota 2 tramite Steam, oppure indica `--game` |
| `<folder> (not there yet: no replay downloaded)` | 2 | Dota 2 c'è, ma non è ancora stato scaricato alcun replay |
| `0 replay(s)` | 2 | la cartella non contiene nessun `.dem` |
