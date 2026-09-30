# Atlas — Snapshot 0 — Lot 04
## Sud + Centre/Balkans + Turquie
**Date figée : 1er janvier 1945 à 00:00**

Objectif : fermer l’essentiel de la **couche 1 territoriale** avant les passes suivantes du Snapshot 0 (villes, plaques, routes, rail, ports, ferries, flux).

## Périmètre
Espagne, Portugal, Andorre, Gibraltar, Suisse, Monaco, Vatican, Italie, Tchécoslovaquie, Hongrie, Roumanie, Bulgarie, Yougoslavie, Albanie, Grèce, **Turquie entière**, Malte, Chypre.

Trous volontaires à sourcer avant fermeture définitive de la couche : Liechtenstein, Saint-Marin, île de Man, Svalbard / Jan Mayen.

## Règles à conserver
- pays occupé ≠ pays de l’Axe ; fond = souverain/alignement, hachures = occupant ;
- souveraineté, contrôle, administration et régime séparés ;
- aucun événement postérieur au 01/01/1945 n’est appliqué rétroactivement ;
- les fronts viennent de cartes datées, jamais d’un tracé inventé ;
- Turquie entière = périmètre permanent de l’Atlas.

## Cas principaux

### Espagne
Au 01/01/1945, Espagne franquiste hors guerre, officiellement neutre/non-belligérante. Ne pas la colorer « Axe ».
Source : FRUS 1943, Europe II, doc. 554.

### Portugal
Neutralité officielle. Les facilités alliées dans les Açores sont un fait militaire/infrastructure, pas une perte de souveraineté portugaise.
Sources : FRUS 1945 V doc. 313 ; FRUS 1944 IV doc. 69.

### Gibraltar
Territoire britannique stratégique, à séparer de l’Espagne. Population civile largement évacuée pour l’effort militaire.
Source : Government of Gibraltar, Political development.

### Suisse
État neutre. Les transits ferroviaires et échanges avec l’Allemagne seront une future couche de flux.
Source : FRUS 1945 V doc. 582.

### Monaco
Libéré le 3 septembre 1944 après occupation italienne puis allemande. Au Snapshot 0 : plus de contrôle allemand.
Sources : Gouvernement princier, exposition « Monaco libéré » ; rapport du groupe d’experts.

### Vatican
État souverain depuis les accords du Latran de 1929. Ne pas fusionner avec l’Italie.
Source : Vatican City State, History.

### Italie
Cas majeur : au 01/01/1945, l’Italie combat l’Allemagne comme **cobelligérante**, mais reste juridiquement sous armistice et n’a pas le même statut que les puissances alliées.
Proposition : `alignement_id: anti_axis_non_allied`.

Créer :
- enveloppe souveraine italienne ;
- zone nord sous contrôle allemand / administration RSI ;
- zone centre-sud sous administration italienne et contrôle militaire allié ;
- front de la Ligne gothique à géoréférencer depuis West Point « Allied Offensives in Italy, 5 June–31 December 1944 ».

Sources : FRUS 1945 IV doc. 973 ; FRUS 1945 I doc. 194 ; West Point DHC.

### Tchécoslovaquie
Ne pas la dessiner homogène.
- enveloppe juridique de l’État restauré ;
- contrôle allemand dominant sur Bohême-Moravie et zones encore occupées ;
- avancée soviétique à l’est ;
- **Ruthénie subcarpatique encore juridiquement tchécoslovaque au 01/01**, même si sous contrôle soviétique ;
- Zaolzie = cas disputé, ne pas le remettre automatiquement dans la Pologne.

Sources : FRUS 1945 IV section Czechoslovakia ; FRUS 1945 II doc. 582.

### Hongrie
Ne surtout pas appliquer l’armistice du **20 janvier 1945** au Snapshot 0. Au 1er janvier, Budapest est encore en pleine bataille et le pays est un espace de front. Géométrie de contrôle à croiser avec West Point au 31/12/1944.
Source : FRUS 1944 III doc. 899.

### Roumanie
Depuis août-septembre 1944 : sortie de guerre contre les Alliés, entrée en guerre contre Allemagne et Hongrie, opérations sous direction générale du commandement allié soviétique.
Modèle : souveraineté roumaine + administration roumaine + forte présence/contrôle militaire soviétique.
Source : armistice du 12/09/1944, Avalon Project.

### Bulgarie
Armistice du 28/10/1944 : rupture avec Allemagne, retrait des territoires grec et yougoslave, forces mises à disposition sous direction alliée soviétique.
Proposition : `anti_axis_non_allied`, pas bleu « Alliés » plein.
Source : armistice du 28/10/1944, Avalon Project.

### Yougoslavie
Les Partisans de Tito contrôlent effectivement les zones libérées et constituent la force dominante, mais le pays reste un espace de front. Géométrie de contrôle à dériver d’une carte du 31/12/1944.
Source : FRUS Malta/Yalta 1945 doc. 180.

### Albanie
Fin 1944, le FNC / gouvernement d’Enver Hoxha contrôle pratiquement tout le pays. Contrôle effectif ≠ reconnaissance diplomatique complète.
Sources : FRUS 1944 III docs. 203 et 210.

### Grèce
Au 01/01/1945, les forces allemandes ne sont plus le principal problème cartographique : les **Dekemvriana** sont encore en cours. Athènes / Pirée sont disputés entre gouvernement soutenu par les Britanniques et EAM-ELAS.
Ne pas tracer une frontière locale fine sans carte militaire datée.
Sources : FRUS 1944 V doc. 157 ; FRUS 1945 VIII doc. 51.

### Turquie
**Territoire entier, périmètre permanent.**
Au 01/01/1945 : pas encore en guerre contre Allemagne/Japon ; neutralité armée à orientation pro-alliée.
Proposition : `alignement_id: pro_allied_armed_neutral`.
La rupture avec le Japon prend effet le **6 janvier** : événement futur. La déclaration de guerre de février est également future.
Sources : FRUS Berlin 1945 I doc. 682 ; FRUS 1944 V doc. 968.

### Malte / Chypre
À garder comme périphéries britanniques structurantes de la Méditerranée. Malte = forteresse/colonie britannique ; Chypre = Crown Colony britannique depuis 1925.

## Après intégration du lot 04
Avant d’avancer au 2 janvier, refaire le Snapshot 0 par passes :
1. capitales + grandes villes + noms historiques temporels ;
2. subdivisions administratives utiles ;
3. plaques d’immatriculation + signe international automobile + code ISO ;
4. routes / autoroutes historiques ;
5. réseau ferroviaire ;
6. ports / ferries / voies maritimes ;
7. ponts / postes-frontières ;
8. flux militaires / migratoires / économiques déjà actifs au 01/01/1945.

Principe UI : **maximum d’information, minimum de visibilité**.
