# Atlas — Snapshot 0 — Lot 03 : Nord et Ouest européen

**Date figée : 1er janvier 1945.**

Lot proposé pour intégration par Claude. On termine d’abord la boucle frontières / souverainetés / contrôles. Les villes, plaques et codes temporels viennent juste après.

## Source géométrique centrale

**Library of Congress — HQ Twelfth Army Group situation map, 1 January 1945**  
https://www.loc.gov/item/2004630304/

À géoréférencer pour le front des Pays-Bas, Belgique, Luxembourg, frontière franco-allemande et Alsace. Toujours conserver une marge d’incertitude liée à l’échelle.

## Danemark et Féroé
- Danemark : souveraineté danoise, contrôle allemand ; après août 1943 le contrôle allemand est direct. Ne pas le colorer comme « État de l’Axe » par simple équivalence occupation = alignement.
- Féroé : territoire lié au Danemark mais coupé de Copenhague occupée ; défense britannique et gestion locale de guerre. Très bon cas pour `administration_id`.

## Norvège
- souveraineté norvégienne, gouvernement allié en exil ; contrôle allemand sur l’essentiel du pays ;
- Est-Finnmark libéré : Soviétiques jusqu’à la Tana, forces et autorités norvégiennes rétablies à Kirkenes dès novembre ;
- entre l’Est-Finnmark libéré et les positions allemandes de Lyngen, ne pas inventer une frontière nette : zone évacuée / faiblement contrôlée.

## Suède, Islande, Irlande
- Suède : neutre.
- Islande : république indépendante depuis le 17 juin 1944 ; non-belligérante ; présence américaine de défense sans perte de souveraineté.
- Irlande : neutre ; Irlande du Nord dans le Royaume-Uni.

## Royaume-Uni et Îles Anglo-Normandes
- Royaume-Uni : puissance alliée.
- Jersey et Guernesey : dépendances de la Couronne, séparées du Royaume-Uni dans les données, sous occupation allemande au Snapshot 0.

## France
- souveraineté française sur la métropole, y compris Alsace-Moselle dans la lecture juridique alliée ;
- Gouvernement provisoire reconnu en octobre 1944 ;
- surcouches de contrôle allemand : poche de Colmar + poches littorales (Dunkerque, Lorient, Saint-Nazaire, La Rochelle/La Pallice, Royan, Pointe de Grave).
- pour l’instant les poches atlantiques peuvent être un MultiPolygon ; les scinder dès qu’on construit les fiches locales.

## Belgique / Luxembourg
Les deux États sont souverains et alliés, mais le saillant allemand des Ardennes traverse leur territoire au 01/01. Le polygone de contrôle allemand doit être dérivé de **la carte datée du 1er janvier**, jamais de l’extension maximale de l’offensive. Pour la Belgique, garder la frontière souveraine de 1920 avec l’Allemagne.

## Pays-Bas
- nord et ouest encore occupés ;
- sud déjà libéré ;
- le front d’hiver suit notamment les îles de Zélande, la Meuse et le Waal.
La géométrie exacte est à caler sur la carte LOC du 01/01.

## Recommandations de modèle
1. **Adopter `administration_id`** : ce lot rend la séparation contrôle militaire / administration civile incontournable.
2. **Pays occupé ≠ Axe** : le mode d’alignement et le mode de contrôle doivent rester indépendants.
3. **Îles Anglo-Normandes** : pas de faux `parent_id` vers le Royaume-Uni ; ce sont des dépendances de la Couronne.

## Après ce lot
Il restera principalement la péninsule Ibérique, l’Italie, l’Europe centrale et les Balkans/Grèce à fermer. Ensuite seulement : capitales/grandes villes, codes pays temporels, plaques et subdivisions liées aux immatriculations, puis réglage de visibilité par zoom.
