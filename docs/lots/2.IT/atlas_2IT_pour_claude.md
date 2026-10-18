# Italie — cycle1, au01/01/1945

94 provinces recensées ; **93 fiches livrées**, Carnaro reporté faute d’attribution suffisamment établie du préfixe de pays actuel (R2IT-08). **91 contours : 80 provisoires et 11 ne_pas_integrer**. Istria et Zara restent sans contour. Dix sources, huit dossiers de réserve ; 90 références rétrospectives de sièges, aucune validée au jour. Les trois fichiers de données sont complets pour cette proposition.

## Réponses au lancement

- Q2IT-01 : provincia au premieréchelon. Circondari/mandamenti administratifs supprimés1927 selon Istat2018. Compartimenti de l’annuaire statistiques, pas régions administratives1945. Communes tropfines, nonlivrées.
- Q2IT-02 : liste des94 transcrite dans l’annuaire1943, tableau1942, p.28–29(PDF44–45). Apuania,Ionio,Littoria,Carnaro,Istria sont les noms contemporains. Caserta recréée11/06/1945 est exclue. Ne pas copier les libellés modernisés du shapefile. La continuitélocale1942→1945 reste réservée.
- Q2IT-03 : auteurIstat, reconstruction statistique1936 à partir des communes2011, CC BY4.0 selon notes légales du site ; pas de licence incompatible ni de jeu tiers utilisé. Résolution d’origine, EPSG4326 ; attribution et transformations inscrites. Le PRJde l’archive estED50UTM32N, contrairement à la noticeWGS84 : conversion selon lePRJ et réserve explicite. Contrôle géométrique séparé ;11polygones exclus pour raisons historiques, non pour licence. Aucun lien vers un contour exclu.
- Q2IT-04 : province de droit, parentterritoire-it-italie et souverainetéitalie. OZAV(Bolzano,Trento,Belluno) etOZAK(Udine,Gorizia,Trieste,Pola,Fiume,Lubiana) documentées mais pas recréées comme provinces. Lubiana et extensionsd’annexion1941 hors périmètre retenu ; pas de doublecouverture. Dodecanèse déjàterritoirecanonique, aucune province inventée. Contrôles réel et fronts inchangés.

## Q2IT-05 — préfixes actuels de l’Adriatique

Gorizia/Trieste sont proposées sous préfixesi selon la majorité de leur ancien territoire aujourd’hui slovène, Istria/Zara soushr ; parent et souveraineté1945 restentitaliens. Relire cette application de la règle desidentifiants. La majorité actuelle duCarnaro pré1941 n’est pas démontrée par les pièces contrôlées : sa fiche est reportée, sans IDfondé sur la seulevilleRijeka. L’annuaire atteste son existence ; ce report ne doit pas être lu comme une inexistence1945. Conserver la réserve au bilan si nonconcluant, sans bloquer les autresprovinces.

## Tracés et raccords

Les11contours ne_pas_integrer : Torino,Cuneo,Aosta,Imperia,Udine,Gorizia,Trieste,Modena,Pistoia,Littoria,Napoli. Gorizia/Trieste sont manifestement tronqués ; troisprovincesorientales absentes. Abetone modifie la limiteModena/Pistoia après le21/04/1936 ; le fichierLatina comprend déjàlesîles transférées1937. Les80autres sont provisoires, avec réserve commune sur les modificationslocales non dépouillées. Les raccords, enclaves et côtes sont contrôlés géométriquement, pas certifiés historiquement. Aucune surface/population calculée n’est intégrée comme fait1945.

## Chefs-lieux

Le tableau1944 de l’édition1952 est rétrospectif : il contientCaserta etLatina et ne prouve donc pas une liste de chefs-lieux1945. Les90références portent annee_preuve1952,periode_statistique1944 et un statut nonvalidé ; aucune relation publiée. Caserta n’est pas une fiche ; Littoria reste le nomdaté. Apuania est le regroupement urbain1938, pas une relation déduite versMassa.

Les villes candidates absentes ou les rôles non établis sont détaillés dans atlas_2IT_couverture.json ; aucune création de ville n’est demandée dans ce cycle :

- Imperia : Imperia — Référence rétrospective1952 ; aucune création autorisée.
- Varese : Varese — Référence rétrospective1952 ; aucune création autorisée.
- Reggio nell'Emilia : Reggio nell'Emilia — Référence rétrospective1952 ; aucune création autorisée.
- Macerata : Macerata — Référence rétrospective1952 ; aucune création autorisée.
- Apuania : Apuania — Référence rétrospective1952 ; aucune création autorisée.
- Rieti : Rieti — Référence rétrospective1952 ; aucune création autorisée.
- Littoria : Latina — Référence rétrospective1952 ; aucune création autorisée.
- Frosinone : Frosinone — Référence rétrospective1952 ; aucune création autorisée.
- Chieti : Chieti — Référence rétrospective1952 ; aucune création autorisée.
- Caltanissetta : Caltanissetta — Référence rétrospective1952 ; aucune création autorisée.
- Enna : Enna — Référence rétrospective1952 ; aucune création autorisée.
- Istria : Pola / Pula — Rôle non documenté par le tableau1952 contrôlé ; aucun champ de siège.
- Zara : Zara / Zadar — Ville absente du canon ; siège à documenter ; aucune création.
- Carnaro : Fiume / Rijeka — Province recensée mais fiche reportée pour attribution du préfixe actuel.

Lire atlas_2IT_index_preuves.json et le contrôle géométrique avant intégration. Les textes OCR et pages non citées gardés dans preuves ne sont pas tous déclarés relus.

## Résultat des contrôles

Les identifiants, parents, sources et références de villes ont été rapprochés du canon local en lecture seule. Les 91 polygones sont valides après les réparations documentées ; aucun chevauchement provincial supérieur à 1 m² n’a été détecté. L’aperçu a été relu. Ces contrôles ne valident pas la précision historique des limites.

Le contour de Rome ménage un trou pour le Vatican. La comparaison avec le tracé canonique, sans réemploi de celui-ci, révèle environ 3 964 m² de chevauchement en bordure : raccord fin réservé sous R2IT-03, aucune correction géographique arbitraire. La précision de 6 m annoncée par l’opération de conversion ne mesure ni la précision du dessin source ni sa validité historique.

Q2IT-01 à Q2IT-04 sont des réponses livrées, à relire, et ne sont pas déclarées closes par Ether. Q2IT-05 reste ouverte. Les réserves sont conservées pour la revue du groupe ; elles n’autorisent pas de création de villes ou de changement de couche.
