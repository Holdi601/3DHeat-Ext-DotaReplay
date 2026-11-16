---
title: Bevor du anfängst
nav_order: 1.5
lang: "de"
source: before-you-start.md
source_hash: "b1cdff264868"
nav_exclude: true
search_exclude: true
---
# Bevor du anfängst {#before-you-start}

Neu auf der Kommandozeile? Diese Seite führt dich von null bis zum ersten Lauf.
Es dauert etwa zehn Minuten, einmal.

## 1. Python installieren {#install-python}

Dieses Werkzeug braucht **Python 3.10 oder neuer**.

- **Windows:** Lade Python von [python.org/downloads](https://www.python.org/downloads/)
  herunter und starte den Installer. Setze auf dem ersten Bildschirm den Haken bei
  **Add python.exe to PATH**, dann klicke auf **Install Now**.
- **macOS und Linux:** Python 3 ist oft schon da. Wo diese Seiten `python` schreiben,
  tippe `python3`.

## 2. Dieses Werkzeug holen {#get-this-tool}

Öffne [github.com/Holdi601/3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay), klicke auf
den grünen Button **Code** und dann auf **Download ZIP**, und entpacke es in einen Ordner
deiner Wahl. Wenn du git benutzt: `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay`.

## 3. Ein Terminal in diesem Ordner öffnen {#open-a-terminal-in-that-folder}

Ein Terminal ist ein Fenster, in das du Befehle tippst.

- **Windows:** Öffne den Ordner im Explorer, klicke in die Adressleiste, tippe
  `powershell` und drücke Enter. Ein blaues oder schwarzes Fenster öffnet sich, schon in
  diesem Ordner.
- **macOS:** Öffne **Terminal**, tippe `cd ` (mit einem Leerzeichen), ziehe den Ordner
  in das Fenster und drücke Enter.

`cd` heißt „Ordner wechseln“: `cd C:\Tools\3DHeat-Ext-DotaReplay` geht in diesen Ordner.

## 4. Das Werkzeug installieren {#install-the-tool}

Tippe das und drücke Enter:

```bash
python -m pip install -e .
```

Es installiert das Werkzeug und gem-dota, den Replay-Leser, über den es liest. Am Ende
solltest du sehen: `Successfully installed ... gem-dota-... heat3d-ext-dota-replay-...`.

## 5. Ein Replay holen und starten {#get-a-replay-and-run-it}

Öffne in Dota 2 die Details eines Matches und klicke auf **Download replay** (oder
Ansehen > Replays). Dann:

```bash
heat3d-dota-replay list
```

Du solltest so etwas sehen:

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
1 replay(s)
```

Weiter: [Konvertieren: convert](convert.md).

## So liest du die Befehle auf diesen Seiten {#how-to-read-the-commands-on-these-pages}

| Du siehst | Es bedeutet |
|---|---|
| `<match>` | ein Platzhalter: Tippe stattdessen deinen eigenen Wert, ohne die `< >` |
| `[--hz N]` | optional: Lass es weg, oder tippe es wie gezeigt |
| `# a note` | ein Kommentar für dich: nicht mittippen |
| `"C:\My Files\x"` | einen Pfad mit Leerzeichen in Anführungszeichen setzen |

## Wenn etwas schiefgeht {#when-something-goes-wrong}

| Die Meldung | Was du tun kannst |
|---|---|
| `'python' is not recognized` | Python ist nicht installiert, oder der Haken bei PATH fehlte: Installiere es neu und setze den Haken (oder tippe `py` statt `python`). |
| `'heat3d-dota-replay' is not recognized` | Führe Schritt 4 im Ordner des Werkzeugs noch einmal aus, oder tippe `python -m heat3d_ext_dota_replay` statt `heat3d-dota-replay`: Das macht dasselbe. |
| `pip install gem-dota (the Dota 2 replay parser, MIT)` | Schritt 4 hat gem-dota nicht installiert: Führe `python -m pip install gem-dota` aus. |
| `Dota 2 not found in any Steam library` | Installiere Dota 2 über Steam, gib den Ordner mit `--game` an, oder gib den Pfad des Replays an `convert` weiter. |
| `... is not a Source 2 demo` | Die Datei ist kein Dota-2-Replay; eine `.dem.bz2` muss zuerst entpackt werden. |
| alles andere | Lies die letzte Zeile der Meldung und eröffne damit ein Issue auf GitHub. |

Jeder Befehl endet außerdem mit einem **Exit-Status**: 0 heißt, es hat geklappt; 2 heißt,
es gab nichts zu lesen (kein Replay, kein Replay-Format, gem-dota fehlt); 1 heißt, ein
Replay ist fehlgeschlagen. Um ihn zu sehen, tippe `echo $LASTEXITCODE` in PowerShell oder
`echo $?` unter macOS und Linux.
