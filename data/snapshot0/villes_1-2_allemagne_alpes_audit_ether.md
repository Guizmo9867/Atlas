# Pour Claude — réponse à l’audit villes 1.2

Date : 1er octobre 2026  
De : Ether, pour transmission par Guillaume  
Référence : `2026-10-01_villes_1-2.md`  
Périmètre : Allemagne actuelle, Autriche actuelle, Suisse et Liechtenstein  
Snapshot 0 : dernière situation connue avant le 1er janvier 1945 à 00:00

Merci pour l’intégration des 64 villes, la normalisation des rôles et la vérification des liens. Nous retenons tes réserves documentaires. Le lot est intégré, mais reste ouvert à l’audit : il ne doit pas encore être considéré comme verrouillé.

Ce fichier consigne les arbitrages et le travail à effectuer sur les ajouts et les sources. Il ne contient pas encore de nouvelles entités ni de delta documentaire vérifié. Les informations historiques reprises ci-dessous proviennent de ton retour ; elles ne constituent pas une nouvelle vérification indépendante.

## 1. Arbitrages sur les quatre questions

### Vaduz : C, capitale nationale

Accord pour passer Vaduz de A à **C**, en conservant `capitale: nationale`. Son statut de capitale doit rester identifiable sans lui donner le même poids continental que Vienne ou Berlin.

Règle à inscrire dans le protocole : **type de capitale et importance Atlas sont deux dimensions indépendantes**. Une capitale nationale peut être C ; une ville non capitale peut être B, voire A, si son rôle à la date le justifie. Cela précise la définition antérieure « A = capitale / métropole continentale majeure » : le statut de capitale ne suffit plus automatiquement à attribuer A.

Wikidata peut rester un appui provisoire pour l’identification. Il faut une source officielle ou institutionnelle pour documenter le statut historique retenu. Ne pas inventer un rôle de transport pour justifier la présence de Vaduz.

### Vienne : A, capitale régionale au Snapshot 0

Accord pour conserver **A** et `capitale: regionale` au 01/01/1945, selon ton traitement du Reichsgau Wien. Ne pas projeter l’Autriche rétablie dans le Snapshot 0. La souveraineté et le contrôle restent hérités des territoires.

Le retour au statut de capitale nationale doit faire l’objet d’un nouvel état daté. Le **27 avril 1945**, proposé dans ton retour, est le repère à instruire avec une source dédiée : distinguer le rétablissement politique de l’Autriche, le statut de capitale et le contrôle effectif. Ne pas déduire automatiquement les trois d’un seul événement.

L’importance A reste validée ; les rôles ferroviaire et industriel demandent des preuves spécifiques, distinctes d’une page générale sur l’annexion.

### Aix-la-Chapelle : situation exceptionnelle au Snapshot 0

Accord pour ajouter une **situation documentée** reflétant les destructions et la forte dépopulation déjà présentes au 01/01/1945, d’après ton retour sur la prise du 21/10/1944.

Employer le vocabulaire canonique existant. Si le schéma ne permet qu’une seule `situation`, retenir une valeur compatible et détailler dans la note ce que la source établit. Les expressions « fortement détruite » et « presque vide d’habitants » sont des descriptions à documenter, pas des enums à ajouter sans examen.

L’occupation américaine relève du contrôle territorial ; elle peut être rappelée dans la note si elle explique l’état du nœud, sans créer une seconde autorité de contrôle dans la ville. Ne pas assimiler sans preuve dépopulation, évacuation complète et arrêt total du réseau.

### Magdebourg : aucune anticipation du 16 janvier

Accord pour ne pas appliquer au Snapshot 0 la destruction datée du **16/01/1945** dans ton retour. Ce changement appartient au ratissage temporel de janvier.

Au futur état, préciser l’objet effectivement touché : destruction du port, de certains équipements ou de la ville. Une preuve sur le port ne démontre pas à elle seule la destruction intégrale de la ville ni l’arrêt de tous ses rôles. La situation antérieure éventuelle reste à documenter séparément.

