# Snapshot 0 — villes, ratissage 1.0 : France, Benelux, îles Britanniques

Fichier : `villes_1-0_france_benelux_iles_britanniques.json` (v0.3, 73 villes : 61 de la liste d'Ether + 12 ajoutées après son audit, intégré par Claude le 30/09/2026 ; Reims entrera au ratissage de février 1945).

- **Liste, rôles, priorités** : proposition d'Ether. Rôles en mots-clés (`roles`) + la phrase d'Ether en `note`. **Rôles à sourcer** : par famille et par pays, source propre pour un rôle particulier (QG du SHAEF…).
- **Position** : Wikidata (CC0), le QID est le `locator` de la source ; Charleroi : Natural Earth (domaine public).
- **Priorité d'affichage** (`importance_atlas`) : A capitales (visibles dès le zoom 3,8), B grandes villes structurantes (zoom 5), C nœuds régionaux (zoom 6,5), D micro-histoire (zoom 7,5). Automatique, jamais un réglage pour l'utilisateur.
- **Souveraineté et contrôle** : une ville n'en porte pas ; elle prend ceux du territoire où elle se trouve à la date affichée (ex. Dunkerque et Saint-Nazaire dans les poches allemandes au 01/01/1945).
- **Noms** : nom français traditionnel quand il existe (Douvres, Édimbourg, Flessingue, Nimègue, La Haye…) ; `nom_local` et `aliases` pour la recherche (Dover, Vlissingen, Derry…).
- **Temps** : `valid_from` inconnu = ville déjà en place avant le début de l'Atlas. Un changement d'importance, de nom ou de rôle = un nouvel état daté.

Script rejouable : `outils/villes/construire_villes_1_0.py` (candidats Wikidata dans `outils/villes/wikidata_ratissage_1_0.json`).
Questions ouvertes : `docs/pour_ether/2026-09-30_villes_1-0.md`.

- **06/10/2026 — audit transversal 1.x d'Ether** : 23 relations documentaires ajoutées à 22 villes (Paris, Marseille, Lyon, Le Havre, Rouen, Cherbourg, Brest, Metz, Toulon, Anvers, Liège, Charleroi, Namur, Londres, Liverpool, Manchester, Glasgow, Hull, Southampton, Portsmouth, Cardiff, Plymouth), sans rien retirer ; mentions de preuve selon la relecture de Claude (`outils/villes/appliquer_audit_1x.py`). 15 villes nouvelles de la même zone dans `villes_1-x_audit_complements.json`.
