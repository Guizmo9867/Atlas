# Boucle automatique Ether ↔ Claude — mode d'emploi de Claude

*Version 5.1, 03/10/2026 : Guizmo peut joindre d'autres liens, des captures et des PDF à une source (§3.5 bis). Version 5, 03/10/2026 : on n'attend jamais Guizmo ; un réveil interrompu est repris dès le réveil suivant (verrou rafraîchi à chaque étape) ; un réveil traite aussi les décisions de Guizmo sur les sources, même sans lot. Version 4, 02/10/2026 (après-midi) : alternance des livraisons d'Ether (`coordination/BOUCLE_LIVRAISON_RATISSAGE.md`) et verrou anti-chevauchement des réveils. Version 3, 02/10/2026 : feu vert global de Guizmo pour toute la série 1.x et réserves différées à la revue finale. Version 2, 01/10/2026 (soir). V1 validée par Guizmo avec les ajouts d'Ether (`STATUT.json`, au plus 3 allers-retours) ; V2 intègre l'organisation en conversations Codex d'Ether (`AGENTS.md`, `coordination/`).*

Ce document est lu **au début de chaque réveil** de la tâche programmée de Claude. Chaque réveil est une session neuve, sans souvenir des conversations : tout ce qu'il faut savoir est ici, dans le journal (`docs/JOURNAL_DECISIONS.md`) et dans le protocole des sources (`docs/protocole_sources_ether_claude.md`).

## 0. L'organisation d'Ether (à lire à chaque réveil)

> **Règle de Guizmo du 03/10/2026 : la boucle n'attend jamais Guizmo.** Elle avance toujours aussi loin que possible sur ce qu'elle peut faire seule. Tout ce qui demande Guizmo (décision, autorisation, clic) est noté dans la rubrique « À trancher par Guizmo » du tableau de bord, et le réveil continue ou termine tout le reste. Jamais de question posée en attendant une réponse. Si une autorisation est refusée ou reste sans réponse, la noter et passer à la suite. Un réveil qui n'a pas fini n'est pas grave : le suivant reprend là où il en était (section 2 bis).

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
- `05_pieces_jointes_guizmo/` (pièces jointes de Guizmo, écrites par `reporter_validations_guizmo.py` ; jamais copiées dans le dépôt public) ;
- `99_archive/` (déplacement de lots clos, après décision).

**Feux verts** :
- **Depuis le 02/10/2026, toute la série 1.x (couche villes du Snapshot 0, toutes zones, audit final compris) est autorisée par Guizmo**, sans feu vert par lot (voir `coordination/AUTORISATIONS_RATISSAGE.json`, `autorisation_globale`, et `coordination/POUR_CLAUDE_2026-10-02.md`).
- **Il faut un nouveau feu vert de Guizmo** pour toute autre couche ou famille (routes, réseaux ferroviaires, ports autonomes, douanes…) et pour le passage aux mois. Le rôle portuaire ou ferroviaire d'une ville reste dans le 1.x.
- Claude intègre toute livraison signalée par `PRET_ether.md`. Dans le tableau de bord, l'état d'une suite est recopié fidèlement d'après `AUTORISATIONS_RATISSAGE.json` (autorisée / proposée), jamais deviné.

**Alternance des livraisons d'Ether (depuis le 02/10/2026 après-midi ; détail : `coordination/BOUCLE_LIVRAISON_RATISSAGE.md`, état : `coordination/ETAT_BOUCLE_RATISSAGE.json`)** :
- Ether **produit sans s'arrêter jusqu'à une livraison complète** (son propre réveil est en pause pendant ce temps), puis attend le retour de Claude.
- À partir de la 2e remise, **une remise = les réponses au lot précédent + un nouveau lot complet**, chacun dans **son propre dossier** avec son `STATUT.json` et son `PRET_ether.md`. Il peut donc y avoir **plusieurs lots prêts au même réveil** : les traiter tous, dans l'ordre (d'abord les réponses aux lots déjà intégrés, puis le nouveau lot), avec **un compte rendu par lot**.
- Si les réponses confirment tout sans correction, le dire en une ligne dans le compte rendu (pas de cycle inutile).
- Un lot neuf peut être gros (70 villes et plus). Prendre le temps qu'il faut ; la section 2 bis évite qu'un autre réveil démarre en parallèle.
- Accuser réception de `coordination/POUR_CLAUDE_2026-10-02_BOUCLE_LIVRAISON.md` dans le premier compte rendu qui suit (une ligne).

**IDs des villes** : code du **pays actuel** (`ville-ru-…`, `ville-by-…`, `ville-ua-…`, `ville-md-…`, comme `ville-lt-klaipeda`, `ville-fr-paris`). Si Ether livre des IDs de travail (`ville-su-…`), les rapprocher vers cette convention à l'intégration et le dire dans le compte rendu.

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

## 2 bis. Verrou : un seul réveil de Claude à la fois

