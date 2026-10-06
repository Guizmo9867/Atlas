# Snapshot 0 — villes, audit transversal 1.x : compléments de couverture

Fichier : `villes_1-x_audit_complements.json` (v0.1, 15 villes, intégrées par Claude le 06/10/2026). Proposées par Ether dans son audit transversal de la série villes 1.x (remise du 05/10/2026), pour combler des trous du lot 1.0 (France et Grande-Bretagne) : Hendaye, Cerbère, Modane, Jeumont (gares frontières), Bastia, Ajaccio (ports corses), Crewe, York, Swindon (rail britannique), Dijon, Le Mans, Saint-Pierre-des-Corps, Tours, Rennes, Limoges (nœuds ferroviaires français). Lens reste différée par Ether.

- Documents d'Ether : `villes_1x_audit_bilan_ether.md` (point d'entrée), `villes_1x_audit_grille_transversale_ether.md`, `villes_1x_audit_corridors_ether.md`, `villes_1x_audit_guides_sources_ether.md`, `villes_1x_audit_index_reserves_ether.md` (299 dossiers de réserve, pour la revue finale). Deltas : `data/sources/deltas_ether/2026-10-05_audit_1x_*.json`.
- **IDs** au code du pays actuel (`ville-fr-…`, `ville-gb-…`) ; aucun doublon avec les 1 544 villes déjà intégrées. Aucune capitale.
- **Positions** : Wikidata (CC0), QID d'Ether recoupés par Claude par SPARQL (`outils/villes/wikidata_ratissage_audit_1x.json`) ; repères actuels (York : précision grossière).
- **Sources** : 18 nouvelles, relues par Claude (`data/sources/verifications_claude/2026-10-05_villes_audit_1x.json`) : 7 confirmées, 8 partielles, 1 faible, 2 illisibles pour l'outil (Jeumont, Dijon). Registre v1.30.
- « À renforcer » : 2 villes depuis le 06/10/2026 (Hendaye frontalier ; Jeumont rail et industrie). Dijon et Limoges (rail) prouvés au cycle 3 d'Ether (captures lues par Claude).
- **Cycle 3 (06/10/2026, réponse à Q19-03)** : 19 relations de l'audit précisées sur 17 villes (13 du lot 1.0, 4 d'ici) après lecture de 15 captures (`data/sources/verifications_claude/2026-10-06_villes_1-9_cycle3.json`) ; Ruppenthal I-3, II-4, II-5, SNCF et Bastia confirmés ; registre v1.31 ; note de Namur (pont sur la Meuse hors service au Snapshot). Script : `outils/villes/integrer_1_9_cycle3.py` (à relancer après `appliquer_audit_1x.py` et `construire_villes_audit_1x.py`).
- L'audit ajoute aussi **23 relations documentaires à 22 villes du lot 1.0** (Ruppenthal, Hansard 1946…) : sources ajoutées sans rien retirer (`outils/villes/appliquer_audit_1x.py`).

Scripts : `fusion_sources_audit_1x.py` (une seule fois, après `fusion_sources_1_9_cycle2.py`), `construire_villes_audit_1x.py`, `appliquer_audit_1x.py`, puis `integrer_1_9_cycle3.py` et `appliquer_validations_guizmo.py`.
