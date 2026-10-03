# Snapshot 0 — villes, ratissage 1.5 : Russie d'Europe et Oural, Biélorussie, Ukraine/Crimée, Moldavie, Prusse-Orientale aujourd'hui russe

Fichier : `villes_1-5_europe_orientale.json` (v0.2, 200 villes : Russie 105, Ukraine 66, Biélorussie 24, Moldavie 5 ; 17 A, 130 B, 53 C). Intégré par Claude le 02/10/2026 depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-02_villes_1-5_proposition_ether.json`, sous la clé `proposition_ether` ; delta des sources, positions brutes, correspondance des IDs et audit de sélection à côté). Documents d'Ether : `villes_1-5_europe_orientale_brief_ether.md`, `…_reserves_ether.md` (R15-01 à R15-36), `…_grille_couverture_ether.md`.

- **IDs** : code du pays actuel (`ville-ru-…`, `ville-ua-…`, `ville-by-…`, `ville-md-…`), exception des villes écrite au lexique (Q15-01).
- **Noms de 1945 dans l'état** pour 67 villes (Sverdlovsk, Molotov, Gorki, Kouïbychev, Leningrad, Stalingrad, Stalino, Königsberg, Pillau, Tilsit…), nom actuel sur la fiche ; aucun `nom_local`.
- **Capitales** : Moscou nationale ; Minsk, Kiev, Kichinev, Petrozavodsk régionales (capitales de RSS, comme Tallinn, Riga, Vilnius). Les 15 chefs-lieux d'oblast ou de RSSA proposés « régionaux » par Ether gardent leurs rôles, sans attribut de capitale (convention non établie, Q15-02, revue finale).
- **Positions** : Wikidata pour 195 villes (QID recoupés par SPARQL, `outils/villes/wikidata_ratissage_1_5.json`) ; GeoNames (CC BY 4.0) pour 5 repères actuels. Ce sont des points de repérage, pas des centres de 1945 certifiés.
- **Rôles vides** : Tilsit, Insterburg, Gumbinnen, Ragnit, Béjitsa (R15-07).
- **Sources** : 192 nouvelles + complément Wikidata ; relecture de Claude : 124 confirmées, 25 partielles, 6 faibles, 32 illisibles par l'outil, 5 liens morts. Registre v1.17. « À renforcer » sur 79 villes.
- 30 candidats différés par Ether (Miass, Medvejiegorsk, Rjev, Sortavala, Feodossia, Eupatoria, Berdiansk, Ungheni…) : non importés.

- **v0.2 (03/10/2026, réponses d'Ether, cycle 2)** : aucune donnée de ville modifiée ; 13 sources complétées (registre v1.18), Soumy confirmée sur la page 353 du recueil, six sources de Q15-03 passent de « faible » à « non vérifiée » (pages lues seulement en partie par l'outil). « À renforcer » : 78 villes. Documents : `villes_1-5_reponses_ether_2026-10-03.md`, `…_chefs_lieux_complement_ether_2026-10-03.md`, `…_reserves_complement_ether_2026-10-03.md`.

Scripts rejouables : `outils/villes/construire_villes_1_5.py` (fusion des sources une seule fois : `outils/villes/fusion_sources_1_5.py`). Comptes rendus : `docs/pour_ether/2026-10-02_villes_1-5.md`, `docs/pour_ether/2026-10-03_villes_1-5_reponses.md` (fusion du cycle 2 : `outils/villes/fusion_sources_1_5_reponses.py`).
