# Atlas Eurasie — fiche de reprise (à lire en premier)

*Fiche courte pour qu'un nouveau Claude, dans n'importe quelle conversation, sache où on en est sans tout relire. Le reste se lit seulement si besoin. Tenue à jour par Claude (section « État » à chaque lot, le reste quand une règle change). Original : `docs/REPRISE.md` du dépôt ; copies : `00_REPRISE.md` du dossier d'échange et `claude/REPRISE.md` du projet claude.ai. Dernière mise à jour : 15/10/2026.*

## 1. Le projet en 5 lignes

- **Atlas Eurasie** : atlas historique interactif des frontières, villes et flux d'Eurasie, de 1945 à aujourd'hui. Projet passion de **Guizmo** (Guillaume, chauffeur routier, niveau technique très faible : **toujours expliquer en français simple, étape par étape, sans jargon**).
- **Snapshot 0** = l'état au 01/01/1945 à 0 h (dernier état connu avant). On le construit couche par couche : frontières (fait), puis villes (série 1.x, en cours).
- **Seule source de vérité** : le dépôt GitHub public https://github.com/Guizmo9867/Atlas (sur le PC : `C:\Users\guill\Documents\GitHub\Atlas`).
- **Dossier d'échange** avec Ether : `C:\Users\guill\Desktop\Atlas` (tableau de bord, lots, réserves, sources à valider).

## 2. Qui fait quoi

| Qui | Rôle | Où |
|---|---|---|
| **Guizmo** | Décide, tranche les réserves en fin de série, valide des sources quand il a le temps. | — |
| **Ether** (ChatGPT, sous Codex) | Ratissage : cherche les données et les sources, livre des lots. | Conversations Codex « ATLAS — MISE EN PLACE », « ATLAS — RATISSAGE 01 », « ATLAS — FINANCEMENT 01 » (dossier de financement, dans `04_financement/`). |
| **Claude — boucle automatique** | Tâche programmée toutes les heures (à la 12e minute, heure de Paris) : intègre les lots d'Ether, vérifie les sources, envoie sur GitHub, écrit les comptes rendus. | Mode d'emploi : `docs/BOUCLE_AUTOMATIQUE.md` du dépôt. |
| **Claude — conversations avec Guizmo** | Réglages, outils, décisions, explications. Ne fait pas le travail de la boucle en double. | Projet claude.ai « Atlas ». |

Pas de contact direct entre Claude et Ether : tout passe par le dossier d'échange (`PRET_ether.md` / `PRET_claude.md`, `STATUT.json` par lot) et par Guizmo.

## 3. Règles qui ne bougent pas

- **Claude fait lui-même les commits et le push** : `bash .git/claude_git.sh …` depuis le dépôt, sur le PC (outil device_bash). Message en français, terminé par les lignes d'attribution de la session.
- **Jamais** : secret dans le dépôt ; suppression de fichier (sauf verrous git `.git/*.lock` après autorisation) ; données OSM/ODbL ; contournement d'un blocage WebFetch ; modification des fichiers d'Ether (`AGENTS.md`, `coordination/`, `04_financement/`, ses fichiers dans `01_lots/`) ; modification de `app/src` sans décision de Guizmo ; push si le validateur (`node app/scripts/validate-data.mjs`) a une erreur.
- **On n'attend jamais Guizmo** : ce qui demande sa décision va au tableau de bord (« À trancher par Guizmo ») et le travail continue sur le reste.
- **Série 1.x (villes)** : feu vert global. Réserves gardées par lot, triées avec Guizmo à la fin de la série (fichier `00_RESERVES_A_TRANCHER.md`). Une valeur incertaine n'est jamais appliquée. Nouveau feu vert nécessaire pour toute autre couche (routes, trains, ports autonomes, douanes) et pour le passage aux mois. Prochaines couches : zone URSS d'Europe coupée en deux.
- **Sources** : relues par des sous-agents (WebFetch). Celles que Claude ne peut pas confirmer vont dans « Sources à valider » pour Guizmo. Les sources restent **dans leur langue d'origine** (pas de traduction). Guizmo peut valider « pour 1945, la suite plus tard » : seule la partie valable au 01/01/1945 est appliquée.
- **Villes** : ID `ville-<code du pays actuel>-<slug>` ; nom actuel sur la fiche, nom de 1945 dans l'état seulement sur preuve ; « À renforcer » pour un rôle sans preuve confirmée.
- **Coût** : Guizmo paie à l'usage. Pas de travail inutile, pas de relecture complète de gros fichiers sans besoin. Optimisation à étudier plus tard (modèle moins cher pour la boucle, vérification par échantillon).

- **Carte en ligne** : https://guizmo9867.github.io/Atlas/ (mise à jour automatique à chaque envoi sur GitHub).

## 4. Où trouver le détail (à lire seulement si besoin)

