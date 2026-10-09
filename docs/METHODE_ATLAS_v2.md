# Atlas Eurasie — Méthode de ratissage v2

*v2.1 du 09/10/2026 : ajustements demandés par Ether après relecture (grille des 30 filtres, objets multimodes, importance distincte de la portée, définition des zones, volumes = cases de travail, repérage avec indice de confiance, rattachement au protocole de boucle, exemple de Parndorf corrigé).*
*v2 du 08/10/2026. Version validée par Guizmo dans sa conversation avec Claude, relue par Ether (avis : garder la v2, préciser ces points, tester les subdivisions françaises avant d'étendre). Remplace la « Méthode de ratissage v1 » d'Ether (07/10/2026), dont elle garde tout ce qui était solide : règles de preuve, réservoir, raccordements aux frontières, livrables.*
*Statut : **rien n'est lancé**. Le passage aux subdivisions (phase 2) et aux campagnes (phase 3) demandera un feu vert explicite de Guizmo.*

---

## 1. Le vocabulaire (un mot = un rôle)

| Mot | Ce que c'est | Change avec le temps ? |
|---|---|---|
| **Zone** | Découpage **de travail**, fixé une fois pour toutes sur les frontières de 2026 (61 zones, voir §6). Sert seulement à savoir **où chercher**. Code = code du pays actuel (`FR`, `PL`, `RU`…), le même que dans les identifiants des villes. | Jamais |
| **Groupe** | Regroupement de zones voisines pour la chronologie (10 groupes, §6). | Jamais |
| **Territoire** | Ce qu'on **dessine** sur la carte à une date : la France de 1945, la Prusse-Orientale, une poche allemande, une république soviétique… | Oui, par états successifs |
| **État** | À **qui** appartient le territoire (souveraineté) et qui le **tient** réellement (contrôle). Ce sont deux informations de la fiche du territoire. | Oui |
| **Subdivision** | Région, département, oblast, Gau… : un territoire plus petit à l'intérieur d'un autre. | Oui |

- Le mot « pays » n'est plus utilisé dans les données (il mélange tout) ; il reste dans l'interface, pour le public.
- Le code dans un identifiant (`ville-ru-kaliningrad`) est une **adresse stable**, comme un code postal : il ne dit rien de l'histoire. La fiche, elle, dit « Königsberg, Reich allemand » au 01/01/1945.
- Le lien entre 1945 et aujourd'hui, c'est **le territoire qui change d'état** : la Prusse-Orientale (Reich, janvier 1945) → nord à l'URSS (1946, Kaliningrad) → Russie (1991). Même bout de terre, plusieurs états successifs.

## 2. Ce qu'on enregistre : deux sortes d'objets

1. **Objets durables**, avec des **états datés** : ville, route, ligne de chemin de fer, gare, port, canal, poste de douane, station-service… et aussi **une règle** (une loi est en vigueur pendant une période, puis change ou disparaît).
2. **Événements** : des faits datés en un lieu (ouverture d'une ligne, bombardement, accident, contrôle, drame humain…).

Un objet ou un événement a **une seule fiche et un seul identifiant**, même s'il est rencontré dans plusieurs campagnes (pont frontalier, traversée, événement transfrontalier).

**Objets multimodes** (pont route-rail, gare maritime, terminal port-rail, bac transportant des trains…) : une seule fiche, avec **une campagne responsable** (celle qui crée et tient la fiche) et une liste de **modes concernés** (`modes : [C2, C3]`). La fiche reste trouvable dans chaque catégorie concernée ; les autres campagnes la réutilisent sans la recréer.

## 3. Comment on le classe : catégories + thèmes + portée

**Catégorie = le mode de circulation** (une catégorie principale par objet ou événement) :

| Code | Catégorie | Contenu |
|---|---|---|
| C1 | **Eau** | Ports maritimes et fluviaux, fleuves navigables, canaux, écluses, ferries et traversées, acteurs du transport par eau. |
| C2 | **Terre** | Axes routiers, ponts, tunnels, cols, raccordements, douanes routières, péages, carburant, aires, restaurants routiers, hébergement, véhicules, entreprises et vie des routiers. |
| C3 | **Fer** | Grandes lignes, gares voyageurs, gares de marchandises, triages, terminaux, raccordements industriels et portuaires, passages internationaux, exploitants. |
| C4 | **Règles** | Cadre territorial, règles de circulation, réglementation professionnelle, douanes et accords, rationnement, carburant, immatriculations, règles environnementales quand elles apparaissent. |
| C5 | **Air** | Réservé, différé : activé plus tard par une décision explicite (sans renuméroter C1 à C4). |

**Thèmes = étiquettes transversales**, autant que nécessaire : industrie et logistique, marchandises, militaire, **migrations**, tourisme et voyageurs, accidents, criminalité, contrôles et bilans, perturbations. Les thèmes ne créent pas de campagnes en plus : ils se posent pendant les campagnes.

Chaque événement porte deux mesures **distinctes** :
- **Portée** = jusqu'où il s'étend : locale, régionale, nationale, internationale ;
- **Importance** = son poids pour les circulations : majeure, notable, mineure (justifiée par les sources et les conséquences, pas par la portée : un événement local peut être majeur, un événement international peut être mineur).

La vue d'ensemble montre les événements majeurs ; les milliers d'autres apparaissent au zoom ou par filtre de thème.

**Qualification et dates sourcées.** La nature d'un événement (accident, crime, attentat…) n'est posée que si une source la donne. On distingue, quand elles diffèrent, la **date des faits**, la **date de la découverte** et la **date du signalement ou du jugement**.

> **Exemple : Parndorf.** Le 27/08/2015, un camion contenant les corps de 71 migrants est découvert sur l'autoroute A4, près de Parndorf (Autriche).
> Événement · catégorie **Terre** (A4, camion) · thèmes **migrations, criminalité (passeurs)** ; l'étiquette « accident » n'est **pas** posée sans source qui la justifie · portée internationale · importance à établir · lieu : A4 près de Parndorf · **date de la découverte : 27/08/2015** ; date des faits : à établir par les sources (récit de l'ORF : https://burgenland.orf.at/magazin/stories/3171201/).
> Seul, c'est un fait divers. Cumulé à des milliers d'autres sous le thème « migrations », il dessine la route des Balkans de 2015 : c'est la **lecture de données** que l'Atlas veut permettre.

### Grille de contrôle : les 30 filtres

Les catégories organisent le travail ; **la grille des 30 filtres sert à vérifier la couverture**. Chaque table de couverture (§9) reprend ces 30 lignes : aucun sujet ne peut disparaître sans laisser de trace.

| N° | Filtre | Rangé dans |
|---|---|---|
| 1 | Régions | Subdivisions (phase 2) + C4 |
| 2 | Départements et équivalents | Subdivisions (phase 2) + C4 |
| 3 | Axes routiers | C2 Terre |
| 4 | Ponts, tunnels, cols routiers | C2 Terre |
| 5 | Installations frontalières routières (règles : C4) | C2 Terre |
| 6 | Péages | C2 Terre |
| 7 | Lignes ferroviaires | C3 Fer |
| 8 | Gares voyageurs | C3 Fer |
| 9 | Fret, triages, terminaux | C3 Fer |
| 10 | Ports maritimes | C1 Eau |
| 11 | Ports fluviaux | C1 Eau |
| 12 | Voies navigables, canaux, écluses | C1 Eau |
| 13 | Liaisons, ferries, traversées | C1 Eau |
| 14 | Ravitaillement routier (carburant, dépôts) | C2 Terre |
| 15 | Aires, parkings | C2 Terre |
| 16 | Vie des routiers (repas, repos, couchage, durée des trajets) | C2 Terre |
| 17 | Organisation du transport routier, entreprises, véhicules | C2 Terre |
| 18 | Industrie et logistique | Thème transversal |
| 19 | Règles générales de circulation | C4 Règles |
| 20 | Règles professionnelles | C4 Règles |
| 21 | Plaques d'immatriculation ordinaires | C4 Règles |
| 22 | Plaques particulières (militaires, diplomatiques, temporaires…) | C4 Règles |
| 23 | Marchandises | Thème transversal |
| 24 | Circulations militaires | Thème transversal |
| 25 | Migrations | Thème transversal |
| 26 | Tourisme et voyageurs | Thème transversal |
| 27 | Accidents | Thème transversal |
| 28 | Criminalité | Thème transversal |
| 29 | Contrôles des autorités et bilans | Thème transversal |
| 30 | Perturbations (grèves, intempéries, destructions…) | Thème transversal |

Les thèmes transversaux sont examinés dans chaque catégorie où ils comptent ; ils ne créent pas de campagne à part.

## 4. Les phases

### Snapshot 0 = l'état au 01/01/1945, 0 h

| Phase | Contenu | État |
|---|---|---|
| **0.x** | Frontières et territoires (74 territoires) | fait |
| **1.x** | Villes (1 559 villes, 10 lots + audit) | fait ; revue des réserves et sources importantes en cours |
| **2.x** | **Subdivisions** de 1945 (régions, départements, Gaue, oblasts…), par zone | prochaine étape, feu vert à donner |
| **3.x** | **Campagnes** zone × catégorie (C1 à C4) : réseaux et règles en vigueur au 01/01/1945 | après les subdivisions |

- Pas d'**événements** dans le Snapshot 0 : c'est une photo de l'état. Ce qui s'est passé avant et explique l'état de 1945 va dans les notes des fiches.
- **Pilote : la France** (puis les autres zones, groupe par groupe). Elle est idéale pour tester la séparation souveraineté / contrôle : Alsace-Moselle annexée de fait, poche de Colmar, poches de l'Atlantique (Lorient, Saint-Nazaire, La Rochelle, Dunkerque).
- **Deux passes de détail** dans une campagne : d'abord le structurant (grands axes, grandes lignes, grands ports), ensuite le détail (stations, aires, restaurants routiers, vie des routiers).

### Chronologie (après le Snapshot 0)

Trois mécanismes, pour ne jamais supposer qu'une période est « calme » ou « agitée » :

1. **Les dates restent toujours exactes.** Le pas de temps sert seulement à découper le travail de recherche, jamais la précision de la carte (Parndorf garde son 27/08/2015).
2. **Liste des jalons majeurs**, établie à l'avance par zone à partir de chronologies de référence (traité de Rome, Mur de Berlin, fin de l'URSS, Schengen…). Ils sont **toujours traités**, quel que soit le volume de la période : une année « vide » ne peut pas cacher un grand événement.
3. **Repérage, puis détail.**
   - **Repérage** : pour chaque année, une passe rapide par groupe × catégorie qui **compte** ce qu'il y a à faire et où (sans remplir de fiches). Il donne aussi un **indice de couverture et de confiance** : quelles sortes de sources ont été consultées (archives, presse, chronologies, études), combien, dans quelles langues, et une confiance bonne / moyenne / faible.
   - **Prudence** : une recherche rapide mesure ce qu'on a **trouvé**, pas tout ce qui **existe**. Une année peu documentée n'est pas une année calme.
   - **Détail** : le pas découle de ce comptage **et** de la confiance, **groupe par groupe et catégorie par catégorie** : beaucoup → au mois ; un peu → au trimestre ; presque rien **avec une confiance bonne** → l'année d'un coup. Avec une confiance faible, on ne descend jamais à « l'année d'un coup » : au moins le trimestre, et la case est signalée pour une recherche complémentaire.
   - **Importance** (un seul grand événement) et **volume** (des milliers de petits faits) sont deux mesures distinctes : les jalons garantissent la première, le repérage mesure la seconde.

À chaque pas : **changements d'état** des objets durables (ouverture, fermeture, destruction, reconstruction, changement de tracé ou d'exploitation, nouvelle règle, changement territorial) **et** nouveaux **événements**. Séparer, quand elles diffèrent, les dates de décision, de travaux, d'ouverture et d'entrée en vigueur. Un changement de frontière ne crée pas une nouvelle route : on garde l'objet et on lui ajoute un état.

## 5. Avancer par paliers, avec un bilan chiffré à chaque palier

1. **Snapshot 0** complet (subdivisions + campagnes).
2. **1 an au mois : 1945** (l'année la plus chargée). Bilan : temps et coût réels d'une campagne, gain apporté par le repérage.
3. Décision sur ces chiffres réels → **5 ans**, puis **10 ans**, puis la suite. Ces mesures servent aussi au dossier de financement.

**Cases de travail** (combinaisons zone ou groupe × catégorie × pas de temps). Ce sont des **cases, pas une mesure de la charge** : elles ne comptent ni les subdivisions, ni les sous-lots, ni les deux passes de détail, ni les audits, ni les corrections, ni les allers-retours avec Claude. Elles ne permettent donc pas encore de chiffrer le temps ou le coût : **c'est le pilote France, puis l'année 1945, qui mesureront ces écarts.**

| Étape | Cases |
|---|---|
| Reste du Snapshot 0 | subdivisions (61 zones) + 61 zones × 4 catégories = **244** campagnes |
| Repérage | 10 groupes × 4 catégories = **40 passes par an** |
| 1 an au mois | 12 × 10 × 4 = **480** |
| 5 ans au mois | **2 400** |
| 10 ans au mois | **4 800** |
| 1945 → 2026 tout au mois (référence) | environ **38 800** |

Avec l'air (C5), multiplier par 5/4. Ether peut regrouper « un groupe × un mois × les 4 catégories » dans une seule livraison.

## 6. Zones et groupes (proposition, à figer avec Ether)

**Carte de référence des zones** : les limites des pays de *Natural Earth* (couche « admin 0 », échelle 1:10 m, domaine public), la même famille de données que le fond de carte de l'Atlas. La version utilisée est notée une fois et ne change plus.

**Règles pour les cas particuliers :**
- **Code** = code ISO 3166-1 alpha-2 du pays ou de la dépendance (`FR`, `JE`, `FO`…). Une dépendance qui a son propre code a sa propre zone (JE, GG, FO, GI ; et IM, SJ ci-dessous).
- **Territoires disputés ou non reconnus** (Crimée, Transnistrie, Abkhazie, Ossétie du Sud, Karabakh, nord de Chypre, Kosovo…) : rangés dans la zone de l'État membre de l'ONU dont ils relèvent selon la reconnaissance internationale majoritaire, **uniquement comme repère de travail** ; la fiche de zone le signale, et l'histoire du territoire est décrite dans ses états, sans prendre parti.
- **Marges différées** : signalées par le bilan des villes. Elles ont une zone, avec le statut « différée » tant qu'elles ne sont pas traitées, pour que la couverture reste honnête :
  - **IM** île de Man → G01 ;
  - **SJ** Svalbard et Jan Mayen → G02.
- **Hors périmètre** : tout ce qui n'est pas dans la liste ci-dessous. Une liste explicite des voisins hors périmètre (avec la raison) sera écrite avec Ether, pour qu'aucune zone ne soit oubliée sans le dire.
- Les 61 zones forment la grille de travail ; elles ne sont pas automatiquement une couverture complète : chaque zone a un statut (à faire, en cours, close avec lacunes, différée).

| Groupe | Zones (codes actuels) |
|---|---|
| G01 Ouest | FR, GB, IE, BE, NL, LU, JE, GG, IM, MC |
| G02 Nord | SE, FI, NO, DK, IS, FO, SJ |
| G03 Centre | DE, PL, CZ, HU, SK, CH, AT, LI |
| G04 Baltique | LV, LT, EE |
| G05 Est | RU, UA, BY, MD |
| G06 Asie centrale et Mongolie | KZ, UZ, MN, KG, TM, TJ |
| G07 Caucase et Turquie | TR, GE, AZ, AM |
| G08 Balkans | BG, RO, BA, RS, HR, AL, ME, MK, SI |
| G09 Italie et Méditerranée | IT, GR, CY, MT, VA, SM |
| G10 Ibérie | ES, PT, AD, GI |

- Chaque zone appartient à **un seul** groupe. Les grandes zones (RU, par exemple) peuvent être divisées en secteurs sans créer de nouvelles zones.
- Chaque fiche de zone liste **les États présents dans la zone au 01/01/1945** (zone PL : Reich allemand — Breslau, Stettin, Dantzig —, Gouvernement général, URSS à l'est), pour chercher dans les archives de chacun et ne pas regarder 1945 avec les frontières de 2026.
- **Aux frontières** : chaque campagne traite jusqu'au point de passage et le note ; l'audit vérifie que les deux bouts se rejoignent.
- À vérifier : Liechtenstein et Saint-Marin ont des villes mais pas de territoire à leur nom dans la couche de 1945.

## 7. Identifiants des lots (courts et lisibles)

| Quoi | Format | Exemple |
|---|---|---|
| Subdivisions (S0) | `2.<zone>` | `2.FR` |
| Campagne (S0) | `3.<zone>.C<n>` | `3.FR.C1` (France, eau) ; sous-lot : `3.FR.C2-L01` |
| Repérage | `R<année>.G<nn>.C<n>` | `R1945.G01.C3` |
| Détail au mois | `M<année>-<mois>.G<nn>.C<n>` | `M1945-01.G01.C3` |
| Détail au trimestre / à l'année | `T<année>-<t>…` / `A<année>…` | `T1951-2.G02.C1`, `A1953.G06.C4` |

Les lots déjà faits gardent leurs noms (`villes_1-x`, frontières `lot01` à `lot04`). Les dossiers d'échange suivent le même nom (`01_lots/3.FR.C1/`).

## 8. Règles de preuve (reprises de la v1)

- On distingue : infrastructure **existante**, effectivement **praticable**, **usage documenté**, **importance estimée**. Un tracé ne prouve ni le passage d'un convoi ni un volume de trafic.
- On ne projette jamais en 1945 un tracé, un numéro de route, une frontière, une règle, un exploitant ou un service d'aujourd'hui.
- On n'invente jamais une date précise ; on garde la précision réelle et les incertitudes.
- Ce qui ouvre après la date de référence va dans le **réservoir** (pas dans l'état actif) ; un chantier en cours peut être décrit comme tel.
- Pour chaque thème : présent et documenté / absence établie / non applicable / à vérifier. **Une absence de résultat n'est pas une inexistence.** On garde tous les thèmes dans la grille, même vides en 1945.
- On ne crée pas une ligne commerciale régulière à partir du seul fait que deux ports échangent des marchandises.
- Les sources restent **dans leur langue d'origine** ; la fiche de lecture en français (ce que dit la source, où le lire, facilitateur de traduction) est faite à l'audit puis à chaque lot.
- Pour l'industrie : seulement ce qui explique un transport, un approvisionnement ou un réseau.

## 9. Livrable de chaque campagne

1. **En-tête** : identifiant, date ou période, zone ou groupe, catégorie, version de la méthode, statut.
2. **Table de couverture** : tous les thèmes applicables, ce qui a été trouvé, les lacunes, les motifs de non-applicabilité ou les preuves d'absence.
3. **Objets durables** : identifiants existants réutilisés, états datés, géométrie justifiée, sources.
4. **Événements** (chronologie) : date, lieu, catégorie, thèmes, portée, conséquences sur les circulations.
5. **Sources** : selon le protocole du projet (`protocole_sources_ether_claude.md`).
6. **Réservoir** : faits postérieurs, pistes, points à reprendre avec une zone voisine.
7. **Bilan** : ce qui a été examiné, ce qui manque, raccordements à vérifier, prochaine campagne.

Statuts : à faire · en cours · à valider · clos avec lacunes documentées · différé (air). On ne déclare pas un thème clos parce qu'une recherche rapide n'a rien donné.

## 9 bis. Exécution : le protocole de boucle reste la règle

Cette méthode décrit **le contenu**. **L'exécution** reste gouvernée par les protocoles existants, sans changement :
- côté Ether : `coordination/BOUCLE_LIVRAISON_RATISSAGE.md` (livraisons vérifiées, `PRET_ether.md`, `STATUT.json` par lot) ;
- côté Claude : `docs/BOUCLE_AUTOMATIQUE.md` (intégration, vérification des sources, comptes rendus, `PRET_claude.md`, envoi sur GitHub) ;
- retours de Claude par lot, questions numérotées, **réserves** gardées pour la revue finale, **plafond de 3 cycles** d'allers-retours par lot, **arrêt après l'audit** de chaque phase ;
- **feu vert de Guizmo** pour ouvrir chaque phase (2.x, 3.x, chronologie) et chaque palier (1, 5, 10 ans) ;
- protocole des sources (`protocole_sources_ether_claude.md`) et page « Sources à valider ».

Pour préparer la France, on traite d'abord, parmi les sources à valider, celles dont dépend son découpage historique.

## 10. Avant de lancer (ordre des actions)

1. Guizmo et Ether relisent cette méthode ; les ajustements vont dans le journal des décisions.
2. Figer la liste des zones et des groupes (§6) et les fiches de zone (États présents en 1945).
3. Définir avec le lexique du projet les nouveaux types d'objets (subdivision, route, ligne, gare, port, poste de douane, règle…) et le gabarit d'événement (catégorie, thèmes, portée), sans modifier le schéma au hasard.
4. **Feu vert de Guizmo** pour la phase 2 (subdivisions), pilote France.
5. Après la France : bilan, ajustement de la méthode, puis extension groupe par groupe.
