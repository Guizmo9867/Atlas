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
