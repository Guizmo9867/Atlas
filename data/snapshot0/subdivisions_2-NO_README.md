# subdivisions_2-NO — Norvège au 01/01/1945 (lot 2.NO)

- Fichier : `data/snapshot0/subdivisions_2-NO.json` (20 subdivisions).
- Livraison d'Ether du 24/10/2026 (cycle 1), intégrée par Claude le 25/10/2026 (réveil automatique) avec `outils/subdivisions/integrer_subdivisions.py`.
- Un seul échelon, sous `territoire-no-norvege` (souveraineté `norvege`) : **20 fylker de droit**, dans l'ordre de l'annuaire SSB (Østfold, Akershus, Oslo, Hedmark, Opland, Buskerud, Vestfold, Telemark, Aust-Agder, Vest-Agder, Rogaland, Hordaland, Bergen, Sogn og Fjordane, Møre og Romsdal, Sør-Trøndelag, Nord-Trøndelag, Nordland, Troms, Finnmark). Oslo et Bergen sont des fylker à part (Aker rattaché à Oslo seulement le 01/01/1948 ; Bergen dans Hordaland en 1972).
- L'état porte **Opland** (graphie des annuaires de 1942 et 1943–1945) ; la fiche et l'ID gardent Oppland pour le repérage (R2NO-05).
- Date : l'annuaire décrit la situation au 01/07/1945 ; la continuité au 01/01/1945 est une inférence documentée (recoupée avec 1942, les cartes de 1941 et Juvkam 1999) : R2NO-02.
- Pas de second niveau général (fogderier dissous 1898–1919 ; districts judiciaires, de police, ecclésiastiques non importés) ; communes hors granularité. `territoire-no-est-finnmark` reste une surcouche de contrôle, pas un 21e fylke (R2NO-03).
- Svalbard et Jan Mayen : pas de territoire parent dans l'Atlas (différés dans `lot04_sud_centre_balkans_turquie.json`), aucune fiche (R2NO-06).
- **Aucun tracé** : cartes « Herredskart » de Kartverket (1918, mises à jour 1941, CC BY 4.0) disponibles mais non géoréférencées ni vectorisées (R2NO-01).
- Chefs-lieux et codes : aucun (R2NO-04).
- Réserves : R2NO-01 à 06 (`docs/lots/2.NO/atlas_2NO_reserves.md`).
- Sources : 11 (5 ok, 4 limite, 2 non vérifiées), `data/sources/verifications_claude/2026-10-24_2NO.json`.
