---
title: Termini e licenza
nav_order: 8
lang: "it"
source: terms.md
source_hash: "46ff3a8c7213"
nav_exclude: true
search_exclude: true
---
# Termini e licenza {#terms-and-licence}

## I replay di Valve {#valves-replays}

3DHeat Dota Replay non è affiliato a Valve né approvato da Valve. Dota 2 e i nomi e i marchi
correlati appartengono ai rispettivi proprietari. Questo strumento non include nulla del gioco e non
parla con nessun server: legge i file dei replay sul tuo computer - quelli che il client di Dota 2
ha salvato per te, o quelli pubblici che hai scaricato - al di fuori del gioco, e non vi modifica
nulla. I replay di Dota 2 non sono cifrati. Le tabelle che scrive restano sul tuo computer.

## Un progetto a sé {#its-own-project}

Ogni lettore di un gioco è un piccolo progetto a sé, con il proprio file di licenza, i propri
rilasci e il proprio tracker delle issue, così può essere installato, aggiornato, mantenuto - o
ritirato su richiesta di un titolare dei diritti - da solo, senza toccare il visualizzatore o gli
altri strumenti.

Titolari dei diritti: aprite una issue su
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) -
rispondiamo in fretta e rimuoviamo qualsiasi cosa su richiesta.

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
