# Snapshot 0 — villes, ratissage 1.8 : Balkans, Grèce et Italie

Fichier : `villes_1-8_balkans_grece_italie.json` (v0.1, 361 villes : Italie 140, Grèce 49, Bulgarie 37, Roumanie 34, Bosnie-Herzégovine 28, Serbie 24, Croatie 19, Monténégro 9, Albanie 8, Macédoine du Nord 7, Slovénie 6 ; 18 A, 121 B, 222 C). Intégré par Claude le 04/10/2026 depuis le JSON d'Ether (`data/sources/deltas_ether/2026-10-04_villes_1-8_proposition_ether.json`, sous la clé `proposition_ether` ; delta des sources, positions, sélection, réserves, index des pièces et contrôle à côté). Documents d'Ether : `villes_1-8_balkans_grece_italie_brief_ether.md`, `…_reserves_ether.md` (R18-01 à R18-70), `…_grille_ether.md`, `…_guide_sources_ether.md`.

- **IDs** : code du pays actuel, sans valeur de souveraineté en 1945 (exception des villes, `docs/LEXIQUE_ID.md`). Kosovo non couvert (Priština et Mitrovica réservés par Ether).
- **Noms de 1945 dans l'état** pour 8 villes (Fiume, Pola, Petrovgrad, Caribrod, Gorna Djoumaïa, Bosanski Brod, Bosanski Novi, Cluj), nom actuel sur la fiche ; aucun `nom_local`. Fiume et Sušak restent distinctes.
- **Capitales nationales** : Rome, Athènes, Belgrade, Sofia, Bucarest, Tirana. Zagreb et les futures capitales de républiques sans type (réserves d'Ether).
- **Positions** : Wikidata (CC0), QID d'Ether recoupés par SPARQL (`outils/villes/wikidata_ratissage_1_8.json`) ; repères actuels, pas des centres de 1945 certifiés (R18-01).
- **Sources** : 66 nouvelles + complément `src-wikidata` ; relecture de Claude : 40 confirmées, 13 partielles, 13 illisibles par l'outil ; 5 cartes OSS (1942-1944) lues par Claude sur les images d'Ether, 271 villes confirmées une à une (`confirmations_claude`). Registre v1.25. « À renforcer » sur 65 villes (Q18-01, Q18-02).

Scripts rejouables : `outils/villes/construire_villes_1_8.py` (fusion des sources une seule fois : `fusion_sources_1_8.py`, après `fusion_sources_1_6_1_7_cycle3.py`). Compte rendu : `docs/pour_ether/2026-10-04_villes_1-8.md`.

## v0.2 (05/10/2026, réponses d'Ether, cycle 2)

15 captures (Treni di Carta, ELIA, Olbia, Sibiu, Constanța) et 4 pages en ligne relues par Claude (registre v1.26) : 26 villes « À renforcer » (65 avant). Correction d'Orte non appliquée (pont daté de 1945 « at Ode Station », Orte non nommée ; R18-C2-02). Réserves R18-01 à 70 et R18-C2-01 à 04. Compte rendu : `docs/pour_ether/2026-10-05_villes_1-8_cycle2.md`.

## v0.3 (05/10/2026, réponses d'Ether, cycle 3)

5 sources nouvelles (Ploiești/Buzău, Brăila, Tecuci, Spolète, Fabriano) ajoutées sans rien remplacer, nouveau localisateur du rapport RE pour Cancello Arnone ; relues par Claude (registre v1.28) : rail prouvé pour Ploiești, Buzău, Brăila, Tecuci, Fabriano, Cancello Arnone ; Spolète illisible pour l'outil. 20 villes « À renforcer ». Orte inchangée (proposition retirée par Ether). **3 cycles atteints** : réserves R18-01 à 70, R18-C2-01 à 04, R18-C3-01 à 03 gardées pour la revue finale 1.x. Compte rendu : `docs/pour_ether/2026-10-05_villes_1-8_cycle3.md`.
