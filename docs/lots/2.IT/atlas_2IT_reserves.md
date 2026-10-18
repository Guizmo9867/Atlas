# Réserves 2.IT — cycle1

Aucune réserve levée ; revue regroupée avec Guizmo.

## R2IT-01 — Échelons et périmètre juridique

Preuves et limites : Annuaire1943 :94provinces ; Istat2018 p.42–49 : suppression des circondari/mandamenti1927 et Caserte recréée11/06/1945. La guerre ne rétablit pas automatiquement ces échelons.

Impact : Un seul échelon livré. Compartimenti statistiques, régions1948 et communes exclus ; Dodecanèse déjàterritoire-it-dodecanese, non doublonné comme province. Annexions1941 non étendues.

Choix à examiner : Confirmer la finesse utile et le traitement documentaire distinct des possessions hors péninsule sans ouvrir une nouvelle couche.

## R2IT-02 — Continuité et approximation1936–1945

Preuves et limites : Liste1942 contemporaine ; reconstitutionIstat1936 fondée sur communes2011. Aucun dépouillement exhaustif de toutes les modifications locales1936–1944.

Impact : 80contours utilisables à titre provisoire seulement, pas limites1945 certifiées ; codes modernes du fichier jamais promus en codesdatés.

Choix à examiner : Renforcer les limites locales sur preuve datée ; ne pas transformer une reconstruction statistique en tracé cadastral.

## R2IT-03 — Projection contradictoire et réparations

Preuves et limites : Page et noticeannoncentWGS84UTM32N ; PRJdéclareED50UTM32N, CPGansi1252.8géométries invalides à la lecture ont reçu make_valid avec suivi de surface.

Impact : Conversion depuis le PRJeffectif, EPSG23032→4326 ; précision de placement réservée, réparationtopologique documentée. Aucune simplification.

Choix à examiner : Confirmer le datum auprès de la documentationIstat ; contrôler les petits résidus et la précision. LicenceCC BY4.0 recevable, pas un motif de rejet.

## R2IT-04 — Frontières tronquées ou à contrôler

Preuves et limites : Istat2018 p.47,49 : Gorizia2702km² etTrieste1230 avant pertes1947 ; shapefile environ217 et465km² seulement. Cuneo etTorino perdent523 et146km² ; Aoste/Imperia etUdine demandent aussi contrôle frontalier.

Impact : 7contours ne_pas_integrer : Torino,Cuneo,Aosta,Imperia,Udine,Gorizia,Trieste. Istria etZara sans contour ; Carnaro absent duZIP. Aucune recomposition à main levée.

Choix à examiner : Obtenir des contours complets antérieurs aux cessions ; raccordsFrance,Yougoslavie,Autriche,Suisse,SanMarin,Vatican à vérifier séparément.

## R2IT-05 — Sièges : statistiques rétrospectives et villes manquantes

Preuves et limites : Édition1952,tableau1944 p.30–33 : sélection des communeschefs-lieux contenant déjàCaserta etLatina. Elle ne démontre pas le statut exact enjanvier1945.

Impact : 90chef_lieu_propose avec annee_preuve1952 et période1944 ; zérorelationvalidée. Pas de champ pourTrieste,Istria,Zara ni ficheCarnaro. Apuania conserve sa propreidentité.

Choix à examiner : Rechercher une preuve explicite à la date pour valider ; villesabsentes seulement listées, aucune créationautomatique.

## R2IT-06 — Limites internes changées après le recensement

Preuves et limites : RDL1297/1936,GU p.2274 : Abetone prend du territoireModena→Pistoia après21avril. IndexGU24/11/1937 p.2 signale le retourPonza/Ventotene àLittoria ; texteintégralnonlu. Le contour1936Latina inclut déjàcesîles : millésimehétérogène.

Impact : 4contours ne_pas_integrer : Modena,Pistoia,Littoria,Napoli. Aucun découpage correctif sans plan probant.

Choix à examiner : Contrôler l’annexeAbetone et actesinsulaires1935/1937 ; vérifierla frontière deNapoli avant recréationCaserta1945.

## R2IT-07 — Occupation et nomenclature à la date

Preuves et limites : OZAV/OZAK documentées par sources institutionnelles ; Apuania attestée1938 et1942, Littoria1942 et préambulejanvier1945, Ionio1942 ; nomduchampcartographiquenonhistorique.

Impact : Souverainetéitalie et parentcanoniqueconservés ; aucune coucheoccupationajoutée. Nomsdatésdansproprietes.nom,identifiantsactuelsdistincts.

Choix à examiner : Relire les noms d’usage dans les zones occupées et conserver le contrôle réel dans les couchesexistantes ; aucune substitutionuniforme de langue.

## R2IT-08 — Adriatique : pays actuel des identifiants et Carnaro reporté

Preuves et limites : Gorizia/Trieste : majorité historique cédée1947 à l’actuelleSlovénie selon surfaces et géographie de ces communes ; Istria/Zara principalementCroatie. Carnaro1930s1121km² réparti aujourd’hui entreSlovénie etCroatie : majorité non établie par les pièces contrôlées.

Impact : Préfixessi pourGorizia/Trieste,hr pourIstria/Zara, à relire ; souveraineté1945italie inchangée. Carnaro recensé danscouverture, sansfiche niIDarbitraire :93fiches/94provinces. Q2IT-05.

Choix à examiner : Vérifier les préfixes sur répartition actuelle et choisir l’IDCarnaro conformément au lancement ; ne pas déduire le paysmajoritaire de la seule villeFiume/Rijeka.
