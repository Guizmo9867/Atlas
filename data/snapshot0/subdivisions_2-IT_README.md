# subdivisions_2-IT — Italie au 01/01/1945 (lot 2.IT)

- Fichier : `data/snapshot0/subdivisions_2-IT.json` (93 provinces, échelon 1 sous `territoire-it-italie`, souveraineté `italie`). 94 provinces recensées : **Carnaro (Fiume) reporté** faute de préfixe de pays actuel établi (R2IT-08).
- Livraison d'Ether du 18/10/2026 (cycle 1), intégrée par Claude le 18/10/2026 (réveil automatique) avec `outils/subdivisions/integrer_subdivisions.py`.
- Liste d'après l'annuaire statistique Istat 1943 (données 1942, p.28–29), noms de la date (Apuania, Ionio, Littoria, Istria, Zara) ; circondari et mandamenti supprimés en 1927 (Istat 2018) ; Caserta, recréée le 11/06/1945, exclue. OZAV et OZAK (occupation allemande) en contexte seulement. Dodécanèse déjà territoire, pas doublonné.
- IDs : Gorizia et Trieste en `si`, Istria et Zara en `hr` (pays actuel majoritaire) ; souveraineté 1945 italienne.
- **80 tracés provisoires** : reconstruction Istat des limites provinciales de 1936 (CC BY 4.0, PRJ ED50 UTM32N), simplifiés. 11 contours refusés (`ne_pas_integrer` d'Ether : frontières tronquées ou limites changées après 1936) ; Istria et Zara sans contour.
- Chefs-lieux : 90 `chef_lieu_propose` (79 reliés à une fiche ville), aucun validé (liste rétrospective de 1952, R2IT-05).
- Réserves : R2IT-01 à 08 (`docs/lots/2.IT/atlas_2IT_reserves.md`).
- Sources : 10 (8 ok, 2 limite), `data/sources/verifications_claude/2026-10-18_2IT.json`.
