# Snapshot 0 — villes, ratissage 1.7 : Caucase et Turquie

Fichier : `villes_1-7_caucase_turquie.json` (v0.1, 166 villes : Turquie 77, Russie — Caucase du Nord 36, Géorgie 26, Azerbaïdjan et Nakhitchevan 16, Arménie 11 ; 6 A, 31 B, 129 C). Intégré par Claude le 04/10/2026 depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-03_villes_1-7_proposition_ether.json`, sous la clé `proposition_ether` ; delta des sources, positions, audit de sélection et réserves à côté). Documents d'Ether : `villes_1-7_caucase_turquie_brief_ether.md`, `…_reserves_ether.md` (R17-01 à R17-27), `…_grille_couverture_ether.md`.

- **IDs** : code du pays actuel (`ville-tr-…`, `ville-ru-…`, `ville-ge-…`, `ville-am-…`, `ville-az-…`), sans valeur de souveraineté en 1945 (exception des villes, `docs/LEXIQUE_ID.md`).
- **Noms de 1945 dans l'état** pour 20 villes (Dzaoudjikaou, Leninakan, Kirovakan, Kirovabad, Noukha, Stalinir, Stepanakert, Urfa…), nom actuel sur la fiche ; aucun `nom_local`. İstanbul et les deux Ereğli : variante gardée en alias (pas un autre nom). Écarts de transcription azerbaïdjanais conservés (Q16-03).
- **Capitales** : Ankara nationale ; Tbilissi, Erevan, Bakou régionales (capitales de RSS) ; RSSA et oblasts sans type (Q15-02).
- **Positions** : Wikidata (CC0) pour les 166 villes, élément relié à l'identifiant GeoNames proposé par Ether (P1566), recoupé par SPARQL ; 22 QID choisis à la main (`outils/villes/wikidata_ratissage_1_7.json`). Repères actuels, pas des centres de 1945 certifiés (R17-01).
- **Sources** : 49 nouvelles + 5 compléments ; relecture de Claude : 28 confirmées, 10 partielles, 12 illisibles par l'outil, 1 lien « 404 », 1 faible ; 16 villes du Caucase relues une à une sur les images des répertoires (champ `confirmations_claude`). Registre v1.22. « À renforcer » sur 124 villes (Q17-01, Q17-02).
- 9 candidats différés par Ether (Malgobek, Nazran, Iriston/Beslan, Nijniaïa Akhta, Soumgaït, Khoudat, Batman, Guleman, Erzincan) : non importés.

Scripts rejouables : `outils/villes/construire_villes_1_7.py` (fusions des sources une seule fois : `fusion_sources_1_5_cycle3.py`, `fusion_sources_1_6_reponses.py`, puis `fusion_sources_1_7.py`). Compte rendu : `docs/pour_ether/2026-10-04_villes_1-7.md`.

**v0.2 (04/10/2026 au soir, réponses d'Ether cycle 2, Q17-01 et Q17-02)** : İzmir perd le rôle industrie (Halkapınar : liste de 1944 et ouverture en 1947 dans la même étude ; correction d'Ether, réserve R17-C2-01). Claude a lu les 7 captures (encyclopédie Atatürk : rail relu pour 30 villes ; Gelibolu confirmée ; Mersin/Tarsus relue) et les 10 images de pages (Géorgie, Arménie, Stavropol : 34 villes confirmées). Registre v1.24. « À renforcer » : 78 villes (124 avant). Compte rendu : `docs/pour_ether/2026-10-04_villes_1-7_cycle2.md`.