Un gros lot peut prendre plus d'une heure, et un autre réveil démarre toutes les heures. Pour éviter deux intégrations en même temps, on utilise le fichier `00_claude_en_cours.json` à la racine du dossier d'échange. Il est **toujours réécrit, jamais supprimé** :
- **Au début**, juste après avoir trouvé du travail (section 3, étape 2), lire ce fichier. S'il dit `"en_cours": true` et que `derniere_activite` (à défaut `depuis`) date de **moins de 50 minutes**, un autre réveil travaille : **s'arrêter aussitôt** sans rien écrire (résumé : « Intégration déjà en cours »). Sinon, l'écrire : `{"en_cours": true, "depuis": "<date-heure ISO>", "derniere_activite": "<idem>", "etape": "<où on en est>", "lots": [...]}`.
- **Pendant le travail**, réécrire `derniere_activite` et `etape` à chaque étape (début de chaque lot, vérification des sources, fusion, construction, validateur, envoi sur GitHub, dossier d'échange). Un réveil vivant garde ainsi son verrou frais.
- **À la fin** (réussite ou erreur), le réécrire avec `"en_cours": false`, `"fin"` et le résultat.
- Un verrou dont `derniere_activite` a **plus de 50 minutes** est celui d'un réveil interrompu (PC éteint, limite atteinte) : le réveil suivant **le reprend** (le dire dans le résumé). Il lit `etape`, puis vérifie avec `git status`, `git log`, les `STATUT.json` et les `PRET_claude.md` ce qui avait déjà été fait, pour reprendre là où ça s'était arrêté sans rien faire deux fois.

## 3. Ce que fait un réveil

> **ORDRE OBLIGATOIRE (incident des 02 et 03/10 : deux réveils se sont arrêtés juste après l'envoi sur GitHub, sans rien déposer pour Ether)** :
> faire **avant** l'envoi sur GitHub (étape 8) tout ce qui concerne le dossier d'échange : copie du compte rendu et du README dans `01_lots/<lot>/`, `STATUT.json`, `02_references/`, fiche de chiffres, `00_RESERVES_A_TRANCHER.md`, `00_SOURCES_A_VALIDER.md`/`.html`, tableau de bord. **Aussitôt le push vérifié, écrire `PRET_claude.md` puis remettre le verrou à `"en_cours": false`.** La republication de la page « Sources à valider » sur claude.ai vient en tout dernier : si elle échoue ou si le réveil s'arrête là, rien d'important n'est perdu.

1. Lire `docs/REPRISE.md` (fiche de reprise), ce document, le tableau de bord et le haut du journal des décisions.
2. Repérer le travail à faire :
   - les lots à traiter (section 2) ;
   - un réveil interrompu à reprendre (verrou `"en_cours": true` sans activité depuis plus de 50 minutes, section 2 bis) ;
   - des **décisions de Guizmo sur les sources** pas encore reportées : `python outils/sources/reporter_validations_guizmo.py --verifier $HOME/mnt/Desktop--Atlas` (fichier `decisions_sources_guizmo.json` et fiches de `05_fiches_sources/` du dossier d'échange) ; et, si l'outil ArtifactData est disponible, la collection `validations` de la page claude.ai comparée à `data/sources/validations_guizmo_claudeai.json`.
   **S'il n'y a rien de tout cela, s'arrêter tout de suite**, sans rien écrire. S'il n'y a que des décisions de Guizmo : faire seulement l'étape 3.5 (report et régénérations), le validateur, l'envoi sur GitHub, `02_references/`, le tableau de bord et la republication de la page, avec le verrou comme pour un lot.
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
   4. **Construire ou mettre à jour le lot** avec `outils/villes/construire_villes_<lot>.py` (modèle : `construire_villes_1_4.py`). Il produit `data/snapshot0/<lot>.json`. Puis lancer `python outils/villes/appliquer_validations_guizmo.py` (applique aux fiches les sources validées par Guizmo : mention « validée par Guizmo », rôles retirés de « À renforcer » ; pour « pour 1945 », seule la partie valable au 01/01/1945 est appliquée).
   5. **Décisions de Guizmo sur les sources** : lire la collection `validations` de la page « Sources à valider » (outil ArtifactData, action list) et l'écrire dans `data/sources/validations_guizmo_claudeai.json` ; puis `python outils/sources/reporter_validations_guizmo.py $HOME/mnt/Desktop--Atlas` et `python outils/villes/appliquer_validations_guizmo.py` (lit aussi `decisions_sources_guizmo.json` déposé par Guizmo dans le dossier d'échange ; écrit aussi `docs/NOTES_GUIZMO_SOURCES.md`). La décision « Prouve pour 1945 (la suite plus tard) » (`verifiee_s0`) vaut validation pour le Snapshot 0 : la source reste au registre, et sa note dit quel changement reprendre plus tard dans la chronologie ; ne jamais retirer une telle source. Ensuite **régénérer** `python outils/sources/liste_sources_a_valider.py`, puis la fiche de chiffres `python outils/projet/chiffres_projet.py` (sert au dossier de financement d'Ether). Puis le fichier de toutes les réserves : mettre à jour la liste `QUESTIONS_CLAUDE` en tête de `outils/projet/reserves_a_trancher.py` (questions nouvelles ou closes du compte rendu), puis `python outils/projet/reserves_a_trancher.py $HOME/mnt/Desktop--Atlas` (écrit `docs/RESERVES_A_TRANCHER.md` et `00_RESERVES_A_TRANCHER.md` dans le dossier d'échange). Puis `python outils/sources/exporter_sources_a_valider.py $HOME/mnt/Desktop--Atlas` (écrit `00_SOURCES_A_VALIDER.md` et `.html` dans le dossier d'échange : la liste lisible par Ether, avec les liens). Si un point de réserve n'a pas de « Sources liées », compléter le dictionnaire `CITEES` du script.
   5 ter. **Fiches de sources écrites avec Ether** (`05_fiches_sources/`, modèle `docs/MODELE_FICHE_SOURCE.md`) : Guizmo discute d'une source avec Ether dans un chat simple, puis dépose la fiche (décision, ce qui est prouvé, citation exacte, où la lire, liens, « vu par Guizmo »). `reporter_validations_guizmo.py` les lit comme les autres décisions (champ `fiche_avec_ether`). Si « vu par Guizmo » n'est pas « oui », essayer de retrouver la citation sur la page (WebFetch) et le dire dans le compte rendu ; une citation introuvable n'est jamais présentée comme lue par Claude. Le « ce qui est prouvé » et la citation servent aussi de base à la fiche de lecture en français de l'audit final.
   5 bis. **Autres liens et pièces jointes de Guizmo** (sources dont `complements_guizmo.a_verifier` est vrai ; liste dans `docs/NOTES_GUIZMO_SOURCES.md`). Quand une source ne prouve pas ou a un lien mort, Guizmo peut proposer d'autres liens et joindre des captures ou des PDF (dans `05_pieces_jointes_guizmo/<source_id>/` du dossier d'échange). Pour chacune :
      - **liens** : les faire lire par les sous-agents, comme les sources d'Ether (WebFetch seulement, jamais de contournement) ;
      - **captures et PDF** (dans la langue d'origine, sans traduction : Claude les lit telles quelles ; pas de rognage demandé à Guizmo) : les copier dans la machine cloud (`device_stage_files`) et les lire soi-même (outil Read ; pour un PDF, les pages utiles) ; noter la citation exacte trouvée ;
      - si la preuve tient : ajouter au registre une **nouvelle source** par lien ou document confirmé (`src-guizmo-<slug>`, mêmes `cibles` et `usages_atlas` que l'ancienne, `verification_claude: ok`, citation dans `resume_passage` ; pour une pièce jointe sans lien public, `url` vide et `archive_locale` = chemin dans le dossier d'échange) ; dans l'ancienne source, mettre `statut_usage: non_verifiee_remplacee` et `sources_remplacement` ; mettre à jour l'`usage` dans les villes concernées et retirer « À renforcer » si le rôle est maintenant prouvé ;
      - si elle ne tient pas : ne rien appliquer, le dire ;
      - dans tous les cas : `a_verifier: false` et `resultat_claude` (une phrase) dans `complements_guizmo`, puis relancer `reporter_validations_guizmo.py` (pour la liste des notes) et le dire au tableau de bord.
      Les pièces jointes ne vont **jamais** dans le dépôt (dépôt public, droits d'auteur) : seulement leur chemin et la citation.
   6. **Valider** avec `node app/scripts/validate-data.mjs` (depuis `app/`) : **zéro erreur obligatoire**. Vérifier aussi qu'aucun secret n'est dans les fichiers : `grep -rIE "github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}" --exclude-dir=.git --exclude-dir=node_modules .` doit ne rien renvoyer.
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
   *Important : un gros lot use beaucoup de contexte. Faire les étapes 9 (dossier d'échange) et 4 à 6 avant le push (encadré ci-dessus) ; si le réveil a été interrompu, le réveil suivant (verrou sans activité depuis plus de 50 minutes) termine ce qui manque sans refaire l'intégration.*
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
4. **Rafraîchir** `02_references/` : copier `JOURNAL_DECISIONS`, `SUIVI_RATISSAGE`, `protocole_sources_ether_claude`, `LEXIQUE_ID`, `IDEES_POUR_PLUS_TARD`, `CHIFFRES_PROJET`, `NOTES_GUIZMO_SOURCES` et ce document.
4 bis. **Mettre à jour la section 5 « État » de `docs/REPRISE.md`** (chiffres, dernière intégration, ce qui attend qui ; le reste seulement si une règle change ; la fiche doit rester courte), puis la copier en `00_REPRISE.md` du dossier d'échange et dans `02_references/`. Si l'outil Projects est disponible, l'écrire aussi en `claude/REPRISE.md` du projet.
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
