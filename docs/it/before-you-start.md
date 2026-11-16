---
title: Prima di iniziare
nav_order: 1.5
lang: "it"
source: before-you-start.md
source_hash: "b1cdff264868"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta da zero a una prima esecuzione.
Richiede circa dieci minuti, una volta sola.

## 1. Installa Python {#install-python}

Questo strumento richiede **Python 3.10 o successivo**.

- **Windows:** scarica Python da [python.org/downloads](https://www.python.org/downloads/)
  ed esegui il programma di installazione. Nella sua prima schermata spunta **Add python.exe to PATH**,
  poi clicca su **Install Now**.
- **macOS e Linux:** Python 3 spesso c'è già. Dove queste pagine dicono
  `python`, scrivi `python3`.

## 2. Ottieni questo strumento {#get-this-tool}

Apri [github.com/Holdi601/3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay), clicca sul
pulsante verde **Code**, poi su **Download ZIP**, e decomprimilo in una cartella a tua scelta.
Se usi git: `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay`.

## 3. Apri un terminale in quella cartella {#open-a-terminal-in-that-folder}

Un terminale è una finestra in cui scrivi i comandi.

- **Windows:** apri la cartella in Esplora risorse, clicca nella barra degli indirizzi, scrivi
  `powershell` e premi Invio. Si apre una finestra blu o nera, già in quella cartella.
- **macOS:** apri **Terminale**, scrivi `cd ` (con lo spazio), trascina la cartella nella
  finestra e premi Invio.

`cd` significa "cambia cartella": `cd C:\Tools\3DHeat-Ext-DotaReplay` va in quella cartella.

## 4. Installa lo strumento {#install-the-tool}

Scrivi questo e premi Invio:

```bash
python -m pip install -e .
```

Installa lo strumento e gem-dota, il parser dei replay da cui legge. Alla fine dovresti vedere:
`Successfully installed ... gem-dota-... heat3d-ext-dota-replay-...`.

## 5. Procurati un replay ed eseguilo {#get-a-replay-and-run-it}

In Dota 2, apri i dettagli di una partita e clicca su **Download replay** (oppure Watch >
Replays). Poi:

```bash
heat3d-dota-replay list
```

Dovresti vedere qualcosa del genere:

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
1 replay(s)
```

Avanti: [Conversione: convert](convert.md).

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

| Vedi | Significa |
|---|---|
| `<match>` | un segnaposto: scrivi invece il tuo valore, senza i `< >` |
| `[--hz N]` | facoltativo: omettilo, oppure scrivilo come mostrato |
| `# a note` | un commento per te: non scriverlo |
| `"C:\My Files\x"` | metti tra virgolette un percorso che contiene spazi |

## Quando qualcosa va storto {#when-something-goes-wrong}

| Il messaggio | Cosa fare |
|---|---|
| `'python' is not recognized` | Python non è installato, oppure non era spuntata la casella PATH: installalo di nuovo e spuntala (o scrivi `py` al posto di `python`). |
| `'heat3d-dota-replay' is not recognized` | Esegui di nuovo il passo 4 nella cartella dello strumento, oppure scrivi `python -m heat3d_ext_dota_replay` al posto di `heat3d-dota-replay`: fa la stessa cosa. |
| `pip install gem-dota (the Dota 2 replay parser, MIT)` | Il passo 4 non ha installato gem-dota: esegui `python -m pip install gem-dota`. |
| `Dota 2 not found in any Steam library` | Installa Dota 2 tramite Steam, indica la sua cartella con `--game`, oppure dai a `convert` il percorso del replay. |
| `... is not a Source 2 demo` | Il file non è un replay di Dota 2; un `.dem.bz2` va prima decompresso. |
| qualsiasi altra cosa | Leggi l'ultima riga del messaggio, poi apri una segnalazione su GitHub con quella riga. |

Ogni comando termina anche con uno **stato di uscita**: 0 significa che ha funzionato, 2 che
non c'era nulla da leggere (nessun replay, file non valido, gem-dota mancante), 1 che la lettura di un replay è
fallita. Per vederlo, scrivi `echo $LASTEXITCODE` in PowerShell oppure `echo $?` su macOS e Linux.
