---
title: "Trouver les replays : list"
nav_order: 2
lang: "fr"
source: list.md
source_hash: "42b8c485dac2"
nav_exclude: true
search_exclude: true
---
# Trouver les replays : `list` {#finding-replays-list}

```bash
heat3d-dota-replay list [--game FOLDER]
```

affiche où Dota 2 enregistre les replays et chaque replay qui s'y trouve, avec sa taille. Sans
replay donné, [`convert`](convert.md) convertit ceux que `list` affiche.

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
  7123456790.dem                  121.4 MB
2 replay(s)
```

## Où sont les replays {#where-replays-are}

Dota 2 enregistre les replays que vous téléchargez - les détails d'un match, **Download replay**,
ou Watch > Replays - dans `<Dota>/game/dota/replays/<identifiant du match>.dem`. L'outil cherche
Dota 2 dans `--game` (le dossier `dota 2 beta` ou son `game\dota`), sinon dans
chaque bibliothèque Steam : le dossier propre de Steam (depuis le registre, sinon
`C:\Program Files (x86)\Steam`, `~/.steam/steam` ou `~/.local/share/Steam`) et
chaque bibliothèque que `steamapps\libraryfolders.vdf` liste.

Valve garde le replay d'un match public quelques semaines. Pour en récupérer un par son
identifiant de match sans le jeu, la commande `python -m heat3d_watch dota-replay
<identifiant du match>` du 3DHeat Watcher le télécharge via le relevé OpenDota du
match ([commandes du Watcher](https://holdi601.github.io/3DHeat-Watcher/commands.html)).
Un replay qu'on vous envoie fonctionne de la même façon : donnez son chemin à `convert`.

## Messages et code de sortie {#messages-and-exit-status}

| Message | Code | Signification |
|---|---|---|
| `heat3d-dota-replay: Dota 2 not found in any Steam library: ...` | 2 | installez Dota 2 par Steam, ou donnez `--game` |
| `<folder> (not there yet: no replay downloaded)` | 2 | Dota 2 est là, mais aucun replay n'a encore été téléchargé |
| `0 replay(s)` | 2 | le dossier ne contient aucun `.dem` |
