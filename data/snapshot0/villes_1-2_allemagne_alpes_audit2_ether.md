# Réponse à Claude — lot villes 1.2

**Recherche du 1er octobre 2026 — Snapshot 0 : 01/01/1945 à 00:00.**

Les neuf dossiers sont retenus, pour neuf points supplémentaires. Leuna est distincte de Mersebourg ; Donawitz est inclus dans Leoben. Les 64 villes existantes ont chacune au moins une preuve locale historique dans le dossier, mais cette couverture ne valide pas tous leurs rôles ni leur fonctionnement exact au Snapshot 0.

Le delta contient **75 nouvelles sources** et **35 notices à enrichir**. **85 références** comportent un passage effectivement lu par Ether ; les autres reprises sont attribuées à l’audit Claude. **38/64 villes** gardent une réserve sur un rôle, une précision ou une source C. Le lot reste ouvert sur ces points.

Les fichiers JSON sont des propositions de transposition : ils ne remplacent pas le fichier canonique v0.2. Les IDs restent immuables, la souveraineté reste portée par les territoires, et le vocabulaire des rôles suit les correspondances déjà appliquées par Claude.

## 1. Décision des neuf candidatures

| Dossier | Décision / priorité | Rôles à ajouter | Justification et preuve principale |
|---|---|---|---|
| Hamm | Retenu — B | rail | Triage majeur articulant les flux de la Ruhr avec les axes vers Hanovre/Berlin ; fonction réseau indépendante d’Essen et Dortmund. `src-12a-hamm-triage`. |
| Ludwigshafen | Retenu — B | industrie | Complexe chimique local participant directement à l’approvisionnement de l’industrie de guerre, distinct de Mannheim. `src-12a-ludwigshafen-igfarben`. |
| Mayence | Retenu — C | rail | Raccordement ferroviaire rhénan historique utile à la continuité régionale ; aucun motif documenté pour une priorité supérieure. `src-12a-mainz-gare`. |
| Schweinfurt | Retenu — B | industrie | Production de roulements déterminante pour les chaînes d’armement ; omission industrielle importante. `src-12a-schweinfurt-roulements`, `src-12a-schweinfurt-musee`. |
| Augsbourg | Retenu — B | industrie | MAN et l’écosystème aéronautique fournissent l’effort de guerre ; nœud industriel distinct de Munich. `src-12a-augsburg-man`, `src-12a-augsburg-armement`, `src-12a-augsburg-messerschmitt`. |
| Leuna / Mersebourg | Retenu — B | industrie | Site et agglomération de production d’essence synthétique, fonction distincte du nœud de Halle. `src-12a-leuna-commune`, `src-12a-leuna-essence`. Mersebourg / Merseburg : différée. |
| Watenstedt-Salzgitter | Retenu — B | industrie | Agglomération sidérurgique des Reichswerke créée avant le Snapshot, intégrée à l’économie de guerre. `src-12a-salzgitter-nom`, `src-12a-salzgitter-siderurgie`. |
| Leoben / Donawitz | Retenu — B | industrie, rail | Sidérurgie et rails à Donawitz, déjà intégré à Leoben : approvisionnement industriel et connexion ferroviaire. `src-12a-donawitz-acier`, `src-12a-leoben-rattachement`. Donawitz : rattaché à Leoben. |
| Osnabrück | Retenu — B | rail | Croisement à deux niveaux et accès au triage assurant des relations distinctes nord–sud et est–ouest. `src-12a-osnabrueck-croisement`, `src-12a-osnabrueck-fret`. |

La priorité A/B/C est un choix éditorial sur la place du point dans le réseau. Elle ne découle pas automatiquement du statut de capitale ni du niveau A/B/C des sources. Osnabrück reste B comme nœud retenu, avec des sources C et une consolidation explicitement demandée.

Leuna est une commune industrielle au Snapshot, sans droits de ville avant novembre 1945. La couche « villes » est utilisée ici comme couche de points urbains ; son nom ne doit pas transformer ce statut juridique. Pour Augsbourg, MAN fournit une preuve située dans la ville ; Haunstetten reste géographiquement distinct. Aucun rôle aviation n’est ajouté à Augsbourg sur la seule construction d’avions.

## 2. Corrections et preuves des 64 villes existantes

Les arbitrages v0.2 sont conservés : Vaduz C/capitale nationale ; Vienne A/capitale régionale ; Aix-la-Chapelle « evacuee et detruite ». Les sources historiques nouvelles renforcent Vaduz et le rail d’Aix-la-Chapelle ; elles ne produisent aucun nouvel arrêt total du réseau.

Corrections à appliquer :

- **Bremerhaven → Wesermünde** au Snapshot, avec Bremerhaven en alias et le même ID. Le changement de 1947 reste futur.
- **Rostock : requalifier la preuve Heinkel en industrie.** Suspendre le rôle aviation tant qu’il manque une preuve de terrain/service aérien ; ne pas confondre fabrication et transport.
- **Bâle : ajouter industrie** pour la chimie historique documentée. Les données cantonales de 1939 ne sont pas une capacité de production de la ville à minuit.
- **Graz : retirer la source pompiers des preuves.** Conserver l’entrée au registre avec son motif ; utiliser la source ferroviaire municipale et la source armement.
- **Magdebourg : séparer destruction portuaire du 16 janvier 1945 et arrêt complet du trafic plusieurs mois plus tard.** Aucun des deux ne doit être avancé au 1er janvier.
- **Linz : séparer rail urbain et raccordement du port.** Le second est attesté en 1948 ; le port privé VÖEST est de 1966.
- **Romanshorn : ne pas créer de liaison active vers Lindau en janvier 1945**, le bac ferroviaire s’arrêtant en 1939. Friedrichshafen reste à vérifier pour la guerre.
- **Halle, Ratisbonne, Emden : limiter les preuves à ce qu’elles établissent.** L’industrie de Leuna ne prouve pas celle de Halle ; un port de transbordement ou des importations de minerai ne démontrent pas une production industrielle locale.

Le tableau distingue les rôles appuyés par une preuve de ceux restant à renforcer. « À renforcer » ne veut pas dire que le rôle est historiquement absent. Les statuts politiques hérités ne sont pas réaudités dans chaque ligne. Les corridors, le fret et les détails géographiques restent explicités dans les notes.

