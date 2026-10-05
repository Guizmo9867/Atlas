# Snapshot 0 — villes, ratissage 1.9 : Ibérie et marges méditerranéennes

Fichier : `villes_1-9_iberie_marges.json` (v0.1, 238 villes : Espagne 158, Portugal 61, Chypre 7, Malte 5, Andorre 2, Saint-Marin 2, Gibraltar 1, Vatican 1, Monaco 1 ; 12 A, 89 B, 137 C). Intégré par Claude le 05/10/2026 depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-05_villes_1-9_proposition_ether.json`, sous la clé `proposition_ether` ; delta des sources, positions, sélection, grille, réserves, index des pièces et contrôle à côté). Documents d'Ether : `villes_1-9_iberie_marges_brief_ether.md`, `…_reserves_ether.md` (R19-01 à R19-24), `…_grille_ether.md`, `…_guide_sources_ether.md`.

- **IDs** : code du pays actuel, sans valeur de souveraineté en 1945 (exception des villes, `docs/LEXIQUE_ID.md`) ; code `sm` (Saint-Marin) ajouté au lexique.
- **Noms de 1945 dans l'état** pour 3 villes (El Ferrol del Caudillo, Mahón, Puerto Cabras), nom actuel sur la fiche ; aucun `nom_local`.
- **Capitales** : « nationale » pour Madrid, Lisbonne, Andorre-la-Vieille, Saint-Marin ; « territoire » pour Nicosie et La Valette (colonies britanniques) ; Monaco et Vatican sans champ capitale (convention de cité-État en réserve).
- **Positions** : Wikidata (CC0), QID d'Ether recoupés par SPARQL (`outils/villes/wikidata_ratissage_1_9.json`, script `wikidata_recouper_1_9.py`) ; aucun écart > 1 km ; repères actuels, pas des centres de 1945 certifiés (R19-01). Cité du Vatican à côté de Rome : entités distinctes.
- **Sources** : 35 nouvelles + complément `src-wikidata` ; relecture de Claude : 15 confirmées, 14 partielles (dont la carte Forcano 1942, lue par Claude sur 19 captures : 167 villes prouvées pour le rail), 5 illisibles par l'outil, 1 faible. Registre v1.27 (860 sources). « À renforcer » sur 70 villes (Q19-01, Q19-02).
- 10 candidats différés par Ether non importés (Canfranc, Chinchilla, La Encina, Bobadilla, Moreda, Casa Branca, Tua, Pocinho, Cabeço de Vide, Estella-Lizarra).

Scripts rejouables : `outils/villes/construire_villes_1_9.py` (fusion des sources une seule fois : `fusion_sources_1_9.py`, après `fusion_sources_1_7_1_8_reponses.py`). Compte rendu : `docs/pour_ether/2026-10-05_villes_1-9.md`.
