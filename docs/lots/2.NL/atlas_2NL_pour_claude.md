# 2.NL — cycle 1, Pays-Bas au 01/01/1945

Remise proposée : **12 fiches**, soit **11 provinces et un organisme spécial** ; 12 contours fournis, **11 proposés et 1 exclu**, quatre sources nouvelles et sept réserves. Aucun chef-lieu n’est validé. Les trois fichiers de données obligatoires sont complets.

## Q2NL-01 — niveaux et mots locaux

Premier niveau : onze `provincie`. Le CBS p.30 et p.64 distingue aussi l’`openbaar lichaam` du Noordoostpolder ; la notice du Nationaal Archief indique que le gouvernement exerce ses fonctions provinciales. Il est proposé à l’échelon 1 comme exception fonctionnelle, directement sous l’État, **sans créer une douzième province** (R2NL-02). Pas de Flevoland en 1945.

Un seul niveau est retenu. Les communes sont trop fines pour le lancement 2.x ; aucun ressort judiciaire, statistique ou d’occupation n’est converti en subdivision administrative générale. Cette recherche n’établit pas l’absence universelle de tout système intermédiaire.

## Q2NL-02 — liste et noms

Groningen, Friesland, Drenthe, Overijssel, Gelderland, Utrecht, Noordholland, Zuidholland, Zeeland, Noordbrabant, Limburg ; séparément : Openbaar lichaam de Noordoostelijke Polder. Ces formes viennent du CBS de 1947, tableau couvrant le 01/01/1945. Les noms usuels français servent à l’affichage. Les trois graphies sans trait d’union suivent la publication ; les actes originaux n’ont pas été vérifiés. Le nom Urkerland signalé pour 1944 reste en note réservée.

Effectifs du CBS pour 1945 : 57, 44, 34, 52, 112, 67, 121, 173, 101, 143 et 111 communes, soit 1 015, plus l’organisme du polder. Concordance exacte avec la composition des unions. Terschelling et Vlieland : Frise ; Urk et Wieringen : Hollande-Septentrionale. Ces rattachements sont visibles dans les captures. Les codes techniques de la base ne sont pas publiés comme codes de 1945.

## Q2NL-03 — contours, auteurs et licence

Dr. O. W. A. Boonstra (Radboud Universiteit Nijmegen), NLGIS, dépôt DANS DOI 10.17026/dans-xb9-t677, **CC0-1.0** explicite dans la version 2.2. Six fichiers SHP/SHX/DBF contrôlés par SHA1. Les limites finales viennent uniquement des communes millésimées 1945. Le repère provincial de 1940, dont les coordonnées sont à une échelle dix fois moindre, est utilisé pour attribuer les communes, jamais comme contour final ; corrections datées pour les îles et l’organisme du polder.

EPSG:28992 inféré, faute de PRJ dans les fichiers sélectionnés, puis vérifié contre les **1 016** objets du service IISH/NLGIS : distance maximale de Hausdorff inférieure à 0,000435 m. Union dans le repère natif, conversion EPSG:4326, sans simplification. Aucun polygone natif invalide, aucun chevauchement provincial significatif. Les 712 rapprochements OCR ne sont pas 1 016 relectures manuelles ; les 304 non rapprochés restent identifiés dans les preuves. Trois faux conflits ont été résolus en image, dont les deux Rijswijk homonymes.

Le Brabant-Septentrional est **ne_pas_integrer** et sans geometrie_ref : détail des enclaves de Baarle non certifié, exclusion prudente R2NL-06. Les onze autres contours sont provisoires, avec réserves de précision, eaux et raccords. Aucune donnée OpenStreetMap/ODbL utilisée. Ne pas confondre la licence des données DANS avec celle du logiciel NLGIS.

## Q2NL-04 — cas particuliers et raccords

Souveraineté de droit `pays_bas`, parent `territoire-nl-pays-bas` vérifiés dans le canon. Les fronts et la zone libérée du sud restent dans leurs couches. Aucun contrôle uniforme déduit. Noordoostpolder distingué des provinces ; les changements ultérieurs de nom, de statut ou de frontière ne sont pas anticipés. Le texte de 1951 sert seulement de référence rétrospective à l’ordonnance de 1942 pour les îles, pas d’état juridique de 1945.

Raccords avec Belgique et Allemagne non certifiés ; pas de recalage sur leurs contours ni sur la côte moderne. La Belgique est livrée sans géométries ; l’Allemagne est hors groupe 1. Cela reste une réserve ciblée, sans empêcher les autres fiches et contours étayés.

## Chefs-lieux et villes

Aucun chef-lieu au jour de référence n’est établi par cette remise. Pistes usuelles à documenter : Groningue, Leeuwarden, Assen, Zwolle, Arnhem, Utrecht, Haarlem, La Haye, Middelbourg, Bois-le-Duc et Maastricht. **Leeuwarden, Assen, Zwolle, Haarlem, Middelbourg et Bois-le-Duc n’ont pas de fiche ville nominalement retrouvée dans le canon** ; ces six candidats ne sont ni validés ni ajoutés. Aucun siège du polder supposé. Le complément autorisé villes_1-10 reste français et distinct.

## Lecture et limites

Commencer par les captures CBS p.33 et p.64, puis les îles/Urk/Wieringen, la preuve de licence DANS, le contrôle géométrique et les sept réserves. Les copies locales sont des preuves de travail, hors dépôt public. La table des trente filtres distingue la recherche des subdivisions des campagnes non ouvertes. Les réserves ne demandent pas d’arbitrage individuel à Guizmo ; elles sont conservées pour la revue du groupe.