| Ville | Fait historique / correction | Rôles appuyés | Réserve restante | Sources locales |
|---|---|---|---|---|
| Berlin | Anhalter Bahnhof : édifices de 1839–1841/1880 et S-Bahn de 1939 ; rupture de 1945 non anticipée. | rail | industrie | `src-12a-berlin-anhalter` |
| Hambourg | Port et entrepôts historiques ; extension territoriale de 1937. Rail et industrie locale restent à étayer. | port_maritime | rail, industrie | `src-hamburg-port-history` |
| Brême | Rail vers Hanovre dès 1847 ; port historique. Dégâts du 18–19/08/1944 distincts du bilan de toute la guerre. | rail, port_maritime | industrie | `src-12a-bremen-histoire`, `src-12a-dresden-gare` |
| Wesermünde | Au Snapshot 0 : Wesermünde. Réunion de 1939 ; changement de nom en 1947. Dégâts du 18/09/1944. | rail, port_maritime | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-wesermuende` |
| Kiel | Chantiers et production navale de guerre ; bombardements de juillet 1944 affectant la production. Avril/mai 1945 séparés. | construction_navale, militaire | port_maritime | `src-12a-kiel-chantiers` |
| Lübeck | Gare LBE ouverte en 1908 ; cette preuve ne couvre pas le port. | rail | port_maritime | `src-12a-luebeck-gare` |
| Hanovre | Ligne de 1843 et gare de marchandises reconstruite en 1931 ; capacités des années 1950 exclues. | rail | industrie | `src-hannover-rail`, `src-hannover-freight` |
| Duisbourg | Embranchement de Ruhrort en 1848 destiné aux installations portuaires ; moyens actuels exclus. | rail, port_fluvial | industrie | `src-12a-duisburg-rail-port` |
| Essen | Mines, acier Krupp, rail local de 1847/1862 et production d’armement ; militaire au sens industriel. | rail, industrie, militaire | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-essen-industry`, `src-essen-krupp` |
| Dortmund | Mines et sidérurgie Hoesch/Union ; port de 1899. Jour d’ouverture divergent dans deux notices municipales. | rail, industrie, port_fluvial | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-dortmund-rail`, `src-12a-dortmund-industrie`, `src-dortmund-port` |
| Cologne | Gare centrale et franchissement du Rhin de 1859 ; pont Hohenzollern antérieur à 1945. | rail | port_fluvial, industrie | `src-12a-koeln-gare` |
| Düsseldorf | Port de 1896 relié au rail ; étude patrimoniale locale C, industrie encore à documenter. | rail, port_fluvial | industrie ; Consolidation de la source patrimoniale C par archives ou opérateur. | `src-12a-duesseldorf-port` |
| Francfort-sur-le-Main | Gare de 1888, extension de 1924. Cela ne valide ni port ni aéroport au Snapshot 0. | rail | port_fluvial, aviation | `src-12a-dresden-gare`, `src-frankfurt-station-district` |
| Mannheim | Port de 1828/1840, première gare de 1840, liaison portuaire par Schleifbahn dès 1854. | rail, port_fluvial | industrie | `src-mannheim-rail`, `src-mannheim-rheinhafen` |
| Stuttgart | Gare de 1922–1928 et production de guerre à Untertürkheim ; chiffres du groupe Daimler non localisés exclus. | rail, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-stuttgart-gare`, `src-12a-stuttgart-daimler` |
| Nuremberg | Gare de 1844–1847, transformation 1900–1906 ; pas d’événement journalier inventé en 1903 ou 1905. | rail | industrie | `src-12a-dresden-gare` |
| Munich | Rail Munich–Augsbourg en 1839–1840 et implantation de Maffei ; pas de capacité industrielle chiffrée en 1945. | rail, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-muenchen-chronologie` |
| Leipzig | Gare ouverte en 1915. Les véhicules exposés aujourd’hui ne prouvent pas leur affectation à Leipzig en 1945. | rail | industrie | `src-leipzig-db-museum` |
| Dresde | Gare de 1898 ; bombardements de février 1945 non anticipés. Rail seul prouvé par cette notice. | rail | industrie, port_fluvial | `src-12a-dresden-gare` |
| Magdebourg | Port de 1888–1893 et raccordement ferroviaire ; destruction du 16/01/1945, puis arrêt complet plusieurs mois après. | rail, port_fluvial | industrie | `src-magdeburg-port` |
| Halle (Saale) | Gare/nœud de 1890. L’industrie chimique de Leuna n’est pas transférée automatiquement à Halle. | rail | industrie | `src-12a-halle-gare` |
| Rostock | Heinkel atteste la construction d’avions, à classer industrie ; cela ne prouve pas un service de transport aérien. | industrie | port_maritime, construction_navale ; aviation suspendue en attente de preuve de transport | `src-12a-rostock-heinkel` |
| Wilhelmshaven | Établissement naval et essor 1933–1939 ; réunion avec Rüstringen en 1937 ; bilan final 1945 exclu. | port_maritime, militaire | construction_navale | `src-12a-wilhelmshaven-marine` |
| Sarrebruck | Liaisons ferroviaires franco-allemandes de 1850–1852 ; ouverture effective des passages en 1945 non démontrée. | rail | industrie, frontiere | `src-12a-saarbruecken-rail` |
| Chemnitz | Auto-Union à partir de 1936, production locale de guerre. Bombardements de février/mars 1945 exclus du Snapshot. | industrie | rail | `src-12a-chemnitz-industrie` |
| Cassel | Henschel/industrie de guerre locale attestée ; ne pas absorber le site distinct d’Altenbauna dans la ville. | industrie, militaire | rail | `src-12a-kassel-industrie` |
| Karlsruhe | Port de 1901 avec accès ferroviaire et charbon ; le Rhin géographique devient ici un rôle portuaire étayé. | rail, port_fluvial | industrie | `src-12a-karlsruhe-port` |
| Aix-la-Chapelle | Gare de 1841/1905 et situation issue des combats d’octobre 1944 ; pas d’arrêt total du rail déduit. | rail, frontiere | industrie | `src-12a-aachen-gare` |
| Coblence | Rail de 1858, lignes rhénanes/Moselle et gare réunie en 1902 ; confluence seule ne prouve pas un port. | rail | port_fluvial | `src-12a-koblenz-gare` |
| Ratisbonne | Transbordement Danube–rail de 1865, port de 1910. Relations avec Linz après 1945 non anticipées. | rail, port_fluvial | industrie | `src-12a-regensburg-port-rail` |
| Passau | Rail Passau–Straubing dès 1860. Confluence et proximité de frontière ne prouvent pas un trafic fluvial de 1945. | rail | port_fluvial, frontiere | `src-12a-passau-rail` |
| Flensbourg | Rail de 1854 et transbordement rail–vapeur de 1856 ; transit frontalier de janvier 1945 non garanti. | rail, port_maritime | frontiere | `src-12a-flensburg-port-rail` |
| Emden | Quais et transbordement charbon/minerai avant 1945 ; ne pas confondre arrêt des extensions et fermeture du port. | port_maritime | industrie, militaire | `src-12a-emden-port-minerais` |
| Vienne | Utiliser les gares Sud/Est historiques, pas le Hauptbahnhof moderne. Statut régional conservé de la v0.2. | rail | port_fluvial, industrie | `src-12a-vienna-suedbahnhof` |
| Linz | Bassins réalisés jusqu’en 1942 ; raccordement ferroviaire du port en 1948, port privé VÖEST en 1966. | industrie, militaire, port_fluvial | rail | `src-linz-1938-1945`, `src-12a-linz-port` |
| Graz | Rail historique distinct de l’industrie d’armement de 1944 ; ancienne référence aux pompiers écartée. | rail, industrie, militaire | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-graz-rail`, `src-graz-armaments` |
| Salzbourg | Raccordement à la Westbahn en 1860 ; services des corridors alpins à étudier séparément. | rail | Services et embranchements des corridors alpins au Snapshot 0. | `src-12a-salzburg-westbahn` |
| Innsbruck | Gare de 1858, Brenner 1867 et Arlberg 1884 ; infrastructure, sans horaires ni garantie de transit de guerre. | rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-innsbruck-gare` |
| Villach | Nœud suprarégional et direction ferroviaire issus du développement de 1864 ; services frontières non précisés. | rail | frontiere | `src-12a-villach-noeud` |
| Klagenfurt | Gare Südbahn et ligne de 1863 attestées par un guide numérisé ; métadonnées d’édition à compléter. | rail | industrie ; Date d’édition et métadonnées complètes du guide ancien. | `src-12a-klagenfurt-guide` |
| Bregenz | Rail de 1870–1872, réseaux allemand/suisse, transbordement et vapeur lacustres avant 1945. | rail, port_fluvial, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-bregenz-rail` |
| Feldkirch | Gare frontière de 1872, renforcée par l’Arlberg dans les années 1880 ; jour exact de 1872 à recouper. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-feldkirch-frontiere` |
| Wels | Présence ferroviaire historique attestée ; bifurcation vers Passau non prouvée par cette notice. | rail | Bifurcation vers Passau et hiérarchie du nœud avant 1945. | `src-12a-wels-rail` |
| Steyr | Armement Steyr-Daimler-Puch et sous-camp de mars 1942 ; preuve locale de guerre remplaçant le commerce ancien. | industrie, militaire | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-steyr-armement` |
| Wiener Neustadt | Terrain aérien de 1909 ; avions en 1940, tenders et A4 en 1943. Ruines finales non datées au 01/01. | industrie, aviation, militaire | rail | `src-12a-wiener-neustadt-industrie` |
| Sankt Pölten | Westbahn construite dès 1856, achevée en 1858 ; nœud et essor industriel local. | rail, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-st-poelten-westbahn` |
| Berne | Ville fédérale depuis 1848, raccordements ferroviaires du XIXe siècle ; nuance juridique de capitale à conserver. | capitale, administration, rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-bern` |
| Zurich | Gare de 1847/1865–1871 ; fret/entrepôts repris de l’audit Claude, industrie locale à compléter. | rail | industrie | `src-12a-dhs-zuerich` |
| Bâle | Ports et gares avant 1945 ; chimie historique attestée. Interruption de navigation pendant les guerres sans bornes exactes. | rail, port_fluvial, frontiere, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-basel` |
| Genève | Rail franco-suisse de 1858 ; terrain aérien de 1920, piste de 1937. Les grandes lignes contournent Genève. | rail, frontiere, aviation | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-geneve`, `src-12a-geneve-aeroport` |
| Lausanne | Gare de 1915, fret Sébeillon de 1927, axe vers Paris/Milan ; remplacement des deux liens Museris. | rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-lausanne` |
| Olten | Nœud et ateliers dès 1856, photographie de l’atelier en 1944 ; pas de tonnage de fret déduit. | rail | Fonction et installations spécifiques de fret : le nœud/atelier ne donne pas leur volume. | `src-12a-dhs-olten` |
| Lucerne | Réseau du XIXe siècle, accès Gothard en 1897 ; commerce lacustre ancien insuffisant pour un port de 1945. | rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-luzern` |
| Winterthour | Six lignes du XIXe siècle, Sulzer/SLM avant 1945 ; notice DHS allemande lisible remplace le long lien SLM. | rail, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-winterthur` |
| Saint-Gall | Rail de 1856, broderie et exportateurs historiques ; ne pas transposer l’apogée d’avant 1914 à 1945. | rail, industrie | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-st-gallen` |
| Schaffhouse | Rail de 1857 et bombardement du 01/04/1944. Maintenir l’absence de port_fluvial, sans destruction totale déduite. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-schaffhausen` |
| Chiasso | Rail de 1874/1876, gare internationale et port franc de 1925 ; passages de guerre non garantis. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-chiasso` |
| Bellinzone | Gothard de 1882, ateliers de 1884 ; infrastructure ferroviaire locale attestée. | rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-bellinzona` |
| Brigue | Simplon de 1906/1921, Lötschberg de 1913, installations de fret/frontière ; pas de service italien quotidien garanti. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-brig` |
| Buchs SG | Gare de 1858, Arlberg de 1884, contexte douanier de 1924 ; preuve locale indépendante de la page ÖBB actuelle. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-buchs` |
| Romanshorn | Lindau : bac ferroviaire arrêté en 1939. Friedrichshafen : plage 1869–1976 insuffisante pour garantir le service en guerre. | rail, port_fluvial | Exploitation des bacs Friedrichshafen et automobile au 01/01/1945. | `src-12a-dhs-romanshorn` |
| Vallorbe | Rail de 1870/1875, tunnel Mont-d’Or de 1915 ; existence du corridor franco-suisse, sans horaire de guerre. | rail, frontiere | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-dhs-vallorbe` |
| Vaduz | Siège du gouvernement depuis 1862, bâtiment de 1903–1905 ; C et capitale nationale, sans rail emprunté à Schaan. | capitale, administration | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-vaduz-gouvernement`, `src-12a-vaduz-portrait-historique` |
| Schaan | Gare de Schaan-Vaduz sur la ligne de 1872 ; rôle ferroviaire local, distinct de Vaduz. | rail | Aucun rôle structurel supplémentaire ; service exact non garanti. | `src-12a-schaan-rail` |

Les notices DHS allemandes d’Olten, Winterthour et Brigue ont été effectivement lues ; les versions françaises ne sont pas déclarées consultées. L’étude de Klagenfurt est un guide ancien numérisé, identifié par son titre et son auteur ; sa date d’édition reste à compléter. Le lecteur ne doit pas prendre ces notices pour des archives d’exploitation du 1er janvier 1945.

## 3. Delta complet, limites et intégration

Le delta fournit les champs du protocole pour chaque notice : ID, niveau, type, titre, institution, URL, consultation, cibles, usages, passage précis et limites. Il enrichit également les 34 entrées initiales sans effacer l’historique, ainsi que l’entrée MWI déjà introduite par Claude. La source `src-vaduz-portrait` déjà présente dans la v0.2 reste conservée ; son enregistrement exact n’a pas été fourni et n’est pas remplacé arbitrairement.

Le suivi des huit liens signalés comme non lisibles distingue une URL relue de références remplacées :

| Ancienne référence | Résultat / remplacement |
|---|---|
| Hambourg | Même URL retrouvée et lue, même `src-hamburg-port-history` enrichi. |
| `src-dortmund-industry` | `src-12a-dortmund-industrie` ; ancienne URL non relue ici. |
| `src-frankfurt-hbf` | `src-12a-dresden-gare` ; ancienne URL non relue ici. |
| `src-lausanne-station` | `src-12a-dhs-lausanne` ; ancienne URL non relue ici. |
| `src-lausanne-simplon` | `src-12a-dhs-lausanne`, `src-12a-dhs-brig` ; ancienne URL non relue ici. |
| `src-olten-rail` | `src-12a-dhs-olten` ; ancienne URL non relue ici. |
| `src-winterthur-locomotive` | `src-12a-dhs-winterthur` ; ancienne URL non relue ici. |
| `src-gotthard-history` | `src-12a-dhs-bellinzona`, `src-12a-dhs-luzern` ; ancienne URL non relue ici. |

Les pages DB Museum et CFF générales restent du contexte national. Les pages de projets ÖBB et FAQ portuaire contemporaines restent du contexte limité. Une source officielle n’est pas automatiquement une preuve historique locale. Les dates initialement déclarées pour les sept références non relues sont conservées séparément, avec `date_consultation: null`.

### Incertitudes précisément délimitées

**Infrastructure versus service actif**. Les notices documentent gares, ports et productions avant 1945. Manque : Horaires, trafics, capacités et interruptions exactes au 01/01/1945 00:00. Décision appliquée : Retenir les points structurels ; aucune arête ou capacité opérationnelle nouvelle déduite de ces seules notices.

**Bâle : navigation de guerre**. Ports construits avant 1945 ; le DHS indique interruption pendant les deux guerres. Manque : Bornes des interruptions et reprises durant 1939–1945. Décision appliquée : Garder le port comme infrastructure ; suspendre toute affirmation de trafic normal au Snapshot 0.

**Romanshorn : bacs**. Lindau 1869–1939 ; Friedrichshafen 1869–1976 ; bac automobile dès 1929. Manque : Suspensions et reprises en guerre pour Friedrichshafen et le bac automobile. Décision appliquée : Aucune liaison active vers Lindau en janvier 1945 ; autres services en attente de source datée.

**Dortmund : jour d’ouverture du port**. Année 1899 commune aux notices. Manque : 11 août dans l’audit de la première notice ; 21 août dans la seconde notice effectivement lue. Décision appliquée : Année seule, pas d’événement quotidien avant recoupement.

**Osnabrück et Düsseldorf**. Histoires locales cohérentes et précises de gare/triage et port. Manque : Recoupement archival/institutionnel historique. Décision appliquée : Conserver les sources au niveau C et le besoin de consolidation ; importance B indépendante de ce niveau.

**Klagenfurt, Feldkirch et Wels**. Implantation ferroviaire historique locale. Manque : Date d’édition du guide ; jour exact d’ouverture de Feldkirch en 1872 ; bifurcation de Wels vers Passau. Décision appliquée : Ne pas créer d’événements précis ou de branches non démontrées.

La règle de travail appliquée est : un point structurel peut être conservé avec des services inconnus. Si le modèle exige une preuve d’exploitation pour afficher le point lui-même, c’est le seul arbitrage de modélisation à trancher ; le dossier contient les preuves et les manques pour le faire. Aucun point ouvert n’a été transformé en consultation fictive ou en événement précis.

### Ordre proposé à Claude

1. Enrichir le registre à partir du delta ; ajouter seulement les IDs absents et conserver les anciennes notices écartées ou limitées avec leur statut.
2. Ajouter les neuf points ; résoudre leurs positions selon Wikidata/Natural Earth et le périmètre historique, sans utiliser un complexe industriel comme un second point urbain.
3. Appliquer les corrections explicites de noms/rôles, puis ajouter les preuves rôle par rôle. Préserver capitale, situation et priorité déjà arbitrées en v0.2.
4. Réévaluer le marqueur « à renforcer » avec les rôles et précisions listés, sans le supprimer parce qu’une seule source locale a été ajoutée.
5. Créer les éventuels événements futurs dans leurs couches datées. Le présent patch ne les déclare pas intégrés.

Contrôles effectués : JSON valides, neuf nouveaux IDs distincts des 64 existants, 64 corrections distinctes, références de sources résolues et cibles concordantes. Aucun contrôle d’import ou de rendu du dépôt Claude n’est revendiqué.

### Index des sources effectivement consultées dans cette recherche

Les liens ci-dessous complètent les notices détaillées du JSON ; ils désignent les passages relus, pas une lecture intégrale de chaque ouvrage.

- `src-hamburg-port-history` — [Hafenhistorie — histoire du port de Hambourg](https://www.hamburg.de/freizeit/hafengeburtstag-hamburg/hafenhistorie-1099522) — Freie und Hansestadt Hamburg ; niveau B. Passage : Sections port au XIXe siècle, Freihafen et loi de 1937.
- `src-hannover-rail` — [Hannover von 1843 bis 1870](https://www.hannover.de/Kultur-Freizeit/Geschichte-Geschichten/Echt-hann%C3%B6versch/Historisches-aus-Hannover/Stadtgeschichte-in-der-Station-Waterloo/Hannover-von-1843-bis-1870) — Landeshauptstadt Hannover ; niveau B. Passage : Entrée 1843 : ligne vers Lehrte et commencement de la gare.
- `src-hannover-freight` — [Hauptgüterbahnhof Hannover](https://www.hannover.de/Kultur-Freizeit/Geschichte-Geschichten/Echt-hann%C3%B6versch/Zehn-Dinge/Zehn-neu-genutzte-Industrie-Anlagen-in-Hannover/Hauptg%C3%BCterbahnhof-Hannover) — Landeshauptstadt Hannover ; niveau B. Passage : Ouverture 1931 ; récit 1877–1931 et dégâts de guerre.
- `src-essen-industry` — [Industrie in Essen](https://historischesportal.essen.de/startseite_7/industrie/industrie_allgemein.de.html) — Haus der Essener Geschichte / Stadtarchiv ; niveau B. Passage : Paragraphes mine, acier, rail de 1847/1862 et production d'armement.
- `src-essen-krupp` — [Krupp](https://historischesportal.essen.de/startseite_7/industrie/krupp_1.de.html) — Haus der Essener Geschichte / Stadtarchiv ; niveau B. Passage : Histoire de la Gussstahlfabrik et production d'armes.
- `src-mannheim-rheinhafen` — [Rheinhafen und Rheinbrücke](https://www.mannheim.de/de/tourismus-entdecken/stadtgeschichte/stadtpunkte/buergertum-handel-industrie/rheinhafen-und-rheinbruecke) — Stadt Mannheim ; niveau B. Passage : Paragraphe Freihafen 1828 et premier bassin 1840.
- `src-mannheim-rail` — [Tattersall](https://www.mannheim.de/de/tourismus-entdecken/stadtgeschichte/stadtpunkte/buergertum-handel-industrie/tattersall) — Stadt Mannheim ; niveau B. Passage : Paragraphe première gare dès 1840, transfert 1876 et Schleifbahn de 1854.
- `src-leipzig-db-museum` — [Museumsgleis 24](https://dbmuseum.de/en/halle/exhibitions/leipzig) — DB Museum ; niveau B. Passage : Paragraphe Leipzig Central Station, ouverture de 1915.
- `src-magdeburg-port` — [Der historische Handelshafen](https://www.magdeburg.de/Wissenschaft-Bildung/Wissenschaft/Wissenschaftshafen/Quartier/Historie/) — Landeshauptstadt Magdeburg ; niveau B. Passage : Historique 1888–1893, pont de 1894 et bombardement du 16/01/1945.
- `src-mwi-aachen-1944` — [Urban Warfare Project Case Study #10: Battle of Aachen](https://mwi.westpoint.edu/urban-warfare-project-case-study-10-battle-of-aachen/) — Modern War Institute, United States Military Academy, West Point ; niveau B. Passage : Sections « The City », « The Battle », fin du 21/10/1944 et bilan immobilier.
- `src-12a-hamm-triage` — [Verschiebebahnhof Hamm — histoire du triage](https://www.hamm.de/verschiebebahnhof-hamm) — Stadtarchiv Hamm ; niveau B. Passage : Sections introduction et « Der größte Verschiebebahnhof Europas » ; légende du 22 avril 1944.
- `src-12a-ludwigshafen-igfarben` — [Nationalsozialismus und Kriegswirtschaft — Ludwigshafen/Oppau](https://www.basf.com/global/de/who-we-are/history/chronology/1925-1944/1933-1945/) — BASF Corporate History ; niveau B. Passage : Sections « Autarkie und Aufrüstung » et « Forschen für den Krieg ».
- `src-12a-salzgitter-nom` — [Chronik 1942–2011 — Watenstedt-Salzgitter](https://stadtbibliothek.salzgitter.de/kultur/stadtgeschichte/teil4.php) — Stadt Salzgitter / Stadtbibliothek ; niveau B. Passage : Entrée 1942, 1er avril.
- `src-12a-augsburg-messerschmitt` — [Informationstafel Messerschmitt — texte de travail municipal](https://machmit.augsburg.de/informationstafel-messerschmitt) — Stadt Augsburg, Erinnerungskultur ; niveau C. Passage : Texte « Messerschmitt Informationstafel », paragraphes 1938 et novembre 1944.
- `src-12a-schweinfurt-roulements` — [Bomben auf Schweinfurt — rôle de la production de roulements](https://www.schweinfurt.de/kultur-freizeit/events?ev%5Bid%5D=225746) — Stadt Schweinfurt ; niveau B. Passage : Description de la visite, paragraphe commençant par Waffen, Panzer oder Flugzeuge.
- `src-12a-osnabrueck-fret` — [Historie Güterbahnhof — Osnabrück](https://lokviertel-os.de/lok-viertel/historie/) — Lok-Viertel-OS / Aloys & Brigitte Coppenrath Stiftung ; niveau C. Passage : Sections 1909–1944 et 1944–1961.
- `src-12a-mainz-gare` — [Hauptbahnhof — histoire de la gare de Mayence](https://www.mainz.de/angebote-entdecken/zu-gast-in-mainz/sehenswertes/hauptbahnhof) — Landeshauptstadt Mainz ; niveau B. Passage : Section Hauptbahnhof auf einen Blick ; Brand und Umbau ; Wiederaufbau.
- `src-12a-leuna-commune` — [Historisches — formation de Leuna](https://www.leuna.de/de/historisches.html) — Stadt Leuna ; niveau B. Passage : Section Historisches, paragraphes 1916–1930 et Stadt Leuna.
- `src-12a-leuna-essence` — [Die Leuna-Tankstelle — carburant synthétique](https://www.leuna.de/de/die-leunatankstelle/die-leuna-tankstelle.html) — Stadt Leuna ; niveau B. Passage : Section Die Leuna-Tankstelle, paragraphes 1926–1927 et 1944.
- `src-12a-donawitz-acier` — [History of the Donawitz site — acier et rail](https://www.voestalpine.com/stahldonawitz/en/company/history/) — voestalpine Stahl Donawitz ; niveau B. Passage : Historical development et Historical views, paragraphes 1878, 1892 et 1941.
- `src-12a-dhs-bellinzona` — [Bellinzone (commune)](https://hls-dhs-dss.ch/fr/articles/002031/2022-12-16/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Section époque contemporaine, paragraphes ouverture du Gothard et ateliers.
- `src-12a-dhs-chiasso` — [Chiasso](https://hls-dhs-dss.ch/fr/articles/002230/2022-06-30/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphe Avec l'arrivée du chemin de fer.
- `src-12a-dhs-buchs` — [Buchs (SG)](https://hls-dhs-dss.ch/fr/articles/001346/2004-08-31/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes ponts et lignes ferrées 1858–1924.
- `src-12a-dhs-romanshorn` — [Romanshorn](https://hls-dhs-dss.ch/fr/articles/001860/2020-04-28/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes port et voie ferrée 1855–1856, bacs ferroviaires.
- `src-12a-dhs-lausanne` — [Lausanne (commune)](https://hls-dhs-dss.ch/fr/articles/002408/2009-04-02/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes XIXe–XXe siècle, nœud Paris–Milan et Sébeillon.
- `src-12a-dhs-vallorbe` — [Vallorbe](https://hls-dhs-dss.ch/fr/articles/002547/2014-12-27/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes arrivée du rail 1870–1875 et tunnel du Mont-d'Or 1915.
- `src-12a-dhs-olten` — [Olten (Gemeinde) — commune d'Olten](https://hls-dhs-dss.ch/de/articles/001168/2010-09-16/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphe Eisenbahnknotenpunkt et photographie de l'atelier principal en 1944.
- `src-12a-dhs-schaffhausen` — [Schaffhouse (commune)](https://hls-dhs-dss.ch/fr/articles/001281/2015-07-31/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes gare 1857, douanes 1913–1914 et bombardement du 1er avril 1944.
- `src-12a-dhs-luzern` — [Lucerne (commune)](https://hls-dhs-dss.ch/fr/articles/000624/2016-11-03/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes réseau 1859–1897, raccordement Immensee–Lucerne.
- `src-12a-dhs-st-gallen` — [Saint-Gall (commune)](https://hls-dhs-dss.ch/fr/articles/001321/2012-01-06/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Introduction, arrivée du chemin de fer en 1856.
- `src-12a-dhs-winterthur` — [Winterthur — Winterthour](https://hls-dhs-dss.ch/de/articles/000157/2015-08-28/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Sections Siedlungsentwicklung et Wirtschaft ; paragraphes 1855–1876 et vers 1910.
- `src-12a-dhs-brig` — [Brig (Stadt) — Brigue (ville)](https://hls-dhs-dss.ch/de/articles/002662/2013-07-17/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes transport, tunnels Simplon et Lötschberg, gare de 1910.
- `src-12a-dhs-bern` — [Berne (commune)](https://hls-dhs-dss.ch/fr/articles/000209/2016-11-10/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphes raccordements 1857–1864 et Ville fédérale 1848.
- `src-12a-dhs-zuerich` — [Zurich (commune)](https://hls-dhs-dss.ch/fr/articles/000171/2015-01-25/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Paragraphe grands chantiers 1847–1871.
- `src-12a-dhs-geneve` — [Genève (commune)](https://hls-dhs-dss.ch/fr/articles/002903/2018-02-07/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Section développement XIXe siècle, réseau ferroviaire de 1858.
- `src-12a-dhs-basel` — [Bâle-Ville](https://hls-dhs-dss.ch/fr/articles/007478/2017-05-30/) — Dictionnaire historique de la Suisse / HLS ; niveau B. Passage : Sections économie et transports : tableau cantonal de 1939, chimie, ports Saint-Jean/Petit-Huningue et gares avant 1945.
- `src-12a-geneve-aeroport` — [Notre histoire centenaire — Genève-Cointrin](https://www.gva.ch/fr/aeroport/presentation/notre-histoire) — Genève Aéroport ; niveau B. Passage : Chronologie 1919, 1920, 1932 et 1937.
- `src-12a-schaan-rail` — [Schaan — gare et liaisons](https://historisches-lexikon.li/Schaan) — Historisches Lexikon des Fürstentums Liechtenstein / Liechtenstein-Institut ; niveau B. Passage : Paragraphe Verkehr, gare Schaan-Vaduz et pont de 1928–1929.
- `src-12a-berlin-anhalter` — [Anhalter Bahnhof — histoire locale](https://www.berlin.de/sehenswuerdigkeiten/3561282-3558930-anhalter-bahnhof.html) — Land Berlin ; niveau B. Passage : Section Entstehung und Funktion ; raccordement S-Bahn 1939.
- `src-12a-wesermuende` — [Stadtgeschichte Bremerhavens — Wesermünde en 1945](https://www.bremerhaven.de/de/freizeit-kultur/stadtarchiv/stadtgeschichte-bremerhavens.13195.html) — Stadtarchiv Bremerhaven ; niveau B. Passage : Paragraphes Geestemünde, fusion 1939 et bombardement du 18 septembre 1944.
- `src-12a-leoben-rattachement` — [Straßennamen mit Geschichte — rattachement de Donawitz](https://www.leoben.at/daten-geschichte/strassennamen/) — Stadt Leoben ; niveau B. Passage : Paragraphe Eingemeindungen, 1er octobre 1939.
- `src-12a-kiel-chantiers` — [Erinnerungstag 1. Juli 1955 — histoire des chantiers de Kiel](https://www.kiel.de/de/kultur_freizeit/stadtarchiv/erinnerungstage.php?id=39) — Kieler Stadtarchiv ; niveau B. Passage : Section Die Kieler Werften ab 1933 im Dienst der Rüstungsindustrie.
- `src-12a-karlsruhe-port` — [Rheinhafen Karlsruhe — port et rail](https://stadtlexikon.karlsruhe.de/index.php/De:Lexikon:ins-1511) — Stadtarchiv Karlsruhe / Stadtlexikon ; niveau B. Passage : Paragraphes construction 1896–1901, charbon et expansions.
- `src-12a-stuttgart-daimler` — [Unsere Geschichte. Unsere Verantwortung. — Daimler-Benz en guerre](https://group.mercedes-benz.com/unternehmen/magazin/kultur/75-jahre-2-weltkrieg.html) — Mercedes-Benz Group / archives de l'entreprise ; niveau B. Passage : Paragraphes reconversion industrielle 1939–1943, Stuttgart-Untertürkheim.
- `src-12a-stuttgart-gare` — [Hauptbahnhof Stuttgart — histoire du Bonatzbau](https://www.lmz-bw.de/statische-newsroom-seiten/hauptbahnhof-stuttgart) — Landesmedienzentrum Baden-Württemberg ; niveau B. Passage : Paragraphes inauguration 1922, voies complètes en 1925, bâtiment 1928.
- `src-12a-dresden-gare` — [Architektonische Schönheiten — Dresden, Nürnberg, Frankfurt et Bremen](https://www.deutschebahn.com/de/architektur_bahnhof-6878040) — Deutsche Bahn ; niveau B. Passage : Sections Dresde (1898), Nuremberg (1844–1847, remaniement 1900–1906), Francfort (1888, extension 1924), Brême (1885–1889).
- `src-12a-halle-gare` — [Chronik — Halle (Saale), gare centrale](https://halle.de/kultur-tourismus/stadtgeschichte/chronik) — Stadt Halle (Saale) ; niveau B. Passage : Entrée 1890, gare centrale et séparation du fret.
- `src-12a-saarbruecken-rail` — [Stadtchronik — gare et industrialisation](https://www.saarbruecken.de/zb/kultur/stadtgeschichte/chronik) — Landeshauptstadt Saarbrücken ; niveau B. Passage : Entrées 1850–1852 et 15 octobre 1852.
- `src-12a-kassel-industrie` — [Kasseler Chronik 1933–1945 — Henschel et industrie de transport](https://www.kassel.de/buerger/stadtgeschichte/chronik/inhaltsseiten/chronik-der-jahre-1933-1945.php) — Stadt Kassel ; niveau B. Passage : Entrées production Henschel, Credé et bombardements 1941–1943.
- `src-12a-vienna-suedbahnhof` — [Geschichte, Daten & Fakten — Südbahnhof et Ostbahnhof](https://hauptbahnhofcity.oebb.at/de/10jahrehauptbahnhof/geschichte-daten-fakten) — Österreichische Bundesbahnen (ÖBB) ; niveau B. Passage : Entrées 1841, 1870 et 1874.
- `src-12a-innsbruck-gare` — [Geschichte, Daten & Fakten — Innsbruck Hauptbahnhof](https://bahnhofcityinnsbruck.oebb.at/de/center/geschichte-daten-fakten) — Österreichische Bundesbahnen (ÖBB) ; niveau B. Passage : Entrées 1858, 1867 et 1884.
- `src-12a-wels-rail` — [Stadtgeschichte — Wels et le chemin de fer](https://www.wels.gv.at/lebensbereiche/bildung-und-kultur/stadtarchiv-und-geschichte/stadtgeschichte/) — Stadtarchiv Wels ; niveau B. Passage : Entrée XIXe siècle / 1800 : Pferdeeisenbahn, vapeur en 1855.
- `src-12a-bregenz-rail` — [Stadtgeschichte — Bregenz, rail et lac](https://www.bregenz.gv.at/rathaus/stadtarchiv/stadtgeschichte) — Stadtarchiv Bregenz ; niveau B. Passage : Entrées 1870–1872, 1883 et 1884.
- `src-12a-salzgitter-siderurgie` — [Im Dienst des NS-Staates — histoire du site de Salzgitter](https://geschichte.salzgitter-ag.com/de/einzelne-geschaeftsbereiche-und-standorte/geschaeftsbereich-stahlerzeugung/salzgitter/im-dienst-des-ns-staates.html) — Salzgitter AG ; niveau B. Passage : § fondation du 15/07/1937 et première fonte du 22/10/1939.
- `src-12a-bremen-histoire` — [Stadtgeschichte: Bremens Geschichte im Überblick](https://www.bremen.de/tourismus/stadt-leute/geschichte) — Portail officiel Bremen.de / Staatsarchiv Bremen ; niveau B. Passage : Chronologie : 1580, 1827, 1847 et 1939–1945.
- `src-12a-duisburg-rail-port` — [25 Jahre duisport rail — Schiene mit Tradition: Von 1848 bis heute](https://duisport.de/25-jahre-duisport-rail-rueckgrat-der-schienenlogistik-im-duisburger-hafen/) — Duisburger Hafen AG / duisport ; niveau B. Passage : Sous-titre « Schiene mit Tradition: Von 1848 bis heute », paragraphe du 14/10/1848.
- `src-12a-duesseldorf-port` — [Der Düsseldorfer Handelshafen — Ralf Herkrath](https://www.rheinische-industriekultur.de/objekte/duesseldorf/Handelshafen/Hafen.html) — Rheinische Industriekultur ; niveau C. Passage : Paragraphes du lancement de 1890 à l'ouverture de 1896, liaison ferroviaire et entrepôts.
- `src-12a-muenchen-chronologie` — [München — ein chronologischer Überblick](https://stadt.muenchen.de/infos/stadtgeschichte.html) — Landeshauptstadt München ; niveau B. Passage : Entrées 1839, 1840, 1847 et 1854.
- `src-12a-rostock-heinkel` — [Heinkel in Rostock. Innovation und Katastrophe — présentation de l'exposition](https://rathaus.rostock.de/de/sonntagsfuehrung_durch_sonderausstellung_heinkel_in_rostock_innovation_und_katastrophe/353245) — Kulturhistorisches Museum Rostock / Stadt Rostock ; niveau B. Passage : Présentation de l'exposition, paragraphes sur les années 1920–1930 et avril 1942.
- `src-12a-wilhelmshaven-marine` — [Stadtgeschichte Wilhelmshaven](https://www.wilhelmshaven.de/Tourismus/Stadtportrait/Stadtgeschichte.php) — Stadt Wilhelmshaven ; niveau B. Passage : Paragraphes « Marine-Etablissement », essor 1933–1939 et réunion de 1937.
- `src-12a-chemnitz-industrie` — [Chronik — industrialisation et Seconde Guerre mondiale](https://www.chemnitz.de/de/unsere-stadt/geschichte/chronik) — Stadt Chemnitz ; niveau B. Passage : Paragraphes sur 1936 et sur les entreprises pendant la Seconde Guerre mondiale.
- `src-12a-regensburg-port-rail` — [Regensburg — Geschichte des Hafens](https://www.bayernhafen.de/hafen/regensburg/) — bayernhafen ; niveau B. Passage : Section histoire : transbordement en 1865 ; ouverture de juin 1910 ; extension 1919–1923.
- `src-12a-passau-rail` — [Neubürgerbroschüre 2023 — Stadtgeschichte](https://www.passau.de/fileadmin/Homepage_Stadt_Passau/2._Rathaus_und_Buergerservice/Buergerservice/Downloadcenter/Broschueren_und_Flyer/22-11-09_Neubuergerbroschuere_2023.pdf) — Stadt Passau ; niveau B. Passage : PDF p. 6 (index 5), chronologie, entrée 1860.
- `src-12a-flensburg-port-rail` — [Stadtgeschichte Flensburg — chronologie](https://www.flensburg.de/Leben-Soziales/Freizeit-Kultur/Stadtportrait/Stadtgeschichte.php?FID=2306.33092.1&ModID=7&NavID=2306.12&object=tx%7C4204.5.1) — Stadt Flensburg ; niveau B. Passage : Entrées 1854, 1856 et 1864.
- `src-12a-emden-port-minerais` — [Hafenrundgang Emden — Nord- und Südkai](https://www.nports.de/haefen/emden/hafenrundgang/historie/nord-und-suedkai) — Niedersachsen Ports ; niveau B. Passage : Sections « Standort Nord- und Südkai », « Start des Erz-Umschlags », 1922 et 1926.
- `src-12a-aachen-gare` — [Aachener Hauptbahnhof — Architektouren](https://www.architektouren.rwth-aachen.de/bauwerke/projekte/aachener-hauptbahnhof/) — RWTH Aachen ; niveau B. Passage : Description historique : première gare de 1841 sur la ligne Cologne–Anvers ; gare de 1905.
- `src-12a-koeln-gare` — [Zeittafel 1859 — Kölner Rheinbrücke et premier Hauptbahnhof](https://www.rheinische-geschichte.lvr.de/chronicle/1859) — Landschaftsverband Rheinland, Portal Rheinische Geschichte ; niveau B. Passage : Entrées 03/10/1859 et 05/12/1859.
- `src-12a-villach-noeud` — [Auf dem Weg in die Gegenwart — Villach et l'essor ferroviaire](https://villach.at/getmedia/7257a007-84e0-4d20-8b6a-2e57cd6a45a8/29_MJ2010_Auf_dem_Weg.pdf.aspx) — Museum der Stadt Villach, Museumsjahrbuch 2010 ; niveau B. Passage : PDF p. 5–7 (index 4–6), rail en 1864, nœud et direction ferroviaire.
- `src-12a-feldkirch-frontiere` — [An Feldkirch ging kein Weg vorbei — Höchste Eisenbahn](https://www.feldkirch.at/fileadmin/user_upload/document/Stadtarchiv/1998_5-Oktober_An_Feldkirch_ging_kein_Weg_vorbei.pdf) — Stadtarchiv Feldkirch, Feldkirch aktuell 5/1998 ; niveau B. Passage : PDF p. 4 (index 3), rubrique « Höchste Eisenbahn ».
- `src-12a-steyr-armement` — [Forced Labour in the Arms Industry — Steyr-Münichholz](https://www.mauthausen-memorial.org/en/History/The-Mauthausen-Concentration-Camp-19381945/Forced-Labour-in-the-Arms-Industry) — KZ-Gedenkstätte Mauthausen ; niveau B. Passage : Paragraphe sur Steyr-Daimler-Puch et le sous-camp de mars 1942.
- `src-12a-wiener-neustadt-industrie` — [Geschichte der Stadt — Flugfeld et industrie de guerre](https://www.wiener-neustadt.at/de/stadt/geschichte) — Stadt Wiener Neustadt ; niveau B. Passage : Sections « Das Wiener Neustädter Flugfeld » et « Zerstörung im Zweiten Weltkrieg und Wiederaufbau ».
- `src-12a-st-poelten-westbahn` — [150 Jahre Westbahn in St. Pölten — exposition de 2008](https://www.stadtmuseum-stp.at/veranstaltungen/150-jahre-westbahn-in-st-poelten/) — Stadtmuseum St. Pölten ; niveau B. Passage : Paragraphes construction 1856, achèvement en deux ans, croissance 1870–1912 et guerre 1944–1945.
- `src-12a-luebeck-gare` — [Lübecker Bahnhof — Nächster Halt seit 1908](https://www.luebeck.de/de/stadtleben/tourismus/luebeck/sehenswuerdigkeiten/luebecker-bahnhof) — Hansestadt Lübeck ; niveau B. Passage : Section « Nächster Halt seit 1908 », ouverture du 01/05/1908.
- `src-12a-koblenz-gare` — [Bahnhöfe — Koblenz Hauptbahnhof](https://www.regionalgeschichte.net/mittelrhein/koblenz/kulturdenkmaeler/hauptbahnhof.html) — Institut für Geschichtliche Landeskunde Rheinland-Pfalz, regionalgeschichte.net ; niveau B. Passage : Sections premier train du 11/11/1858 et gare centrale de 1902 ; références Franke et Dehio.
- `src-12a-salzburg-westbahn` — [Namen der Salzburger Stadtteile — extension urbaine et Westbahn](https://facelift.stadt-salzburg.at/archiv/namen-der-salzburger-stadtteile) — Stadtarchiv Salzburg ; niveau B. Passage : Paragraphe sur le raccordement de 1860 à la Kaiserin-Elisabeth-Westbahn.
- `src-12a-klagenfurt-guide` — [Markus Frhr. v. Jabornegg von und zu Gamsenegg, Klagenfurt und der Wörther-See — no 52](https://ubdocs.aau.at/open/voll/altbestand/AC11123827.pdf) — Universitätsbibliothek Klagenfurt / édition Caesar Schmidt, Zurich ; niveau B. Passage : Titre et auteur : scan p. 9 (index 8) ; gare et ligne de 1863 : p. 17 (index 16), p. imprimée 9.
- `src-12a-osnabrueck-croisement` — [Der Hauptbahnhof Osnabrück — Eisenbahnkreuz Osnabrück](https://www.osnabahn.de/bahnhoefe/osnabrueck-hbf/) — Matthias Beermann, Osnabahn ; niveau C. Passage : Historique : gare du 24/04/1895 au croisement des deux lignes ; courbes du triage de 1911–1914.
- `src-12a-augsburg-man` — [Tag des offenen Denkmals 2015 — MAN-Museum](https://www.augsburg.de/fileadmin/portale/stadtplanung/Publikationen/Tag_des_offenen_Denkmals/pdf/Tag_des_offenen_Denkmals_2015.pdf) — Stadt Augsburg ; niveau B. Passage : PDF p. 11 (index 10), chronologie et Forschungsanstalt de 1938.
- `src-12a-augsburg-armement` — [Tobias Brenner, Ein unbequemes Denkmal als Symbol der Befreiung — Halle 116](https://opus.bibliothek.uni-augsburg.de/opus4/files/2731/AVN_2014_H1_NR38.pdf) — Augsburger Volkskundliche Nachrichten, Universitätsbibliothek Augsburg ; niveau B. Passage : PDF p. 45 (index 44), texte sur MAN, moteurs de sous-marins et Messerschmitt ; article à partir de p. 37.
- `src-12a-schweinfurt-musee` — [Oma, bist Du … — Industriearbeit, Schweinfurter Museumsschriften 1 (2013)](https://www.schweinfurt.de/media/www.schweinfurt.de/org/med_1935/13142_museen-sw_low.pdf) — Museen und Galerien der Stadt Schweinfurt ; niveau B. Passage : PDF p. 9–10 (index 8–9), légendes d'archives VKF des années 1930 et assemblage des années 1940.
- `src-12a-dortmund-industrie` — [Geschichte der Innenstadt-Nord — Hoesch, Union et mines](https://www.dortmund.de/themen/stadtbezirke/innenstadt-nord/geschichte/) — Stadt Dortmund ; niveau B. Passage : Sections 1850–1870 et 1871–1914 : sidérurgie, mines et arrivées de minerai ; section guerre pour limites.
- `src-12a-vaduz-gouvernement` — [Regierung — Paul Vogt](https://historisches-lexikon.li/Regierung) — Historisches Lexikon des Fürstentums Liechtenstein / Liechtenstein-Institut ; niveau B. Passage : Introduction : siège à Vaduz depuis 1862 ; bâtiment de gouvernement de 1903–1905.
- `src-12a-vaduz-portrait-historique` — [Vaduz — Hauptort et résidence princière](https://www.vaduz.li/vaduz/portrait/vaduz) — Gemeinde Vaduz ; niveau B. Passage : Paragraphes Hauptort, rattachement de 1719, résidence depuis 1939.
- `src-12a-graz-rail` — [Graz historisch — Eisenbahngeschichte, BIG janvier 2010](https://www.graz.at/cms/dokumente/10135466_7747759/dabdc6cb/BIG_01_2010.pdf) — Stadt Graz, bulletin municipal BIG ; niveau B. Passage : PDF p. 5 (index 4), chronique ferroviaire : trajet Vienne–Graz–Trieste de 1857, gares.
- `src-12a-linz-port` — [Geschichte des Linzer Hafens](https://www.linzag.at/portal/de/businesskunden/logistik/hafen_1/geschichte_1) — LINZ AG ; niveau B. Passage : Section historique : transbordement de 1894, aménagements réalisés jusqu'en 1942, raccordement ferroviaire de 1948.
