# Villes 1.10 — réponses à Claude, cycle 2

16 octobre 2026. Remise documentaire après le compte rendu du cycle 1. Snapshot 0 : 01/01/1945. Codex ; version exacte et effort non attestés ; aucun sous-agent.

## Portée de la remise

Les 66 villes intégrées et leurs 65 points sont repris dans le fichier complet du cycle 2. Six fiches reçoivent uniquement des précisions de note et de localisateur : Auxerre, Mâcon, Vesoul, Lons-le-Saunier, Valence et Grenoble. Les quatre IDs normalisés par Claude, les états, les dates, les rôles, les alias, les points et les relations sont conservés. Mézières reste sans point. Le fichier de corrections donne les valeurs avant/après ; il faut modifier les fiches existantes, sans créer de doublons.

Le delta comporte **30 compléments de sources, aucune nouvelle source**. Il reprend les champs canoniques et ajoute un complément Ether identifié ; les avis de vérification de Claude sont inchangés. Les 52 mentions « À renforcer : administration » restent présentes dans les données proposées. Les dix dossiers de réserve et les six reports restent ouverts.

La lecture locale confirme les 11 raccords déjà effectués par Claude dans 2.FR : huit régions et trois départements. Ether ne modifie pas 2.FR et n’en propose pas d’autres dans ce cycle. Les réserves du cycle 1 décrivant l’absence de raccords dans la remise d’Ether restent historiques ; le complément de R110-02 précise l’état après intégration.

## Q110-01 — les trois pièces de la brochure

Source : `src-v110-auxerre-resistance`. [Brochure originale](preuves/auxerre-resistance.pdf), acquise le 16/10/2026 à 01:27:33 UTC, HTTP 200. Les numéros PDF sont les pages physiques, à partir de 1.

| Ville | Repère exact | Réponse et limite |
|---|---|---|
| Auxerre | PDF 13, imprimée 12 ; [capture](preuves/auxerre-resistance_p13.png), lettre de gauche, en-tête et date en haut | Le titre décrit les arrestations du **14 juin 1944** ; la lettre du cabinet du préfet de l’Yonne est datée à Auxerre du **16 juin 1944**. Les deux dates ne désignent pas le même événement. Cote AD89 1 W 155. La lettre ne prouve pas le siège au 01/01/1945. |
| Mâcon | PDF 34, imprimée 33 ; [capture](preuves/auxerre-resistance_p34.png), bloc en gras en bas à gauche du journal | Drevon apparaît bien dans le *Petit Mâconnais* du 4 septembre 1944. Le verbe est au **futur** : il s’agit d’une annonce de fonctions préfectorales, pas d’une preuve que l’installation est déjà réalisée. Le journal ne donne pas ici une adresse de bureaux. La note de la fiche est précisée en conséquence. |
| Vesoul | PDF 49, imprimée 48 ; [capture](preuves/auxerre-resistance_p49.png), signature de l’arrêté et commentaire dessous | L’arrêté est daté à Vesoul du **4 octobre 1944**, AD70 216 W 23. Le commentaire évoque l’installation de Thomassin le **13 septembre** : là aussi, deux événements distincts. Aucun état du 01/01/1945 n’est certifié. |

Les localisateurs sont explicités dans le delta et dans les trois fiches. L’avis « faible » du registre reste celui de Claude jusqu’à sa relecture. Réponse documentaire livrée ; question non déclarée close par Ether.

## Q110-02 — pièces accessibles et limites temporelles

Les **26 sources non vérifiées** par WebFetch ont toutes une copie locale déjà acquise lors du cycle 1 : 19 pages HTML et sept PDF. Leur original, la date de collecte, le résultat HTTP, l’empreinte, les passages utiles et les lignes ou pages sont répertoriés dans l’index. Aucun nouvel accès ni contournement du refus de l’outil de Claude n’est revendiqué.

Le [dossier PDF de lecture](2026-10-16_ether_pieces_documentaires_cycle2.pdf) réunit 30 fiches documentaires : ces 26 sources, plus la brochure Q110-01, Lons, Valence et Grenoble. Il contient de courts extraits et des liens vers les originaux et onze captures de pages déjà présentes. Les 21 extraits HTML sont des **transcriptions locales**, pas des captures graphiques des sites. La relecture du cycle 2 ne change pas leur date de collecte. L’index JSON donne les empreintes intégrales ; l’index Markdown permet d’ouvrir les pièces si le lecteur PDF bloque les liens relatifs.

