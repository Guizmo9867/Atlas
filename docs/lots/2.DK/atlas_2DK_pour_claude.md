# 2.DK — Danemark et Féroé — cycle 1

Proposition au **1er janvier 1945 à 00:00** : **30 fiches**, soit 22 amter d’État et Copenhague au Danemark proprement dit, Færø Amt et six sysler aux Féroé. **Aucun contour, aucun chef-lieu, aucun code historique proposé.** Les dix sources nouvelles et les trois fichiers de données complets accompagnent cette note. Intégration attendue, non annoncée comme réalisée.

Le feu vert du 24 octobre ouvre ce pays et autorise les Féroé dans le même lot. Le parent géopolitique féroïen est bien `territoire-dk-feroe`, de souveraineté `danemark` ; ses subdivisions utilisent le préfixe actuel `fo`, conformément à la règle des subdivisions. Le Danemark proprement dit utilise `territoire-dk-danemark`. Aucun territoire n’est créé ou modifié. Saint-Marin cycle 2 est une autre remise dans la même file.

## Q2DK-01 — Échelons et systèmes retenus

Le tableau 1 du recensement de 1945, **Overøvrighedskredse. Amter**, compte 23 lignes principales : **Copenhague + 22 amter**. Ce sont les circonscriptions de l’administration d’État. Le total souvent cité de 25 désigne les districts des conseils départementaux, un autre découpage :

| Amt d’État | Districts de conseils distincts |
|---|---|
| Københavns Amt | Københavns et Roskilde Amtsraadskredse ; Frederiksberg appartient à l’amt, mais pas à ces conseils ruraux |
| Odense Amt | Odense et Assens Amtsraadskredse |
| Aabenraa-Sønderborg Amt | Aabenraa et Sønderborg Amtsraadskredse |

Ne pas importer Roskilde, Assens et les deux moitiés d’Aabenraa-Sønderborg comme autant d’amter d’État. Le tableau de l’annuaire 1944 distingue lui-même les termes. Les limites ne sont pas toujours emboîtées : Herlufsholm est partagé entre Sorø et Præstø pour l’amt, mais relève du seul conseil de Sorø ; Dronninglund est partagé entre Aalborg et Hjørring pour l’amt, mais relève du conseil de Hjørring.

Un seul échelon général est retenu au Danemark proprement dit. Les communes ordinaires sont trop fines pour la phase ; les herreder, circonscriptions judiciaires, de police, fiscales et ecclésiastiques sont des systèmes distincts, non un second niveau général uniforme à fabriquer. **Ne pas dire que les herreder auraient tous disparu en 1919** : la notice de Jens Ulf Jørgensen précise qu’ils continuent à servir de base à des juridictions. Leur pertinence supplémentaire reste en R2DK-04, avec l’inventaire des systèmes ; cela n’est pas une couverture exhaustive de chaque juridiction.

Aux Féroé, l’amt constitue le premier niveau sous l’État et les six sysler le second. Le parent géopolitique conserve le statut de guerre, tandis que la fiche `subdivision-fo-feroe` permet de représenter cette hiérarchie administrative sans changer la convention d’échelon. Les sysler sont explicitement décrits comme juridictions territoriales dans les recensements. R2DK-07 conserve la question de représentation ; aucune autonomie de 1948 n’est anticipée.

## Q2DK-02 — Liste, noms et preuve à la date

Les 22 amter sont : København, Frederiksborg, Holbæk, Sorø, Præstø, Bornholm, Maribo, Svendborg, Odense, Vejle, Skanderborg, Aarhus, Randers, Aalborg, Hjørring, Thisted, Viborg, Ringkøbing, Ribe, Haderslev, Aabenraa-Sønderborg et Tønder. Copenhague est une unité distincte dans le tableau des overøvrighedskredse ; cette exception au niveau communal ordinaire justifie sa fiche de rang 1. Frederiksberg n’est pas détaché de son amt d’État.

Le recensement 1935 fournit la base antérieure. L’annuaire 1944 vérifie les noms contemporains. Le recensement 1945 donne la liste postérieure et un relevé des changements : Aarhus et Skanderborg deviennent **deux amter le 1er avril 1942**, en application de la loi n° 530 du 22 décembre 1941 (p. 306/PDF 310). Ce changement est donc pris en compte ; l’amt commun de 1935 n’est pas recopié.

**Limite temporelle :** le recensement danois date du **15 juin 1945**, celui des Féroé du **31 décembre 1945**. L’annuaire 1945 décrit le **1er avril**. Aucun de ces trois états n’est présenté comme un recensement de janvier. La liste au Snapshot est proposée par rapprochement avec les sources antérieures et les changements datés. Les superficies et populations postérieures ne sont pas reprises.

Les six sysler féroïens sont attestés en 1935 et en 1945 : Norderøernes, Østerø, Strømø, Vaagø, Sandø et Suderø. Les noms féroïens contemporains figurent au niveau des fiches stables ; les formes danoises lues dans la source restent dans l’état de 1945. **Tórshavn appartient à Strømø** : le tableau 21 la sépare dans ses comptes communaux, mais le tableau 22 précise « med Thorshavn » (p. 276/PDF 280), conformément au classement de 1935 (p. 204). Il ne faut pas fabriquer un septième syssel à partir de cette séparation statistique. Les districts électoraux, qui partagent Strømø en deux secteurs, ne sont pas non plus une liste de sept sysler.

