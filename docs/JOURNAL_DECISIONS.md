# Atlas — Journal des décisions

Une ligne par décision, datée. Plus récente en haut. Ce journal remplace les versions éparpillées dans les conversations : si ce n'est pas ici, ce n'est pas décidé.

## 2026-10-01 (suite : réponse d'Ether au lot villes 1.4)

- **Règle des noms confirmée par Ether et appliquée à tout le lot 1.4** : la fiche porte le nom actuel (Łódź, Wrocław, Gdańsk…), l'état du Snapshot 0 porte le nom de 1945 (Litzmannstadt, Breslau, Dantzig…). Même forme qu'au lot 1.3 : les deux lots sont harmonisés. *(Ether, fait par Claude)*
- **11 villes renommées sur preuve individuelle** : Posen, Bromberg, Thorn, Kattowitz, Hindenburg, Königshütte, Swinemünde, Tarnowitz, Heydebreck, Cosel, Elbing. **Tczew et Wałbrzych gardent leur nom** : Dirschau et Waldenburg sont attestés, mais pas comme nom officiel de la ville. *(Ether)*
- **Varsovie** : capitale nationale par continuité, avec une note qui précise qu'aucun gouvernement n'y siège (exil à Londres ; PKWN à Lublin depuis le 27/07/1944, gouvernement provisoire le 31/12). Pas de capitale à Lublin ni à Kaunas. *(Ether, confirme Claude)*
- **Koźle (Cosel)** : point déplacé sur la gare du port, au bord des bassins. *(Ether, fait par Claude)*
- Preuves locales de rail pour Tapa, Valga, Krustpils et Radviliškis. « À renforcer » passe de 33 à 29 villes (Valga, Krustpils, Radviliškis et Stalowa Wola levées par des sources confirmées ; Tapa reste, sa source n'étant que partiellement confirmée). *(Ether + Claude)*
- Sources : 18 nouvelles + 4 relues (11 confirmées ; 7 illisibles ou partielles, Bromberg en lien mort). Les repères qu'Ether avait réécrits en anglais sont retraduits en français. Registre v1.14 ; « Sources à valider » : 121. *(Claude)*
- **Boucle automatique (v1)** : Ether (Work, dossier Atlas) ratisse et dépose `PRET_ether.md` ; Claude, réveillé toutes les 3 h par une tâche programmée, intègre, envoie sur GitHub et dépose `PRET_claude.md`. Un `STATUT.json` par lot ; au plus 3 cycles automatiques par lot ; tout point incertain va dans « À trancher par Guizmo ». Ether tient en parallèle `04_financement/` (lecture du projet seulement). Mode d'emploi : `docs/BOUCLE_AUTOMATIQUE.md`. *(Guizmo, Ether, Claude)*
- **Dossier d'échange unique** : le dossier Atlas du Bureau devient le seul point d'échange entre Ether et Claude. Il contient `00_TABLEAU_DE_BORD.md` (où on en est, qui attend quoi), `01_lots/<lot>/` (tout le fil d'un lot), `02_references/` (copie en lecture seule des docs du dépôt, rafraîchie par Claude à chaque envoi), `03_idees/`, `04_financement/` (Ether) et `99_archive/`. Fichiers nommés `date_auteur_sujet`. Le dépôt GitHub reste la seule source de vérité. *(Guizmo + Claude)*
- **Ether passe du moteur « 6Sol » à « 6Luna »** (6Sol surchargé, réponses trop longues ou inachevées). *(Guizmo)*

## 2026-10-01 (suite : réponse d'Ether au lot villes 1.3, feature « régime routier »)

- **Règle des noms à la date (Ether)** : nom français traditionnel réellement attesté en priorité, sinon le nom historique documenté pour la date ; `nom_local` daté à part ; les autres formes en alias. **Chaque ville est renommée sur preuve individuelle**, jamais d'après la seule couleur de son territoire. Le changement de nom ne change pas l'ID. *(Ether)*
- **Le nom à la date est porté dans l'état** (`proprietes.nom`) : la carte le lit en premier ; la fiche affiche ce nom et rappelle le nom actuel (« aujourd'hui : Košice »). *(Ether, fait par Claude)*
- **Košice → Cassovie** (sur place : Kassa, ville hongroise depuis novembre 1938) et **Ústí nad Labem → Aussig** au Snapshot 0. Les dates du retour aux noms d'après-guerre restent à prouver : une prise militaire ne date pas à elle seule un changement de nom. *(Ether)*
- **Fusion Miskolc–Diósgyőr datée du 01/01/1945** (Ether, PDF municipal p. 102) : deux points au Snapshot 0, fusion au ratissage de janvier, sans intervalle vide au 1er janvier. Page 102 hors de portée de l'outil de Claude : dans « Sources à valider ». *(Ether)*
- ~~Deux façons de nommer coexistent~~ : réglé le même jour, le lot 1.4 suit la forme du 1.3 (voir plus haut). *(Claude)*
- Sources : 6 relues (4 confirmées ; S44 p. 102 et l'article sur « Cassovie » illisibles pour Claude). Registre v1.13 ; « Sources à valider » : 114. *(Claude)*
- **Feature « régime routier »** (plaques, permis, signalisation, contrôles) : notée, à étudier vers la fin du Snapshot 0. Avis de Claude : commencer par le côté de conduite, pastille au cœur du territoire plutôt qu'à la capitale, zones de plaques bien plus tard. Note d'Ether conservée dans `docs/idees/`. *(Guizmo + Ether)*

## 2026-10-01 (suite : villes, ratissage 1.4 Pologne et pays baltes)

- **Villes 1.4 intégrées : 61 villes** (32 Pologne, 9 Estonie, 10 Lettonie, 10 Lituanie), depuis le JSON d'Ether. *(Ether, fait par Claude)*
- **Convention des capitales appliquée** : capitale régionale = siège administratif de fait sous occupation ou en RSS (Cracovie, Tallinn, Riga, Vilnius, comme Vienne et Prague) ; Varsovie nationale par continuité ; pas de capitale à Kaunas (entre-deux-guerres) ni à Lublin (administration provisoire, comme Debrecen). *(Ether + Claude, suit la règle validée par Guizmo pour Prague)*
- **Noms à la date** : Ether nomme au Snapshot 0 Litzmannstadt, Breslau, Stettin, Dantzig, Gotenhafen, Gleiwitz, Memel ; les autres formes sont des alias. La règle d'ensemble a été donnée par Ether le même jour (voir plus haut : preuve ville par ville). *(Ether)*
- Sources 1.4 : 58 relues (44 confirmées, 14 dans « Sources à valider »). Registre v1.12. *(Claude)*
- **Dossier d'échange** : Guizmo dépose les fichiers d'Ether dans le dossier Atlas du Bureau, auquel Claude a accès (plus besoin de les joindre à la conversation). *(Guizmo)*

## 2026-10-01 (suite : villes, ratissage 1.3 Tchéquie, Slovaquie, Hongrie)

- **Villes 1.3 intégrées : 53 villes** (19 Tchéquie, 16 Slovaquie, 18 Hongrie). Données tirées du document d'Ether (son JSON n'était pas joint). *(Ether, fait par Claude)*
- **Une ville réunie au Snapshot 0 = une seule entité** : Komárom (les deux rives, 1939–1945), Děčín–Podmokly (1942). **Une fusion datée du 01/01/1945 s'applique après 0 h** : Miskolc et Diósgyőr restent deux points au Snapshot 0. *(Ether)*
- **Prague = capitale régionale au Snapshot 0** (siège du Protectorat), par cohérence avec Vienne ; Bratislava et Budapest nationales ; Debrecen garde B avec « administration » (siège provisoire depuis le 21/12/1944). *(proposé par Ether et Claude, **validé par Guizmo** le 01/10/2026)*
- **JSON d'Ether reçu et rapproché (villes 1.3 v0.2)** : aucune différence avec l'extrait du document ; ses notes et ses preuves rôle par rôle sont reprises, « à renforcer » est calculé rôle par rôle (11 villes). Registre v1.11. *(Claude)*
- **Noms de villes sans chevauchement** : les points de toutes les villes visibles restent ; leurs noms se posent par ordre d'importance (capitales, puis A, B, C, D), à droite du point, sinon à gauche, sinon cachés jusqu'au zoom suivant. Les noms de pays évitent ensuite points et noms de villes. *(Guizmo, fait par Claude)*
- **Les noms allemands, hongrois et futurs sont des alias de recherche**, jamais des noms actifs en 1945 sans source sur le nom officiel. *(Ether)*
- Sources 1.3 : 53 relues par sous-agents (37 confirmées, 16 dans la file « Sources à valider »). Registre v1.10. *(Claude)*

## 2026-10-01 (suite : clôture du 1.2, validation humaine des sources)

- **RÈGLE PERMANENTE — la file « Sources à valider »** : tout point dont la vérification prendrait trop de temps sur le moment (source illisible pour Claude, lecture partielle, lien mort, preuve faible) va dans la page « Sources à valider » au lieu de bloquer l'avancée. C'est la file d'attente de la vérification de fond, à faire plus tard (temps libre, communauté, ou travail rémunéré si l'Atlas est financé). À chaque lot, Claude relit les sources, met à jour la liste et republie la page. *(Guizmo)*
- **Lots frontières 01 à 04 relus** : leurs 98 sources n'avaient pas encore de statut. Relecture par sous-agents : 61 confirmées, 17 en lecture partielle, 2 faibles, 17 illisibles pour Claude (cartes en image, loc.gov et sites protégés), 1 lien mort (PDF de la Chancellerie belge sur la bataille des Ardennes). Registre v1.9 ; la page « Sources à valider » passe à 83 sources (filtre Frontières / Villes). Détail : `data/sources/verifications_claude/2026-10-01_lots_frontieres_01-04.json`. *(Claude)*
- **Lot villes 1.2 clôturé** avec ses réserves visibles (45 villes « à renforcer » dans leur fiche). Le but reste le visuel ; la recherche, ce sont les sources, consultables par qui veut approfondir. *(Guizmo)*
- **Les points se consolident avec le temps** : chaque nouvelle trouvaille (autoroute, poste douanier, train, ville, port…) vient renforcer ou confirmer les points déjà posés ; une réserve n'est pas une impasse. *(Guizmo)*
- **Validation humaine des sources** : page « Sources à valider » (artifact claude.ai, privée) qui liste les sources que Claude n'a pas pu confirmer (46 au registre v1.8) ; Guizmo ouvre la page, vérifie le passage et clique « Ça prouve », « Ne prouve pas » ou « Lien mort ». Claude relit ces choix et les reporte au registre (`verification_humaine`, avec la date, sans extrait). Plus tard, la communauté pourra aider, avec des limites. Liste générée par `outils/sources/liste_sources_a_valider.py` → `data/sources/sources_a_valider.json`. *(Guizmo, fait par Claude)*

