---
title: Startseite
nav_order: 1
lang: "de"
source: index.md
source_hash: "ec2b5e26aa1a"
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

Neu auf der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).
Du brauchst Python 3.10 oder neuer und ein Replay: Lade eines in Dota 2 herunter (die Details
eines Matches, **Download replay**), es landet im Replay-Ordner von Dota. Führe diese Befehle
in dem Ordner aus, den du geklont oder entpackt hast:

```bash
python -m pip install -e .                  # installs heat3d-dota-replay and gem-dota
heat3d-dota-replay list                     # where Dota 2 saves replays, the ones there
heat3d-dota-replay convert -o tables        # every replay there, as tables
```

`list` zeigt den Replay-Ordner von Dota und eine Zeile pro Replay; `convert` zeigt die zwei
Dateien, die es für jedes geschrieben hat, `tables/<match>.parquet` und
`tables/<match>.match.json`. Öffne die `.parquet` im Viewer mit **Dateien…** oder indem du sie auf
das Fenster ziehst ([Konvertieren](convert.md#loading-it-in-the-viewer)).

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
