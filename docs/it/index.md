---
title: Home
nav_order: 1
lang: "it"
source: index.md
source_hash: "df20c820922e"
nav_exclude: true
search_exclude: true
permalink: /it/
---
# 3DHeat Dota Replay {#dheat-dota-replay}

**Che cos'è?** Questo strumento legge i replay di Dota 2 (file `.dem`) e scrive ciò che vi è accaduto
come tabelle per il visualizzatore [3DHeat](https://github.com/Holdi601/3DHeat)
([documentazione](https://holdi601.github.io/3DHeat/)): il percorso di ogni eroe sulla mappa, ogni
uccisione, torre, vedetta, segnale e ordine nel punto in cui è avvenuto, e l'intera partita.

**Perché usarlo?** Per vedere una partita di Dota 2 - la tua o una pubblica qualsiasi - come mappa di calore
e replay sulla mappa: dove un eroe ha passato la partita, dove c'erano i combattimenti, dove sono finite le vedette.

**Esempio:** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet`, la tabella da aprire nel visualizzatore, con la partita e le
tabelle secondarie accanto.

## Avvio rapido {#quick-start}

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).
Ti servono Python 3.10 o successivo e un replay: scaricane uno in Dota 2 (i dettagli di una partita,
**Download replay**), e finisce nella cartella dei replay di Dota. Esegui questi comandi nella cartella in cui
hai clonato o decompresso lo strumento:

```bash
python -m pip install -e .                  # installa heat3d-dota-replay e gem-dota
heat3d-dota-replay list                     # dove Dota 2 salva i replay, quelli presenti
heat3d-dota-replay convert -o tables        # tutti i replay presenti, come tabelle
```

`list` stampa la cartella dei replay di Dota e una riga per replay; `convert` stampa i due file
scritti per ciascuno, `tables/<match>.parquet` e `tables/<match>.match.json`. Apri il `.parquet` nel
visualizzatore con **File…** o trascinandolo sulla finestra ([Conversione](convert.md#loading-it-in-the-viewer)).

## Pagine {#pages}

| Pagina | Cosa contiene |
|---|---|
| [Prima di iniziare](before-you-start.md) | Python, un terminale, una prima esecuzione |
| [Trovare i replay: list](list.md) | dove Dota 2 salva i replay, come ottenerne uno, cosa stampa `list` |
| [Conversione: convert](convert.md) | ogni opzione, le tabelle colonna per colonna, come caricarle, come sono state verificate |
| [Termini e licenza](terms.md) | i replay di Valve, la licenza di gem-dota, perché è un pacchetto separato |
| [Riferimento dei comandi](../cli-reference.md) | ogni opzione, generata dal codice |
| [Manutenzione di questa documentazione](maintaining.md) | la lista di controllo per ogni rilascio |

## Collegamenti {#related}

- Il visualizzatore 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentazione su [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Il 3DHeat Watcher esegue questo strumento su ogni replay che Dota 2 salva, e scarica i replay
  delle partite pubbliche per id: [replay di Dota 2 nel Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- La mappa di Dota 2 come livello 3D sotto queste tabelle: [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Gli strumenti 3DHeat {#the-3dheat-tools}

| Strumento | Cosa fa | Codice | Documentazione |
|---|---|---|---|
| visualizzatore 3DHeat | mostra i dati: mappe di calore, analisi di gara, revisione delle partite | [3DHeat](https://github.com/Holdi601/3DHeat) | [documentazione](https://holdi601.github.io/3DHeat/) |
| GameFiles | livelli e percorsi dai file propri di un gioco | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [documentazione](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetria dei giri, e livelli ricostruiti dal video di gioco | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [documentazione](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin per Unreal Editor: un livello come un unico `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [documentazione](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demo e mappe di Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [documentazione](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra ciò che i giochi pubblicano mentre giochi | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [documentazione](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replay di War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replay di World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replay di World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [documentazione](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demo dei server di Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mappe di DCS World come livelli 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [documentazione](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mappe di IL-2 Sturmovik come livelli 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [documentazione](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la mappa di Dota 2 come livello 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replay di Dota 2 | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [documentazione](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replay di League of Legends e VALORANT: ciò che contengono in chiaro | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | percorsi, gare e auto di Forza dalla tua installazione | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | livelli di Battlefield (Frostbite) come livelli 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | percorsi di BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [documentazione](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tappe di Assetto Corsa Rally come percorsi | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [documentazione](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondi di Arma Reforger (Enfusion) come livelli 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [documentazione](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replay di partite di Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [documentazione](https://holdi601.github.io/3DHeat-Ext-R6/) |