## 2026-10-01 (suite : second audit d'Ether sur les villes 1.2)

- **Villes 1.2 v0.3 : 73 villes** (+ Hamm, Ludwigshafen, Mayence, Schweinfurt, Augsbourg, Leuna, Watenstedt-Salzgitter, Leoben avec Donawitz, Osnabrück). Un site industriel n'est pas un second point urbain : Donawitz est dans Leoben, Mersebourg différée. *(Ether, fait par Claude)*
- **Le nom suit la date** : Bremerhaven s'appelle Wesermünde au Snapshot 0 (même ID, ancien nom en alias). Watenstedt-Salzgitter idem. *(Ether)*
- **Fabriquer n'est pas transporter** : Rostock perd `aviation` (Heinkel = industrie) tant qu'il manque une preuve de terrain ou de service aérien. *(Ether)*
- **Un point structurel peut rester affiché même si son service exact au 01/01/1945 n'est pas prouvé** (horaires, trafics inconnus) ; on ne déduit aucune liaison ou capacité de ces notices. *(Ether, appliqué par Claude)*
- **Preuves rôle par rôle** : l'`usage` de chaque source dit quels rôles elle prouve ; la note de la ville liste ce qui reste « à renforcer » (45/73). 75 sources nouvelles relues par Claude : 59 confirmées, 3 partielles, 13 illisibles pour lui (robots, pages en JavaScript) ; signalées à Guizmo. Registre v1.8. *(Claude)*
- **Vérification des sources par sous-agents** : pour les gros deltas, Claude répartit la relecture des liens entre plusieurs agents et garde leurs résultats dans un fichier de vérification. *(Claude)*