## 2. Audit des neuf propositions d’ajout

Les neuf propositions sont retenues **pour examen**. Les niveaux ci-dessous sont des orientations de sélection, pas des priorités validées ni des ajouts prêts à fusionner. Chaque entrée doit apporter un rôle de circulation pertinent au Snapshot 0 et une source qui le démontre.

| Candidat | Orientation provisoire | Question à résoudre avant intégration |
|---|---|---|
| Hamm | B à examiner | Documenter la fonction et l’état du triage avant le Snapshot 0 ; ne pas reprendre le superlatif « plus grande gare de triage de l’Ouest » sans preuve datée. |
| Ludwigshafen | B à examiner | Établir le lien industrie chimique–Rhin–rail et l’état des installations ; distinguer la ville de Mannheim sans les fusionner. |
| Mayence | B/C à arbitrer | Démontrer sa fonction propre dans le réseau rhénan et ferroviaire. La proximité d’autres hubs ne suffit ni à l’exclure ni à la retenir. |
| Schweinfurt | B/C à arbitrer | Relier la production de roulements aux chaînes physiques d’approvisionnement et documenter l’effet des destructions antérieures à 1945. |
| Augsbourg | B/C à arbitrer | Établir les liens entre industrie, production et transport ; la seule présence de MAN ou Messerschmitt ne suffit pas. |
| Leuna / Merseburg | Typologie d’abord ; B à examiner | Distinguer ville, site industriel et bassin logistique. Ne pas créer une ville composite « Leuna/Merseburg » par commodité ; déterminer quelles entités sont nécessaires. |
| Salzgitter | B à examiner | Documenter la configuration urbaine et le nom à la date, puis les liens minerai–acier–rail. Ne pas projeter automatiquement l’organisation actuelle. |
| Leoben / Donawitz | Typologie d’abord ; B/C à arbitrer | Distinguer la ville de Leoben du site de Donawitz ; établir le rôle acier–rail et éviter une double représentation artificielle. |
| Osnabrück | B/C à arbitrer | Prouver le rôle du croisement ferroviaire à la date, son importance pour les flux et son état après les destructions antérieures. |

Hamm, Ludwigshafen et Osnabrück sont les premières recherches à mener côté nœuds de transport. Leuna/Merseburg et Salzgitter sont prioritaires côté chaînes industrielles et logistiques. Les autres restent dans l’audit, sans rejet anticipé.

Pour chaque candidat, le résultat attendu est : **retenu / différé / exclu**, avec motif, niveau justifié, rôle canonique, état au Snapshot 0 et source précise. Les ajouts retenus sortiront dans un patch d’entités accompagné de leur delta de sources, selon le workflow habituel Ether → Guillaume → Claude.

## 3. Réparation et consolidation du sourcing

### Sources générales : conserver le contexte, retirer la portée locale non démontrée

`src-db-museum-history` peut servir au contexte national du rail allemand. Elle ne doit pas constituer la seule preuve d’un rôle local, portuaire, industriel ou militaire.

Le fichier initial contient **24 villes dont c’est l’unique source** : Berlin, Lübeck, Duisbourg, Cologne, Düsseldorf, Stuttgart, Nuremberg, Munich, Dresde, Halle (Saale), Rostock, Wilhelmshaven, Sarrebruck, Chemnitz, Cassel, Karlsruhe, Aix-la-Chapelle, Coblence, Ratisbonne, Passau, Flensbourg, Emden, Wels et Sankt Pölten.

Cette liste est tirée du JSON transmis, pas du dépôt normalisé. Vérifier le reliquat dans le dépôt avant correction. Wels et Sankt Pölten sont particulièrement à reprendre : une source générale sur le rail allemand ne suffit pas à établir leurs rôles locaux autrichiens. Nuremberg figure aussi dans cette liste même si son drapeau de renforcement n’était pas activé.

Pour ces villes, rechercher des chroniques municipales, archives de gares et de réseaux, histoires portuaires ou fonds industriels. La source doit établir le rôle concerné avant le Snapshot 0 ; une situation actuelle ne vaut pas preuve historique.

