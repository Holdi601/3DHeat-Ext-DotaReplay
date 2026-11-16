---
title: "Conversione: convert"
nav_order: 3
lang: "it"
source: convert.md
source_hash: "58226d5bc388"
nav_exclude: true
search_exclude: true
---
# Conversione: `convert` {#converting-convert}

```bash
heat3d-dota-replay convert [<replay.dem> or <folder> ...] -o <folder> [--game FOLDER] [--hz N]
```

legge ogni replay e lo scrive come tabelle 3DHeat nella cartella `-o`, con il nome dell'id della partita.
Senza un replay converte ogni `.dem` nella cartella dei replay di Dota ([list](list.md) mostra quale).
Una cartella indicata converte ogni `.dem` che contiene. Codice:
[`heat3d_ext_dota_replay/dota_replay.py`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/heat3d_ext_dota_replay/dota_replay.py).

| Opzione | Fa |
|---|---|
| `<replay.dem>` o `<folder>` | cosa convertire; se ne possono indicare più d'uno (predefinito: la cartella dei replay di Dota) |
| `-o`, `--out FOLDER` | dove vanno le tabelle (obbligatorio); viene creata se manca |
| `--game FOLDER` | la cartella `dota 2 beta`, quando non è indicato alcun replay e Dota 2 non è in nessuna libreria Steam |
| `--hz N` | campioni degli eroi al secondo (predefinito 7,5, ogni quarto dei 30 tick del replay) |

Per ogni replay stampa i due file principali che ha scritto:

```text
tables\7123456789.parquet
tables\7123456789.match.json
```

Una partita lunga richiede uno o due minuti e circa un gigabyte di memoria durante la lettura.

## Cosa esce {#what-comes-out}

| File | Contiene |
|---|---|
| `<match>.parquet` | la tabella da aprire: ogni eroe 7,5 volte al secondo mentre è vivo (posizione, altezza, salute, livello, direzione, mana, esperienza, attributi, armatura, velocità, danno, oggetti, il cursore del giocatore), e ogni evento nel punto in cui è accaduto: uccisioni dove stava l'assassino, morti dove è caduto l'eroe, torri, caserme, Roshan e Tormentor dove sono caduti, vedette dove sono state piazzate e dove sono finite, le voci del combat log sugli eroi, i segnali sulla mappa, i disegni sulla mappa e ogni ordine (movimento, attacco, incantesimo, acquisto, ...) |
| `<match>.units.parquet` | ogni altra unità - creep, evocazioni, illusioni, corrieri, edifici - una volta al secondo |
| `<match>.combatlog.parquet` | l'intero combat log, ogni campo |
| `<match>.match.json` | la partita: squadre, punteggio, vincitore, la riga di ogni giocatore, morti, obiettivi, vedette, draft, chat, tutto il resto che gem-dota estrae, l'intestazione e le informazioni del file di replay, e il record di fine partita del gioco (`matchDetails`, `matchMetadata`); `selfCheck` dice quanto è completa la lettura |
| `<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet` | tutto il resto che il replay contiene, conservato per intero: ogni frame e messaggio di rete, ogni cambio di proprietà delle entità, ogni voce delle string table |

Le posizioni sono nelle unità del mondo di Dota (unità Hammer): x verso est, y verso nord, z verso l'alto; la
mappa giocabile va più o meno da -8200 a 8200 su entrambi gli assi - le stesse unità che riporta l'integrazione
di stato di gioco di Dota 2, così replay e sessione dal vivo coincidono. Il tempo è l'orologio di gioco in
secondi: negativo prima del corno, fermo durante la pausa. Ogni riga ha un `life`: le vite di un eroe contate
da 1, così una traccia finisce dove l'eroe è morto. Tutte le colonne: [Riferimento dei comandi](../cli-reference.md#output).

## Caricarlo nel visualizzatore {#loading-it-in-the-viewer}

Apri `<match>.parquet` nel visualizzatore con **File…** oppure trascinandolo sulla finestra. Il suo piè di pagina
dice al visualizzatore gli assi, le unità e le colonne (i giocatori come persone, le squadre, le vite come sessioni,
la direzione come orientamento), quindi non serve alcuna mappatura. Le tabelle secondarie si aprono allo stesso
modo quando vengono scelte da sole. Per la mappa sottostante in 3D, costruisci il livello di Dota 2 con
[3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Come è stato verificato {#how-it-was-checked}

Su un replay di una partita pubblica: uccisioni, morti, assist, livello, ultimi colpi e negazioni letti dal flusso
coincidono con il record di fine partita del gioco per tutti e dieci i giocatori (`selfCheck.crossCheck` nel file
della partita contiene il confronto per ogni replay), e ogni messaggio nella tabella dei pacchetti viene
riserializzato byte per byte. I test girano solo su dati inventati.

Una nuova patch di Dota può cambiare le entità del replay prima che gem-dota le segua. Un replay che gem-dota
non riesce a leggere fino in fondo viene convertito fin dove arriva e segnato come `incomplete` nel suo file della partita.

## Messaggi e stato di uscita {#messages-and-exit-status}

| Messaggio | Uscita | Significa |
|---|---|---|
| due nomi di file per replay | 0 | fatto |
| `heat3d-dota-replay: no replay (.dem) found in ...` | 2 | nessun file da convertire dove è stato cercato |
| `heat3d-dota-replay: <file>: <file> is not a Source 2 demo ...` | 2 | non è un replay di Dota 2 (un `.dem.bz2` va prima decompresso); tra gli altri che sono stati convertiti: 1 |
| `heat3d-dota-replay: pip install gem-dota ...` | 2 | gem-dota non è installato: `python -m pip install gem-dota` |
| `heat3d-dota-replay: <file>: <error>` | 1 | quel replay è fallito; gli altri vengono comunque convertiti |
