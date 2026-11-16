---
title: "Convertir : convert"
nav_order: 3
lang: "fr"
source: convert.md
source_hash: "58226d5bc388"
nav_exclude: true
search_exclude: true
---
# Convertir : `convert` {#converting-convert}

```bash
heat3d-dota-replay convert [<replay.dem> or <folder> ...] -o <folder> [--game FOLDER] [--hz N]
```

lit chaque replay et l'écrit sous forme de tables 3DHeat dans le dossier `-o`, nommé d'après
l'identifiant du match. Sans replay, il convertit chaque `.dem` du dossier des replays
de Dota ([list](list.md) montre lesquels). Un dossier donné convertit chaque `.dem` qu'il contient.
Code : [`heat3d_ext_dota_replay/dota_replay.py`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/heat3d_ext_dota_replay/dota_replay.py).

| Option | Rôle |
|---|---|
| `<replay.dem>` ou `<folder>` | ce qu'il faut convertir ; plusieurs peuvent être donnés (par défaut : le dossier des replays de Dota) |
| `-o`, `--out FOLDER` | où vont les tables (obligatoire) ; créé s'il manque |
| `--game FOLDER` | le dossier `dota 2 beta`, quand aucun replay n'est donné et que Dota 2 n'est dans aucune bibliothèque Steam |
| `--hz N` | échantillons de héros par seconde (par défaut 7,5, un sur quatre des 30 ticks du replay) |

Pour chaque replay, il affiche les deux fichiers principaux qu'il a écrits :

```text
tables\7123456789.parquet
tables\7123456789.match.json
```

Un long match prend une minute ou deux et environ un gigaoctet de mémoire pendant sa lecture.

## Ce qui en sort {#what-comes-out}

| Fichier | Contient |
|---|---|
| `<match>.parquet` | la table à ouvrir : chaque héros 7,5 fois par seconde tant qu'il est vivant (position, hauteur, vie, niveau, orientation, mana, expérience, attributs, armure, vitesse, dégâts, objets, le curseur du joueur), et chaque événement là où il s'est produit : les kills là où se tenait le tueur, les morts là où le héros est tombé, les tours, casernes, Roshan et les Tormentors là où ils sont tombés, les wards là où ils ont été posés et où ils ont fini, les entrées du journal de combat qui concernent des héros, les pings de la carte, les dessins sur la carte et chaque ordre (déplacer, attaquer, lancer, acheter, ...) |
| `<match>.units.parquet` | chaque autre unité - créatures, invocations, illusions, coursiers, bâtiments - une fois par seconde |
| `<match>.combatlog.parquet` | tout le journal de combat, chaque champ |
| `<match>.match.json` | le document de partie : équipes, score, gagnant, la ligne de chaque joueur, morts, objectifs, wards, la sélection, le chat, tout le reste que gem-dota extrait, l'en-tête et les informations propres du replay, et le relevé de fin de match du jeu (`matchDetails`, `matchMetadata`) ; `selfCheck` dit à quel point la lecture est complète |
| `<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet` | tout le reste que le replay contient, gardé entier : chaque image et chaque message réseau, chaque changement de propriété d'entité, chaque entrée des tables de chaînes |

Les positions sont les unités-monde de Dota (unités Hammer) : x vers l'est, y vers le nord, z vers le haut ; la
carte jouable va d'environ -8200 à 8200 sur les deux axes - les mêmes unités que celles que rapporte
l'intégration d'état de jeu de Dota 2, donc un replay et une session en direct s'alignent. Le temps est
l'horloge de jeu en secondes : négatif avant le coup de sifflet, figé pendant la pause.
Chaque ligne a un `life` : la vie d'un héros comptée à partir de 1, si bien qu'un tracé s'arrête là où le héros est mort. Toutes les colonnes :
[Référence des commandes](../cli-reference.md#output).

## Le charger dans le visualiseur {#loading-it-in-the-viewer}

Ouvrez `<match>.parquet` dans le visualiseur avec **Fichiers…** ou déposez-le sur la fenêtre. Son
pied de page indique au visualiseur les axes, les unités et les colonnes (les joueurs comme des personnes,
les équipes, les vies comme des sessions, l'orientation comme une direction), donc rien n'a besoin d'être relié.
Les tables annexes s'ouvrent de la même façon quand on les choisit seules. Pour la carte en 3D
dessous, construisez le niveau de la carte de Dota 2 avec [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Comment elle a été vérifiée {#how-it-was-checked}

Sur le replay d'un match public : les kills, morts, assistances, niveau, derniers coups et dénis
lus dans le flux correspondent au relevé de fin de match du jeu pour les dix
joueurs (`selfCheck.crossCheck` dans le document de partie contient la comparaison pour chaque replay), et chaque
message de la table des paquets se re-sérialise octet pour octet. Les tests ne tournent que sur des
données inventées.

Un nouveau patch de Dota peut changer les entités du replay avant que gem-dota ne suive.
Un replay que gem-dota ne sait pas lire jusqu'au bout est converti jusqu'où il peut, et
marqué `incomplete` dans son document de partie.

## Messages et code de sortie {#messages-and-exit-status}

| Message | Code | Signification |
|---|---|---|
| deux noms de fichiers par replay | 0 | terminé |
| `heat3d-dota-replay: no replay (.dem) found in ...` | 2 | rien à convertir à l'endroit cherché |
| `heat3d-dota-replay: <file>: <file> is not a Source 2 demo ...` | 2 | pas un replay de Dota 2 (un `.dem.bz2` doit d'abord être décompressé) ; parmi d'autres qui ont été convertis : 1 |
| `heat3d-dota-replay: pip install gem-dota ...` | 2 | gem-dota n'est pas installé : `python -m pip install gem-dota` |
| `heat3d-dota-replay: <file>: <error>` | 1 | ce replay a échoué ; les autres sont tout de même convertis |
