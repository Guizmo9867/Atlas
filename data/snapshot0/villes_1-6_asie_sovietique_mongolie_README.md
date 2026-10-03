# Snapshot 0 — villes, ratissage 1.6 : URSS d'Asie (hors Caucase) et Mongolie

Fichier : `villes_1-6_asie_sovietique_mongolie.json` (v0.1, 254 villes : Russie 135, Kazakhstan 41, Ouzbékistan 23, Mongolie 19, Kirghizistan 16, Turkménistan 12, Tadjikistan 8 ; 13 A, 54 B, 187 C). Intégré par Claude le 03/10/2026 depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-03_villes_1-6_proposition_ether.json`, sous la clé `proposition_ether` ; delta des sources à côté). Documents d'Ether : `villes_1-6_asie_sovietique_mongolie_brief_ether.md`, `…_reserves_ether.md` (R16-01 à R16-69), `…_grille_couverture_ether.md`.

- **IDs** : code du pays actuel (`ville-ru-…`, `ville-kz-…`, `ville-uz-…`, `ville-kg-…`, `ville-tj-…`, `ville-tm-…`, `ville-mn-…`), sans valeur de souveraineté en 1945.
- **Noms de 1945 dans l'état** pour 89 villes (Frounzé, Stalinabad, Alma-Ata, Achkhabad, Stalinsk, Akmolinsk, Djibkhalantou…), nom actuel sur la fiche ; aucun `nom_local`. Une partie de ces noms ne sont qu'une autre transcription (Q16-03, revue finale).
- **Capitales** : Alma-Ata, Tachkent, Frounzé, Stalinabad, Achkhabad régionales (capitales de RSS) ; Oulan-Bator nationale. RSSA et oblasts sans type d'affichage (Q15-02, R16-02).
- **Positions** : Wikidata pour les 254 villes (QID recoupés par SPARQL, `outils/villes/wikidata_ratissage_1_6.json`). Points de repérage actuels, pas des centres de 1945 certifiés (R16-01, R16-20).
- **Rôles vides** : Sükhbaatar (transit routier en note).
- **Sources** : 113 nouvelles + complément Wikidata ; relecture de Claude : 47 confirmées, 24 partielles, 6 faibles, 30 illisibles par l'outil, 6 liens morts. Registre v1.19. « À renforcer » sur 225 villes (surtout répertoires administratifs illisibles par l'outil, Q16-02).
- 49 candidats différés par Ether : non importés. Sud de Sakhaline et Kouriles (japonais au Snapshot 0) hors du lot.

Scripts rejouables : `outils/villes/construire_villes_1_6.py` (fusions des sources une seule fois : `outils/villes/fusion_sources_1_5_reponses.py` puis `outils/villes/fusion_sources_1_6.py`). Compte rendu : `docs/pour_ether/2026-10-03_villes_1-6.md`.
