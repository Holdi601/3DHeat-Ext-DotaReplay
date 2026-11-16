---
title: "Konvertieren: convert"
nav_order: 3
lang: "de"
source: convert.md
source_hash: "58226d5bc388"
nav_exclude: true
search_exclude: true
---
# Konvertieren: `convert` {#converting-convert}

```bash
heat3d-dota-replay convert [<replay.dem> or <folder> ...] -o <folder> [--game FOLDER] [--hz N]
```

liest jedes Replay und schreibt es als 3DHeat-Tabellen in den `-o`-Ordner, benannt nach
der Match-ID. Ohne Replay konvertiert es jede `.dem` im Replay-Ordner von Dota
([list](list.md) zeigt, wo das ist). Ein angegebener Ordner konvertiert jede `.dem`
darin. Code: [`heat3d_ext_dota_replay/dota_replay.py`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/heat3d_ext_dota_replay/dota_replay.py).

| Option | Macht |
|---|---|
| `<replay.dem>` oder `<folder>` | was konvertiert wird; mehrere sind möglich (Standard: der Replay-Ordner von Dota) |
| `-o`, `--out FOLDER` | wohin die Tabellen kommen (Pflicht); wird angelegt, wenn er fehlt |
| `--game FOLDER` | der Ordner `dota 2 beta`, wenn kein Replay angegeben ist und Dota 2 in keiner Steam-Bibliothek liegt |
| `--hz N` | Heldenproben pro Sekunde (Standard 7,5, jede vierte der 30 Ticks des Replays) |

Für jedes Replay gibt es die zwei Hauptdateien aus, die es geschrieben hat:

```text
tables\7123456789.parquet
tables\7123456789.match.json
```

Ein langes Match braucht eine oder zwei Minuten und beim Lesen etwa ein Gigabyte Speicher.

## Was herauskommt {#what-comes-out}

| Datei | Enthält |
|---|---|
| `<match>.parquet` | die Tabelle zum Öffnen: jeder Held 7,5-mal pro Sekunde, solange er lebt (Position, Höhe, Leben, Stufe, Blickrichtung, Mana, Erfahrung, Attribute, Rüstung, Tempo, Schaden, Gegenstände, der Mauszeiger des Spielers), und jedes Ereignis dort, wo es passierte: Kills, wo der Killer stand, Tode, wo der Held fiel, Türme, Kasernen, Roshan und Tormentors, wo sie fielen, Wards, wo sie gesetzt wurden und wo sie endeten, die Einträge des Combat Log zu Helden, Kartenmarkierungen, Zeichnungen auf der Karte und jeder Befehl (Bewegen, Angreifen, Zaubern, Kaufen, ...) |
| `<match>.units.parquet` | jede andere Einheit - Creeps, Beschworene, Illusionen, Kuriere, Gebäude - einmal pro Sekunde |
| `<match>.combatlog.parquet` | das ganze Combat Log, jedes Feld |
| `<match>.match.json` | das Match: Teams, Stand, Sieger, die Zeile jedes Spielers, Tode, Ziele, Wards, das Draft, der Chat, alles Weitere, was gem-dota herauslöst, der eigene Dateikopf und die Infos des Replays sowie der Endbericht des Spiels (`matchDetails`, `matchMetadata`); `selfCheck` sagt, wie vollständig das Lesen war |
| `<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet` | alles andere, was das Replay enthält, ungekürzt: jeder Frame und jede Netzwerknachricht, jede Änderung an Entity-Eigenschaften, jeder Eintrag der String-Tabellen |

Positionen sind Dotas Weltkoordinaten (Hammer-Einheiten): x nach Osten, y nach Norden,
z nach oben; die spielbare Karte reicht auf beiden Achsen etwa von -8200 bis 8200 - dieselben
Einheiten, die die Game-State-Integration von Dota 2 meldet, sodass Replay und Live-Sitzung
zusammenpassen. Die Zeit ist die Spieluhr in Sekunden: negativ vor dem Horn, stehend bei
Pause. Jede Zeile hat ein `life`: die Leben eines Helden, ab 1 gezählt, sodass eine Spur endet,
wo der Held starb. Alle Spalten: [Befehlsreferenz](../cli-reference.md#output).

## In den Viewer laden {#loading-it-in-the-viewer}

Öffne `<match>.parquet` im Viewer mit **Dateien…** oder ziehe die Datei auf das Fenster.
Ihr Footer sagt dem Viewer die Achsen, Einheiten und Spalten (Spieler als Personen, Teams,
Leben als Sitzungen, Blickrichtung als Richtung), sodass nichts zugeordnet werden muss. Die
Nebentabellen öffnen sich genauso, wenn man sie allein auswählt. Für die Karte darunter in
3D baue das Dota-2-Level mit [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## So wurde es geprüft {#how-it-was-checked}

Bei einem öffentlichen Match-Replay stimmen Kills, Tode, Assists, Stufe, Last Hits und Denies,
die aus dem Stream gelesen werden, mit dem Endbericht des Spiels für alle zehn Spieler überein
(`selfCheck.crossCheck` in der Match-Datei enthält den Vergleich für jedes Replay), und jede
Nachricht in der Packets-Tabelle wird Byte für Byte wieder serialisiert. Die Tests laufen nur
mit erfundenen Daten.

Ein neuer Dota-Patch kann die Entities des Replays ändern, bevor gem-dota nachzieht. Ein Replay,
das gem-dota nicht bis zum Ende lesen kann, wird so weit konvertiert, wie es geht, und in seiner
Match-Datei als `incomplete` markiert.

## Meldungen und Exit-Status {#messages-and-exit-status}

| Meldung | Exit | Bedeutung |
|---|---|---|
| zwei Dateinamen pro Replay | 0 | fertig |
| `heat3d-dota-replay: no replay (.dem) found in ...` | 2 | dort, wo gesucht wurde, gibt es nichts zu konvertieren |
| `heat3d-dota-replay: <file>: <file> is not a Source 2 demo ...` | 2 | kein Dota-2-Replay (eine `.dem.bz2` muss zuerst entpackt werden); unter anderen, die konvertiert wurden: 1 |
| `heat3d-dota-replay: pip install gem-dota ...` | 2 | gem-dota ist nicht installiert: `python -m pip install gem-dota` |
| `heat3d-dota-replay: <file>: <error>` | 1 | dieses Replay ist fehlgeschlagen; die anderen werden trotzdem konvertiert |
