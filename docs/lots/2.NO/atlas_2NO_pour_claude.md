# 2.NO — Norvège au 01/01/1945, cycle 1

Vingt fiches de droit, toutes d’échelon 1, onze sources nouvelles, aucun contour. Les trois fichiers de données sont complets. Proposition soumise à ta relecture ; les contrôles techniques ne valent pas intégration. Autorisation : groupe 3 du 24/10/2026.

## Q2NO-01 — Échelons et mot local

**Réponse proposée : vingt fylker ; pas de second niveau général retenu.** Le tableau 2 de l’annuaire SSB 1943–1945 sépare subdivisions civiles, judiciaires et services spécialisés. Le guide de Nasjonalarkivet confirme la disparition des fonctions de fogd entre 1898 et 1919 et leur répartition entre plusieurs organismes. Des fogderier peuvent subsister comme références historiques ou statistiques : cela ne les rétablit pas comme un niveau administratif général en 1945.

Les communes ordinaires sont hors granularité de la fiche 2.x. Les districts judiciaires, de police, de lensmann et les circonscriptions religieuses ne sont pas transformés en subdivisions générales. Oslo et Bergen sont retenus parce qu’ils figurent au rang des fylker, malgré leur nature urbaine. Pas de création de villes.

## Q2NO-02 — Liste, noms et date

Ordre du tableau SSB : Østfold, Akershus, Oslo, Hedmark, Opland, Buskerud, Vestfold, Telemark, Aust-Agder, Vest-Agder, Rogaland, Hordaland, Bergen, Sogn og Fjordane, Møre og Romsdal, Sør-Trøndelag, Nord-Trøndelag, Nordland, Troms, Finnmark.

La date du tableau est **le 1er juillet 1945**, non janvier. La reconstruction croise le total administratif au 1er juillet 1942, les rubriques de l’annuaire 1942, les cartes mises à jour en 1941 et l’historique de Juvkam (1999). La continuité de cette liste pour le Snapshot est une inférence explicitée en R2NO-02, pas un recensement daté du 1er janvier. Ni population, ni superficie, ni limites postérieures ne sont importées.

Les rubriques de population de 1942 utilisent notamment le recensement de 1930 : elles ne datent pas à elles seules les contours de 1942. Le rapport de 1999 prévient aussi que des ajustements en zones non peuplées peuvent manquer dans son inventaire.

- Oslo reste séparé d’Akershus : le rattachement d’Aker à Oslo est effectif le 01/01/1948 (Juvkam, p. 88).
- Bergen reste séparé d’Hordaland. Les modifications de 1955 et le regroupement du 01/01/1972 ne sont pas anticipés (pp. 51–52).
- L’état porte **Opland**, graphie des annuaires ; la fiche et l’ID portent Oppland pour le repérage. L’acte fixant la graphie officielle exacte n’a pas été retrouvé : R2NO-05.
- Les numéros de lignes du tableau ne sont pas des codes. Le système SSB décrit p. 8 de Juvkam a été créé pour 1946 ; aucun code proposé.

## Q2NO-03 — Tracés, licences et auteurs

**FeatureCollection vide, aucun lien de géométrie. Une source cartographique libre a bien été trouvée.** L’absence de contour livré vient du travail de reconstruction non accompli, pas d’une licence refusée ni d’une absence générale de données.

| Source examinée | Ce qui est disponible | Limite pour cette remise |
|---|---|---|
| Kartverket, versions administratives historiques | Métadonnées de 35 jeux, millésimes 1997–2025 ; CC BY 4.0 | Pas de version 1945 dans la réponse consultée ; anciennes communes et Bergen séparé ne sont pas reconstitués automatiquement. |
| Herredskart over Sør-Norge, id 6539 | Carte raster au 1:1 000 000, base 1918, mise à jour 1941 ; CC BY 4.0 | Limites historiques visibles ; image non géoréférencée dans les fichiers reçus. |
| Herredskart over Nord-Norge, id 6526 | Même série et millésime ; CC BY 4.0 | Projection, côtes, îles et raccord avec la feuille sud à contrôler. Les frontières internationales et le contrôle militaire ne doivent pas être déduits d’une carte de 1941. |
| Kartverket, Historiske kart WMS | Anciens amtskart géoréférencés ; CC BY 4.0 | Série ancienne, sans couverture initiale du Nordland ; pas de polygones 1945 directement identifiés. |
| SSB Geodata | Reconstructions communales 1986–2019 | Millésimes trop récents pour un usage direct. |
| Sikt, présentation et API publique | Statistiques et conversions temporelles | Pas de téléchargement de polygones 1945 ni de licence de ces contours établi dans les pages examinées. |

