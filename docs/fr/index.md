---
title: "Accueil"
nav_order: 1
lang: "fr"
source: index.md
source_hash: "ec2b5e26aa1a"
nav_exclude: true
search_exclude: true
permalink: /fr/
---
# 3DHeat Dota Replay {#dheat-dota-replay}

**Qu'est-ce que c'est ?** Cet outil lit les replays de Dota 2 (fichiers `.dem`) et écrit ce qui s'y
est passé sous forme de tables pour le visualiseur [3DHeat](https://github.com/Holdi601/3DHeat)
([documentation](https://holdi601.github.io/3DHeat/)) : le chemin de chaque héros sur la carte, chaque kill, tour, ward, ping et ordre là où il a eu lieu, et tout le match.

**À quoi cela sert-il ?** À voir un match de Dota 2 - le vôtre ou n'importe quel match public - en carte de chaleur
et en replay sur la carte : où un héros a passé la partie, où ont eu lieu les combats, où sont allés les wards.

**Exemple :** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet`, la table à ouvrir dans le visualiseur, avec le document de partie
et les tables annexes à côté.

**Un projet à part :** Chaque lecteur de jeu est un petit projet à part, avec son propre
fichier de licence, ses propres versions et son propre suivi des tickets : il peut être
installé, mis à jour, maintenu - ou retiré à la demande d'un ayant droit - seul, sans
toucher au visualiseur ni aux autres outils.

## Démarrage rapide {#quick-start}

Vous ne connaissez pas la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).
Il vous faut Python 3.10 ou plus récent et un replay : téléchargez-en un dans Dota 2 (les détails d'un
match, **Download replay**), et il atterrit dans le dossier des replays de Dota. Lancez ces commandes
dans le dossier où vous avez cloné ou décompressé l'outil :

```bash
python -m pip install -e .                  # installe heat3d-dota-replay et gem-dota
heat3d-dota-replay list                     # où Dota 2 enregistre les replays, ceux qui s'y trouvent
heat3d-dota-replay convert -o tables        # chaque replay de là, en tables
```

`list` affiche le dossier des replays de Dota et une ligne par replay ; `convert` affiche les
deux fichiers écrits pour chacun, `tables/<match>.parquet` et
`tables/<match>.match.json`. Ouvrez le `.parquet` dans le visualiseur avec **Fichiers…**
ou en le déposant sur la fenêtre ([Convertir](convert.md#loading-it-in-the-viewer)).

## Pages {#pages}

| Page | Ce qu'elle couvre |
|---|---|
| [Avant de commencer](before-you-start.md) | Python, un terminal, un premier lancement |
| [Trouver les replays : list](list.md) | où Dota 2 enregistre les replays, en obtenir un, ce qu'affiche `list` |
| [Convertir : convert](convert.md) | chaque option, les tables colonne par colonne, les charger, comment elles ont été vérifiées |
| [Conditions et licence](terms.md) | les replays de Valve, la licence de gem-dota, cet outil comme projet à part |
| [Référence des commandes](../cli-reference.md) | chaque option, générée à partir du code |
| [Maintenance de ces documents](maintaining.md) | la liste de contrôle des versions |

## Liens utiles {#related}

- Le visualiseur 3DHeat : [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation sur [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Le 3DHeat Watcher lance cet outil sur chaque replay que Dota 2 enregistre, et télécharge les replays
  de matchs publics par identifiant : [Replays Dota 2 dans le Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- La carte de Dota 2 en niveau 3D sous ces tables : [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Les outils 3DHeat {#the-3dheat-tools}

| Outil | Ce qu'il fait | Code | Documentation |
|---|---|---|---|
| visualiseur 3DHeat | montre les données : cartes de chaleur, analyse de course, revue de match | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveaux et parcours tirés des fichiers d'un jeu | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | télémétrie de tours, et niveaux reconstruits à partir de vidéos de jeu | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin pour l'éditeur Unreal : un niveau en un seul `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | démos et cartes de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | enregistre ce que les jeux publient pendant que vous jouez | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replays de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replays de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replays de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | démos de serveurs Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | cartes de DCS World en niveaux 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | cartes d'IL-2 Sturmovik en niveaux 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | la carte de Dota 2 en niveau 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | replays de Dota 2 en tables | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | replays de League of Legends et VALORANT : ce qu'ils contiennent en clair | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | parcours, courses et voitures de Forza tirés de votre propre installation | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveaux de Battlefield (Frostbite) en niveaux 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | parcours de BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | étapes d'Assetto Corsa Rally en parcours | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mondes d'Arma Reforger (Enfusion) en niveaux 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | replays de matchs de Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |
