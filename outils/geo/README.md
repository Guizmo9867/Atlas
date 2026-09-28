# Outils géographiques

Scripts qui **fabriquent** les géométries du corpus. Ils servent de trace d'audit : on peut les relire, les relancer et contester chaque opération.

- `ohm_outils.py` : fonctions communes (téléchargement OpenHistoricalMap, reconstruction des polygones, trait de côte Natural Earth, licences par segment).
- `deriver_snapshot0_lot01.py` : Snapshot 0, lot 01 (URSS, RSS kazakhe, Touva, Mongolie, Finlande, Petsamo, Porkkala). L'URSS y est corrigée de la Pologne du lot 02.
- `deriver_snapshot0_lot02.py` : Snapshot 0, lot 02 (Allemagne 1937, Autriche, Pologne, frontière Pologne–URSS, RSS baltes, Memel, Dantzig).
- `deriver_snapshot0_fronts.py` : fronts du Snapshot 0. Télécharge la carte West Point n° 31, la **géoréférence** (projection conique de Lambert + déformation « plaque mince » sur les points d'appui), extrait le trait rouge du 31/12/1944 et en tire le front de l'Est et la poche de Courlande ; la Laponie vient du cours de la Lätäseno (OHM). Affiche l'erreur de géoréférencement (validation croisée).
- `deriver_snapshot0_lot03.py` : Snapshot 0, lot 03 (Nord et Ouest) : 13 États depuis OHM, puis zones de contrôle dérivées du front de l'Ouest (carte LOC du 01/01/1945) et des poches (cartes West Point 71 et 75a). Le géoréférencement de ces cartes est dans `lot03/` (voir son README).
- `points_appui_westpoint_map31.py` : les 23 points d'appui (ville, coordonnées réelles, position en pixels sur la carte), à relire si on conteste le calage.

Pour relancer (nécessite Python 3 et Internet), depuis la racine du dépôt :

```
pip install shapely pyproj numpy scipy scikit-image networkx pillow
python outils/geo/deriver_snapshot0_lot02.py . ./cache_geo
python outils/geo/deriver_snapshot0_lot01.py . ./cache_geo
python outils/geo/deriver_snapshot0_fronts.py . ./cache_geo
python outils/geo/deriver_snapshot0_lot03.py . ./cache_geo
```

Le dossier `cache_geo/` (téléchargements bruts) ne va pas dans Git.