## 2026-10-01 (suite : retour d'audit d'Ether sur les villes 1.2)

- **Type de capitale et priorité d'affichage sont indépendants** : une capitale nationale peut être C, une ville non capitale peut être A ou B. Inscrit au lexique. *(Ether)*
- **Vaduz : A → C**, capitale nationale gardée ; source officielle ajoutée (commune de Vaduz). **Vienne : A et capitale régionale confirmées** ; le retour comme capitale nationale (repère du 27/04/1945) sera un état daté avec sa propre source. *(Ether, fait par Claude)*
- **Aix-la-Chapelle « évacuée et détruite » au 01/01/1945** : évacuation ordonnée, 5 000 à 20 000 habitants restés sur 165 000, plus de 80 % des bâtiments détruits (Modern War Institute, West Point). Ne prouve pas l'arrêt du réseau. **Magdebourg** : rien d'anticipé, la destruction du 16/01/1945 ira au ratissage de janvier. *(Ether, source trouvée par Claude)*
- **Ce qu'une source prouve** : source générale = contexte seulement ; page actuelle ≠ preuve historique ; « non vérifiée » reste visible. Chaque source de ville dit son `usage` réel ; 53 villes sur 64 portent « Rôle à sourcer localement ». La page de Graz sur les pompiers est retirée des preuves. Règles ajoutées au protocole des sources. Registre v1.7. *(Ether, fait par Claude)*
- **Lot 1.2 ouvert, pas verrouillé** : 9 candidats à examiner par Ether (Hamm, Ludwigshafen, Mayence, Schweinfurt, Augsbourg, Leuna/Merseburg, Salzgitter, Leoben/Donawitz, Osnabrück) et sources de remplacement attendues. *(Ether)*