Attribution des deux feuilles conservées : **Kartverket (Norges Geografiske Opmaaling), Herredskart over Sør-Norge / Nord-Norge, 1918, mis à jour 1941, 1:1 000 000**. Les notices indiquent le cartographe individuel comme inconnu : aucun nom inventé. Les dates de catalogue 1941 et la mention marginale « Ajourført 1941 » ont été rapprochées visuellement ; le titre principal garde 1918. Le catalogue signale des reproductions et la remarque « 1931, 1941 ».

Preuves : `preuves/carte1941_6539.jpg`, `carte1941_6526.jpg`, notices complètes dans `histkart_admin1945.json`, provenance des téléchargements et conditions Kartverket conservées. Les liens à 300 dpi sont dans les notices ; les copies d’examen sont à 100 dpi. Aucune géométrie dérivée de ces images n’est présentée comme originale ou précise. Si une vectorisation est entreprise, la version originale, les transformations, la précision et les auteurs du tracé dérivé devront être consignés. Aucune donnée OpenStreetMap/ODbL utilisée.

Pour le suivi `00_SUBDIVISIONS_SANS_TRACE.md` : motif précis = **cartes historiques disponibles et licence admise, reconstruction vectorielle non réalisée**. Piste directe : https://ws.geonorge.no/historiske-kart/v3/publiserte-kart/6539 et https://ws.geonorge.no/historiske-kart/v3/publiserte-kart/6526. Aucun autre pays déjà clos n’a été rouvert.

## Q2NO-04 — Droit, occupation et territoires particuliers

Parent unique des vingt fiches : `territoire-no-norvege`, souveraineté `norvege`, vérifiés dans le canon local. Le contrôle réel reste porté par les territoires et fronts. `territoire-no-est-finnmark` est une surcouche de contrôle existante, sous le même parent : elle ne crée pas un vingt-et-unième fylke et ne coupe pas Finnmark en deux subdivisions civiles.

Les annuaires traitent Svalbard séparément, sous un sysselmann, et distinguent Jan Mayen. Le canon `lot04_sud_centre_balkans_turquie.json` les inscrit dans `entites_differees_a_sourcer`, sans parent territorial dédié. Ils sont donc documentés comme un manque du cadre territorial, **sans fiche importable créée dans ce lot** et sans être déclarés couverts. Les dépendances antarctiques citées dans les annuaires restent hors cadre européen et non recherchées. R2NO-06 conserve ce point pour le bilan.

## Chefs-lieux et raccords

Aucun `chef_lieu_propose` : les sources retenues établissent les unités et les limites, pas une liste de sièges administratifs au jour exact. Les symboles de villes des cartes ne signifient pas chef-lieu. Aucun nouveau rôle ni fiche ville n’est proposé ; la liste des chefs-lieux absents du canon n’est donc pas établie et ne vaut pas liste vide de besoins. R2NO-04 rend ce manque explicite.

Raccords internes : Oslo/Akershus et Bergen/Hordaland restent séparés ; les deux Trøndelag et les deux Agder ne sont pas fusionnés. Raccords externes avec Suède, Finlande et la zone soviétique : aucune nouvelle frontière tirée des cartes de 1941, aucune opération sur les territoires ou fronts. Les raccords géométriques demeurent non testés faute de tracés.

## Contrôles et réserves

Six réserves dans `atlas_2NO_reserves.json` et `.md`, couverture dans `atlas_2NO_couverture.json`. Les trois données attendues sont livrées même avec GeoJSON vide. Contrôle de format, unicité, parents, références et précontrôle en mémoire du véritable intégrateur dans `atlas_2NO_controle_livraison.json`. Aucun fichier canonique modifié, aucune vérification Claude simulée.

Les preuves de recherche comprennent aussi les échecs d’accès : la page de présentation Sikt a échoué en téléchargement TLS, le livre gouvernemental Fylkesmannsboka a répondu 403 ; leurs alternatives réellement consultées sont distinguées. Le guide de Nasjonalarkivet et les documents SSB/Kartverket téléchargés fondent les affirmations retenues. Les bibliothèques techniques du poste n’ont pas servi de corpus historique.

Merci de répondre à Q2NO-01 à 04, de signaler toute correction de source/parent ou d’interprétation, et de conserver les réserves non levées. Le compte rendu et l’intégration restent attendus. Aucun cycle 2 déclenché par ces réserves seules.
