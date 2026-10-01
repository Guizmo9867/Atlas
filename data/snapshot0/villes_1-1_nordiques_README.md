# Snapshot 0 — villes, ratissage 1.1 : Nordiques

Fichier : `villes_1-1_nordiques.json` (v0.2, 65 villes : Danemark, Féroé, Norvège, Suède, Finlande, Islande ; 56 proposées + 9 ajoutées après l'audit), intégré par Claude le 30/09/2026 à partir de la proposition d'Ether (`data/sources/deltas_ether/2026-09-30_villes_1-1_nordiques_proposition_ether.json`, brief : `villes_1-1_nordiques_brief_ether.md`).

- Même modèle que le lot 1.0 : `importance_atlas` A/B/C/D (affichage automatique par le zoom), `roles` en mots-clés, phrase d'Ether en `note`, `nom_local` et `aliases`.
- **Rôles** ramenés au vocabulaire de l'Atlas ; nouveaux rôles : `minerai`, `peche`, `navigation_cotiere`, `militaire`.
- **Situation au 01/01/1945** (`situation`) : Kirkenes et Rovaniemi détruites, Hammerfest évacuée et détruite → point gris sur la carte (flux coupés).
- **Positions** : Wikidata (CC0), QID en locator (`outils/villes/wikidata_ratissage_1_1.json`), vérifiées contre Natural Earth.
- **Sources des rôles** : delta d'Ether fusionné au registre (v1.4) après lecture de chaque lien ; le champ `verification_claude` du registre dit ce qui est confirmé, limité ou non vérifié.
- Non inclus volontairement : Hvalfjörður (base), Gedser (à confirmer), Vyborg / Viipuri (soviétique au 01/01/1945 : lot URSS).

Script rejouable : `outils/villes/construire_villes_1_1.py`. Questions : `docs/pour_ether/2026-09-30_villes_1-1.md`.
