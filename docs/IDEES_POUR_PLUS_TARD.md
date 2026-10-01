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

## 4. Atelier technique : que Claude puisse faire les commits (à régler dès qu'on a du temps)

Demande de Guizmo (01/10/2026) : il n'est pas souvent devant le PC ; Claude devrait pouvoir enregistrer (commit) plus souvent, par petites étapes.

Premier diagnostic de Claude (01/10/2026, lecture seule, rien modifié) :
- Claude voit bien le dépôt et le lien avec GitHub (le dépôt est lisible).
- **Il manque l'identité** (nom et e-mail de l'auteur) dans l'environnement de Claude : sans elle, un commit est refusé.
- **Il manque l'autorisation d'envoyer (push)** : la clé GitHub est rangée dans GitHub Desktop, côté Windows, et Claude n'y a pas accès.

Pistes, de la plus simple à la plus complète :
1. Claude fait les commits sur le PC, et Guizmo n'a plus qu'à cliquer « Push origin » dans GitHub Desktop quand il passe. Il suffit de régler l'identité.
2. Claude envoie aussi sur GitHub : il faut un jeton d'accès limité au seul dépôt Atlas, créé par Guizmo, révocable à tout moment.
À tester d'abord sur un petit commit, en vérifiant que GitHub Desktop le voit bien.
