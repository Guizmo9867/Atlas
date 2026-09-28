# Atlas — Journal des décisions

Une ligne par décision, datée. Plus récente en haut. Ce journal remplace les versions éparpillées dans les conversations : si ce n'est pas ici, ce n'est pas décidé.

## 2026-09-28 (suite : retour d'Ether sur le lot 03)

- **Lot 03 validé** : harmonisation Courlande/Laponie, alignement allié de Jersey/Guernesey, les deux zones tirées du front (Allemagne tenue par les Alliés, secteur de Bitche). *(Ether)*
- **RÈGLE DU SNAPSHOT 0 (précisée par Guizmo)** : le Snapshot 0 montre l'état au **01/01/1945 à 00:00**, construit avec la **dernière situation connue AVANT ce moment**. Ce qui est observé après — même le 01/01 à 12:00 — n'entre pas au Snapshot 0 : il deviendra un nouvel état lors du ratissage de janvier (ex. front du 01/01 à midi → état suivant ; réduction de la poche de Colmar → janvier). Un objet dont aucune source antérieure n'atteste l'existence n'entre pas au Snapshot 0. Chaque géométrie tirée d'une carte datée porte `reference_temporelle` (date de la source, écart, `derniere_situation_connue_avant_snapshot`, état suivant connu), affichée dans la fiche. *(Guizmo, d'après la remarque d'Ether)*
- Application : front de l'Ouest refait depuis la **carte LOC du 31/12/1944 à 12:00** ; sud de la poche de Colmar depuis **West Point 70 (15/12/1944)** au lieu de la ligne du 20/01 ; poches de l'Atlantique : 15/12/1944 ; front de l'Est : « 31 Dec. » ; Laponie : position du 29/11/1944. Les cartes du 01/01 à 12:00 (LOC) et du 20/01 (West Point 75a) sont gardées pour janvier. *(Claude)*
- **Îles des poches retirées** (Groix, Belle-Île, Ré, Oléron, Noirmoutier) : pas de rattachement sans source par île. *(Ether)*
- **Île de Man et Svalbard / Jan Mayen** : entités voulues, mais plus tard (pas prioritaire devant le lot 04). *(Ether)*
- **Lot 04 = Ibérie → Italie → Suisse → Europe centrale (Tchécoslovaquie avec Zaolzie, Hongrie) → Roumanie, Bulgarie → Yougoslavie, Albanie → Grèce → Turquie ENTIÈRE** (pont Europe / Caucase / mer Noire / Méditerranée orientale : on ne la coupe pas à Istanbul). *(Ether + Guizmo)*
- Les briefs d'Ether sont archivés à côté de leur lot (`data/snapshot0/lot0X_…_brief_ether.md`) ; les comptes rendus d'intégration de Claude dans `docs/pour_ether/` (historique de fabrication du corpus). *(Ether)*

## 2026-09-28 (suite : lot 03, Nord et Ouest)