## Q2DK-03 — Tracés, auteurs et licences

**Danemark : DigDag est une piste historique réelle sous licence acceptée CC BY 4.0**, établie par sa notice officielle XML. Rigsarkivet dirige l’infrastructure et possède le jeu ; la diffusion est assurée par Klimadatastyrelsen. Le projet achevé en 2012 associe Statens Arkiver, Københavns Universitet, Syddansk Universitet, Nationalmuseet, Det Kongelige Bibliotek, Kulturarvsstyrelsen et Kort & Matrikelstyrelsen. Les polygones sont calculés à partir d’environ 10 000 ejerlav numérisés. EPSG:25832 annoncé ; toute extraction future doit être transformée en EPSG:4326 à sa résolution d’origine et conserver la date historique.

La collecte du service cartographique a reçu **HTTP 455**, et celle du WFS une erreur de certificat expiré ; l’outil web n’a pas rendu le XML du WFS. La documentation publique indique un jeton pour les services, hors exceptions DAWA/Inspire. Aucun compte créé, aucun jeton tiers utilisé, aucune vérification de certificat désactivée. Le site DigDag signale lui-même une disponibilité réduite. **R2DK-01 porte sur l’accès et la vérification de l’extraction, pas sur un refus de la licence.** Ne pas écrire « aucun tracé libre n’existe au Danemark ».

**Féroé :** Umhvørvisstovan publie une carte officielle des six sysler, datée du **28 janvier 2011**, disponible en PDF sans géoréférencement annoncé. Elle a été téléchargée et inspectée ; elle sert aux formes actuelles des noms et à repérer une piste, pas à produire un contour de 1945. Les conditions de juin 2019 permettent notamment la modification et l’usage commercial, avec attribution de l’agence, du jeu et de la date de téléchargement, et accès aux conditions. Ce texte spécifique **n’est pas présenté comme CC BY** et ne figure pas parmi les licences nommément acceptées par la fiche. R2DK-02 garde ce point et l’adéquation historique pour la revue ; aucun tracé n’est livré sous une fausse licence.

Les données source ne proviennent pas d’OpenStreetMap/ODbL. La FeatureCollection est volontairement vide, sans `geometrie_ref` dans les fiches. Les preuves PDF et les observations de lecture web sont distinguées ; les échecs de téléchargement sont conservés.

## Q2DK-04 — Exceptions, occupation, raccords

- **Christiansø** : l’annuaire 1944, tableau 2 note 4, indique une administration par le ministère de la Marine, hors commune. Cette exception est documentée mais n’a pas de fiche dans cette proposition. Ne pas déduire son rattachement administratif à Bornholm d’une agrégation statistique. R2DK-05 précise ce manque de représentation.
- **Copenhague** : le transfert de Mørkhøj, parcelle 2az, prend effet le **1er octobre 1944** (arrêté du 25 octobre). Le transfert de terrains de Rødovre, arrêté le **18 décembre 1944**, ne prend effet que le **1er avril 1945**. La date de signature ne doit pas déclencher son anticipation. D’autres réglages de 1944 et de 1945 sont relevés ; aucune limite n’est inventée à partir des tableaux.
- **Occupation** : souveraineté de droit danoise conservée. Contrôle allemand au Danemark et britannique aux Féroé déjà portés par les territoires ; aucune couche militaire concurrente créée. La libération, l’occupation soviétique de Bornholm et l’autonomie féroïenne ultérieures ne sont pas appliquées.
- **Frontières** : aucune extension au Schleswig allemand, aucun changement maritime vers la Suède ou la Norvège. La frontière internationale existante reste la référence ; il n’y a pas de nouveau contour pour en tester les raccords.
- **Périmètre** : les deux seuls territoires danois présents dans le fichier canonique trouvé sont Danemark et Féroé. Le Groenland n’est ni livré ni déclaré couvert historiquement.

## Chefs-lieux et noms nouveaux pour le lexique

Aucun chef-lieu n’est proposé : les tableaux utilisés ne suffisent pas à établir tous les sièges au jour du Snapshot. **Aucune ville nouvelle à créer à partir de ce lot et aucune liste de chefs-lieux « manquants » déduite du nom de l’amt.** R2DK-06 conserve cette limite. Les numéros des lignes statistiques ne sont pas des codes administratifs historiques.

Propositions lexicales pour Claude : `fo` comme préfixe actuel des subdivisions des Féroé (le territoire historique garde son ID existant `territoire-dk-feroe`), `amt`, `syssel`, `kommune` pour l’exception de Copenhague. Les IDs de ce lot restent uniques et n’écrasent aucun ID canonique existant.

## Contrôles et attente

Les fichiers de contrôle, couverture, inventaire des systèmes, temps et manifeste accompagnent la remise. Les sept réserves sont individualisées. Leur conservation ne valide aucun point incertain. La réception et l’intégration de ces propositions restent à confirmer par Claude ; aucun cycle supplémentaire n’est créé pour la préparation ou pour une simple vérification.

Aucune nouvelle source de tracés concernant un pays déjà livré n’a été établie pendant ce dossier. `00_SUBDIVISIONS_SANS_TRACE.md` reste à Claude ; DigDag doit y être décrit comme **piste historique CC BY, accès/extraction à résoudre**, si les fiches danoises sont intégrées sans contours.
