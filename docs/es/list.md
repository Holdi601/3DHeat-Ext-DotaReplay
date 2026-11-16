---
title: "Encontrar repeticiones: list"
nav_order: 2
lang: "es"
source: list.md
source_hash: "42b8c485dac2"
nav_exclude: true
search_exclude: true
---
# Encontrar repeticiones: `list` {#finding-replays-list}

```bash
heat3d-dota-replay list [--game FOLDER]
```

muestra dónde guarda Dota 2 las repeticiones y cada repetición de allí con su tamaño. Si no se da ninguna repetición, [`convert`](convert.md) convierte las que muestra `list`.

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
  7123456790.dem                  121.4 MB
2 replay(s)
```

## Dónde están las repeticiones {#where-replays-are}

Dota 2 guarda las repeticiones que descargas - los detalles de una partida, **Download replay**,
o Watch > Replays - en `<Dota>/game/dota/replays/<match id>.dem`. La herramienta busca Dota 2 en
`--game` (la carpeta `dota 2 beta` o su `game\dota`); si no, en
cada biblioteca de Steam: la carpeta propia de Steam (desde el registro, si no
`C:\Program Files (x86)\Steam`, `~/.steam/steam` o `~/.local/share/Steam`) y
cada biblioteca que figura en su `steamapps\libraryfolders.vdf`.

Valve guarda la repetición de una partida pública durante unas semanas. Para bajar una por su
id de partida sin el juego, el comando `python -m heat3d_watch dota-replay <match id>` del
3DHeat Watcher la descarga a través del registro de la partida de OpenDota
([comandos del Watcher](https://holdi601.github.io/3DHeat-Watcher/commands.html)).
Una repetición que alguien te envíe funciona igual: da su ruta a `convert`.

## Mensajes y código de salida {#messages-and-exit-status}

| Mensaje | Salida | Significa |
|---|---|---|
| `heat3d-dota-replay: Dota 2 not found in any Steam library: ...` | 2 | instala Dota 2 a través de Steam, o indica `--game` |
| `<folder> (not there yet: no replay downloaded)` | 2 | Dota 2 está ahí, pero aún no se ha descargado ninguna repetición |
| `0 replay(s)` | 2 | la carpeta no tiene ningún `.dem` |
