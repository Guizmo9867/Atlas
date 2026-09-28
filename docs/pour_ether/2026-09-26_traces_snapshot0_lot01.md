# Atlas — Premiers tracés du Snapshot 0 (lot 01) : ce qui est fait, ce qu'il faut sourcer

*De Claude, pour Ether. Transmis par Guizmo le 26/09/2026.*

Les 7 entités du lot 01 ont maintenant un **tracé provisoire** au 1er janvier 1945, 0 h 00. Tout est dans `data/geometries/snapshot0/` : un fichier par géométrie, qui contient aussi sa provenance et ses points à vérifier. La méthode complète est rejouable : `outils/geo/deriver_snapshot0_lot01.py`.

## Méthode

1. **OpenHistoricalMap (OHM)** : extraction des frontières datées valides au 01/01/1945. Licence CC0, donc réutilisable librement. Niveau **C** dans le registre : c'est une référence de comparaison, pas une base de vérité. D'où le statut « provisoire ».
2. **Natural Earth 1:10m** : OHM inclut les eaux territoriales, on ne garde que les terres (côtes précises à environ 1 km).
3. **Petsamo et Porkkala** : ils n'existent pas comme territoires dans OHM. Je les ai calculés : « Finlande 1940-1944 » moins « Finlande après l'armistice ». La partie nord donne Petsamo, la partie sud Porkkala.
4. **Porkkala** est retiré de l'URSS (OHM la compte comme soviétique) et rattaché à la Finlande, parce que notre modèle dit : souveraineté finlandaise, contrôle soviétique.
5. **Contrôle croisé avec CShapes 2.0** (ETH Zurich, jeu de données universitaire). Attention, sa licence est **non commerciale** : il sert uniquement à repérer les écarts, on ne copie jamais ses tracés.
6. **Vérifications automatiques** : chaque « enfant » est bien contenu dans son « parent » (Kazakhstan, Touva et Petsamo dans l'URSS, Porkkala dans la Finlande), à 0 km² près.

| Entité | Surface obtenue | Source du tracé |
|---|---|---|
| URSS | 22 066 000 km² | OHM relation 2957472 (1944-10-11 → 1945-08-01) |
| RSS kazakhe | 2 712 000 km² | OHM relation 2697958 |
| Touva (oblast autonome) | 169 000 km² | OHM relation 2958149 |
| Mongolie extérieure | 1 559 000 km² | OHM relation 2942671 |
| Finlande (avec Porkkala) | 335 500 km² | OHM relation 2855285 + Porkkala |
| Petsamo | 11 200 km² | OHM 2692833 − OHM 2855285 (partie nord) |
| Porkkala (terres) | 200 km² | OHM 2692833 − OHM 2855285 (partie sud) |

## Ce qu'il faut sourcer (par ordre d'importance)

### 1. Frontière soviéto-polonaise au 01/01/1945 : une DÉCISION à prendre

OHM place Białystok et Przemyśl côté soviétique, selon la ligne de 1941. Or :

- l'**accord URSS–PKWN du 27/07/1944** prévoit leur retour à la Pologne ;
- la région de Białystok serait passée **sous administration polonaise (PKWN) dès l'automne 1944** ;
- CShapes, lui, garde la frontière polonaise **d'avant-guerre** jusqu'au 07/05/1945, soit environ 200 000 km² d'écart en Biélorussie et Ukraine occidentales. C'est la lecture « reconnaissance internationale ».

**À trouver** : le texte de l'accord du 27/07/1944, et la date réelle du passage de Białystok et de Przemyśl sous administration polonaise.

**À trancher avec Guizmo** : dans ce cas, que met-on dans `souverainete_id` et `controle_id` ?

### 2. États baltes

Ils sont inclus dans l'URSS (annexion de 1940). Mais les États-Unis et le Royaume-Uni ne l'ont pas reconnue : c'est à écrire dans `note`. La **poche de Courlande**, tenue par l'armée allemande au 01/01/1945, relève de la future couche contrôle / ligne de front.

### 3. District de Bostanliq (RSS kazakhe)

OHM reprend la frontière moderne du Kazakhstan. Or le district de Bostanliq (vers 70°E, 41,6°N) était kazakh en 1945 et n'a été transféré à la RSS ouzbèke qu'en **1956**. Il manque probablement dans notre tracé. **À sourcer**, puis je corrige la géométrie.

### 4. Frontière sino-mongole

Elle n'a été délimitée qu'en **1962**, et OHM utilise le tracé moderne. CShapes donne environ 5 800 km² de plus à la Mongolie vers 116,6°E 47,7°N (secteur de Khalkhin Gol / Nomonhan), plus deux zones d'environ 1 100 km². **À sourcer** avec une carte des années 1940.

### 5. Touva

Le tracé vient des limites administratives modernes russes. À comparer avec une carte de 1944-1945, surtout pour la frontière Touva–Mongolie.

### 6. Surfaces à confronter

- **Petsamo** : nous obtenons environ 11 200 km² de terres. Quelle surface donnent les sources historiques ?
- **Porkkala** : environ 200 km² de terres seulement. Le bail couvrait aussi des eaux (environ 1 000 km² au total selon les sources secondaires). Une carte du bail serait idéale.

## Ce qui est bon (vérifié)

Au 01/01/1945, ces territoires sont bien **exclus** de l'URSS : Königsberg, Memel/Klaipėda, la Ruthénie subcarpatique (traité du 29/06/1945), Sakhaline du Sud et les Kouriles (août-septembre 1945).

Ils sont bien **inclus** : Vyborg, la Bessarabie, la Bucovine du Nord, Petsamo, Touva (depuis le 11/10/1944) et Pechory.

## Pour aller plus loin : cartes d'archives

Pour passer de « provisoire » à « confirmé », l'idéal est une **carte de 1944-1945 à grande échelle**, par exemple :

- les cartes de situation de la Library of Congress (déjà dans le registre pour le front Ouest) ;
- les cartes AMS (Army Map Service) ;
- les atlas soviétiques de 1945.

Si tu trouves une carte numérisée en haute définition, avec son lien et ses droits d'usage, Claude peut la **géoréférencer** et comparer le tracé point par point avec OHM.

Chaque confirmation fera passer le fichier au statut `confirme`, avec la source A/B ajoutée.
