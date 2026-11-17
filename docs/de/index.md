---
title: Startseite
nav_order: 1
lang: "de"
source: index.md
source_hash: "7ee2763ffd33"
nav_exclude: true
search_exclude: true
permalink: /de/
---
# 3DHeat Dota Replay {#dheat-dota-replay}

**Was ist das?** Dieses Werkzeug liest Dota-2-Replays (`.dem`-Dateien) und schreibt, was darin
passiert ist, als Tabellen für den [3DHeat](https://github.com/Holdi601/3DHeat)-Viewer
([Dokumentation](https://holdi601.github.io/3DHeat/)): der Weg jedes Helden über die Karte, jeder
Kill, Turm, Ward, jede Markierung und jeder Befehl dort, wo er geschah, und das ganze Match.

**Wozu brauche ich das?** Um ein Dota-2-Match - deins oder ein beliebiges öffentliches - als
Heatmap und als Replay auf der Karte zu sehen: wo ein Held die meiste Zeit verbrachte, wo die
Kämpfe waren, wohin die Wards gingen.

**Beispiel:** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet`, die Tabelle zum Öffnen im Viewer, mit dem Match und den
Nebentabellen daneben.

**Ein eigenes Projekt:** Jeder Spiel-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei,
eigenen Releases und eigenem Issue-Tracker. So lässt er sich für sich allein installieren,
aktualisieren, pflegen – oder auf Wunsch eines Rechteinhabers zurückziehen –, ohne den Viewer oder
die anderen Werkzeuge zu berühren.

## Schnellstart {#quick-start}

Du brauchst Windows, Python 3.10 oder neuer (im Installer "Add python.exe to PATH"
ankreuzen) und ein Replay: Öffne in Dota 2 die Details eines Matches und klicke
**Download replay**; es landet im Replay-Ordner von Dota
(`...\dota 2 beta\game\dota\replays`), wo das Werkzeug es von selbst findet. Git ist
nicht nötig. Neu auf der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).

```bash
python -m pip install https://github.com/Holdi601/3DHeat-Ext-DotaReplay/archive/refs/tags/v0.1.0.zip
heat3d-dota-replay list                     # wo Dota 2 Replays speichert, die Replays dort
heat3d-dota-replay convert -o tables        # jedes Replay dort, als Tabellen
heat3d-dota-replay convert 7123456789.dem -o tables   # oder ein Replay
```

pip installiert auch gem-dota, den Replay-Parser, mit dem das Werkzeug liest. Dota 2
außerhalb deiner Steam-Bibliotheken: `--game "<...>\dota 2 beta"` anhängen. `list` zeigt
den Replay-Ordner von Dota und eine Zeile pro Replay; `convert` schreibt je Replay, nach
seiner Match-ID benannt, `tables\<match>.parquet` (die Tabelle zum Öffnen),
`tables\<match>.match.json` und die Nebentabellen ([Konvertieren](convert.md)). Ein
langes Match dauert ein bis zwei Minuten und braucht etwa ein Gigabyte Speicher.

Dann öffne die `.parquet` im [3DHeat-Viewer](https://github.com/Holdi601/3DHeat#quick-start):
herunterladen (**Code -> Download ZIP**, entpacken), `start.bat` doppelklicken (es bietet
an, Node.js zu installieren, wenn es fehlt, und öffnet `http://127.0.0.1:5273`), dann
**Quelle -> Dateien...**, die Datei wählen (oder sie auf das Quelle-Panel ziehen) und
**Datei laden** klicken ([Konvertieren](convert.md#loading-it-in-the-viewer)). Die Dota-2-Karte in 3D darunter:
[3DHeat-Ext-Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

Wenn ein neues Release erscheint, sagt das Werkzeug es beim Start und bietet an, sich
selbst zu aktualisieren (`python -m heat3d_ext_dota_replay.update` macht dasselbe).

## Seiten {#pages}

| Seite | Was sie behandelt |
|---|---|
| [Bevor du anfängst](before-you-start.md) | Python, ein Terminal, ein erster Lauf |
| [Replays finden: list](list.md) | wo Dota 2 Replays speichert, ein Replay holen, was `list` ausgibt |
| [Konvertieren: convert](convert.md) | jede Option, die Tabellen Spalte für Spalte, Laden im Viewer, wie es geprüft wurde |
| [Begriffe und Lizenz](terms.md) | Valves Replays, die Lizenz von gem-dota, dieses Werkzeug als eigenes Projekt |
| [Befehlsreferenz](../cli-reference.md) | jede Option, aus dem Code erzeugt |
| [Diese Dokumentation pflegen](maintaining.md) | die Checkliste für Releases |

## Verwandtes {#related}

- Der 3DHeat-Viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  Dokumentation unter [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Der 3DHeat Watcher führt dieses Werkzeug bei jedem Replay aus, das Dota 2 speichert, und lädt
  Replays öffentlicher Matches anhand der ID herunter: [Dota-2-Replays im Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- Die Dota-2-Karte als 3D-Level unter diesen Tabellen: [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Die 3DHeat-Werkzeuge {#the-3dheat-tools}

| Werkzeug | Was es tut | Code | Dokumentation |
|---|---|---|---|
| 3DHeat-Viewer | zeigt die Daten: Heatmaps, Rennanalyse, Match-Auswertung | [3DHeat](https://github.com/Holdi601/3DHeat) | [Doku](https://holdi601.github.io/3DHeat/) |
| GameFiles | Level und Strecken aus den eigenen Dateien eines Spiels | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [Doku](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | Rundentelemetrie und aus dem Spielvideo nachgebaute Level | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [Doku](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | ein Unreal-Editor-Plugin: ein Level als eine `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [Doku](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike-2-Demos und Karten | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [Doku](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | zeichnet auf, was Spiele veröffentlichen, während du spielst | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [Doku](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War-Thunder-Replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [Doku](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World-of-Tanks-Replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World-of-Warships-Replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [Doku](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad-Server-Demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [Doku](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS-World-Karten als 3D-Level | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [Doku](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2-Sturmovik-Karten als 3D-Level | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [Doku](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | die Dota-2-Karte als 3D-Level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [Doku](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota-2-Replays als Tabellen | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [Doku](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League-of-Legends- und VALORANT-Replays: was sie offen mitbringen | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [Doku](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza-Strecken, Rennen und Autos aus deiner eigenen Installation | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [Doku](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield-Level (Frostbite) als 3D-Level | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [Doku](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive-Strecken | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [Doku](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto-Corsa-Rally-Etappen als Strecken | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [Doku](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma-Reforger-Welten (Enfusion) als 3D-Level | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [Doku](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow-Six-Siege-Match-Replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [Doku](https://holdi601.github.io/3DHeat-Ext-R6/) |
