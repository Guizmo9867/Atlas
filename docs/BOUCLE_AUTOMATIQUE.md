# Boucle automatique Ether ↔ Claude — mode d'emploi de Claude

*Version 1, 01/10/2026. Validée par Guizmo, avec les ajouts d'Ether (`STATUT.json` par lot, au plus 3 allers-retours automatiques).*

Ce document est lu **au début de chaque réveil** de la tâche programmée de Claude. Chaque réveil est une session neuve, sans souvenir des conversations : tout ce qu'il faut savoir est ici, dans le journal (`docs/JOURNAL_DECISIONS.md`) et dans le protocole des sources (`docs/protocole_sources_ether_claude.md`).

## 1. Les lieux

- **Dossier d'échange** : le dossier « Atlas » du Bureau de Guizmo, connecté à la session (dans le shell de l'ordinateur : `$HOME/mnt/Desktop--Atlas`).
  - `00_TABLEAU_DE_BORD.md` : écrit par Claude seul.
  - `01_lots/<lot>/` : un dossier par lot, avec les fichiers d'Ether et de Claude, `STATUT.json`, `PRET_ether.md` et `PRET_claude.md`.
  - `02_references/` : copie des docs du dépôt, rafraîchie par Claude à chaque envoi.
  - `03_idees/` : idées pour plus tard.
  - `04_financement/` : domaine d'Ether. **Claude n'y écrit jamais.**
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
   5. **Régénérer** `python outils/sources/liste_sources_a_valider.py`.
   6. **Valider** avec `node app/scripts/validate-data.mjs` (depuis `app/`) : **zéro erreur obligatoire**. Vérifier aussi qu'aucun secret n'est dans les fichiers (`grep -rIl "github_pat_\|ghp_"` hors `.git` et `node_modules`).
   7. **Documenter** :
      - README du lot dans `data/snapshot0/` ;
      - journal des décisions (une section datée en haut) ;
      - `docs/SUIVI_RATISSAGE.md` ;
      - compte rendu pour Ether dans `docs/pour_ether/<date>_<lot>.md`.
   8. **Envoyer sur GitHub** (depuis le dépôt sur l'ordinateur) :
      - `bash .git/claude_git.sh add -A` ;
      - `bash .git/claude_git.sh commit -F -`, avec un message en français qui se termine par les lignes d'attribution fournies par la session ;
      - `bash .git/claude_git.sh push origin main` ;
      - puis vérifier avec `bash .git/claude_git.sh ls-remote origin main`.
   9. **Dossier d'échange** :
      - copier le compte rendu dans `01_lots/<lot>/<date>_claude_compte_rendu_<n>.md` ;
      - mettre à jour `STATUT.json` ;
      - écrire `PRET_claude.md` **en dernier** (une ligne : date, ce qui a été fait, s'il y a des questions).
4. **Rafraîchir** `02_references/` : copier `JOURNAL_DECISIONS`, `SUIVI_RATISSAGE`, `protocole_sources_ether_claude`, `LEXIQUE_ID`, `IDEES_POUR_PLUS_TARD` et ce document.
5. **Mettre à jour `00_TABLEAU_DE_BORD.md`** : où on en est, qui attend quoi, rubrique « À trancher par Guizmo ».
6. **Republier la page « Sources à valider »** (artifact https://claude.ai/artifact/YBCUsTgEb1XwNmRwVnd9Lr) :
   - lire d'abord l'artifact (Artifact, action `read`) ;
   - remplacer `__DONNEES__` dans `outils/sources/page_sources_a_valider_modele.html` par le contenu de `data/sources/sources_a_valider.json` (en échappant `</`) ;
   - publier avec `url` = cette adresse.
   Si ça échoue, le noter au tableau de bord : ça ne bloque pas la boucle.
7. **Notifier Guizmo** (notification push) seulement s'il y a un point « à trancher » ou une erreur. Sinon, une ligne au tableau de bord suffit.

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

## 5. Limites automatiques : quand s'arrêter et passer la main à Guizmo

Mettre `etat` à `attente_guizmo` et `validation_guizmo_requise` à `true`, ajouter le point à `a_trancher` et à la rubrique « À trancher par Guizmo » du tableau de bord, puis notifier. **Intégrer quand même tout ce qui est sûr.** Les cas :

- **plus de 3 cycles** sur un lot sans clôture ;
- conflit de sources qu'on ne peut pas départager ;
- décision historique contestable : frontière, capitale, nom sans preuve, rang ;
- changement du modèle de données ou de la structure du dépôt ;
- modification de l'interface (code dans `app/src`) ;
- suppression de données ;
- livraison d'Ether incomplète, illisible ou contraire au protocole (champs en anglais, sources sans URL…) : intégrer le reste et poser la question dans le compte rendu.

## 6. Clore un lot

Quand un compte rendu de Claude n'a plus de question ouverte et qu'Ether confirme (ou que Guizmo le décide) :
- `etat` passe à `clos` ;
- le dossier du lot est déplacé dans `99_archive/` (déplacement avec `mv -n`, jamais de suppression) ;
- le tableau de bord est mis à jour.
