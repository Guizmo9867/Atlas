# Atlas — Licences et attributions

Ce qu'on a le droit de faire avec chaque source de données ou chaque outil, et comment le créditer. À mettre à jour dès qu'une nouvelle source de **géométrie** ou de **fond de carte** entre dans le dépôt. Les sources historiques (documents, livres, archives) sont dans le registre des sources.

## Données utilisées dans l'Atlas

| Source | Licence | Ce qu'on en fait | Obligation |
|---|---|---|---|
| **OpenHistoricalMap (OHM)** | CC0 (domaine public), sauf certains objets sous leur licence d'origine | tracés provisoires du Snapshot 0 (`data/geometries/`) | Crédit **demandé mais pas obligatoire** pour la partie CC0. Formule proposée par OHM : « Map data courtesy of the OpenHistoricalMap project, in the public domain unless otherwise noted. » |
| ↳ segments **Kartverket** (limites communales norvégiennes), importés dans OHM | CC BY 4.0 | frontière Finlande–Norvège et URSS–Norvège (Petsamo) | **Crédit obligatoire** : « Kartverket (Norwegian Mapping Authority), CC BY 4.0 » |
| ↳ segments **OCHA / HDX** (limites administratives du Kazakhstan), importés dans OHM | CC BY-IGO | frontières de la RSS kazakhe | **Crédit obligatoire** : « OCHA / Humanitarian Data Exchange, CC BY-IGO » |
| ↳ segments **GURS** (Administration géodésique de Slovénie, e-prostor), importés dans OHM | CC BY 4.0 | frontière sud de l'Autriche (lot 02) | **Crédit obligatoire** : « GURS / e-prostor (Slovénie), CC BY 4.0 » |
| ↳ segments tagués « CC BY 4.0 » sans auteur indiqué (relations URSS et Pologne 1945) | CC BY 4.0 | frontière de l'URSS | origine à identifier ; en attendant, créditer « contributeurs OpenHistoricalMap » |
| **Natural Earth** | domaine public | fond de carte (terres, lacs, fleuves) + découpage du trait de côte | aucune (crédit apprécié) |
| **OpenStreetMap** (tuiles du calque « repères modernes ») | données ODbL ; tuiles soumises à la politique d'usage d'OSM | simple affichage des tuiles, aucune donnée copiée | **Crédit obligatoire** « © OpenStreetMap contributors » (affiché par la carte). Les serveurs de tuiles d'OSM ne sont pas faits pour un site public à fort trafic : **avant la mise en ligne**, passer par un autre fournisseur de tuiles ou héberger les nôtres. Si un jour on **copie** des données OSM dans le corpus, l'ODbL impose le partage à l'identique de la base dérivée : à éviter ou à décider consciemment. |
| **CShapes 2.0** (ETH Zurich) | CC BY-NC-SA 4.0 (**non commercial**, partage à l'identique) | **comparaison uniquement** (repérer des écarts) | Ne jamais copier ses tracés dans l'Atlas. |

Le détail « segment par segment » se trouve dans chaque fichier de géométrie (propriété `licences_segments`), rempli par les scripts `outils/geo/deriver_snapshot0_lot*.py`.

## Logiciels

| Outil | Licence |
|---|---|
| MapLibre GL JS | BSD 3 clauses |
| React | MIT |
| Vite | MIT |
| QGIS (si utilisé pour vectoriser à la main) | GNU GPL (libre) ; les cartes produites avec QGIS n'héritent pas de cette licence |
| Shapely / GEOS, pyproj | BSD / LGPL / MIT |

## Dans l'application

Le bouton ⓘ en bas à droite de la carte affiche les crédits : Natural Earth, OpenHistoricalMap (CC0), Kartverket (CC BY 4.0), GURS Slovénie (CC BY 4.0), OCHA (CC BY-IGO), et OpenStreetMap quand le calque « repères modernes » est actif.

## À décider avant toute publication

- La **licence du code** de l'Atlas (ex. MIT) et celle du **contenu** (fiches, textes, géométries retravaillées), à choisir séparément. L'ouverture du contenu reste à discuter (récap technique, §10).