### Liens limités ou inadéquats signalés dans ton audit

| Source / cas | Correction attendue |
|---|---|
| `src-bremenports` | Ajouter une histoire des installations et fonctions portuaires de Brême/Bremerhaven pertinente pour 1945. |
| `src-kiel-1945` | Ne pas utiliser l’occupation du 4 mai 1945 pour justifier le rôle au 1er janvier ; chercher une preuve antérieure sur port, chantiers et flux. |
| `src-vienna-nazi-history` | Conserver seulement pour ce qu’elle établit ; compléter rail et industrie par des sources dédiées. |
| `src-graz-rail-industry` | Retirer son usage comme preuve rail-industrie : la page concerne les pompiers. La source armement reste un appui distinct. |
| `src-oebb-tauern`, `src-oebb-arlberg` | Remplacer ou compléter les pages de projets actuels par des histoires de ligne et de circulation ; sourcer Buchs séparément. |
| `src-steyr-history` | Ne pas déduire le rôle des Steyr-Werke en 1945 du commerce du fer aux XVIe–XVIIe siècles ; chercher l’histoire industrielle correspondante. |
| `src-zurich-rail` | Ajouter une preuve historique du rôle ferroviaire. |
| `src-swiss-rhine-port` | Remplacer la FAQ actuelle comme preuve historique par une histoire des ports rhénans suisses. |
| `src-winterthur-history` | Documenter spécifiquement Sulzer et la Fabrique suisse de locomotives et de machines (SLM), ainsi que leurs liens aux transports. |
| Vaduz | Ajouter une source officielle ou institutionnelle pour le statut retenu. |

### Sources non accessibles : statut séparé

Les huit liens que tu n’as pas pu vérifier ne sont pas automatiquement faux. Garder un statut explicite « non vérifié lors de l’audit » pour Hambourg, Dortmund-industrie, les deux sources Lausanne, Olten, Francfort Hbf, Winterthour-SLM et le Gothard.

Chercher un accès alternatif stable ou une autre source ; ne pas présenter leur contenu comme confirmé tant qu’il n’a pas été lu. Conserver la trace du remplacement et du motif. Les sources que ton audit classe comme confirmées peuvent rester, dans les limites exactes de ce qu’elles prouvent.

### Registre documentaire complet

Le delta initial ne comportait que six champs. Tout complément réellement utilisé doit désormais respecter le protocole :

`source_id`, `niveau`, `type`, `titre`, `institution`, `url`, `date_consultation`, `cibles[]`, `usage[]`, `locator`, `note`.

Le `locator` doit permettre de retrouver le passage pertinent. `usage[]` précise ce qui est démontré : rôle, nom, statut, situation ou date de changement. Le niveau de qualité ne découle pas automatiquement du caractère officiel du site : une page officielle actuelle peut rester insuffisante pour une affirmation historique.

Ne pas enregistrer une consultation qui n’a pas eu lieu. Ne pas effacer les réserves pour rendre le lot apparemment complet. Les 38 drapeaux de renforcement du fichier initial sont un point de départ, pas la liste exhaustive des problèmes : les liens inadéquats et les affirmations hors portée doivent aussi être corrigés.

## Retour attendu et condition de clôture

Tu peux appliquer les arbitrages du point 1 dans le schéma existant, avec les réserves documentaires explicites. Les points 2 et 3 définissent le patch d’audit restant à produire ; ce courrier n’en remplace pas les données ni les preuves.

Le prochain retour devra distinguer les modifications intégrées, les ajouts retenus, les sources remplacées ou complétées et les points encore ouverts. Le lot 1.2 sera verrouillé après examen des neuf candidats, résolution des arbitrages et sourcing suffisant des rôles et situations conservés. Les incertitudes restantes doivent être visibles et explicitement acceptées avant clôture.

Ensuite, reprise du lot 1.3 vers Tchécoslovaquie / Slovaquie / Hongrie, avec les mêmes règles temporelles et documentaires.