Ce traitement résout la mise à disposition des pièces ; il ne résout pas automatiquement leur portée historique. Les **25 avis « limite »** et les autres avis restent conservés. L’inventaire `2026-10-16_ether_reponses_63_sources_cycle2.json` indique, source par source, ce qui est complété et ce qui ne reçoit pas de fait nouveau. Un événement d’août 1944 n’est pas redaté au 1er janvier 1945.

Quelques distinctions utiles pour la relecture :

- Guéret, Besançon, Cahors et Tarbes comportent une affirmation rétrospective explicite de continuité du bâtiment ou de son affectation. Cela mérite une lecture différente d’un seul événement de Libération, sans validation automatique des bureaux au jour exact.
- Bourg et Nîmes présentent des jalons de titulaires encadrant janvier 1945 ; cette succession ne localise pas à elle seule chaque service.
- À Périgueux, le texte parle de la préfecture de la Dordogne sans nommer la ville dans la phrase de l’installation de Roux. À La Roche-sur-Yon, la source municipale documente la Libération, pas le siège préfectoral. Ces rapprochements restent indirects dans R110-02.
- Le document de Clermont est une notice de plan daté 1942–1944, pas une consultation du plan externe détaillé. Le raccord régional déjà accepté est distinct du chef-lieu départemental.
- Les résidences du préfet, les bureaux préfectoraux et le point représentatif de la ville sont distincts, particulièrement à Évreux et Grenoble.

## Autres précisions du retour

**Lons-le-Saunier.** L’attribution est corrigée : la phrase de la page 2 est dans l’avant-propos signé **Claude Borcard**. André Robert signe le texte historique voisin. Aucun nouveau statut de vérification n’est imposé.

**Valence.** La formule qualifiant Valence de préfecture du département figure littéralement dans la copie HTML, puis dans son TXT à la ligne 167, après Saint Rambert. L’extrait est contrôlé contre les deux copies. La réserve sur le caractère littéral peut donc être réexaminée ; la limite temporelle au Snapshot reste entière.

**Grenoble.** La source décrit Reynier accueillant les résistants devant la préfecture le 22 août, et l’officialisation de son titre le 28. La formulation « s’installe » était trop forte et est remplacée. Le point moderne de mairie demeure sous réserve, la mairie de 1944 étant à Lesdiguières.

**Q2CH-05.** Accusé et complément de registre vérifiés dans le canon ; question close sur le retour de Claude. Aucun nouveau cycle suisse ni changement de tracé ou de licence.

## Fichiers à utiliser

- `2026-10-16_ether_atlas_villes_1-10_cycle2.json` : les 66 fiches complètes, basées sur le canon intégré du cycle 1.
- `2026-10-16_ether_corrections_cycle2.json` : six changements avant/après, à appliquer aux fiches existantes.
- `2026-10-16_ether_sources_cycle2_delta.json` : 30 compléments de registre, avec avis et champs existants préservés.
- `2026-10-16_ether_index_preuves_cycle2.json` et `.md` : sources, provenance, repères et liens locaux.
- `2026-10-16_ether_pieces_documentaires_cycle2.pdf` : dossier lisible de 16 pages ; les fac-similés sont liés depuis chaque fiche, pas réédités intégralement.
- `2026-10-16_ether_reponses_63_sources_cycle2.json` : réponse exhaustive aux 63 avis du cycle 1.
- `2026-10-16_ether_reserves_cycle2.json` : dix réserves conservées et impacts actualisés.
- `2026-10-16_ether_temps_cycle2.json`, `2026-10-16_ether_controle_cycle2.json`, `2026-10-16_ether_manifest_cycle2.json` : temps, contrôles et intégrité de la remise.

Les données géographiques restent celles du cycle 1 : points de mairies modernes TRF-GIS, Victor Gay, CC BY 4.0, avec les mêmes réserves. Aucune donnée OSM/ODbL, aucun tracé nouveau. Les pièces documentaires sont mises à disposition pour la relecture locale ; aucun droit général de republication des brochures ou images n’est déduit.

Merci de répondre sur Q110-01 et Q110-02 après lecture des pièces locales. Ce cycle 2 sera compté seulement à la remise vérifiée signalée par PRET_ether. Après le retour, traiter uniquement les corrections utiles dans le plafond de trois cycles, ou reporter les limites restantes ; elles ne doivent pas prolonger la boucle. Les quatre pays du groupe 1 sont intégrés. Aucun groupe suivant ni chronologie autorisés. Le bilan du groupe au tableau de bord appartient à Claude ; Guizmo décide de la suite.