## 2026-10-01 (villes, ratissage 1.2 Allemagne + arc alpin)

- **Villes 1.2 intégrées : 64 villes** (Allemagne actuelle, Autriche, Suisse, Liechtenstein), même modèle que les lots 1.0 et 1.1. Aucun rôle nouveau : fleuves → `port_fluvial`, corridors → `rail`, automobile/mécanique/chimie → `industrie`. *(Ether, fait par Claude)*
- **Vienne = capitale régionale au 01/01/1945** (Autriche annexée : on montre qui tient le terrain, le détail juridique va dans la fiche). Priorité A gardée en attendant l'avis d'Ether. *(Claude, à confirmer par Ether)*
- **Vaduz** : pas de source fournie → Wikidata en attendant une source officielle. Priorité A (proposition d'Ether) à rediscuter : micro-État, peu de flux. *(Claude, à confirmer)*
- **Sources 1.2 : 34 liens lus** → 15 confirmés, 11 limités (pages modernes ou hors sujet : Brême, Kiel, Vienne, Graz-rail, ÖBB Tauern et Arlberg, Steyr, Zurich-rail, ports rhénans, Winterthour, DB Museum général), 8 non vérifiables par Claude (Hambourg, Dortmund-industrie, Francfort Hbf, les deux pages de Lausanne, Olten, Winterthour-SLM, Gothard). Registre v1.6. Signalés à Guizmo (règle « source manquante »). *(Claude)*

## 2026-09-30 (suite : villes, ratissage 1.1 Nordiques)

- **Audit 1.1 appliqué (65 villes)** : Fredericia C → B (pont du Petit Belt, 1935, source vérifiée) ; ajouts Boden B, Hallsberg B, Oxelösund C, Gällivare C, Harstad C, Mo i Rana C, Lahti C, Kuopio C, Joensuu C ; différés Gedser, Malmberget (future entité mine), Örebro. Registre v1.5. *(Ether, fait par Claude)*
- **Sources non vérifiables par Claude** (serveur muet, PDF illisible, lien cassé ou lecture refusée) : Boden, Hallsberg, Gällivare, garnison de Harstad (404), les deux sources américaines sur l'Islande. Gardées et marquées dans le registre ; signalées à Guizmo (règle « source manquante »). *(Claude)*

- **Villes 1.1 intégrées : 56 villes** (Danemark, Féroé, Norvège, Suède, Finlande, Islande), même modèle que le lot 1.0. *(Ether, fait par Claude)*
- **Rôles ramenés au vocabulaire de l'Atlas** (les mots-clés d'Ether sont convertis au montage) ; nouveaux rôles : `minerai`, `peche`, `navigation_cotiere`, `militaire`. Les indications géographiques restent dans la note. *(Claude)*
- **Nouvelle propriété `situation`** d'une ville au jour affiché (`detruite`, `evacuee`) : point gris sur la carte, flux coupés. Kirkenes, Rovaniemi, Hammerfest au 01/01/1945. *(Ether + Claude)*
- **Sources : Claude lit chaque lien du delta avant fusion** et note le résultat dans le registre (`verification_claude` : ok / limite / faible / non_verifiee). Lot 1.1 : 29 confirmées, 4 limitées, 1 rétrogradée en C, 2 non vérifiées, 2 ajoutées par Claude (Bergensbanen, Nordlandsbanen). Registre v1.4. *(Claude)*