- `docs/JOURNAL_DECISIONS.md` : toutes les décisions, datées (lire seulement le haut).
- `docs/BOUCLE_AUTOMATIQUE.md` : le mode d'emploi complet de la boucle.
- `docs/protocole_sources_ether_claude.md`, `docs/LEXIQUE_ID.md` : format des sources et des identifiants.
- `00_TABLEAU_DE_BORD.md` (dossier d'échange) : qui attend quoi, en détail.
- `docs/IDEES_POUR_PLUS_TARD.md` : idées reportées (régime routier, sources traduites…).
- `docs/NOTES_GUIZMO_SOURCES.md`, `docs/RESERVES_A_TRANCHER.md`, `docs/CHIFFRES_PROJET.md`.

## 5. État (mis à jour à chaque lot)

- **Frontières** : lots 01 à 04 intégrés (74 territoires, 4 lignes de front).
- **Subdivisions (phase 2)** : pilote **2.FR intégré le 15/10** (en conversation) : 90 départements + 18 régions de 1945 (commissariats régionaux), 103 tracés reconstitués (TRF-GIS 1940), réserves R2FR-01 à 13 pour la revue. Sur la carte : calque « Découpage administratif », échelon 1 dès le zoom 5, échelon 2 dès 6,5, mêmes seuils pour tous les pays. Demandé à Ether : complément `villes_1-10` (72 chefs-lieux sans fiche ville). **Phase 2.x en boucle automatique depuis le 15/10** (un lot par État de 1945) : groupe 1 = 2.BE, 2.LU, 2.NL, 2.CH ; groupes suivants ouverts par Guizmo après le bilan du groupe 1. **2.BE intégré le 15/10 (nuit)** : 9 provinces + 41 arrondissements, sans tracé (pas de source ouverte de 1945), réserves R2BE-01 à 06. **2.LU intégré le 15/10 (nuit)** : 3 districts + 12 cantons, 11 tracés reconstitués (ACT 1920–1977, CC0), 4 laissés sans tracé (Vianden/Diekirch, Remich/Grevenmacher), réserves R2LU-01 à 07. **2.NL intégré le 16/10 (nuit)** : 11 provinces + Noordoostpolder, 11 tracés reconstitués (NLGIS Boonstra 1945, CC0), Brabant-Septentrional sans tracé (Baarle), réserves R2NL-01 à 07. **2.CH intégré le 16/10 (nuit)** : 25 cantons et demi-cantons + 175 districts, sans tracé (contours OFS « terms_open » hors licences acceptées : à trancher par Guizmo), réserves R2CH-01 à 08. **Groupe 1 complet** ; groupe suivant à ouvrir par Guizmo. Fiche `docs/lancements/2.x_lancement.md`, boucle §3 ter, outil `outils/subdivisions/integrer_subdivisions.py`.
- **Villes** : 1.0 à 1.9 intégrés + 15 villes de l'audit transversal + **1.10 complément France (66 chefs-lieux départementaux, 16/10)**, **1 625 villes**. Lots 1.3 à 1.9 : 3 cycles faits, en attente de la revue finale des réserves (1.9 : 49 villes « à renforcer » ; audit : 2).
- **Dernière intégration (16/10, matin, réveil automatique)** : villes 1.10 cycle 2 (réponses d'Ether : 4 sources « ok » sur pièces locales, 48 villes « à renforcer », 15 chefs-lieux 2.FR raccordés en tout ; Q110-01 et 02 closes, aucune question ouverte : clôture à confirmer par Ether). Avant : villes 1.10 cycle 1 et Q2CH-05 (close). Avant : 2.NL et 2.CH, groupe 1 complet. À trancher par Guizmo : licence « terms_open » des contours suisses (R2CH-01) et ouverture du groupe 2.
- **Ether** : plus de cycle automatique sur les villes ; prochaine étape = **bilan final et index**, phase « villes terminées, attente de Guizmo ». Puis revue des réserves avec Guizmo. Financement : réveil quotidien.
- **Sources** : registre v1.38, 980 sources ; 359 à valider par Guizmo, dont **161 importantes**. Page « Sources à valider » : sur claude.ai, ou `00_SOURCES_A_VALIDER.html` dans le dossier d'échange.
- **Suite du projet : `docs/METHODE_ATLAS_v2.md`** (08/10, validée par Guizmo, à relire avec Ether ; rien de lancé) : zones fixes (frontières 2026) et groupes, catégories Eau / Terre / Fer / Règles (+ Air plus tard), événements avec thèmes et portée ; Snapshot 0 → 2.x subdivisions puis 3.x campagnes (pilote France) ; chronologie par repérage puis détail, paliers 1 an (1945) → 5 → 10 ans avec bilan chiffré. Pilote **2.FR** fait (voir plus haut) ; fiche de lancement `docs/lancements/2.FR_lancement.md`.
- **Réserves pour la revue finale** : 253 points dans `00_RESERVES_A_TRANCHER.md` (+ l'index de 301 dossiers d'Ether).
- **Reste de la série 1.x** : bilan final d'Ether, fiche de lecture en français de chaque source (guides d'Ether livrés avec l'audit : 860 notices), revue des réserves avec Guizmo, puis feu vert pour la couche suivante.
