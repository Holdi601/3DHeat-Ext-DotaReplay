---
title: "Avant de commencer"
nav_order: 1.5
lang: "fr"
source: before-you-start.md
source_hash: "b1cdff264868"
nav_exclude: true
search_exclude: true
---
# Avant de commencer {#before-you-start}

Vous ne connaissez pas la ligne de commande ? Cette page vous mène de zéro
jusqu'à un premier lancement.
Cela prend une dizaine de minutes, une seule fois.

## 1. Installer Python {#install-python}

Cet outil demande **Python 3.10 ou plus récent**.

- **Windows :** téléchargez Python sur [python.org/downloads](https://www.python.org/downloads/)
  et lancez l'installateur. Sur son premier écran, cochez **Add python.exe to PATH**,
  puis cliquez sur **Install Now**.
- **macOS et Linux :** Python 3 est souvent déjà là. Là où ces pages disent
  `python`, tapez `python3`.

## 2. Obtenir cet outil {#get-this-tool}

Ouvrez [github.com/Holdi601/3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay), cliquez sur le
bouton vert **Code**, puis sur **Download ZIP**, et décompressez-le dans un
dossier de votre choix. Si vous utilisez git : `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay`.

## 3. Ouvrir un terminal dans ce dossier {#open-a-terminal-in-that-folder}

Un terminal est une fenêtre où vous tapez des commandes.

- **Windows :** ouvrez le dossier dans l'Explorateur, cliquez dans la barre
  d'adresse, tapez `powershell` et appuyez sur Entrée. Une fenêtre bleue ou noire
  s'ouvre, déjà dans ce dossier.
- **macOS :** ouvrez **Terminal**, tapez `cd ` (avec un espace), glissez le
  dossier dans la fenêtre et appuyez sur Entrée.

`cd` veut dire « changer de dossier » : `cd C:\Tools\3DHeat-Ext-DotaReplay` va dans ce dossier.

## 4. Installer l'outil {#install-the-tool}

Tapez ceci et appuyez sur Entrée :

```bash
python -m pip install -e .
```

Il installe l'outil et gem-dota, le lecteur de replays par lequel il passe. Vous
devez voir, à la fin : `Successfully installed ... gem-dota-... heat3d-ext-dota-replay-...`.

## 5. Obtenir un replay et le lancer {#get-a-replay-and-run-it}

Dans Dota 2, ouvrez les détails d'un match et cliquez sur **Download replay** (ou Watch >
Replays). Ensuite :

```bash
heat3d-dota-replay list
```

Vous devez voir quelque chose comme :

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
1 replay(s)
```

Suite : [Convertir : convert](convert.md).

## Comment lire les commandes de ces pages {#how-to-read-the-commands-on-these-pages}

| Vous voyez | Cela veut dire |
|---|---|
| `<match>` | un espace réservé : tapez votre propre valeur à la place, sans les `< >` |
| `[--hz N]` | facultatif : omettez-le, ou tapez-le comme indiqué |
| `# a note` | un commentaire pour vous : ne le tapez pas |
| `"C:\My Files\x"` | mettez entre guillemets un chemin qui contient des espaces |

## Quand quelque chose ne va pas {#when-something-goes-wrong}

| Le message | Que faire |
|---|---|
| `'python' is not recognized` | Python n'est pas installé, ou la case PATH n'était pas cochée : réinstallez-le et cochez-la (ou tapez `py` au lieu de `python`). |
| `'heat3d-dota-replay' is not recognized` | Relancez l'étape 4 dans le dossier de l'outil, ou tapez `python -m heat3d_ext_dota_replay` au lieu de `heat3d-dota-replay` : cela fait la même chose. |
| `pip install gem-dota (the Dota 2 replay parser, MIT)` | L'étape 4 n'a pas installé gem-dota : lancez `python -m pip install gem-dota`. |
| `Dota 2 not found in any Steam library` | Installez Dota 2 par Steam, donnez son dossier avec `--game`, ou donnez le chemin du replay à `convert`. |
| `... is not a Source 2 demo` | Le fichier n'est pas un replay de Dota 2 ; un `.dem.bz2` doit d'abord être décompressé. |
| tout le reste | Lisez la dernière ligne du message, puis ouvrez un ticket (issue) sur GitHub avec cette ligne. |

Chaque commande se termine aussi par un **code de sortie** : 0 veut dire que
cela a marché, 2 qu'il n'y avait rien à lire (pas de replay, pas un replay,
gem-dota manquant), 1 qu'un replay a échoué. Pour le voir, tapez
`echo $LASTEXITCODE` dans PowerShell, ou `echo $?` sur macOS et Linux.