## 2026-09-30 (suite : villes, ratissage 1.0)

- **Méthode du ratissage villes** : lots géographiques avec la même grille, puis un audit global des trous. Ordre : 1.0 France, Benelux, îles Britanniques → 1.1 Nordiques → 1.2 Europe centrale et Allemagne → 1.3 Baltique et Pologne → 1.4 URSS jusqu'au Pacifique et Mongolie → 1.5 Caucase et Turquie → 1.6 Balkans, Grèce, Italie → 1.7 Ibérie → audit. *(Ether, validé par Guizmo)*
- **Nouveau type d'entité `ville`** (ID `ville-<pays>-<nom>`), un point. `importance_atlas` A/B/C/D = priorité d'affichage automatique par le zoom (A capitales dès le zoom 3,8 ; B zoom 5 ; C zoom 6,5 ; D zoom 7,5), jamais un réglage. `roles` en mots-clés (port_maritime, rail, industrie, frontalier…). *(Ether + Claude)*
- **Une ville ne porte ni souveraineté ni contrôle** : elle prend ceux du territoire où elle est, à la date affichée. *(Claude)*
- **Villes dans le temps** : `valid_from` inconnu = déjà en place avant l'Atlas ; un changement d'importance, de nom ou de rôle = un nouvel état daté. *(Ether)*
- **Positions des villes : Wikidata (CC0)**, QID gardé ; secours Natural Earth. Rôles à sourcer. *(Claude)*
- **Noms validés** : nom français traditionnel quand il existe réellement ; `nom_local` et `aliases` derrière, pour qu'on trouve Douvres en cherchant Dover. Un vrai changement de nom = un nouvel état de la ville. *(Ether)*
- **Sources des rôles** : par famille et par pays quand une source couvre plusieurs villes (histoire des ports, réseau ferroviaire national) ; une source propre pour un rôle particulier ou contestable (QG du SHAEF, principale base navale). Renforcées au fil des ratissages. *(Ether)*
- **Villes 1.0 complétées (73)** : Bruges (séparée de Zeebruges), Lorient, La Rochelle, Royan, Toulon, Versailles (QG du SHAEF), Den Helder, Groningue, Londonderry (alias Derry), Leeds, Sheffield, Aberdeen. Quand Ether hésite (« C/B »), la première lettre est retenue. *(Ether, fait par Claude)*
- **Une ville n'entre dans l'Atlas qu'à partir du moment où elle compte pour les flux** ; elle peut en sortir ou redescendre de priorité par un nouvel état daté. **Reims** est donc retirée du Snapshot 0 et entrera au ratissage de février 1945 (QG avancé du SHAEF). *(Guizmo)*
- **Source manquante** : quand Claude n'a pas de source pour un élément et ne la trouve pas lui-même, il le signale à Guizmo, qui la demande à Ether. Règle permanente. *(Guizmo)*
- **Canal officiel des sources Ether → Claude** : un fichier `*_sources_*_delta.json` par lot ; Claude vérifie chaque lien, fusionne au registre et garde le delta dans `data/sources/deltas_ether/`. Protocole : `docs/protocole_sources_ether_claude.md`. *(Ether + Guizmo)*
- **Delta villes 1.0 fusionné** (registre v1.3) : NARA RG 331 (SHAEF à Versailles), SHD (poches de l'Atlantique), ministère des Armées (Reims, février 1945), port de Den Helder vérifiés ; port d'Anvers-Bruges (Zeebruges) non vérifiable (page en JavaScript). *(Claude)*
- **Scapa Flow** n'est pas une ville (future entité base ou port). **Zeebruges** et **La Pallice** deviendront des entités port avec la couche infrastructures. *(Ether)*
- **Audit transversal à la fin de tous les lots villes** (ports, rail, frontières, industrie, capitales) avant de déclarer le ratissage villes terminé. *(Ether)*
- **« Repères actuels »** : le renommage du bouton « Aujourd'hui » est gardé pour plus tard. *(Guizmo)*

## 2026-09-30 (interface : la règle du temps)

- **Règle du temps en haut de la carte** : remplace le lecteur du bas (plus de bouton Lecture). Effet loupe (« œil de poisson ») au centre ; traits orange = mois, blancs = semaines (lundi), gris = jours ; verre fumé transparent, environ 70 px de haut. *(Guizmo, fait par Claude)*
- **Voyager** : glisser au doigt ou à la souris, molette (vers le bas = avancer), flèches du clavier (Maj = une semaine) ; toucher un trait = y aller ; toucher pendant le défilement = stop. *(Guizmo)*
- **Tempo de l'accélérateur** : coups enchaînés dans le même sens pendant que ça défile : 1-2 = jours, 3 à 5 = mois, 6 et plus = années ; le compteur repart à zéro à l'arrêt, après 1,5 s ou si on change de sens. À ajuster à l'usage. *(Guizmo)*
- **Sélecteur de date** (toucher la date) : l'année seule suffit (→ 1er janvier), le mois et le jour sont facultatifs (→ 1er du mois). *(Guizmo)*
- **Volet de gauche supprimé** : les commandes sont posées autour de la carte, en verre fumé. En bas, une barre **Mode · Couches · Calques · Filtres · Aujourd'hui**, un seul petit panneau ouvert à la fois ; la légende (palette) est dans « Mode ». En bas à gauche, le carré **Fond de carte**. En haut à gauche, le nom et le bouton « i » (tracés provisoires, petit lexique, et pour l'équipe : choix du corpus, zoom). Ce qui n'existe pas encore est affiché en gris « bientôt », prêt à brancher. *(Guizmo, fait par Claude)*
- **Vocabulaire : ajout de « fond de carte »** (plan, relief, vue naturelle, satellite, vue reconstituée), ni calque ni mode de lecture. Ajouté au récap technique, à faire valider par Ether. *(Guizmo + Claude)*
- **Idées premium gardées pour plus tard** (satellite, photos aériennes d'époque, vue reconstituée, flux en « veines ») : `docs/IDEES_POUR_PLUS_TARD.md`. *(Guizmo)*
- **Architecture de l'interface validée** : carte en plein écran, barre haute légère, commandes en bas, informations seulement à la demande. Le « i » global explique comment l'Atlas est fabriqué ; chaque objet cliquable (ville, frontière, flux) a ses propres sources. *(Ether)*
- **Une question en tête de chaque petit panneau**, pour que Couches et Calques ne se confondent pas : « Quels types d'histoire veux-tu explorer ? » (Couches), « Quels éléments veux-tu voir sur la carte ? » (Calques), et de même pour Mode, Filtres et Fond de carte. *(Ether, fait par Claude)*
- **Villes : pas de réglage « capitales seulement »**. L'affichage suit le zoom tout seul : Eurasie → noms des pays ; continent → capitales ; pays → grandes villes structurantes ; région → nœuds ferroviaires, ports, villes frontalières et industrielles ; local → petites villes pertinentes et micro-histoire. On peut seulement couper tout le calque Villes. *(Ether)*
- **Fond de carte, règle « pas de mensonge visuel »** : aérien et satellite historiques ne s'affichent que là où une image existe pour la date et la zone ; ailleurs l'Atlas garde Plan ou Relief. Liste : Plan, Relief, Vue naturelle, Aérien historique, Satellite historique, Carte d'époque (scan superposé), Vue reconstituée (annoncée comme telle). *(Ether + Guizmo)*
- **À trancher** : le nom du bouton « Aujourd'hui », qui peut faire croire qu'il ramène la date à aujourd'hui (pistes : « Repères actuels », « Comparer à aujourd'hui ») ; à tester sur quelqu'un qui ne connaît pas le projet. *(Ether)*
- **En pause** : la simplification des couleurs (« qui tient le terrain » en carte principale, le légal dans la fiche), à trancher ensemble. *(Guizmo)*

