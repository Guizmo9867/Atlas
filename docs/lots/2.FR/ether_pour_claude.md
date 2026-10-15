# 2.FR — remise pour revue manuelle

France métropolitaine et Corse, **1er janvier 1945 à 00 h 00**. Première remise d’Ether, encore à examiner et à intégrer par Claude. Réveil maintenu PAUSED.

## Contenu

- 108 fiches : 90 départements et 18 circonscriptions de commissariat régional de la République.
- 79 rattachements régionaux proposés. Six départements restent sans rattachement régional entier résolu (16, 18, 33, 37, 40, 86) ; cinq relèvent de cas particuliers (Corse, Moselle, Seine, Seine-et-Marne, Seine-et-Oise).
- 103 géométries de travail : 90 bases départementales et 13 unions régionales. **98 sont référencées comme reconstructions sous réserves.** Cinq bases alpines ne sont liées à aucun état : Hautes-Alpes, Alpes-Maritimes, Savoie, Lyon et Marseille. Cinq autres régions n’ont pas de polygone complet.
- 90 chefs-lieux de référence de 1940, séparés des champs validés pour 1945 ; 18 rapprochements avec des villes déjà présentes, aucune ville créée.
- 11 sources nouvelles, 13 réserves, les 30 filtres renseignés (28 hors phase 2), huit raccords examinés.

## Réponses à Claude

### Q2FR-01 — administration allemande de fait

Proposition : conserver les trois départements français de droit et une note sur l’annexion de fait. Les références aux couches existantes de contrôle gardent leurs réserves. Le ressort encore opérationnel des administrations allemandes et leurs effets précis sur les circulations à la date ne sont pas suffisamment établis pour créer des fiches autonomes. **Réserves R2FR-08 et R2FR-09.**

### Q2FR-02 — échelon régional

Il s’agit du cadre des **commissariats régionaux de la République de 1944**. Dix-huit circonscriptions sont documentées ; treize compositions complètes sont proposées, cinq restent incomplètes. L’existence de l’échelon est distinguée de la disponibilité de sa géométrie. Le total de dix-huit ne prétend pas épuiser les dispositifs spéciaux, notamment à Paris et en Moselle. La Corse est provisoirement hors région selon le décret du 9 novembre 1944 cité par la réponse ministérielle de 1981. **Réserves R2FR-03, 04, 06 et 13.**

### Q2FR-03 — liste et noms

La nomenclature proposée compte **90 départements**, Corse comprise. Charente-Maritime remplace l’exemple Charente-Inférieure de la fiche de lancement. Basses-Alpes, Basses-Pyrénées, Côtes-du-Nord, Loire-Inférieure, Seine-Inférieure, Seine, Seine-et-Oise et Corse sont conservés sous leurs noms historiques. Les codes sont recoupés par une étude du COG 1943 ; ses pages originales n’ont pas été obtenues. Aucun chiffre de population postérieur au Snapshot n’est repris. Les chefs-lieux de 1940 restent des propositions à confirmer. **Réserves R2FR-05, 07, 10 et 11.**

### Q2FR-04 — limites et licence

La base retenue est **TRF-GIS 1940, version 2.4, sous CC BY 4.0**. Elle reconstitue les départements historiques à partir des contours communaux de GEOFLA 2011. Cette méthode impose une réserve sur la fidélité locale et sur les changements non reconstruits. Les cessions franco-italiennes de 1947 ne sont pas anticipées ; les trois bases départementales alpines concernées ne sont pas liées aux états. Aucun tracé n’est déclaré certifié pour 1945 et aucun alignement automatique sur le canon n’a été appliqué. **Réserves R2FR-01, 02 et 12.**

## Lecture de la remise

| Fichier | Usage |
|---|---|
| [Bilan](atlas_2FR_bilan_pilote.md) | Résultats, limites, temps et suite proposée |
| [Table des départements](atlas_2FR_table_departements.md) | Lecture des 90 noms, chefs-lieux de référence et rattachements |
| [Fiches](atlas_2FR_subdivisions_proposees.json) | 108 objets temporels proposés |
| [Compositions régionales](atlas_2FR_composition_regionale.json) | Membres documentés et candidats non validés |
| [Géométries](geometries/atlas_2FR_geometries_proposees.geojson) | Reconstructions et bases alpines réservées |
| [Registre géométrique](atlas_2FR_registre_geometries.json) | Identifiants et provenance |
| [Delta de sources](atlas_registre_sources_2FR_delta.json) | Onze sources nouvelles, URL, usages et preuves |
| [Réserves](atlas_2FR_reserves.md) | Treize dossiers pour la revue avec Guizmo |
| [Couverture](atlas_2FR_couverture.md) | Trente filtres, sans déclaration abusive de couverture |
| [Raccords](atlas_2FR_raccordements.json) | Huit voisins et comparaison au canon |
| [Contrôles](atlas_2FR_controle_livraison.json) | Vérifications et limites |
| [Manifeste](atlas_2FR_manifest.json) | Empreintes des fichiers remis |

## Convention d’intégration

Le type `subdivision` est l’extension demandée dans la fiche de lancement. Claude reste responsable de son ajout au validateur et au lexique. Ether ne modifie aucun fichier canonique. Les IDs des anciennes Seine, Seine-et-Oise et Corse gardent leur identité historique ; les noms actuels des simples renommages sont seulement des aliases de repérage.

`valid_from=1945-01-01` marque le début de la fenêtre observée, pas la création historique de l’objet. `valid_to` reste inconnu. Nom, niveau, code, parent et sources sont portés par l’état.

`chef_lieu_propose` est une référence de 1940 : ne pas la convertir silencieusement en chef-lieu validé de 1945. Les liens de ville sont uniquement des rapprochements avec les fiches existantes. Les sièges régionaux désignent la circonscription ; les adresses physiques successives des bureaux pendant la guerre ne sont pas établies.

Tous les polygones portent `validation_historique_1945=false` et `affichage_automatique_autorise=false`. Les cinq bases alpines ne doivent pas être importées comme limites du Snapshot. Les 98 autres références restent des reconstructions à examiner. Les différences de raccord entre bases de résolution différente ne sont pas des preuves de transferts territoriaux.

Attribution des géométries : Victor Gay, *TRF-GIS Départements (1870–1940)*, version 2.4, DOI 10.7910/DVN/ULQYM5 ; Gay (2021), *Historical Methods* 54(4), 189–207, DOI 10.1080/01615440.2021.1937421. Le working paper de 2020 a été lu ; l’article publié est l’attribution demandée par le producteur. Licence CC BY 4.0, fichiers et provenance conservés. Aucune donnée OSM/ODbL utilisée dans ces nouvelles géométries.

## État des preuves

Images vues : annuaire p. 6, réponse ministérielle p. 164, inventaire du Rhône p. 3, traité italien p. 6–7. Annuaire p. 7 : OCR lu, image non obtenue. Fonds Boursicot 9 J et guide de la Manche : extraits indexés lus seulement. Les actes originaux de 1944 ne sont pas présentés comme relus directement. Le fichier `Loiret_commissariat.pdf` est une réponse HTML, exclue des preuves. Les pièces collectées mais non utilisées sont distinguées au manifeste.

## Suite proposée

Revue manuelle avec Guizmo et Claude : examiner la précision acceptable, les chefs-lieux et les ressorts incomplets, puis intégrer ce qui est suffisamment étayé. Les réserves restent ouvertes et aucune nouvelle zone n’est lancée. Le réveil reste PAUSED après remise.
