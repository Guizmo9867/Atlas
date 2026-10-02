# Boucle automatique Ether ↔ Claude — mode d'emploi de Claude

*Version 3, 02/10/2026 : feu vert global de Guizmo pour toute la série 1.x et réserves différées à la revue finale. Version 2, 01/10/2026 (soir). V1 validée par Guizmo avec les ajouts d'Ether (`STATUT.json`, au plus 3 allers-retours) ; V2 intègre l'organisation en conversations Codex d'Ether (`AGENTS.md`, `coordination/`).*

Ce document est lu **au début de chaque réveil** de la tâche programmée de Claude. Chaque réveil est une session neuve, sans souvenir des conversations : tout ce qu'il faut savoir est ici, dans le journal (`docs/JOURNAL_DECISIONS.md`) et dans le protocole des sources (`docs/protocole_sources_ether_claude.md`).

## 0. L'organisation d'Ether (à lire à chaque réveil)

Depuis le 01/10/2026 au soir, Ether travaille dans deux conversations Codex reliées au dossier Atlas :
- **ATLAS — RATISSAGE 01** (Ether + Guizmo) : recherches et réponses point par point à mes comptes rendus ;
- **ATLAS — FINANCEMENT 01** : écrit seulement dans `04_financement/`.

**Au début de chaque réveil, lire aussi** (lecture seule) :
- `AGENTS.md` (consignes communes) ;
- `coordination/00_FONCTIONNEMENT.md` ;
- `coordination/CONVERSATIONS.json` et `coordination/AUTORISATIONS_RATISSAGE.json` (feux verts de Guizmo) ;
- `coordination/QUESTIONS_CLAUDE.md` (le suivi par Ether de mes questions, avec leurs numéros : Q13-01, Q14-02…).

**Fichiers d'Ether : jamais modifiés, déplacés ou écrasés par Claude**, y compris lors des synchronisations :
- `AGENTS.md` ;
- tout `coordination/` ;
- tout `04_financement/` ;
- les fichiers d'Ether dans `01_lots/`.

Claude écrit seulement :
- ses propres fichiers dans `01_lots/<lot>/` (comptes rendus, `00_claude_README_du_lot.md`, `PRET_claude.md`, et `STATUT.json` en conservant tous les champs inconnus) ;
- `00_TABLEAU_DE_BORD.md` ;
- `02_references/` ;
- `99_archive/` (déplacement de lots clos, après décision).

**Feux verts** :
- **Depuis le 02/10/2026, toute la série 1.x (couche villes du Snapshot 0, toutes zones, audit final compris) est autorisée par Guizmo**, sans feu vert par lot (voir `coordination/AUTORISATIONS_RATISSAGE.json`, `autorisation_globale`, et `coordination/POUR_CLAUDE_2026-10-02.md`).
- **Il faut un nouveau feu vert de Guizmo** pour toute autre couche ou famille (routes, réseaux ferroviaires, ports autonomes, douanes…) et pour le passage aux mois. Le rôle portuaire ou ferroviaire d'une ville reste dans le 1.x.
- Claude intègre toute livraison signalée par `PRET_ether.md`. Dans le tableau de bord, l'état d'une suite est recopié fidèlement d'après `AUTORISATIONS_RATISSAGE.json` (autorisée / proposée), jamais deviné.

**Comptes rendus** : toujours dans cet ordre de rubriques :
1. **Intégré** ;
2. **Corrigé** ;
3. **Questions encore ouvertes** : reprendre l'ID de `coordination/QUESTIONS_CLAUDE.md` quand la question y figure (exemple : « Q14-02 ») ; pour une question nouvelle, proposer un ID au même format (exemple : « Q15-01 ») ;
4. **Réserves de source** ;
5. **Décisions attendues de Guizmo** ;
6. **Qualité de la livraison**.



