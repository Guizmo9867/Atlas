# Idées pour plus tard (Atlas « premium »)

Idées de Guizmo, gardées ici pour ne pas les perdre. Elles ne sont **pas** au programme du prototype. Beaucoup demandent un vrai travail de recherche : elles deviennent réalistes quand le projet est financé.

Principe (Guizmo, 30/09/2026) : l'Atlas ne doit pas se résumer à « une IA a fait des recherches et voilà les flux ». Il faut une vraie recherche, des choix sur ce qu'on montre et ce qu'on ne montre pas, et une vision du produit, celle de Guizmo.

## 1. Fonds de carte

Le **fond de carte** est l'image du dessous, sur laquelle tout le reste est posé (comme « Plan / Satellite / Relief » dans Google Maps). Le bouton existe déjà en bas à gauche de l'Atlas. Seul « Plan » marche pour l'instant.

| Fond | Années | État | Piste |
|---|---|---|---|
| Plan | toutes | fait | Natural Earth (domaine public) |
| Relief | toutes | à brancher | relief ombré de Natural Earth (domaine public) |
| Vue naturelle | toutes | à brancher | couleurs du terrain de Natural Earth (domaine public) |
| Satellite historique | à partir de 1960 environ | plus tard, gros chantier | 1960-1972 : satellites CORONA (noir et blanc, par endroits, publics depuis 1995) ; à partir de 1972 : Landsat (libre de droits) |
| Aérien historique | années 1940 et après | plus tard, par endroits | photos de reconnaissance alliées et allemandes, prises à des dates différentes et rarement prêtes à l'emploi : à géoréférencer secteur par secteur ; droits d'utilisation à vérifier archive par archive |
| Carte d'époque | toutes | plus tard | une carte scannée de l'époque, calée et superposée |
| Vue reconstituée | 1945 et après | projet, si financement | partir de la vue naturelle, puis recréer ce qui a changé (taille des villes, barrages et lacs artificiels construits après 1945, mer d'Aral encore pleine…). Toujours l'appeler « reconstituée », jamais « satellite ». |

**Règle « pas de mensonge visuel »** (Ether) : aérien et satellite historiques ne s'affichent que là où une image existe pour la date et la zone (ex. Strasbourg couvert, Sibérie non). Ailleurs, l'Atlas garde automatiquement Plan ou Relief. Il faudra donc noter, pour chaque image, sa date et la zone qu'elle couvre.

## 2. Les flux en « veines »

- Des flux dessinés comme un **liquide** qui coule dans des veines, sur les réseaux concernés.
- Inspiration : l'état de la circulation de Google Maps (vert = fluide, orange = léger ralentissement, rouge = bouchon), mais en version Atlas.
- Un code couleur par type de flux, à fixer. Premières idées de Guizmo : bleu = maritime, rouge = ferroviaire, jaune = routier, vert ou noir pour les flux migratoires et militaires.
- Les veines n'apparaissent que selon la couche, les calques et les filtres choisis (principe « maximum d'informations, minimum de visibilité »).

## 3. Interface (déjà notées dans SUIVI_RATISSAGE.md)

- Fiches courtes : un clic, quelques lignes et le lien vers la source.
- On zoome et on comprend l'essentiel ; on clique pour le détail.

## 4. Claude fait les commits : RÉGLÉ le 01/10/2026

Guizmo a choisi la piste complète : Claude enregistre (commit) et envoie (push) lui-même, par petites étapes.
- Clé GitHub « Claude Atlas » : limitée au seul dépôt Atlas, droit « Contents : Read and write », expire au bout de 90 jours (à renouveler vers fin décembre 2026). Guizmo peut l'annuler à tout moment sur GitHub (Settings > Developer settings > Personal access tokens).
- La clé est rangée dans le dossier caché `.git` du dépôt, que Git n'envoie jamais. La configuration partagée avec GitHub Desktop n'est pas modifiée.
- Les commits de Claude apparaissent sous le nom « Claude (pour Guizmo) ». Revenir en arrière reste possible à tout moment (historique Git).
- Avant chaque commit, Claude lance le validateur ; il ne commite jamais un fichier de clé ou un fichier hors du dépôt.

## 5. Sources : recherche et validation (01/10/2026)

- **Recherche par mot-clé dans les sources** (une fois l'Atlas financé), pour ceux qui veulent approfondir. Pas le but premier : l'Atlas reste visuel. *(Guizmo)*
- **Validation par la communauté** : la page « Sources à valider » est privée pour l'instant ; plus tard, l'ouvrir à des contributeurs, avec des limites (droits « contributeur », trace de qui valide quoi, relecture avant report au registre). *(Guizmo)*

## 6. Feature « régime routier » (01/10/2026) — à étudier vers la fin du Snapshot 0

Note complète d'Ether : `docs/idees/2026-10-01_feature_regime_routier_ether.md`. Idée : le filtre Route montre aussi *comment* on circule à une date (plaques, permis, règles, signalisation, contrôles), avec une pastille « régime routier » par territoire dont le détail suit le zoom (pays → région → local). *(Guizmo + Ether)*

Avis de Claude (01/10/2026) :
- Compatible avec l'architecture : état (ce qui s'applique) / événement (le changement), comme pour les frontières et les villes ; le détail selon le zoom réutilise le placement des étiquettes.
- Commencer petit : au Snapshot 0, le **côté de conduite** (gauche/droite) par territoire — visuel, lié aux flux, bien documenté (Tchécoslovaquie 1939, Hongrie 1941, Suède 1967…). Plaques et permis ensuite, au niveau national.
- Ancrer la pastille au « cœur » du territoire (point déjà calculé pour son nom), pas à la capitale, pour ne pas suggérer une règle propre à la capitale.
- Zones de plaques (ex. Allemagne) = de vrais contours à construire : bien plus tard.
- Photos de plaques : Wikimedia Commons (licences libres), chargées seulement à l'ouverture de la fiche.

## 7. Sources dans la langue du lecteur (04/10/2026) — plus tard, après le Snapshot 0

Idée de Guizmo : le lecteur choisit sa langue, et les passages cités des sources s'affichent traduits dans cette langue (traduction automatique, avec l'original toujours visible à côté). Pour le Snapshot 0, on ne traduit rien : les citations restent dans la langue de la source (journal, 04/10/2026).
