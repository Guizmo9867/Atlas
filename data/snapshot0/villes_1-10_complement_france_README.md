# Snapshot 0 — villes, ratissage 1.10 : complément France (chefs-lieux départementaux de 1945)

Fichier : `villes_1-10_complement_france.json` (v0.1, 66 villes, toutes C, rôle « administration »). Intégré par Claude le 16/10/2026 (boucle automatique) depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-16_villes_1-10_proposition_ether.json`). Demande issue du pilote 2.FR (feu vert de Guizmo du 15/10).

- **IDs** au nom actuel ; 4 noms de 1945 dans l'état (Bourg, Digne, Le Puy, Châlons-sur-Marne), anciens noms en alias. Mézières : ville distincte, sans point.
- **Positions** : TRF-GIS (Victor Gay, CC BY 4.0, mairies modernes ; crédit dans `docs/LICENCES_ET_ATTRIBUTIONS.md`), recoupées avec Wikidata par code INSEE (écart max. 1,1 km).
- **Sources** : 63 nouvelles (11 ok, 25 limite, 1 faible, 26 non vérifiées) ; registre v1.37. « À renforcer : administration » sur 52 villes.
- **Raccords 2.FR** : 11 `chef_lieu_id` (8 régions, Ardennes, Aveyron, Tarn) par `outils/villes/raccorder_chefs_lieux_1_10.py`.
- 6 candidats reportés par Ether non importés (Carcassonne, Saint-Lô, Pau, Perpignan, Colmar, Annecy). Réserves R110-01 à 04 et R110-REPORT-* : `villes_1-10_complement_france_reserves_ether.md` ; grille : `villes_1-10_complement_france_grille_couverture_ether.md`.

Scripts : `fusion_sources_1_10.py` (une seule fois), puis `construire_villes_1_10.py`, puis `raccorder_chefs_lieux_1_10.py`. Compte rendu : `docs/pour_ether/2026-10-16_villes_1-10.md`.
