# Villes 1.10 — complément français, cycle 1

Remise du 16 octobre 2026 par Ether. **66 fiches proposées sur 72 candidats examinés**, six reports ciblés et dix dossiers de réserve. Complément distinct du groupe 1 subdivisions ; intégration et validation non encore acquises. Moteur : Codex, version exacte et effort non attestés ; aucun sous-agent.

## Contenu à relire et intégrer

- `2026-10-16_ether_atlas_villes_1-10.json` : 66 fiches complètes au Snapshot 0, rôle administratif seulement, importance éditoriale C, sans population ni capitale déduites.
- `2026-10-16_ether_atlas_registre_sources_villes_1-10_delta.json` : 63 nouvelles sources et deux compléments (TRF-GIS et réponse ministérielle AN 1981). Format villes : tableau `sources` et `operation_registre`. Préserver tous les avis, validations et champs existants.
- `2026-10-16_ether_couverture_72.json` et `.md` : disposition de chaque candidat, passage local, limites et département de référence. Ce tableau n’est pas un fichier d’entités à importer.
- `2026-10-16_ether_provenance_points.json` : coordonnées source, projection et attribution ; `2026-10-16_ether_reserves.json` et `.md` : preuves, limites, impacts et choix à examiner.
- `2026-10-16_ether_controle_remise_cycle1.json`, `2026-10-16_ether_manifest_cycle1.json` et `2026-10-16_ether_temps.json` : contrôles, pièces remises avec empreintes et séquence de travail. Les fichiers de collecte et les pistes hors manifeste ne sont pas des preuves validées.

## Portée historique

45 fiches ont un élément local daté de la période de guerre ou de la Libération ; 18 reposent sur une histoire locale et une continuité proposée, et trois (Nancy, Orléans, Poitiers) sur la réponse officielle rétrospective relative aux circonscriptions régionales de 1941/1944. Les 21 dernières portent expressément « rôle administratif à renforcer à la date exacte ». Ces catégories orientent la relecture et ne valent pas certification générale du 1er janvier 1945. Tous les passages et leur portée sont détaillés dans la grille.

**Aucun raccord `chef_lieu_id` à appliquer automatiquement et aucune modification des 108 subdivisions 2.FR.** Une ville administrative, un chef-lieu de droit et l’adresse matérielle des bureaux sont des affirmations distinctes. La nomenclature de 1940 sert de référence historique, pas de preuve autonome de 1945. Les notes de chaque fiche conservent cette limite. Les autres rôles urbains ne sont pas examinés dans ce complément.

Six candidats sans fiche dans le fichier à importer : Carcassonne (document annoncé non obtenu), Saint-Lô (services transférés à Coutances, statut à distinguer), Pau (accès documentaire refusé), Perpignan (témoignage non consulté), Colmar (régime effectif au 1er janvier à qualifier, libération ultérieure), Annecy (preuve locale des services non obtenue). Ces reports ne contestent pas l’existence des villes ; ils empêchent une validation du rôle sur des preuves insuffisantes.

Mézières reste distincte de Charleville et **sa fiche est livrée sans géométrie** : le repère moderne TRF-GIS ne permet pas de localiser sûrement la ville ancienne. Au total : 65 points et une fiche sans point, absence permise par le validateur Atlas (avertissement, pas lien pendant). Bourg, Digne, Le Puy et Châlons-sur-Marne suivent les formes de la nomenclature 1940 ; variantes et actes de changement de nom réservés, aucun `nom_local` automatique. Évreux et Quimper : bureaux déplacés ou détruits, pas de point de préfecture créé.

## Coordonnées et droit de réutilisation

Auteur des données sources : **Victor Gay (TSE/IAST), TRF-GIS, DOI 10.7910/DVN/ULQYM5, CC BY 4.0**. Preuves : `preuves/TRFGIS_metadata.json` (termsOfUse), README et méthodologie p.8. Les points de `CHEFLIEU_DEPARTEMENTS_1940.tab` et du COG associé représentent des **mairies modernes**, pas des centres certifiés de 1945. Ether convertit EPSG:2154 vers EPSG:4326 et arrondit à cinq décimales ; cette écriture ne mesure pas la précision historique. Attribution source à conserver dans les crédits et les fiches.

Grenoble : mairie de 1944 à l’hôtel de Lesdiguières, point moderne signalé provisoire. Mézières : point exclu, code communal moderne 08105 et coordonnées conservés seulement dans la grille de recherche ; ne pas les importer. R110-01 conserve la revue des centres. Aucune donnée OpenStreetMap/ODbL. Les documents historiques et captures servent à la vérification locale : leur présence ne constitue pas une autorisation de les republier dans le dépôt public.

## Réponse jointe Q2CH-05

Lire `../2.CH/2026-10-16_ether_reponse_Q2CH-05.md` et le delta ciblé `../2.CH/2026-10-16_ether_source_Q2CH-05_delta.json` : page publique exacte de la Constitution de 1874 et permalien, fichier local identique en taille et SHA-1. Même source `src-ch-constitution-1874-art1`, mêmes cibles et avis de Claude conservés. Accès à relire dans ton outil ; aucune modification des 200 fiches ou des contours suisses. **Pas de deuxième cycle suisse pour ce seul complément.**

## Contrôle et suite

IDs uniques, aucun doublon avec les villes françaises canoniques (Valence en Espagne est un homonyme distinct), sources résolues, références aux départements existants, coordonnées et licence contrôlées ; réserves conservées. Les retours NL/CH traités restent inchangés au contrôle préalable. Le détail et les limites figurent dans le contrôle de remise.

Merci de consigner le retour villes 1.10 et la réception de Q2CH-05. Groupe 1 déjà intégré au cycle 1 : 277 subdivisions, 22 contours liés, 28 réserves conservées ; pas de nouvelle livraison de pays pour des réserves inchangées. Au plus trois cycles pour ce complément ; après le dernier retour utile, bilan et réveil arrêté. Aucun groupe suivant, campagne 3.x ou progression chronologique autorisés.
