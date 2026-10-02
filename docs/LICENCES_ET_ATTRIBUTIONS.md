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
| **Natural Earth** | domaine public | fond de carte (terres, lacs, fleuves) + découpage du trait de côte + position de secours d'une ville (Charleroi) | aucune (crédit apprécié) |
| **Wikidata** | CC0 (domaine public) | position des villes (`data/snapshot0/villes_*.json`), QID noté dans chaque source | aucune (crédit apprécié) |
| **GeoNames** | CC BY 4.0 | position de repérage de 5 villes du lot 1.5 (Ivanovo, Rodniki, Teïkovo, Kokhma, Tchernikovsk) quand Wikidata manquait ou était trop grossier | **Crédit obligatoire** : « GeoNames (geonames.org), CC BY 4.0 » (registre : `src-geonames-ivanovo-textile-reperes`, `src-geonames-tchernikovsk-568834`) |
| **OpenStreetMap** (tuiles du calque « repères modernes ») | données ODbL ; tuiles soumises à la politique d'usage d'OSM | simple affichage des tuiles, aucune donnée copiée | **Crédit obligatoire** « © OpenStreetMap contributors » (affiché par la carte). Les serveurs de tuiles d'OSM ne sont pas faits pour un site public à fort trafic : **avant la mise en ligne**, passer par un autre fournisseur de tuiles ou héberger les nôtres. Si un jour on **copie** des données OSM dans le corpus, l'ODbL impose le partage à l'identique de la base dérivée : à éviter ou à décider consciemment. |
| **Carte West Point n° 31** (US Military Academy, Department of History) | œuvre d'une institution fédérale américaine, en principe domaine public aux États-Unis | géoréférencée pour tracer le front de l'Est et la Courlande (seules des **coordonnées dérivées** sont dans le dépôt, pas l'image) | crédit donné par politesse et traçabilité (registre : `src-westpoint-russian-balkan-baltic-1944`) |
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

Le bouton ⓘ en bas à droite de la carte affiche les crédits : Natural Earth, OpenHistoricalMap (CC0), Kartverket (CC BY 4.0), GURS Slovénie (CC BY 4.0), OCHA (CC BY-IGO), West Point (fronts), et l'Atlas lui-même (CC BY 4.0), et OpenStreetMap quand le calque « repères modernes » est actif.

## Licences de l'Atlas (décidées le 28/09/2026)

- **Code** (`app/`, `outils/`) : **MIT** (fichier `LICENSE`).
- **Données et textes** (`data/`, `docs/`, `gabarits/`) : **CC BY 4.0** (fichier `LICENCE_DONNEES.md`) : réutilisation libre, y compris commerciale, **citation obligatoire**.
- Guizmo reste l'auteur : ces licences ne l'empêchent pas de proposer plus tard une version financée, des services ou une autre licence pour ses propres contributions.

## Règle d'entrée d'une nouvelle source de données

Avant qu'une donnée **copiée** (tracé, point, attribut) entre dans `data/`, vérifier que sa licence permet de la republier sous CC BY 4.0 :

| Licence de la source | Peut entrer dans le corpus ? |
|---|---|
| Domaine public, CC0 | oui |
| CC BY, CC BY-IGO, licence ouverte Etalab / OGL | oui, **avec le crédit** (dans `licences_segments` et le bouton ⓘ) |
| ODbL (OpenStreetMap) | **oui, mais dans un dossier à part** (`data/osm/`, sous ODbL, avec « © OpenStreetMap contributors ») : jamais mélangée aux fichiers CC BY. Une donnée tirée ou retouchée d'OSM (ex. une route de 1945 redessinée sur une route OSM) reste ODbL et va dans ce dossier |
| CC BY-SA | même principe : dossier à part, sous sa propre licence |
| NC (non commercial), ND (pas de modification), « tous droits réservés » | **non** : comparaison, lecture ou citation courte seulement |

Pourquoi OSM à part : l'ODbL autorise tout (y compris public et commercial), mais exige que la base qui **contient** ses données soit partagée sous ODbL. Deux bases posées côte à côte gardent chacune leur licence ; une base où on les a mélangées devient entièrement ODbL. La **carte affichée** (l'image) peut, elle, combiner les deux avec les crédits.

Les documents historiques (livres, archives, articles) ne sont jamais copiés : on les **cite** (référence + court extrait), ce qui reste permis quelle que soit leur licence.
