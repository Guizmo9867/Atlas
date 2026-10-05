# Villes 1.9 — Ibérie et marges, cycle 1

**238 propositions de villes**, 10 candidats différés pour identité ou position, 35 sources nouvelles et un complément Wikidata. Snapshot0 : **1er janvier1945 à 00:00**. Remise commune avec les réponses1.7 cycle3 et1.8 cycle2 ; leurs notes sont dans les dossiers propres aux lots.

Le périmètre comprend l’Espagne et le Portugal avec leurs archipels examinés, Andorre, Gibraltar, Monaco, Vatican, Saint-Marin, Malte/Gozo et Chypre. Les neuf catégories de la méthode sont documentées dans une grille de **14 zones de contrôle**. Il s’agit d’une couverture recherchée et partielle : les omissions et pistes insuffisamment étayées sont explicites. Aucun territoire non recherché n’est déclaré couvert.

## Données et provenance

`2026-10-05_ether_atlas_villes_1-9.json` suit le gabarit d’entité temporelle existant : fiche stable, état historique, point, sources par usage, importance de zoom A/B/C. Les rôles de port, rail, industrie et transit concernent les villes ; aucune infrastructure autonome n’est créée. Aucun `nom_local` ni souveraineté déduite du préfixe de pays actuel.

La carte **Forcano1942** constitue la principale preuve ferroviaire ibérique. Les captures régionales et la légende distinguent lignes exploitées, en construction et projetées. Les localités sur les dernières ne sont pas automatiquement considérées desservies. Les notices d’époque Treccani et les histoires locales apportent les autres rôles. Chaque source a un résumé français, un localisateur et un facilitateur de traduction dans `2026-10-05_ether_guide_sources.md` ; le delta porte les URL brutes et les cibles.

Les 238 repères Wikidata ont été rapprochés par identité, pays actuel, déclaration P625 et emprise géographique. Les réponses brutes et révisions sont conservées ; aucun centre exact de1945 n’est certifié par le point actuel. Les homonymes de Casa Branca et La Encina sont écartés. Ibiza désigne la ville, Saint-Marin la ville-capitale, Mġarr le port de Gozo.

Les formes historiques d’état sont **El Ferrol del Caudillo**, **Mahón** et **Puerto Cabras** ; les noms actuels restent sur la fiche. Les autres variantes restent des alias. Monaco et Vatican n’ont pas de champ `capitale` tant que la convention de cité-État reste réservée. Nicosie et La Valette ont le type `territoire`, sans souveraineté actuelle projetée sur1945. Le code `sm` (Saint-Marin) est proposé à l’ajout au lexique par Claude, conformément à la convention des villes ; Ether n’écrit pas la copie de référence.

## Limites retenues

Les dix différés sont Canfranc, Chinchilla, La Encina, Bobadilla, Moreda, Casa Branca, Tua, Pocinho, Cabeço de Vide et Estella-Lizarra. Les pistes complémentaires — petites îles, centres miniers chypriotes, Encamp/FHASA, Pas de la Case, Pasaia, etc. — restent dans les réserves et ne sont pas comptées parmi ces dix candidats géoréférencés. Le rôle ferroviaire de Portalegre est retiré de la proposition : la gare distante n’est pas assimilée au centre-ville.

Les anciennes lignes de Malte et Saint-Marin ne sont pas prolongées au Snapshot après leur interruption. Evrychou n’est pas retenue par simple extrapolation de la durée du réseau chypriote. ENSIDESA1950, SATA1947 et les aménagements portuaires modernes sont exclus des preuves pour1945. Les notices et cartes antérieures prouvent des fonctions historiques, pas leur fonctionnement continu ni leur capacité en décembre1944.

Quatre sources restent lues par passages indexés : CUF, Horta/SATA, arsenaux espagnols, Arrecife. Leurs usages le signalent. Le rapport de l’arsenal de Malte est lu en transcription, sans collation complète des images. Les **24 réserves R19-01 à24** portent preuves, limites, impact et choix à examiner ; aucune ne vaut arbitrage.

## Fichiers de remise

- `2026-10-05_ether_atlas_villes_1-9.json` : seules les 238 propositions importables.
- `2026-10-05_ether_atlas_registre_sources_villes_1-9_delta.json` : 35 ajouts, un complément par union ; conserver les champs et validations du registre.
- `2026-10-05_ether_selection.json` et `2026-10-05_ether_positions_wikidata.json` : sélection, différés et provenance des points.
- `2026-10-05_ether_grille_couverture.json/.md` : examen des neuf catégories et corridors.
- `2026-10-05_ether_reserves_revue_finale.json/.md` et `2026-10-05_ether_guide_sources.md`.
- `2026-10-05_ether_index_pieces.json` et `2026-10-05_ether_controle_livraison.json` : pièces retenues, empreintes, contrôles et limites.

Les scripts et carnets sont des traces de préparation, pas des imports alternatifs. Ne pas les relancer après livraison. L’essai `2026-10-05_ether_Forcano1942_baleares.jpg` montre la Catalogne ; seule la capture `_baleares_lu.jpg` est utilisée pour les Baléares.

Le contrôle compare les propositions au canon lu de **1306 villes et825 sources**. Sept paires distantes de moins de3km ont été examinées : communes voisines, villes portuaires distinctes ou enclave Vatican/Rome ; elles ne sont pas fusionnées automatiquement. Les chiffres livrés ne sont pas des chiffres déjà intégrés.

Après ton retour, les réponses restantes et **l’audit transversal des villes** remplacent le prochain lot géographique. Cet audit doit encore examiner les lacunes des lots précédents et dresser le bilan des réserves. Aucun quatrième cycle automatique1.7, aucune nouvelle couche ni mois sans feu vert de Guizmo.

Moteur : Codex fondé sur GPT-6 ; aucun sous-agent. Toutes les réserves seront présentées ensemble à Guizmo à la fin de la série.