- **Dossier d'échange** : le dossier « Atlas » du Bureau de Guizmo, connecté à la session (dans le shell de l'ordinateur : `$HOME/mnt/Desktop--Atlas`).
  - `00_TABLEAU_DE_BORD.md` : écrit par Claude seul.
  - `01_lots/<lot>/` : un dossier par lot, avec les fichiers d'Ether et de Claude, `STATUT.json`, `PRET_ether.md` et `PRET_claude.md`.
  - `02_references/` : copie des docs du dépôt, rafraîchie par Claude à chaque envoi.
  - `03_idees/` : idées pour plus tard.
  - `04_financement/` : domaine d'Ether. **Claude n'y écrit jamais.** Claude l'aide seulement avec la fiche de chiffres (`02_references/CHIFFRES_PROJET.md`), et par une relecture de vérité si Guizmo la demande.
  - `99_archive/` : lots clôturés.
- **Dépôt** : `C:\Users\guill\Documents\GitHub\Atlas` (dans le shell de l'ordinateur : `$HOME/mnt/GitHub--Atlas`). Public sur GitHub : https://github.com/Guizmo9867/Atlas. **Seule source de vérité.**
- **Travailler sur l'ordinateur de Guizmo** (`device_bash`), directement dans ces deux dossiers. On n'utilise la machine cloud que pour ce que l'ordinateur ne peut pas faire : requêtes Wikidata si le réseau local les refuse, sous-agents de vérification, publication de la page « Sources à valider ».

## 2. La machine à états (par lot)

`01_lots/<lot>/STATUT.json` :

```json
{"lot": "villes_1-5", "etat": "attente_claude", "dernier_acteur": "ether", "cycles": 1,
 "validation_guizmo_requise": false, "a_trancher": [], "mis_a_jour": "2026-10-02T09:00"}
```

- `etat` : `attente_claude` | `attente_ether` | `attente_guizmo` | `clos`.
- `cycles` : nombre de livraisons d'Ether sur ce lot (le ratissage = 1, chaque réponse d'Ether = +1).
- Un lot est **à traiter par Claude** si `PRET_ether.md` est **plus récent** que `PRET_claude.md` (ou si `PRET_claude.md` n'existe pas). Sinon, Claude n'y touche pas : une livraison sans `PRET_ether.md` est peut-être encore en cours d'écriture.
- Si `STATUT.json` manque mais que `PRET_ether.md` est là, Claude le crée.

## 3. Ce que fait un réveil

1. Lire ce document, le tableau de bord et le haut du journal des décisions.
2. Repérer les lots à traiter (section 2). **S'il n'y en a aucun, s'arrêter tout de suite**, sans rien écrire.
3. Pour chaque lot à traiter, dans l'ordre :
   1. **Lire toute la livraison d'Ether** : le `.md` pour Claude, les JSON de données et le delta de sources. Copier les fichiers d'Ether dans le dépôt, comme pour les lots précédents :
      - données ou corrections → `data/sources/deltas_ether/<date>_<lot>_*.json` ;
      - document principal → `data/snapshot0/<lot>_brief_ether.md` ou `<lot>_reponses_ether_<date>.md`.
   2. **Vérifier les sources nouvelles** (et celles qu'Ether a relues) avec des sous-agents en parallèle :
      - outil Agent, type `general-purpose`, modèle `sonnet`, au plus 6 sources par sous-agent ;
      - WebFetch seulement, jamais de contournement d'un blocage ;
      - chaque sous-agent écrit un `{id, statut, citation, commentaire}` par source ;
      - statuts possibles : ok / limite / faible / non_verifiee / lien_casse.
      Recompter soi-même à partir des fichiers. Garder le résultat dans `data/sources/verifications_claude/<date>_<lot>.json`.
   3. **Fusionner les sources au registre** avec un script `outils/villes/fusion_sources_<lot>.py` (modèle : `fusion_sources_1_4_reponses.py`) : fusion par `source_id`, version du registre +0.01, tous les champs en **français**.
   4. **Construire ou mettre à jour le lot** avec `outils/villes/construire_villes_<lot>.py` (modèle : `construire_villes_1_4.py`). Il produit `data/snapshot0/<lot>.json`.
   5. **Régénérer** `python outils/sources/liste_sources_a_valider.py`, puis la fiche de chiffres `python outils/projet/chiffres_projet.py` (sert au dossier de financement d'Ether).
   6. **Valider** avec `node app/scripts/validate-data.mjs` (depuis `app/`) : **zéro erreur obligatoire**. Vérifier aussi qu'aucun secret n'est dans les fichiers (`grep -rIl "github_pat_\|ghp_"` hors `.git` et `node_modules`).
   7. **Documenter** :
      - README du lot dans `data/snapshot0/` ;
      - journal des décisions (une section datée en haut) ;
      - `docs/SUIVI_RATISSAGE.md` ;
      - compte rendu pour Ether dans `docs/pour_ether/<date>_<lot>.md`.
   7 bis. **Noter la qualité de la livraison** (pour régler le moteur d'Ether) : à la fin du compte rendu, ajouter une section « Qualité de la livraison » avec :
      - le moteur indiqué par Ether dans `PRET_ether.md` ;
      - le % de ses sources confirmées par la relecture ;
      - le nombre d'affirmations introuvables sur la page citée ;
      - les liens morts ;
      - les champs pas en français ;
      - les fichiers ou champs du protocole manquants ;
      - les corrections que Claude a dû faire.
      Ajouter une ligne au tableau `docs/QUALITE_LIVRAISONS.md` (le créer s'il n'existe pas) : date, lot, moteur, et ces chiffres.
   *Git a besoin d'effacer ses fichiers de verrou (`.git/index.lock`). Si git répond « unable to unlink » ou « index.lock: File exists », demander d'abord l'autorisation de suppression pour le dossier du dépôt (outil `device_request_delete_permission`, raison : verrous temporaires de git), puis effacer uniquement les fichiers `.git/*.lock` laissés par l'essai raté et recommencer. Jamais d'autre suppression.*
   8. **Envoyer sur GitHub** (depuis le dépôt sur l'ordinateur) :
      - pour regarder l'état : `GIT_OPTIONAL_LOCKS=0 bash .git/claude_git.sh status --short` (sans cette variable, un verrou `.git/index.lock` impossible à effacer peut rester) ;
      - `bash .git/claude_git.sh add -A` ;
      - `bash .git/claude_git.sh commit -F -`, avec un message en français qui se termine par les lignes d'attribution fournies par la session ;
      - `bash .git/claude_git.sh push origin main` ;
      - puis vérifier avec `bash .git/claude_git.sh ls-remote origin main`.
   9. **Dossier d'échange** :
      - copier le compte rendu dans `01_lots/<lot>/<date>_claude_compte_rendu_<n>.md` ;
      - copier (ou mettre à jour) le README du lot dans `01_lots/<lot>/00_claude_README_du_lot.md` ;
      - mettre à jour `STATUT.json` ;
      - écrire `PRET_claude.md` **en dernier** (une ligne : date, ce qui a été fait, s'il y a des questions).
4. **Rafraîchir** `02_references/` : copier `JOURNAL_DECISIONS`, `SUIVI_RATISSAGE`, `protocole_sources_ether_claude`, `LEXIQUE_ID`, `IDEES_POUR_PLUS_TARD`, `CHIFFRES_PROJET` et ce document.
5. **Mettre à jour `00_TABLEAU_DE_BORD.md`** : où on en est, qui attend quoi, « Réserves pour la revue finale 1.x », rubrique « À trancher par Guizmo » (vide en temps normal).
6. **Republier la page « Sources à valider »** (artifact https://claude.ai/artifact/YBCUsTgEb1XwNmRwVnd9Lr) :
   - lire d'abord l'artifact (Artifact, action `read`) ;
   - remplacer `__DONNEES__` dans `outils/sources/page_sources_a_valider_modele.html` par le contenu de `data/sources/sources_a_valider.json` (en échappant `</`) ;
   - publier avec `url` = cette adresse.
   Si ça échoue, le noter au tableau de bord : ça ne bloque pas la boucle.
7. **Notifier Guizmo** (notification push) seulement s'il y a un point « à trancher » de la liste de la section 5 (hors réserves 1.x) ou une erreur. Sinon, une ligne au tableau de bord suffit.

## 4. Les règles de fond (rappel ; le détail est dans le journal)

- **Snapshot 0** = dernier état connu avant le 01/01/1945 à 00:00. Un changement daté du 1er janvier s'applique après : on le note pour le ratissage de janvier.
- **Villes** :
  - ID : `ville-<cc>-<slug>`, type `ville`, géométrie Point, état `etat-01`, `valid_from` inconnu ;
  - `proprietes` : `nom` (nom à la date, seulement s'il diffère du nom actuel), `nom_local`, `importance_atlas` (A/B/C/D), `capitale` (nationale / regionale / territoire), `roles[]`, `note`.
- **Noms** :
  - la fiche porte le nom actuel ;
  - l'état porte le nom de 1945, **sur preuve individuelle** ;
  - exonyme français s'il est attesté, sinon la forme locale attestée à la date ;
  - les autres formes vont en `aliases` ;
  - on ne renomme jamais d'après la seule couleur d'un territoire.
- **Capitale régionale** = siège administratif de fait sous occupation ou en RSS (Vienne, Prague, Cracovie, Tallinn, Riga, Vilnius). Le rang (importance) et la capitale sont indépendants.
- **Preuves** : rôle par rôle. Dans chaque ville, l'`usage` d'une source dit ce qu'elle prouve, avec la mention « (non vérifiée par Claude) » ou « (lecture partielle) » si besoin. La note de la ville finit par « À renforcer : … » pour chaque rôle qui n'a aucune preuve confirmée (`ok`).
- **Positions** :
  - Wikidata (CC0), SPARQL sur `query.wikidata.org` avec l'User-Agent `AtlasEurasie/0.1` ;
  - garder le QID dans `outils/villes/wikidata_ratissage_<lot>.json` ;
  - vérifier que le QID est le bon (erreurs passées : Brno, Plzeň, Poznań).
- **Interdits** :
  - supprimer quoi que ce soit (on archive) ;
  - mettre des données OSM/ODbL dans le corpus ;
  - contourner un blocage WebFetch ;
  - écrire dans `04_financement/` ;
  - commiter un secret ;
  - envoyer sur GitHub si le validateur signale une erreur.

## 5. Réserves et limites automatiques

**Règle de Guizmo du 02/10/2026 (série 1.x)** : toutes les réserves sont gardées **par lot** pour une revue avec Guizmo **à la fin de toute la série 1.x**. On ne lui pose **aucune question au cas par cas** et on ne le notifie pas pour elles.
- Conflit de sources impossible à départager, décision historique contestable (frontière, capitale, nom sans preuve, rang), point non conclu après **3 cycles** : **intégrer ce qui est sûr, ne pas appliquer le point incertain**, l'écrire dans la rubrique « Réserves » du compte rendu et dans la section « Réserves pour la revue finale 1.x » du tableau de bord (une ligne par lot, renvoi au fichier de réserves d'Ether `01_lots/<lot>/<date>_ether_reserves_revue_finale.md` s'il existe).
- Après 3 cycles, le lot reste ouvert avec ses réserves (`etat` : `reserves_revue_finale` dans `STATUT.json`, sans effacer les champs existants) ; cela ne gèle ni les autres lots 1.x ni la suite.
- Le report ne vaut jamais validation : une valeur incertaine n'est pas appliquée parce qu'elle est reportée.

**Restent « À trancher par Guizmo » avec notification** (hors série 1.x ou à risque pour le dépôt) :
- changement du modèle de données ou de la structure du dépôt ;
- modification de l'interface (code dans `app/src`) ;
- suppression de données ;
- livraison d'Ether **hors du périmètre autorisé** (autre couche, passage aux mois) : ne pas l'intégrer, la signaler.

**Pour Ether, pas pour Guizmo** : livraison incomplète, illisible ou contraire au protocole (champs en anglais, sources sans URL…) → intégrer le reste et poser la question dans le compte rendu.

## 6. Clore un lot

Quand un compte rendu de Claude n'a plus de question ouverte et qu'Ether confirme (ou que Guizmo le décide) :
- `etat` passe à `clos` ;
- le dossier du lot est déplacé dans `99_archive/` (déplacement avec `mv -n`, jamais de suppression) ;
- le tableau de bord est mis à jour.
