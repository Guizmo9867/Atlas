# Atlas Eurasie — Récapitulatif technique

Ce document résume toutes les décisions techniques prises entre Guizmo, Ether (ChatGPT) et Claude (chat), en amont d'une session Cowork/Claude Code chargée de construire le prototype V0. Il complète — sans le remplacer — le document fondateur v0.1 (vision, couches, philosophie éditoriale) qui existe déjà séparément.

## 1. Équipe et méthode de travail

- **Ether (ChatGPT)** : structure, idéation, recherche historique brute.
- **Claude (chat)** : validation technique, architecture, gabarits, contrôle de cohérence.
- **Guizmo** : décideur final, testeur, pont humain entre les deux IA (pas de communication directe Claude ↔ Ether, mur réglementaire EEE).

Méthode de production du contenu historique, en 4 étapes :

```
RECHERCHE BRUTE → BROUILLON → SÉLECTION → JSON CANONIQUE
```

Le brouillon est volontairement plus libre que le JSON final (champ de travail : date/période, événement candidat, lieu, ce qui s'est passé, pourquoi ça concerne les flux, catégories probables, portée pressentie, géographie possible, sources trouvées, événements liés possibles, questions/incertitudes, verdict GARDER/RÉSERVE/REJETER/FUSIONNER).

### Convention d'ID (verrouillée, immuable une fois intégrée)

- **Événements** : `annee-pays-motcle-titre` (ex: `1945-de-partition-berlin`). Le titre peut évoluer, l'ID jamais.
- **Entités temporelles** : `type-pays-motcle[-precision]` (ex: `pont-fr-trois-pins`).
- Règles communes : minuscules, sans accents, sans apostrophes, séparés par `-`, courts.
- Un `LEXIQUE_ID.md` doit tracer chaque mot-clé utilisé dans un ID (par domaine : territoire, frontière, infrastructure, transport, migration, criminalité, accidentologie) pour éviter les synonymes involontaires (ouverture/inauguration/mise-service...). Construit organiquement, jamais pré-rempli à l'avance.
- **Point non tranché repéré dans les vraies données** : le préfixe géographique n'est pas encore uniforme entre codes courts façon ISO (`fi`, `mn`) et noms complets (`urss`). À trancher avant que l'URSS génère beaucoup d'autres sous-entités (RSS ukrainienne, biélorusse, etc.).
- Un registre canonique des pays/acteurs (ex: éviter URSS / Union soviétique / USSR selon le jour) est nécessaire, dans le même esprit que le lexique d'ID. Les identifiants sémantiques (`souverainete_id`, `controle_id`, etc.) doivent rester courts et réutilisables — la nuance interprétative va dans `note`, jamais dans l'id lui-même.

## 2. Périmètre géographique et temporel

- **Début** : 1945-01-01. **Fin** : glissante, année courante.
- **Zone permanente** : Europe entière (UK/Irlande, Scandinavie, Baltes, Balkans, Turquie, Caucase compris) + URSS entière de 1945 (Russie euro/asiatique, Ukraine, Biélorussie, Moldavie, Caucase soviétique, Kazakhstan, Asie centrale soviétique jusqu'au Pacifique).
- **Zone contextuelle** : Moyen-Orient, Afghanistan, Afrique du Nord — uniquement quand un phénomène étudié les connecte directement aux flux principaux.
- **Hors périmètre de recherche systématique** : Chine, Inde, Japon — mais peuvent apparaître ponctuellement (ex: Japon ↔ Sakhaline/Kouriles, parce que ça modifie le territoire soviétique).

## 3. Snapshot 0 (1945-01-01 00:00)

- Ce n'est **pas** un objet de données séparé : c'est simplement le premier `etat` (avec `valid_from: 1945-01-01`) de chaque entité concernée. La carte à une date donnée est toujours *calculée* à partir des états valides ce jour-là, jamais stockée telle quelle.
- **Obligatoire dans Snapshot 0** : limites des États/territoires du périmètre, statut juridique, contrôle effectif quand il diverge du statut juridique, zones occupées/annexées/contestées pertinentes, géométrie sourcée des frontières, principaux repères géographiques.
- **Pas obligatoire dès Snapshot 0** : routes, rails, ponts, ports, flux — ces couches s'enrichissent progressivement, seulement quand un événement réel le justifie.
- Le 1er janvier 1945 est une date de guerre active (fronts mouvants). Pour les zones de combat, une géométrie approximative (`zone`, Polygon) avec `certitude: estime` est acceptable plutôt que de forcer une ligne précise inexistante dans les sources. "Complet" veut dire *aucune zone du périmètre sans entrée*, pas *toutes les lignes tracées au mètre*.
- Rythme de travail : mensuel pour 1945 spécifiquement (front très mouvant) — pas forcément la bonne cadence pour des décennies plus calmes plus tard, à réévaluer par période.

## 4. Gabarit JSON — Événement

Fichier : `gabarit_evenement_atlas.json` (joint).

Champs clés : `id`, `titre`, `annee`, `date_precise`, `date_fin`, `pays`, `lieu`, `geographie` (type point/zone/frontiere/parcours/corridor + `geometrie` GeoJSON + `geometrie_ref` optionnelle), `categories`, `niveau_importance` (structurel/evenement_majeur/micro_histoire), `profondeur_affichage` (atlas/regional/archive — archive = pastille visible seulement en zoom rapproché), `resume`, `contexte`, `deroulement`, `consequences` (humaines/economiques/politiques/reglementaires/logistiques), `relations`, `certitude_evenement`, `etat_sources`, `notes_incertitude`, `sources` (niveau A/B/C), `temoignage_personnel`.

**Corrections apportées en cours de route :**
- Géométrie : passée d'une simple paire de coordonnées à du vrai GeoJSON (Point/LineString/Polygon/MultiLineString), ordre **[longitude, latitude]** impératif.
- `certitude` scindé en deux axes indépendants : `certitude_evenement` (l'événement a-t-il bien eu lieu) vs `etat_sources` (les sources sont-elles d'accord sur les détails) — un événement peut être confirmé avec des chiffres divergents.
- `relations[].cible_type` ajouté (`evenement` | `entite`) : une relation `modifie` vise presque toujours une entité, pas un autre événement.

## 5. Gabarit JSON — Entité temporelle

Fichier : `gabarit_entite_temporelle_atlas.json` (joint).

Une entité (frontière, route, pont, port, ferry, poste-frontière, territoire, voie ferrée, **ligne_front**, autre) n'est pas une fiche unique : c'est une suite d'`etats[]` dans le temps, chacun avec ses propres dates de validité, sa géométrie, ses propriétés et ses sources. On n'écrase jamais un état : un changement crée un nouvel état.

Chaque `etat` porte :
- `valid_from` / `valid_to` avec précision (`exacte`/`mois`/`annee`/`inconnue`/`en_cours`).
- `statut` (libre : intact, detruit, ouvert, ferme, controle, ligne_de_contact...).
- `proprietes` — toutes facultatives : `souverainete_id`, `controle_id`, `alignement_id`, `regime_id`, `statut_administratif`, `note` libre. Ces valeurs sont des **identifiants sémantiques**, jamais des couleurs (ex: `allies_ww2`, pas `#0057B8`) — le futur thème visuel du frontend décide la couleur associée.
- `geometrie` (GeoJSON) ou `geometrie_ref` (jamais les deux).
- `zone_incertitude` optionnelle (surtout pour `ligne_front`, quand la position exacte n'est pas connue).
- `sources[]`.

`relations[]` au niveau entité sert uniquement aux liens **entité ↔ entité** (ex: une route qui en remplace une autre) — jamais pour retrouver l'événement causal, déjà porté dans l'autre sens par le gabarit événement.

**Point non résolu, trouvé sur les vraies données (voir §7)** : il manque un type de relation pour l'appartenance territoriale (subdivision d'un État fédéral, cession partielle de territoire) — `explique` a été utilisé par erreur pour ça, alors qu'il est réservé aux liens narratifs/causaux. Un type dédié (ex: `partie_de` ou `subdivision_de`) est à ajouter.

Trois exemples fictifs inclus dans le fichier : un pont (intact → détruit → reconstruit), une ligne de front (avec zone d'incertitude qui se referme quand les sources deviennent précises), un territoire fictif "Ruritanie" démontrant `souverainete_id` ≠ `controle_id` sur la même géométrie.

## 6. Vocabulaire de visualisation (verrouillé avec Ether)

- **Couche** = domaine de recherche historique (territoires, infrastructures, transport, migration, criminalité...).
- **Calque** = élément cartographique affichable/masquable.
- **Filtre** = sélection de contenu à l'intérieur des calques affichés.
- **Mode de lecture** = logique visuelle d'interprétation (souveraineté / contrôle effectif / alignements / infrastructures / flux). Un même objet, une même géométrie, une même date peuvent être lus différemment selon le mode actif — c'est pour ça que `souverainete_id`, `controle_id` et `alignement_id` coexistent sur le même état.
- **Palette** = association couleur ↔ valeur sémantique, propre à un mode de lecture donné. Vit uniquement dans le frontend/thème, jamais dans les données historiques.
- **Fond de carte** = l'image de base sous tout le reste (plan, relief, vue naturelle, satellite, vue reconstituée). Ni un calque ni un mode de lecture. *(ajouté le 30/09/2026 par Guizmo et Claude, à faire valider par Ether)*

Principe éditorial : **la politique n'est pas un sujet de l'Atlas, c'est parfois une cause des flux qu'il étudie.** On ne documente un régime que lorsqu'il explique un changement de frontière, un déplacement de population, un corridor commercial modifié, etc.

## 7. Premier lot de données réelles reçu (Snapshot 0, lot 01 Nord/Est)

Contenu : URSS, RSS kazakhe, Touva, République populaire mongole, Finlande post-armistice, Petsamo/Pechenga, Porkkala-Udd.

**Validation technique** : JSON valide, aucun ID dupliqué, aucune relation cassée, dates bien formées, vocabulaire respecté. Sourçage rigoureux (FRUS en niveau A, archive d'État de Touva en A, Britannica/Constitution en B).

**Deux points à corriger avant que ça se propage** (voir §5 et §1) :
1. Ajouter un type de relation pour l'appartenance territoriale, distinct des relations causales.
2. Trancher la convention de préfixe pays pour l'URSS (code court type ISO vs nom complet) et l'écrire dans le lexique.

Rien de tout ça n'invalide le lot : les données restent utilisables telles quelles, ce sont des ajustements de gabarit à faire au propre avant le lot suivant.

## 8. Architecture technique V0 (proposée par Ether, validée par Claude)

- **Stack** : React + TypeScript + Vite, MapLibre GL JS (moteur cartographique, GeoJSON/vector tiles/raster/relief), Natural Earth (fond physique neutre, domaine public, sans frontières politiques ni routes modernes), Git (versionnage + audit historique : qui a changé quelle géométrie, quand).
- OpenHistoricalMap = source/référence de comparaison (logique start_date/end_date proche de la nôtre), **jamais** la base de vérité. OpenStreetMap = calque moderne optionnel (bouton "repères modernes" ON/OFF), jamais le fond par défaut sur une date historique.
- QGIS = atelier de géoréférencement/vectorisation des cartes d'archives.
- **Pas de base de données pour l'instant** (pas de PostgreSQL/PostGIS/backend/auth) — JSON + GeoJSON + Git suffit pour le prototype. Évolution prévue vers PMTiles quand les géométries deviendront trop lourdes, sans changer le modèle métier.
- **Moteur temporel** : état actif si `valid_from <= date_affichee` ET (`valid_to` null OU `date_affichee < valid_to`). `valid_to` exclusif — pas de chevauchement ni d'ambiguïté sur la date de bascule.
- **Validateur de données dès le début** (`npm run validate:data`) : conformité au schéma, unicité des IDs, existence des `cible_id`, `cible_type` correct, GeoJSON valide, ordre longitude/latitude, `valid_from < valid_to`, pas de chevauchement illégal d'états, catégories et niveaux de certitude autorisés.
- **Structure de dossiers proposée** :
```
atlas/
├─ src/{map, timeline, events, entities, sources, ui}
├─ public/data/{events/1945/, entities/{territories,borders,roads,railways,ports}, geometries}
├─ schemas/{event.schema.json, entity.schema.json}
└─ scripts/{validate-data, check-relations, build-index}
```
Le corpus JSON/GeoJSON reste indépendant du frontend (survit à un changement de framework).
- **Prototype V0 minimal demandé** : données 100% fictives — 2 territoires (2 polygones), 1 frontière qui change le 1945-01-15, 1 pont intact→détruit le 1945-01-20, 2 événements causes de ces changements, timeline de janvier, clic sur événement → fiche, filtre de calques, bouton repères modernes ON/OFF. Objectif : prouver que déplacer le curseur temporel met à jour correctement chaque état.
- Déploiement prévu : Netlify (build Vite statique), plus tard.

## 9. Outils et environnement de travail

- **Claude Cowork est confirmé capable** de faire ce travail (scaffolding, npm, git, code) — même moteur que Claude Code, exécution de code/commandes shell dans un environnement isolé. Déjà utilisé avec succès pour Fidios (React + Vite). Pas besoin de passer par un autre outil.
- Le code doit être poussé sur un dépôt **GitHub** propre à Guizmo dès que le prototype tourne — une session Cowork est une couche de confort/continuité, pas le coffre-fort durable du code.
- Setup fait sur le PC fixe ("machine de guerre"), utilisation à distance via le téléphone quand pas devant l'ordinateur.

## 10. Sujet en attente, non tranché

Ouverture communautaire du **contenu** (pas du code, qui peut être open source sans souci) : prudence recommandée vu les sujets sensibles (frontières contestées, migrations, criminalité) et le risque de modération. Piste envisagée pour plus tard : soumissions communautaires entrantes en "source C" en attente de validation, jamais en édition directe façon wiki. Pas urgent — à rouvrir une fois le squelette 1945→2026 posé et la voix éditoriale établie.

## 11. Suite

Les deux points non tranchés des §1, §5 et §7 (préfixe pays, relation d'appartenance territoriale) ont été résolus le 26/09/2026 : voir `docs/JOURNAL_DECISIONS.md` et `docs/LEXIQUE_ID.md`. Toute décision postérieure est consignée dans le journal, pas dans ce récap.
