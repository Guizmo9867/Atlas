# Snapshot 0 — villes, ratissage 1.3 : Tchéquie, Slovaquie, Hongrie

Fichier : `villes_1-3_tchequie_slovaquie_hongrie.json` (v0.1, 53 villes : 19 Tchéquie, 16 Slovaquie dont Komárom des deux rives, 18 Hongrie ; 3 A, 35 B, 15 C), intégré par Claude le 01/10/2026 à partir du document d'Ether (`villes_1-3_tchequie_slovaquie_hongrie_brief_ether.md`). Le JSON d'Ether n'avait pas été transmis : extrait par Claude dans `data/sources/deltas_ether/2026-10-01_villes_1-3_extrait_du_brief.json`, à rapprocher dès réception.

- Même modèle que les lots précédents (`importance_atlas`, `roles`, `capitale`, note, alias).
- **Noms au Snapshot 0** : Moravská Ostrava, Děčín–Podmokly, Nový Bohumín, Komárom (une seule ville des deux rives), Párkány. Noms allemands, hongrois et plus récents en alias, pour la recherche seulement.
- **Capitales** : Bratislava et Budapest nationales ; Prague régionale (Protectorat), par cohérence avec Vienne, à confirmer.
- **Miskolc et Diósgyőr** : deux points au Snapshot 0 ; leur fusion du 01/01/1945 sera un état daté.
- **Positions** : Wikidata (`outils/villes/wikidata_ratissage_1_3.json`) ; Nový Bohumín = gare ; Most à déplacer sur le vieux Most ; Komárom placé sur la rive nord.
- **Sources** : 53, relues par Claude (37 confirmées, 4 partielles, 2 faibles, 7 illisibles, 3 liens morts) ; registre v1.10. Les douteuses vont dans la page « Sources à valider ».
- Différés par Ether : Dunapentele, Esztergom (pont à part), Tatabánya, Kazincbarcika, Otrokovice, Karlovy Vary.

Script rejouable : `outils/villes/construire_villes_1_3.py`. Questions : `docs/pour_ether/2026-10-01_villes_1-3.md`.
