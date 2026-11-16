---
title: Begriffe und Lizenz
nav_order: 8
lang: "de"
source: terms.md
source_hash: "59d062678c54"
nav_exclude: true
search_exclude: true
---
# Begriffe und Lizenz {#terms-and-licence}

## Valves Replays {#valves-replays}

Dota 2 und seine Replays gehören Valve, das dieses Projekt nicht unterstützt. Dieses Werkzeug
liefert nichts vom Spiel mit und spricht mit keinem Server: Es liest Replay-Dateien auf deinem
Rechner - solche, die der Dota-2-Client für dich gespeichert hat, oder öffentliche, die du
heruntergeladen hast - außerhalb des Spiels, und verändert nichts darin. Dota-2-Replays sind nicht
verschlüsselt; OpenDota, Stratz und Dotabuff lesen sie seit zehn Jahren. Die Tabellen, die es
schreibt, gehören dir zum Ansehen; das Werkzeug zu benutzen ist deine Entscheidung, unter den
Bedingungen, die du für Dota 2 und Steam akzeptiert hast.

Deshalb ist es ein eigenes Paket: Falls Valve je verlangt, dass es verschwindet, geht nur dieses
Paket, und der Viewer, der Watcher und die anderen Werkzeuge bleiben.

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