- **Lot 03 intégré** (Danemark, Féroé, Norvège, Suède, Islande, Royaume-Uni, Jersey, Guernesey, Irlande, France, Belgique, Luxembourg, Pays-Bas) : 22 entités, toutes tracées. *(Ether, intégré par Claude)*
- **Front de l'Ouest tracé depuis la carte officielle LOC du 12e groupe d'armées (01/01/1945, midi)**, géoréférencée automatiquement sur les fleuves (écart ≈ 1-2 km). Zones dérivées du front : Ardennes belges et luxembourgeoises, Pays-Bas libérés, poche de Colmar (sud d'après West Point 75a). Poches de l'Atlantique et Dunkerque d'après West Point 71 (15/12/1944, ≈ 5 km). *(Claude)*
- **Règle « pays occupé ≠ Axe » appliquée partout** : un territoire garde le camp de son souverain ; l'occupation = hachures à la couleur du camp de l'occupant. Conséquence : Courlande et Laponie perdent leur `alignement_id: axis_ww2` et deviennent « couleur du parent + hachures anthracite ». *(Ether, harmonisation Claude)*
- **Nouveau statut particulier `occupe_hors_coalitions`** (Danemark) : fond ivoire + hachures de l'occupant. *(Ether + Claude)*
- **`administration_id` utilisé** : Féroé (`feroe`, contrôle britannique), Est-Finnmark (`norvege`, contrôle soviétique), Pays-Bas libérés (`pays_bas`). *(Ether)*
- **Îles Anglo-Normandes séparées du Royaume-Uni** (`souverainete_id: couronne_britannique`) ; alignement allié ajouté par Claude, à valider. *(Ether + Claude)*
- **Propositions de Claude, à valider** : `territoire-de-zone-alliee-ouest` (Aix-la-Chapelle, bords de la Sarre) et `territoire-fr-zone-allemande-nord-est` (Bitche), tirés du même front. *(Claude)*
- **Affichage** : étiquettes posées au « cœur » du territoire (algorithme polylabel) ; zones locales étiquetées seulement de près ; une zone « enfant » masque les hachures de son parent. *(Claude)*

## 2026-09-28 (suite : ouverture publique)

- **Le dépôt GitHub devient public, en lecture seule** : chacun peut suivre l'avancée et proposer une correction sourcée ; seul Guizmo écrit dans le dépôt. *(Guizmo)*
- **Licences : code MIT, données et textes CC BY 4.0** : réutilisation libre, y compris commerciale, avec citation obligatoire de l'Atlas. Objectif : que l'Atlas serve (enseignants, élèves, chercheurs) et que son origine soit toujours citée. *(Guizmo, mis en forme par Claude)*
- **Règle d'entrée des sources** : une donnée copiée dans `data/` doit être compatible CC BY 4.0 (domaine public, CC0, CC BY) ; ODbL/SA/NC/ND interdites dans le corpus (voir `docs/LICENCES_ET_ATTRIBUTIONS.md`). *(Claude)*
- **OpenStreetMap autorisé, mais rangé à part** : données OSM (ou dérivées d'OSM) dans `data/osm/` sous ODbL, jamais mélangées au corpus CC BY ; la carte affichée combine les deux avec les crédits. *(question de Guizmo, règle proposée par Claude)*
- L'adresse e-mail des commits reste visible : choix assumé par Guizmo. *(Guizmo)*

## 2026-09-28 (suite : fronts, Courlande, Laponie)

- **Front de l'Est et poche de Courlande tracés** depuis la carte West Point n° 31 (trait rouge du 31/12/1944), géoréférencée par Claude (23 points d'appui, erreur ≈ 9 km en moyenne) : incertitude affichée de 15 km. Courlande ≈ 15 200 km², `alignement_id: axis_ww2` (anthracite). *(Ether a fourni la carte, Claude a tracé)*
- **Laponie ajoutée** : `territoire-fi-laponie-nord-ouest` (souveraineté finlandaise, contrôle allemand, anthracite hachuré, ≈ 3 100 km²) du 29/11/1944 au retrait vers Kilpisjärvi (27/04/1945, à dater au ratissage) + `ligne_front-de-fi-laponie` sur la Lätäseno (tracé OHM de la rivière). *(Ether + Claude)*
- **Pays baltes : « transfert soviétique effectif, formalisation incomplète »** — tracé après transferts (Petserimaa et Abrene août 1944, rive est de la Narva 24/11/1944) ; la formalisation du 18/01/1945 deviendra un nouvel état juridique, sans changement de tracé. *(Ether)*
- **Zaolzie reste hors de la Pologne** au Snapshot 0 (contesté, sous contrôle allemand) ; position américaine du 11/01/1945 favorable au retour à la frontière d'avant 1938 (FRUS 1945 IV doc. 432). À traiter avec la Tchécoslovaquie. *(Ether)*
- **Memel** : tracé conservé (≈ 2 500 km²), drapeau maintenu sur l'écart 2 657 / 2 828 km² ; on ne force pas le polygone pour atteindre un chiffre. *(Ether)*
- **Lot 02 verrouillé** (sauf retours de sources). On reprend le balayage géographique. *(Ether + Guizmo)*

## 2026-09-28 (suite : lot 02)

- **Fond de carte passé en Natural Earth 1:10m** (au lieu de 1:50m), soit le même trait de côte que celui qui découpe les territoires : fin des décalages visibles au zoom. **Lacs et fleuves dessinés au-dessus des territoires** ; petits fleuves à partir du zoom 5. *(retour de Guizmo après le premier `npm run dev`, corrigé par Claude)*
- Étiquette « Allemagne (1937) » → « Allemagne » : la référence 1937 est dans la fiche. *(Guizmo)*
- **Lot 02 intégré** (Pologne, Allemagne, Autriche, pays baltes, Memel, Dantzig) : 11 entités, 9 tracés provisoires (OHM). Restent la poche de Courlande et la ligne de front, à tracer depuis la carte de West Point (map 31). *(Ether, intégré par Claude)*
- **TRANCHÉ : frontière soviéto-polonaise au 01/01/1945 = accord URSS–PKWN du 27/07/1944** (Białystok, Łomża, Przemyśl côté polonais), présentée comme non définitive. L'URSS du lot 01 est corrigée en conséquence. Tracé approché par celui du traité du 16/08/1945, faute de carte de l'accord. *(Ether + Guizmo)*
- **Allemagne = frontières du 31/12/1937** (référence alliée) ; Autriche, Dantzig, Memel et territoires annexés restent des entités séparées. *(Ether)*
- **Règle d'ID : un ID d'entité commence par son `type_entite` exact** (`ligne_front-…`). Vérifiée par le validateur. *(Claude)*
- **Un acteur = un seul ID ; le régime va dans `regime_id`** (`controle_id: allemagne`, `regime_id: allemagne_nazie`). *(Claude, à confirmer par Ether)*
- **Souveraineté contestée → `souverainete_id` absent + `souverainete_revendiquee_par`** (RSS baltes, Courlande, Mongolie). Affichée « souveraineté non tranchée ». *(Ether + Guizmo)*
- **Code couleur : 4 familles principales + statuts particuliers quand les faits l'exigent.** Finlande = `anti_axis_non_allied` (ivoire, sans bleu territorial) ; Mongolie = `pro_sovietique_non_belligerant` (ivoire + liseré bleu), passage à `allies_ww2` le 10/08/1945. `pro_sovietique_hors_urss` supprimé. *(Ether + Guizmo)*
- **Mongolie** : pas de `parent_id` (l'URSS la domine sans l'avoir annexée), pas de `souverainete_id` (revendication chinoise = juridique, pas contrôle), frontière sino-mongole signalée comme imparfaitement délimitée. *(Ether)*
- **Hors périmètre (Chine, Iran, Afghanistan, Moyen-Orient…) : « on montre par contact, pas par exhaustivité »** — seulement la bande utile pour comprendre un flux, une frontière, une occupation ou un événement lié au cœur de l'Atlas. *(Ether + Guizmo)*
- **Affichage : un territoire « enfant » sans alignement hérite de celui de son parent** ; hachures quand le contrôleur diffère du souverain, ou, sans souverain déclaré, du contrôleur du parent. *(Claude)*
- **ADOPTÉ : deux nouveaux champs d'état** — `souverainete_revendiquee_par` (liste des acteurs qui revendiquent un territoire à souveraineté contestée ; `souverainete_id` reste alors absent) et `administration_id` (administration civile quand elle diffère du contrôle militaire). Appliqués : Mongolie (`[republique_de_chine]`), RSS baltes et Courlande (`[urss]`). *(proposé par Ether, validé par Guizmo)*

## 2026-09-28

- **Code couleur du Snapshot 0 (mode Alignements, mode par défaut)** : Alliés = bleu ; Allemagne nazie = anthracite ; États associés à l'Axe = gris/brun sombre ; neutres = ivoire. Occupation / contrôle concurrent = **hachures** ; fronts = **bande semi-transparente**. Aucune 5e famille politique. Couleurs uniquement dans le thème du frontend. Nouvel ID d'alignement `axis_associe_ww2`. *(Ether + Guizmo, intégré par Claude)*
- **Terres « sans données » en gris clair**, pour ne pas les confondre avec les neutres en ivoire. *(Claude)*
- **Licences verrouillées** dans `docs/LICENCES_ET_ATTRIBUTIONS.md` : OHM = CC0 mais certains segments importés gardent leur licence (Kartverket CC BY 4.0, OCHA CC BY-IGO) → crédits affichés sur la carte ; OSM = ODbL + politique d'usage des tuiles (autre fournisseur avant mise en ligne) ; CShapes = comparaison seulement. *(Ether a soulevé l'ODbL, Claude a vérifié segment par segment)*
- **À trancher** : famille de la **Finlande** au 01/01/1945 (en guerre contre l'Allemagne en Laponie depuis l'automne 1944, sans être formellement « Alliée ») et de la **Mongolie** (alignée sur Moscou, mais pas en guerre en Europe ; n'entre en guerre que contre le Japon en août 1945). *(Ether + Guizmo)*
- **Préfixe pays reformulé** (correction d'Ether) : code ISO 3166-1 alpha-2 ; pour un État disparu, son **ancien** code alpha-2 (`su`, `yu`, `cs`, `dd`). Ce ne sont PAS des codes ISO 3166-3, qui ont 4 lettres (SUHH, YUCS, CSHH, DDDE). Les IDs existants ne changent pas. *(Ether, intégré par Claude)*
- **Porkkala** : deux sources B ajoutées au registre (Yle : frontière fermée le 29/09/1944 à 8 h ; Musée ferroviaire : gare de Kirkkonummi remise le 03/10/1944). Pas de changement de date sans source A. *(Ether, citations vérifiées par Claude)*
- **Traité de Paris 1947 validé par Ether** : fermeture des états « régime d'armistice » au 15/09/1947. *(Ether)*
- **Rôles officialisés** : Ether = ratissage, recherche, sourçage ; Claude = intégration, contrôles, registre ; Guizmo = décisions. Le dépôt GitHub est la seule référence, pas les fichiers générés dans les conversations. *(Ether + Guizmo)*
- **Ordre du ratissage du Snapshot 0 : Est → Nord → Ouest → Sud**, puis les couches (infrastructures, flux) une par une. Suivi dans `docs/SUIVI_RATISSAGE.md`. *(Guizmo)*

## 2026-09-26

- **Snapshot 0 = uniquement le 1er janvier 1945, 0 h 00.** Premières frontières avant tout changement ; le ratissage (janvier d'abord) ajoute ensuite les états datés, couche par couche. *(Guizmo)*
- **Premiers tracés réels (lot 01), statut PROVISOIRE** : dérivés d'OpenHistoricalMap (CC0), découpés au trait de côte Natural Earth 1:10m, comparés à CShapes 2.0. Petsamo et Porkkala calculés par différence « Finlande 1940-44 − Finlande 1944 ». Script rejouable : `outils/geo/deriver_snapshot0_lot01.py`. *(Claude, sur demande de Guizmo : « tous les outils pour être le plus précis possible »)*
- **Une géométrie = un fichier** `data/geometries/<snapshot>/<geometrie_ref>.geojson`, avec sa provenance (sources, opérations, précision, points_a_verifier) dans ses propriétés, comme le demande le protocole des sources. *(Claude)*
- **CShapes 2.0 : comparaison uniquement** (licence non commerciale, partage à l'identique) ; jamais copié dans l'Atlas. OHM = niveau C. *(Claude)*
- **Champ facultatif `nom_court`** pour les étiquettes de la carte. *(Claude)*
- **Décision en attente** : la frontière soviéto-polonaise au 01/01/1945 (ligne de 1941, accord URSS–PKWN du 27/07/1944, ou frontière d'avant-guerre reconnue internationalement ?). Voir `docs/pour_ether/2026-09-26_traces_snapshot0_lot01.md`. *(à trancher : Guizmo + Ether)*
- **Prototype V0 codé** (`app/`) : moteur temporel, carte MapLibre sur fond Natural Earth, curseur jour par jour, 3 modes de lecture, calques, pastilles selon le zoom (atlas / regional ≥ 5 / archive ≥ 6,5), fiches, parcours tracés, repères modernes OSM en option. Données 100 % fictives dans `data/prototype_v0/`. *(Claude)*
- **Codes pays `xa`–`xz` = données fictives** (codes ISO réservés à l'usage privé, aucun pays réel). *(Claude)*
- **Validateur `npm run validate:data`** : IDs, dates, chevauchements d'états, sources présentes au registre, géométries (ordre lon/lat), relations. Le prototype a son propre registre fictif. *(Claude)*
- **Aucune frontière réelle tracée pour l'instant** : les géométries du lot 01 restent « à vectoriser » ; on n'invente pas de tracé. *(rappel de la règle)*
- **Dépôt GitHub = version officielle unique.** Claude range les fichiers et signale les changements. Plus de copies « v2 » / « vierge » / « final » : Git garde l'historique. *(Guizmo)*
- **Préfixe pays des IDs = code ISO à 2 lettres en minuscules**, codes historiques inclus (`su`, `yu`, `cs`, `dd`). Préfixe = pays du premier état, immuable. *(Guizmo, sur proposition de Claude)*
- **L'ID désigne le lieu stable, jamais un statut daté** (`territoire-fi-finlande`, pas `…-post-armistice-1944`). *(Claude, validé par Guizmo)*
- **Appartenance territoriale = `proprietes.parent_id`** dans chaque état (datable). Nouvelle relation `detache_de`. `explique` = narratif uniquement. *(Claude, validé par Guizmo)*
- **Sources : le registre est la référence unique** ; les fiches pointent par `source_id` + `locator` + `usage`. *(Claude, validé par Guizmo)*
- **Identifiants d'acteurs courts**, nuances dans `note` (`republique_de_chine`). *(rappel d'une règle du récap)*
- **`valid_to` vide = état ouvert** jusqu'à ce qu'un document le ferme. Confirmé, voulu. *(Guizmo)*
- **Traité de Paris 1947** : confirme Petsamo (art. 2) et Porkkala (art. 4) ; en vigueur le 15/09/1947 → nouveaux états à cette date lors du ratissage. *(Claude, vérifié sur le texte officiel)*
- **`pays` des événements = codes ISO** (`["fr", "ch"]`). *(Claude, découle du préfixe)*

## 2026-09-25 et avant

Voir `docs/recap_technique.md` (stack, périmètre, Snapshot 0, gabarits, vocabulaire de visualisation, architecture V0).
