# Réserves du pilote 2.FR

Aucune réserve n’est validée par défaut. Revue manuelle avec Guizmo après livraison.

## R2FR-01 — Fidélité des limites départementales de 1945

**Preuves et limites.** TRF-GIS reconstruit le millésime 1940 à partir des communes GEOFLA 2011 ; détails historiques non tous restitués. Topologie valide ≠ fidélité au 01/01/1945.

**Impact sur les données.** 87 géométries départementales proposées approximatives ; aucune validée automatiquement. Le périmètre des trois départements alpins reste réservé séparément.

**Choix à examiner.** Accepter ce niveau de reconstruction pour une carte nationale ou demander des corrections locales datées avant affichage.

## R2FR-02 — Frontière alpine antérieure à 1947

**Preuves et limites.** TRF-GIS exclut Tende/La Brigue mais les communes modernes ne garantissent pas le retrait des petites cessions. Le traité art.2 documente plusieurs secteurs alpins. Pas de ligne antérieure géoréférencée obtenue.

**Impact sur les données.** 05, 06, 73 : bases fournies mais aucune geometrie_ref dans leurs états ; même traitement pour Lyon et Marseille. Aucune anticipation 1947.

**Choix à examiner.** Reconstruire les secteurs anciens à partir des cartes annexées et cartes pré 1947 ; coordonner 2. IT après nouveau feu vert.

## R2FR-03 — Cinq ressorts régionaux incomplets ; anciennes fractions

**Preuves et limites.** Angers, Bordeaux, Orléans, Poitiers, Toulouse établis ; la réponse 1981 récapitule des départements coupés en 1941 sans fournir ici une table civile consolidée au 01/01/1945. Tableau militaire non authentifié non substitué.

**Impact sur les données.** Pas de géométrie complète pour ces cinq régions. Les départements 16, 18, 33, 37, 40, 86 gardent France comme contenant ; aucun parent régional entier inventé. Les membres non ambigus restent proposés.

**Choix à examiner.** Collationner les actes de 1943–1944 et les annuaires régionaux ; décider du niveau suffisant avant intégration des fractions.

## R2FR-04 — Limoges : inventaire 9 J lu via index seulement

**Preuves et limites.** Introduction de l’inventaire : cinq départements, fonctions 1944–1946. Le texte indexé est lisible ; fac-similé complet non obtenu.

**Impact sur les données.** Ressort et union des cinq départements proposés avec cette limite de preuve, à collationner par Claude.

**Choix à examiner.** Conserver la proposition documentaire sous réserve ou obtenir l’image correspondante.

## R2FR-05 — Chefs-lieux départementaux : référence 1940

**Preuves et limites.** Les 90 noms proviennent du COG TRF-GIS 1940. Aucun annuaire administratif complet 1945 des chefs-lieux n’a été collationné.

**Impact sur les données.** Champ chef_lieu_propose séparé : aucune valeur n’est publiée comme chef-lieu 1945 validé. Liens vers villes existantes seulement, pas de création automatique. Mézières non assimilé automatiquement à Charleville-Mézières.

**Choix à examiner.** Recouper le répertoire des chefs-lieux avec un annuaire proche de 1945 et les transferts documentés.

## R2FR-06 — Nature des 18 circonscriptions et inférences depuis 1941

**Preuves et limites.** La réponse ministérielle décrit la continuité du cadre de 1941 en 1944 et ses modifications. Les 13 compositions complètes sont des reconstructions documentaires, avec preuves locales pour Lyon et Limoges.

**Impact sur les données.** 18 fiches de circonscription ; pas 18 collectivités régionales actuelles. Le nombre ne prétend pas épuiser les dispositifs spéciaux. Pas de nom Rhône-Alpes actuel substitué à Lyon.

**Choix à examiner.** Collationner les actes originaux et confirmer le vocabulaire/siège à l’intégration ; garder existence séparée de géométrie.

## R2FR-07 — Chef-lieu de droit versus siège effectif des services

