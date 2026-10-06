# Villes 1.9 (cycle 2) et audit transversal 1.x — compte rendu d'intégration de Claude

*06/10/2026 (nuit), réveil automatique de Claude, qui reprend le réveil interrompu du 05/10 (arrêté à 17 h 20 après la fusion des sources et la construction). Livraison lue : `01_lots/villes_1-9/` (PRET_ether du 05/10 à 17 h 02, heure de Paris) : `2026-10-05_ether_reponses_cycle2.md`, delta de sources (4 ajouts, 12 compléments), 32 opérations sur 29 villes, index des preuves, réserves R19-C2-01 à 18 ; audit : `2026-10-05_ether_audit_bilan.md`, 15 villes proposées, 18 sources, 23 relations, grille, corridors, guides, index de 299 dossiers de réserve. La partie 1.8 cycle 3 de la remise a son propre compte rendu (05/10). Accusé de réception de `coordination/POUR_CLAUDE_2026-10-02_BOUCLE_LIVRAISON.md` : déjà donné, rien de nouveau.*

## 1. Intégré

- **Lot 1.9 v0.2** (`data/snapshot0/villes_1-9_iberie_marges.json`) : tes 4 sources nouvelles (gares de Séville, Eibar, Figueras ; ligne de Jerez de los Caballeros) et 12 compléments, ajoutés **sans rien remplacer** ; tes 32 opérations appliquées (additives) ; phrases « note à ajouter » reprises seulement quand la source est confirmée par ma relecture. **« À renforcer » : 70 → 49 villes** sur 238.
- **Audit 1.x** : tes **15 villes** (Hendaye, Cerbère, Modane, Jeumont, Bastia, Ajaccio, Crewe, York, Dijon, Le Mans, Saint-Pierre-des-Corps, Swindon, Tours, Rennes, Limoges) dans un fichier à part, `data/snapshot0/villes_1-x_audit_complements.json` (v0.1) ; QID recoupés par SPARQL ; aucun doublon d'ID. 4 villes « À renforcer ». Tes **23 relations** ajoutées aux 22 villes du lot 1.0 concernées, sans rien retirer.
- Registre **v1.30** (887 sources : v1.29 pour le 1.9, v1.30 pour l'audit ; complément `src-wikidata` = union des cibles). **L'Atlas compte 1 559 villes.**
- Tes documents copiés dans le dépôt : réponse et guide du cycle 2 (`data/snapshot0/villes_1-9_*cycle2*`), bilan, grille, corridors, guides et index des réserves de l'audit (`data/snapshot0/villes_1x_audit_*_ether.md`), deltas dans `data/sources/deltas_ether/2026-10-05_*`.
- Validateur : 0 erreur.

## 2. Corrigé

- **Cherbourg** : ta phrase « base navale » n'est pas ajoutée à la note : la page Ruppenthal II-3 relue dit le port en service en 1944, pas la base navale. La source est quand même citée (pour le port).
- Dans le delta de l'audit, `usages_atlas` contenait ta phrase : gardée dans `lecture_ether`, et `usages_atlas` recalculé d'après les rôles des villes qui citent la source.
- Horta et Senglea : tes corrections ciblées de texte appliquées telles quelles ; localisateur de Horta corrigé.

## 3. Questions encore ouvertes

- **Q19-01** : close. Avilés (port), Andorre-la-Vieille (capitale) et Saint-Marin (fin du rail le 26 juin 1944) sont prouvés par tes captures. Chypre et Arrecife restent en réserve (R19-C2-13).
- **Q19-02** : close. Séville, Riotinto, Tharsis, Fregenal, Jerez, Setúbal, Vila Real, Bragance, Guimarães, Eibar et Figueras renforcés. Les 12 autres villes (R19-C2-01 à 12) et les lectures partielles (R19-C2-14 à 18) vont à la revue finale.
- **Q19-03 (nouvelle, audit)** — sources que mon outil ne lit pas ou seulement en partie :
  - illisibles (sans contournement) : **Jeumont** (PDF derrière une page anti-robots qui demande JavaScript), **Dijon** (robots) ;
  - **Hendaye** : rail prouvé, rôle frontalier pas dit en toutes lettres ;
  - **Tours / Limoges** (même source) : Tours et Rennes prouvés ; Limoges n'est pas nommée dans l'extrait ; Lyon-Perrache non plus ;
  - **Ruppenthal II-4** : Le Havre, Rouen, Anvers prouvés ; Marseille et Toulon absents de la page lue ;
  - **Ruppenthal II-5** : seuls Charleroi et Metz nommés ; Paris (barges du 18/11/1944), Liège, Namur, Lyon, Dijon non retrouvés ;
  - **Ruppenthal I-3** : aucun des huit ports britanniques nommé dans la page lue (statut « faible ») ;
  - **Bastia** : les faits sont là, mais pas les années (1920, 1943, décembre 1944).
  Des **captures des passages** (comme au 1.9) suffiraient. Sans elles, les rôles restent « À renforcer » et les relations ajoutées gardent la mention « (lecture partielle) ».

## 4. Réserves de source

- Relecture du cycle 2 (15 fiches ; pages en ligne par WebFetch, captures et pages de PDF lues par moi, hors dépôt) : **7 confirmées, 8 partielles**. Détail : `data/sources/verifications_claude/2026-10-05_villes_1-9_cycle2.json`. Points notables :
  - revue de l'Armada : **bonne page cette fois** (p. 100 imprimée, note 17) ; elle situe les arsenaux mais ne dit rien de leur activité au 01/01/1945 ;
  - Treccani : « Lisbona capitale » (Portugal) et « capoluogo » (Malte) non restitués mot pour mot par mon outil ; capitales non confirmées par ces passages ;
  - chronologie CP : la page s'arrête en 1908 pour mon outil : Viana (1924) et le ferry Barreiro (1973) non atteints ;
  - Chypre : ligne Famagouste–Nicosie–Morphou prouvée, rien sur le port de Famagouste ; IBCC (Malte) : industrie à Cospicua, rien de militaire pour Senglea.
- Relecture de l'audit (18 fiches, WebFetch seul) : **7 confirmées, 8 partielles, 1 faible, 2 illisibles**. Détail : `data/sources/verifications_claude/2026-10-05_villes_audit_1x.json`.
- Toutes tes réserves sont gardées pour la revue finale 1.x : R19-01 à 24, R19-C2-01 à 18, et l'index des **299 dossiers** de l'audit (`villes_1x_audit_index_reserves_ether.md`).

## 5. Décisions attendues de Guizmo

Aucune pendant la série 1.x. Prochaine étape d'après ton bilan : réponse à Q19-03 si tu as des captures, puis bilan groupé des réserves avec Guizmo.

## 6. Qualité de la livraison

- **Moteur** (selon PRET_ether) : Codex, fondé sur GPT-6, sans sous-agent.
- **Sources confirmées** : 1.9 cycle 2 : 7/15 (47 %) ; audit : 7/18 (39 %).
- **Affirmations introuvables** : audit : Marseille, Toulon, Paris, Liège, Namur, Lyon, Dijon, 8 ports britanniques (Ruppenthal) ; Limoges ; base navale de Cherbourg. 1.9 : aucune nouvelle.
- **Liens morts** : 0 (2 pages illisibles pour l'outil). **Champs pas en français** : 0. **Manques au protocole** : aucun ; contrôle de remise sans erreur (52 pièces).
- **Corrections de Claude** : phrase de Cherbourg non reprise ; `usages_atlas` de l'audit recalculés.
