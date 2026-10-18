# subdivisions_2-PT — Portugal au 01/01/1945 (lot 2.PT)

- Fichier : `data/snapshot0/subdivisions_2-PT.json` (33 subdivisions, toutes à l'échelon 1 sous `territoire-pt-portugal` : **11 provinces**, **18 districts continentaux** et **4 districts autonomes des îles adjacentes** — Angra do Heroísmo, Horta, Ponta Delgada, Funchal).
- Livraison d'Ether du 18/10/2026 (cycle 1), intégrée par Claude le 18/10/2026 (réveil automatique) avec `outils/subdivisions/integrer_subdivisions.py`.
- **Deux organisations parallèles** (champ `systeme_administratif`) : provinces (Code administratif, art. 284–286) et districts (circonscription du gouverneur civil, art. 404). Un district peut être réparti entre plusieurs provinces (Guarda, Viseu, Aveiro… au MAPA III de 1936) : pas d'arbre province → district (R2PT-02, Q2PT-05).
- Listes d'après le Código Administrativo de 1936 (MAPA III/IV, p.1869–1870), les annexes du décret 30214 de 1939 (îles) et l'art. 2 du décret 31095 du 31/12/1940 qui les reprend ; contrôle de la modification de 1941 (décret 31386). Noms de la date (Pôrto…). Pas de concelhos ni de freguesias. Possessions d'outre-mer hors périmètre.
- **Aucun tracé** : CAOP actuelle seulement ; projet Atlas (NOVA) sans fichier ni droits établis ; REGIS en licence NC — R2PT-01.
- Chefs-lieux : 26 `chef_lieu_propose` reliés à des fiches villes existantes, aucun validé ; 7 sièges de district non proposés (R2PT-04).
- Réserves : R2PT-01 à 05 (`docs/lots/2.PT/atlas_2PT_reserves.md`).
- Sources : 6 (6 ok), `data/sources/verifications_claude/2026-10-18_2PT.json`.
