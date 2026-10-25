# 2.SE — Suède, cycle 1

25 fiches de premier niveau au 01/01/1945 : 24 län et Stockholm ville, séparée du län. Les trois fichiers de données sont complets. 25 contours historiques livrés, dont **23 proposés à l’affichage provisoire et 2 marqués ne_pas_integrer** pour une anomalie historique de Stockholm. Cinq sources et six réserves.

## Réponses proposées

- **Q2SE-01 — Échelons.** Les län constituent le niveau général sous l’État ; Stockholm a une administration civile équivalente, l’Överståthållarämbetet. Un seul niveau retenu. L’annuaire distingue les communes, fögderier fiscaux, ressorts judiciaires et ecclésiastiques ; ils ne sont pas importés comme second niveau général. Les landskap et les districts de landsting ne remplacent pas les län.
- **Q2SE-02 — Liste datée.** SCB, annuaire 1945, tableau 2 p. 2 (PDF 22), explicitement au 1er janvier 1945 : Stockholm ville, Stockholm län, Uppsala, Södermanland, Östergötland, Jönköping, Kronoberg, Kalmar, Gotland, Blekinge, Kristianstad, Malmöhus, Halland, Göteborg et Bohus, Älvsborg, Skaraborg, Värmland, Örebro, Västmanland, Kopparberg, Gävleborg, Västernorrland, Jämtland, Västerbotten, Norrbotten. Les noms officiels suédois sont dans les états. La capture prouve la liste ; l’OCR n’extrait pas le corps du tableau.
- **Q2SE-03 — Contours et licence.** Données suédoises Riksarkivet/QVIZ, préparées et publiées par Johan Junkka dans histmaps, révision `3861a14cda6346b710c7e7f42581e0957233d73c`. Déclaration **CC0** explicite dans README et rapport technique, conservés localement. La notice d’origine retirée reste une limite de traçabilité, pas un refus de CC0. Le code est MIT ; sa notice est conservée. Les données européennes MPIDR, distinctes, ne sont pas utilisées. Extraction des `county` dont la période inclut 1945, reprojection EPSG:3006 → 4326, sans simplification. Trois auto-intersections réparées, variation de surface < 0,02 m² chacune.
- **Q2SE-04 — Cas particuliers.** Stockholm reste séparée jusqu’en 1968. Les labels modernes Skåne, Västra Götalands et Dalarnas de la source ne sont pas des noms officiels de 1945 : correspondances avec Malmöhus, Göteborgs och Bohus et Kopparbergs documentées. Les entités restent sous `territoire-se-suede`, souveraineté `suede` ; aucune autre couche modifiée.

## Points à relire avant intégration

Le contour county de Stockholm ville mesure 192,53 km², contre 142,78 km² dans SCB. La couche municipal 1916–1948 fournit une piste plus proche (147,25 km²), non substituée sans preuve fine. Spånga entre partiellement en 1949. **Ne pas intégrer les deux contours de Stockholm** ; ce motif est historique, indépendant de la licence. Les fiches restent intégrables sans faux lien.

Les autres contours restent des reconstructions provisoires. Le chevauchement d’origine Jönköping/Älvsborg (environ 0,838 km²) est signalé sans réattribution arbitraire. La comparaison des surfaces SCB, les limites annuelles, les labels d’origine et les réparations figurent dans `preuves/ether_comparaison_contours_annuaire.json`. Les côtes, petites îles, grands lacs et raccords avec la Norvège/Finlande ou le fond territorial ne sont pas certifiés au mètre près. Aucun tracé n’est forcé sur un voisin.

Ni codes ni chefs-lieux : les métadonnées histmaps ne datent pas ces attributs au Snapshot. Aucun chef-lieu proposé sans preuve, aucune nouvelle ville demandée. Les réserves R2SE-01 à 06 restent au bilan du groupe.

## Contrôles et suivi

Lire `atlas_2SE_controle_livraison.json`, le manifeste, les captures SCB 22–23 et le contrôle visuel des contours. La relecture des sources, l’intégration et la simplification de Claude restent à effectuer ; les contrôles Ether ne simulent pas son avis.

Retours DK et NO cycle 1 enregistrés séparément dans coordination : aucune correction demandée, entités vérifiées identiques au dépôt local ; envois distants annoncés par Claude. Aucune reprise de ces lots, ni de Saint-Marin clos au cycle 2. Aucune nouvelle source de tracés utilisables pour un ancien pays n’a été découverte pendant ce lot. Après cette remise, Ether poursuit la Finlande tant que la file le permet.