**Preuves et limites.** Manche : un guide archivistique signale Cherbourg puis Coutances, sans date précise dans le passage lu. La Rochelle et Colmar sont dans des secteurs de guerre ; aucun siège préfectoral de repli n’est prouvé ici à minuit.

**Impact sur les données.** Saint-Lô, La Rochelle et Colmar restent références 1940 seulement. Aucun transfert juridique ou bureau de repli appliqué.

**Choix à examiner.** Établir dates des sièges effectifs, sans remplacer automatiquement le chef-lieu légal.

## R2FR-08 — Administration allemande de fait : représentation autonome

**Preuves et limites.** Le Mémorial atteste des rattachements distincts en 1940. Ressorts administratifs encore opérationnels et effets précis sur les circulations au 01/01/1945 non établis.

**Impact sur les données.** Note historique dans 57/67/68 ; pas de Gau ni de district opérationnel inventé ; aucune germanisation uniforme des noms.

**Choix à examiner.** Garder la note ou autoriser ultérieurement des fiches autonomes après preuves de ressort, date et fonction.

## R2FR-09 — Précision des couches de contrôle héritées

**Preuves et limites.** Canon lu : poches atlantiques approximatives, carte 15/12/1944 au 1: 5 millions ; îles non toutes couvertes. Colmar et nord-est basés sur dernières sources antérieures, dont LOC 31/12 midi avant Nordwind ; zone nord-est initialement proposition de Claude.

**Impact sur les données.** Références aux couches existantes sans les recopier ni améliorer implicitement leur exactitude. Aucun contrôle uniforme au département.

**Choix à examiner.** Examiner les réserves héritées si un usage local exige une précision supérieure ; pas de réouverture générale de 1.x.

## R2FR-10 — Codes départementaux et COG 1943 original

**Preuves et limites.** Histoire de Gérard Lang : codes 01–90, trois départements annexés de fait conservés. Recoupement avec la nomenclature TRF-GIS ; pagesoriginales 7–8 non obtenues.

**Impact sur les données.** Codes proposés, source secondaire signalée ; aucun code contemporain 95 ou Corse 2 A/2 B appliqué.

**Choix à examiner.** Collationner les deux pages du COG original avant validation définitive des codes.

## R2FR-11 — Annuaire 1946 : lecture partielle et dates des effectifs

**Preuves et limites.** p 6 image vue ; p 7 OCR lu seulement. Notes : effectifs Corse août 1945, Moselle/deux Rhin juin 1945. Existence de droit recoupée par COG 1943 et cadre 1944.

**Impact sur les données.** 90 noms proposés ; aucune population et aucune valeur dejuin/août 1945 anticipée. La source n’établit pas chefs-lieux et limites.

**Choix à examiner.** Collationner p 7 et confirmer les usages limités du tableau ; ne pas rejeter ou généraliser indistinctement toute la source.

## R2FR-12 — Raccords avec huit voisins et géométrie nationale du canon

**Preuves et limites.** Mesures disponibles dans atlas_2FR_raccordements.json ; différences de résolution et de reconstruction. L’Italie présente les cessions 1947 documentées ; sept autres comparaisons n’établissent pas l’absence de changements.

**Impact sur les données.** Ni ajustement automatique ni fusion au canon. Petits chevauchements techniques présents ; précision historique locale à examiner.

**Choix à examiner.** Définir une précision d’affichage, contrôler les segments utiles sur preuve, puis faire l’alignement par Claude sans déplacer un tracé juridique par simple proximité.

## R2FR-13 — Paris, Moselle et Corse : régimes particuliers

**Preuves et limites.** Corse provisoirement hors région après 09/11/1944 ; Moselle : préfet investi des pouvoirs du CRR après 29/09/1944. Trois départements parisiens : aucun ressort civil unique suffisamment établi ici.

**Impact sur les données.** France comme parent pour 20, 57, 75, 77, 78 ; Moselle et Corse explicitement distinguées. Pas de CRRParis ou Metz créé par assimilation à une région militaire.

**Choix à examiner.** Conserver ces distinctions ; approfondir Paris et la modélisation des pouvoirs de Moselle lors de la revue.

