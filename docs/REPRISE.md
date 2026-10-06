# Atlas Eurasie — fiche de reprise (à lire en premier)

*Fiche courte pour qu'un nouveau Claude, dans n'importe quelle conversation, sache où on en est sans tout relire. Le reste se lit seulement si besoin. Tenue à jour par Claude (section « État » à chaque lot, le reste quand une règle change). Original : `docs/REPRISE.md` du dépôt ; copies : `00_REPRISE.md` du dossier d'échange et `claude/REPRISE.md` du projet claude.ai. Dernière mise à jour : 06/10/2026.*

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

## 4. Où trouver le détail (à lire seulement si besoin)

- `docs/JOURNAL_DECISIONS.md` : toutes les décisions, datées (lire seulement le haut).
- `docs/BOUCLE_AUTOMATIQUE.md` : le mode d'emploi complet de la boucle.
- `docs/protocole_sources_ether_claude.md`, `docs/LEXIQUE_ID.md` : format des sources et des identifiants.
- `00_TABLEAU_DE_BORD.md` (dossier d'échange) : qui attend quoi, en détail.
- `docs/IDEES_POUR_PLUS_TARD.md` : idées reportées (régime routier, sources traduites…).
- `docs/NOTES_GUIZMO_SOURCES.md`, `docs/RESERVES_A_TRANCHER.md`, `docs/CHIFFRES_PROJET.md`.

## 5. État (mis à jour à chaque lot)

- **Frontières** : lots 01 à 04 intégrés (74 territoires, 4 lignes de front).
- **Villes** : 1.0 à 1.9 intégrés + 15 villes de l'audit transversal, **1 559 villes**. Lots 1.3 à 1.8 : 3 cycles faits, en attente de la revue finale des réserves. 1.9 : 2 cycles (49 villes « à renforcer »).
- **Dernière intégration (06/10, nuit)** : réponses 1.9 cycle 2 (Q19-01 et Q19-02 closes, restes en réserve) et **audit transversal 1.x d'Ether** : 15 villes ajoutées (France, Grande-Bretagne : `data/snapshot0/villes_1-x_audit_complements.json`), 23 sources ajoutées à 22 villes du lot 1.0, index de 299 dossiers de réserve. Nouvelle question Q19-03 (sources de l'audit illisibles ou partielles).
- **Ether** : prochaine étape = réponse à Q19-03 si utile, puis **bilan groupé des réserves avec Guizmo** (pas de nouveau lot géographique). Financement : réveil quotidien.
- **Sources** : registre v1.30, 887 sources ; 305 à valider par Guizmo, dont **161 importantes**. Page « Sources à valider » : sur claude.ai, ou `00_SOURCES_A_VALIDER.html` dans le dossier d'échange.
- **Couches suivantes prévues** (une par une, chacune avec feu vert) : routes, rail, maritime, douanes, plaques d'immatriculation, anecdotes sur les flux, migrations ; puis janvier 1945.
- **Réserves pour la revue finale** : 252 points dans `00_RESERVES_A_TRANCHER.md` (+ l'index de 299 dossiers de l'audit d'Ether).
- **Reste de la série 1.x** : fiche de lecture en français de chaque source (guides d'Ether livrés avec l'audit : 860 notices), revue des réserves avec Guizmo, puis feu vert pour la couche suivante.