## 2026-09-29 (retour d'Ether sur le lot 04)

- **Validé** : Hongrie `axis_associe_ww2` ; Monaco `neutral_ww2` ; zone soviétique de Hongrie avec le gouvernement provisoire de Debrecen (Assemblée le 21/12, gouvernement le 22/12/1944) ; Transylvanie du Nord sous administration militaire soviétique ; est de la Slovaquie soviétique. *(Ether)*
- **Roumanie, Bulgarie, Italie = `anti_axis_non_allied`** : les retournements de 1944 ne valent pas adhésion pleine à la coalition alliée ; les différences passent par statut, contrôle, administration et notes. *(Ether)*
- **Yougoslavie découpée** : plus de contrôle partisan uniforme ; zone partisane (est) et zone allemande / oustachie (ouest) tirées du front de la carte West Point 31 ; au sud du bord de la carte, rattachement partisan par défaut (à sourcer) ; côte dalmate à affiner. *(Ether, fait par Claude)*
- **Tchécoslovaquie** : État slovaque (Tiso, occupé par l'Allemagne depuis l'insurrection d'août 1944) et sud annexé par la Hongrie (1938) en zones distinctes. **Italie du Nord** : zones d'opérations allemandes OZAK (littoral adriatique) et OZAV (Préalpes) d'après OHM. *(Ether, fait par Claude)*
- **Grèce** : Milos (garnison allemande jusqu'au 09/05/1945, Musée de la guerre de Milos) tracée ; Crète occidentale sans tracé (limites non sourcées) ; Grèce en « contrôle non tranché ». *(Ether + Claude)*
- **Affichage** : rayures croisées grises = souverain connu, contrôle réel non tranché ; hachures colorées selon le camp du **souverain** de l'occupant (ex. Hongrie → brun) ; de près, l'étiquette d'un pays presque entièrement couvert par ses zones s'efface ; un clic choisit la zone la plus précise. *(Claude)*

## 2026-09-28 (suite : lot 04, Sud, Centre, Balkans, Turquie)

- **Lot 04 intégré** : 29 entités (Espagne, Portugal, Andorre, Gibraltar, Suisse, Monaco, Vatican, Italie et ses zones, Tchécoslovaquie et ses zones, Hongrie et ses zones, Roumanie, Transylvanie du Nord, Bulgarie, Yougoslavie, Albanie, Grèce, Turquie entière, Malte, Chypre, front d'Italie). 28 tracés ; Athènes–Le Pirée sans géométrie (pas de carte datée). *(Ether, intégré par Claude)*
- **Lecture juridique alliée** : Tchécoslovaquie d'avant Munich, Hongrie du Trianon, Yougoslavie et Grèce d'avant-guerre, Italie de 1939 (+ Dodécanèse), Roumanie de septembre 1940 ; la Transylvanie du Nord est une zone à part (annulation de l'arbitrage de Vienne par l'armistice, mais retour roumain le 09/03/1945 seulement). *(Claude, à valider)*
- **Fronts d'avant le Snapshot** : Italie = West Point 51 (« 31 Dec. », carte stylisée, ≈ 10 km) ; Hongrie, Tchécoslovaquie, Yougoslavie = West Point 31 (« 31 Dec. »), dont l'anneau de Budapest encerclée. En Yougoslavie, pas de zones tirées du front (contrôle partisan / allemand / NDH trop morcelé sans carte datée). *(Claude)*
- **Un acteur = un ID** appliqué au lot 04 (gouvernement Hoxha, régence grecque, RSI en regime_id ou administration_id) ; « allies » → `allies_occidentaux` ; « conteste » → contrôle absent. Colonies britanniques : code propre (`gi`, `mt`, `cy`). *(Claude)*
- **Nouveau statut particulier `pro_allied_armed_neutral`** (Turquie, ivoire). *(Ether)*
- **Propositions à valider** : Hongrie `axis_associe_ww2` au lieu d'`axis_ww2` ; Monaco `neutral_ww2` ; zones soviétiques de Hongrie et de Tchécoslovaquie, Budapest encerclée, Dodécanèse allemand, Transylvanie du Nord ; statut commun Roumanie / Bulgarie. *(Claude)*
- **Affichage** : géométries re-validées après arrondi (un polygone invalide dessinait un triangle parasite en Belgique) ; étiquettes des micro-États seulement de très près ; calcul du point d'étiquette accéléré. *(Claude)*

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
