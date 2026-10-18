# subdivisions_2-GB — Royaume-Uni au 01/01/1945 (lot 2.GB)

- Fichier : `data/snapshot0/subdivisions_2-GB.json` (197 subdivisions, toutes à l'échelon 1).
- Livraison d'Ether du 18/10/2026 (cycle 1), intégrée par Claude le 18/10/2026 (réveil automatique) avec `outils/subdivisions/integrer_subdivisions.py`.
- Contenu : Angleterre et pays de Galles = 62 administrative counties + 83 county boroughs (recensement 1931, CR03 ; York compté une fois) + îles Scilly (régime particulier, Order 1930) ; Écosse = 33 counties + 4 cities (Aberdeen, Dundee, Édimbourg, Glasgow) ; Irlande du Nord = 6 counties + 2 county boroughs (recensement 1937) ; Chypre = 6 districts coloniaux (sous `territoire-cy-chypre`, IDs en `cy`).
- Organisations parallèles au même rang, distinguées par `systeme_administratif` (angleterre, pays_de_galles, ecosse, irlande_du_nord, chypre_coloniale) : pas d'arbre county → county borough (Q2GB-05 acceptée).
- Pas de deuxième échelon (boroughs, districts, burghs, paroisses : R2GB-06). London County historique, pas Greater London. Malte, Gibraltar : aucune subdivision (R2GB-07). Jersey et Guernesey hors lot (souveraineté distincte).
- **Aucun tracé** : ONS 1921 (OGL) = comtés de 1921 ; OS Boundary-Line = limites actuelles ; GBHGIS 1961 sous CC BY-SA (hors licences acceptées) (R2GB-01).
- Chefs-lieux : aucun proposé (R2GB-05).
- Réserves : R2GB-01 à 08 (`docs/lots/2.GB/atlas_2GB_reserves.md`).
- Sources : 16 (12 ok, 4 limite), `data/sources/verifications_claude/2026-10-18_2GB.json`.
