# Snapshot 0 — villes, ratissage 1.3 : Tchéquie, Slovaquie, Hongrie

Fichier : `villes_1-3_tchequie_slovaquie_hongrie.json` (v0.2, 53 villes : 19 Tchéquie, 16 Slovaquie dont Komárom des deux rives, 18 Hongrie ; 3 A, 35 B, 15 C), intégré par Claude le 01/10/2026 à partir du document d'Ether (`villes_1-3_tchequie_slovaquie_hongrie_brief_ether.md`). v0.1 faite depuis le document seul ; v0.2 lit le JSON d'Ether (`data/sources/deltas_ether/2026-10-01_villes_1-3_proposition_ether.json`, delta et contrôles à côté) : notes et preuves rôle par rôle reprises.

- Même modèle que les lots précédents (`importance_atlas`, `roles`, `capitale`, note, alias).
- **Noms au Snapshot 0** : Moravská Ostrava, Děčín–Podmokly, Nový Bohumín, Komárom (une seule ville des deux rives), Párkány. Noms allemands, hongrois et plus récents en alias, pour la recherche seulement.
- **Capitales** : Bratislava et Budapest nationales ; Prague régionale (Protectorat), par cohérence avec Vienne, validé par Guizmo.
- **Miskolc et Diósgyőr** : deux points au Snapshot 0 ; leur fusion du 01/01/1945 sera un état daté.
- **Positions** : Wikidata (`outils/villes/wikidata_ratissage_1_3.json`) ; Nový Bohumín = gare ; Most à déplacer sur le vieux Most ; Komárom placé sur la rive nord.
- **Sources** : 53, relues par Claude (37 confirmées, 4 partielles, 2 faibles, 7 illisibles, 3 liens morts) ; registre v1.10. Les douteuses vont dans la page « Sources à valider ».
- Différés par Ether : Dunapentele, Esztergom (pont à part), Tatabánya, Kazincbarcika, Otrokovice, Karlovy Vary.

Script rejouable : `outils/villes/construire_villes_1_3.py`. Questions : `docs/pour_ether/2026-10-01_villes_1-3.md`.

## v0.3 (01/10/2026) — réponse d'Ether

- **Noms à la date dans l'état** (`proprietes.nom`, lu en premier par la carte) : Košice → **Cassovie** (sur place : Kassa) ; Ústí nad Labem → **Aussig**. Mêmes IDs ; les noms actuels sont rappelés dans la fiche.
- **Miskolc–Diósgyőr** : fusion datée du 01/01/1945 (S44, p. 102) ; deux points au Snapshot 0.
- 6 sources (S44 complétée + 5 ajouts), registre v1.13. Réponse d'Ether : `villes_1-3_reponses_ether_2026-10-01.md` ; corrections et sources : `data/sources/deltas_ether/2026-10-01_villes_1-3_reponses_*.json` ; compte rendu : `docs/pour_ether/2026-10-01_villes_1-3_reponses.md`.

## v0.4 (01/10/2026) — cycle 3 d'Ether

- **Cinq noms à la date** dans l'état, chacun sur une preuve individuelle relue par Claude : **Reichenberg** (Liberec), **Eger** (Cheb), **Brüx** (Most), **Tetschen-Bodenbach** (Děčín), **Érsekújvár** (Nové Zámky). Fiches, IDs, `nom_local`, rôles et positions inchangés. Dates de retour aux noms d'après-guerre non établies.
- **En réserve par décision de Guizmo** (aucune donnée modifiée) : noms bilingues du Protectorat (Q13-02), note Budapest/Szálasi (Q13-03), déplacement du vieux Most (Q13-04 ; relevé d'Ether gardé au registre).
- 9 sources ajoutées (8 confirmées ; la carte municipale de Most illisible pour l'outil), registre v1.15. Réponse d'Ether : `villes_1-3_reponses_ether_cycle3_2026-10-01.md` ; corrections et sources : `data/sources/deltas_ether/2026-10-01_villes_1-3_cycle3_*.json` ; compte rendu : `docs/pour_ether/2026-10-01_villes_1-3_cycle3.md`.
- **Trois cycles atteints** : la suite (clôture avec réserves ou 4e cycle) attend Guizmo.
