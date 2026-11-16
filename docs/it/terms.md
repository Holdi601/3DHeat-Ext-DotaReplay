---
title: Termini e licenza
nav_order: 8
lang: "it"
source: terms.md
source_hash: "59d062678c54"
nav_exclude: true
search_exclude: true
---
# Termini e licenza {#terms-and-licence}

## I replay di Valve {#valves-replays}

Dota 2 e i suoi replay appartengono a Valve, che non approva questo progetto. Questo
strumento non include nulla del gioco e non parla con nessun server: legge i file dei replay sul tuo
computer - quelli che il client di Dota 2 ha salvato per te, o quelli pubblici che hai scaricato - al
di fuori del gioco, e non vi modifica nulla. I replay di Dota 2 non sono cifrati; OpenDota, Stratz e
Dotabuff li leggono da dieci anni. Le tabelle che scrive sono tue da visualizzare; usare lo strumento è una
tua decisione, secondo i termini che hai accettato per Dota 2 e Steam.

Per questo è un pacchetto a sé: se Valve un giorno chiedesse di ritirarlo, andrebbe ritirato da solo,
e il visualizzatore, il Watcher e gli altri strumenti restano.

## gem-dota {#gem-dota}

Il formato dei replay (demo di Source 2: pacchetti protobuf compressi e delta delle entità) è decodificato da
gem-dota (licenza MIT, [github.com/whanyu1212/gem-dota](https://github.com/whanyu1212/gem-dota)),
che pip installa come dipendenza. Viene usato come libreria; nessun suo codice è copiato in questo strumento.
La parte propria di questo strumento gli chiede i fatti, campiona gli eroi nello stesso passaggio, colloca gli
eventi e scrive le tabelle. Vedi [`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSES.md).

## Licenza e fonti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSE)).
Richiede gem-dota (MIT) e ciò che porta con sé, numpy (BSD-3-Clause) e pyarrow
(Apache-2.0); i test richiedono pytest (MIT). Scritto per questo progetto, prima come parte del
3DHeat Watcher; nessun codice è stato preso da altri progetti.
