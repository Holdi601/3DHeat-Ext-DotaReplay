---
title: Begriffe und Lizenz
nav_order: 8
lang: "de"
source: terms.md
source_hash: "46ff3a8c7213"
nav_exclude: true
search_exclude: true
---
# Begriffe und Lizenz {#terms-and-licence}

## Valves Replays {#valves-replays}

3DHeat Dota Replay ist weder mit Valve verbunden noch von Valve unterstützt. Dota 2 und zugehörige
Namen und Marken gehören ihren Inhabern. Dieses Werkzeug liefert nichts vom Spiel mit und spricht
mit keinem Server: Es liest Replay-Dateien auf deinem Rechner - solche, die der Dota-2-Client für
dich gespeichert hat, oder öffentliche, die du heruntergeladen hast - außerhalb des Spiels, und
verändert nichts darin. Dota-2-Replays sind nicht verschlüsselt. Die Tabellen, die es schreibt,
bleiben auf deinem Rechner.

## Ein eigenes Projekt {#its-own-project}

Jeder Spiel-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei, eigenen Releases und
eigenem Issue-Tracker. So lässt er sich für sich allein installieren, aktualisieren, pflegen – oder
auf Wunsch eines Rechteinhabers zurückziehen –, ohne den Viewer oder die anderen Werkzeuge zu
berühren.

Rechteinhaber: Eröffnet ein Issue unter
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) – wir
antworten schnell und entfernen auf Wunsch alles.

## gem-dota {#gem-dota}

Das Replay-Format (Source-2-Demos: komprimierte Protobuf-Pakete und Entity-Änderungen) wird von
gem-dota dekodiert (MIT-Lizenz,
[github.com/whanyu1212/gem-dota](https://github.com/whanyu1212/gem-dota)), das pip als Abhängigkeit
installiert. Es wird als Bibliothek benutzt; kein Code daraus wird in dieses Werkzeug kopiert. Der
eigene Teil dieses Werkzeugs fragt es nach Fakten, misst die Helden im selben Durchgang, ordnet die
Ereignisse ein und schreibt die Tabellen. Siehe
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSES.md).

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSE)).
Braucht gem-dota (MIT) und was es mitbringt, numpy (BSD-3-Clause) und pyarrow
(Apache-2.0); die Tests brauchen pytest (MIT). Für dieses Projekt geschrieben, zuerst als Teil des
3DHeat Watcher; kein Code wurde aus einem anderen Projekt übernommen.
