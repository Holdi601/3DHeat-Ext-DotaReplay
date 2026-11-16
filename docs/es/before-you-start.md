---
title: "Antes de empezar"
nav_order: 1.5
lang: "es"
source: before-you-start.md
source_hash: "b1cdff264868"
nav_exclude: true
search_exclude: true
---
# Antes de empezar {#before-you-start}

¿Nunca has usado la línea de comandos? Esta página te lleva de cero a una primera ejecución.
Tarda unos diez minutos, una sola vez.

## 1. Instalar Python {#install-python}

Esta herramienta necesita **Python 3.10 o posterior**.

- **Windows:** descarga Python desde [python.org/downloads](https://www.python.org/downloads/)
  y ejecuta el instalador. En su primera pantalla, marca **Add python.exe to PATH**,
  y luego haz clic en **Install Now**.
- **macOS y Linux:** Python 3 suele estar instalado ya. Donde estas páginas dicen
  `python`, escribe `python3`.

## 2. Conseguir esta herramienta {#get-this-tool}

Abre [github.com/Holdi601/3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay), haz clic en el
botón verde **Code** y luego en **Download ZIP**, y descomprímela en una carpeta de tu elección. Si usas git: `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay`.

## 3. Abrir una terminal en esa carpeta {#open-a-terminal-in-that-folder}

Una terminal es una ventana donde escribes comandos.

- **Windows:** abre la carpeta en el Explorador, haz clic en la barra de direcciones, escribe
  `powershell` y pulsa Intro. Se abre una ventana azul o negra, ya en esa carpeta.
- **macOS:** abre **Terminal**, escribe `cd ` (con un espacio), arrastra la carpeta a
  la ventana y pulsa Intro.

`cd` significa "cambiar de carpeta": `cd C:\Tools\3DHeat-Ext-DotaReplay` va a esa carpeta.

## 4. Instalar la herramienta {#install-the-tool}

Escribe esto y pulsa Intro:

```bash
python -m pip install -e .
```

Instala la herramienta y gem-dota, el analizador de repeticiones con el que lee. Al final
deberías ver: `Successfully installed ... gem-dota-... heat3d-ext-dota-replay-...`.

## 5. Conseguir una repetición y ejecutarla {#get-a-replay-and-run-it}

En Dota 2, abre los detalles de una partida y haz clic en **Download replay** (o Watch >
Replays). Después:

```bash
heat3d-dota-replay list
```

Deberías ver algo parecido a:

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
1 replay(s)
```

Siguiente: [Convertir: convert](convert.md).

## Cómo leer los comandos de estas páginas {#how-to-read-the-commands-on-these-pages}

| Ves | Significa |
|---|---|
| `<match>` | un marcador: escribe tu propio valor en su lugar, sin los `< >` |
| `[--hz N]` | opcional: déjalo fuera, o escríbelo tal como aparece |
| `# a note` | un comentario para ti: no lo escribas |
| `"C:\My Files\x"` | pon entre comillas una ruta que tenga espacios |

## Cuando algo sale mal {#when-something-goes-wrong}

| El mensaje | Qué hacer |
|---|---|
| `'python' is not recognized` | Python no está instalado, o no se marcó la casilla PATH: instálalo de nuevo y marca la casilla (o escribe `py` en vez de `python`). |
| `'heat3d-dota-replay' is not recognized` | Repite el paso 4 en la carpeta de la herramienta, o escribe `python -m heat3d_ext_dota_replay` en vez de `heat3d-dota-replay`: hace lo mismo. |
| `pip install gem-dota (the Dota 2 replay parser, MIT)` | El paso 4 no instaló gem-dota: ejecuta `python -m pip install gem-dota`. |
| `Dota 2 not found in any Steam library` | Instala Dota 2 a través de Steam, indica su carpeta con `--game`, o da la ruta de la repetición a `convert`. |
| `... is not a Source 2 demo` | El archivo no es una repetición de Dota 2; un `.dem.bz2` hay que descomprimirlo antes. |
| cualquier otro | Lee la última línea del mensaje y abre una incidencia en GitHub con ella. |

Cada comando también termina con un **código de salida**: 0 significa que funcionó, 2 que
no había nada que leer (ninguna repetición, algo que no es una repetición, falta gem-dota), 1 que una
repetición falló. Para verlo, escribe `echo $LASTEXITCODE` en PowerShell o `echo $?`
en macOS y Linux.
