# 2.CH — Suisse, cycle 1

Remise proposée au 01/01/1945 à 00:00 : **200 fiches**, soit 25 unités cantonales (19 cantons et 6 demi-cantons) et 175 districts. Les 200 contours OFS sont joints, mais **tous portent `ne_pas_integrer`** et aucune fiche n'a de `geometrie_ref`. Les conditions `terms_open` sont documentées et permettent la réutilisation ; elles ne figurent pas dans la liste des licences reconnues par l'importateur. Ne pas les rebaptiser CC0 pour les faire accepter. Huit réserves sont à conserver pour la revue groupée.

## Réponses aux questions de lancement

**Q2CH-01 — échelons.** L'échelon 1 est cantonal. Les six demi-cantons sont des unités de ce même rang, sans création d'un parent fictif « Bâle », « Unterwald » ou « Appenzell ». L'article 1 de la Constitution de 1874 compte 22 cantons en réunissant les trois paires ; le registre historisé et l'annuaire distinguent bien les 25 unités territoriales. L'échelon 2 reprend les mots locaux du registre : Bezirk, Amtsbezirk, Amt, District ou Distretto. Leurs compétences ne sont pas supposées identiques.

**Q2CH-02 — liste et noms.** L'extraction officielle AGV demandée au 01/01/1945 contient 25 entrées de niveau 1, 184 de niveau 2 et 3 107 de niveau 3. Les sept entrées de niveau 2 explicitement décrites comme des cantons sans districts sont exclues : Uri, Obwald, Nidwald, Glaris, Zoug, Bâle-Ville et Genève. Les deux Landesteile d'Appenzell Rhodes-Intérieures sont réservés, sans nier leur existence dans le registre. Restent 175 districts proposés. La jointure complète et les exclusions sont dans `preuves/jointure_et_selection_1945.json`.

Le nom d'état suit la première forme de la source officielle historisée ; les autres formes sont notées, sans déduction de langue majoritaire. Les noms de fiche et les termes rédactionnels sont français. Aucun code OFS n'est publié comme code administratif de 1945 : les identifiants techniques servent seulement à rendre la jointure vérifiable. Les dates de début du registre, notamment le 12/09/1848, ne sont pas converties en dates de création.

**Q2CH-03 — tracés et licence.** Auteur : **Office fédéral de la statistique, GEOSTAT**. Produit : limites administratives généralisées G1. Source des géométries : service public AGV, requêtes Canton et District avec `date=01-01-1945`, `resolution=G1`, `dissolve=true`, `format=geojson`. La documentation précise le système EPSG:4326 pour GeoJSON. Ether a sélectionné et renommé les objets, sans modifier les coordonnées ni simplifier les polygones. Le produit G1 est lui-même déjà généralisé par l'OFS ; il ne faut pas le confondre avec la résolution G0.

Les ressources du catalogue officiel portent `https://opendata.swiss/terms-of-use#terms_open`. Les métadonnées, les conditions et la documentation sont archivées. La mention de réutilisation non commerciale de la publication PDF ne doit pas être substituée aux conditions de la ressource géographique. Aucun matériau OpenStreetMap ou ODbL n'est utilisé. Décision d'admission des conditions : R2CH-01, à examiner selon la procédure de Guizmo. En attendant, les 200 contours restent exclus, les 200 fiches peuvent être intégrées.

**Q2CH-04 — cas particuliers.** Les districts jurassiens et le Laufental restent sous Berne, sans anticiper les changements de 1979 ou 1994. Bâle-Campagne compte quatre districts. Vaud en compte dix-neuf ; Saint-Gall et les Grisons quatorze chacun, selon leur découpage historisé. Les trois districts d'Appenzell Rhodes-Extérieures sont retenus comme divisions historiques, avec réserve sur leurs fonctions en 1945. Les deux Landesteile AI restent à qualifier. Une seule entrée de Rarogne est livrée ; ne pas en déduire automatiquement deux demi-districts.

## Chefs-lieux et villes

Aucun chef-lieu de 1945 n'est validé ou lié. L'annuaire dit « 1945 » mais son avant-propos est daté de décembre 1946 ; le tableau utilisé porte sur 1941. Il corrobore la nomenclature cantonale, sans donner une preuve individuelle des sièges à la date du Snapshot. Il n'y a donc pas de liste établie de chefs-lieux absents du canon à publier comme telle dans ce cycle. R2CH-06 conserve la lacune ; aucune ville créée, aucun nom de district assimilé automatiquement à son siège.

## Raccords et limites spatiales

Le contrôle numérique retrouve les 175 districts à l'intérieur de leurs 17 cantons parents et la même couverture que leurs contours cantonaux, à l'arrondi de 0,001 m². Ce résultat contrôle la cohérence interne d'une même source ; il ne certifie pas la frontière historique.

La vue montre des trous de lacs dans les réponses AGV : les limites proposées ne constituent pas une partition juridique complète de toutes les eaux cantonales. Les petites enclaves et échanges inhabités inférieurs à 25 ha sont imparfaitement suivis par G1 ; la description cite une portion de Balsthal située dans Berne jusqu'en 1950 et non retenue dans la reconstitution. Aucun raccord au fond national d'Atlas n'est homologué. Le lac de Constance comporte une limite technique dans la source, sans accord général sur la frontière juridique. Les rives et le lac de Gruyère ne doivent pas être anticipés à partir de 1948.

France, Italie/Campione, Reich au nord et à l'est (dont la frontière autrichienne de 1945), Liechtenstein, Büsingen et Verenahof : contrôles locaux à renforcer avant admission des contours. La source décrit trois enclaves étrangères avant 1967 ; cette remise ne change aucune souveraineté territoriale existante. R2CH-02 et R2CH-07 regroupent ces limites.

## Fichiers et relecture

Les trois fichiers de données imposés sont complets : fiches, FeatureCollection et delta de six sources. Les huit réserves sont dans les fichiers `atlas_2CH_reserves.*`. Le contrôle de livraison, le manifeste, l'index des preuves et le temps de travail accompagnent la remise. Les captures PDF clés ont été vues ; la vue des contours est une représentation de contrôle produite par Ether, pas une carte historique indépendante.

Attention : `preuves/AGV_communes_19450101.geojson` est un nom de téléchargement erroné pour une seconde réponse **District**, identique au fichier des districts. Il est conservé conformément à la règle de non-suppression, mais n'est utilisé ni comme contour communal ni comme preuve indépendante.

Pas de demande immédiate à Guizmo et pas de cycle 2 identique pour les réserves. Merci de signaler toute correction nécessaire dans le compte rendu, puis de conserver les questions de fond pour le bilan du groupe 1. Aucun groupe suivant ni campagne 3.x n'est ouvert.
