# Atlas — Suivi du ratissage

Ce tableau de bord dit où on en est, pour ne rien oublier. Claude le met à jour à chaque lot intégré dans le dépôt.

## La méthode

1. **Snapshot 0** (01/01/1945, 0 h 00) : les premières frontières, construites **zone par zone**, dans l'ordre **Est → Nord → Ouest → Sud**. Un continent en guerre ne se traite pas d'un seul coup.
2. **Ratissage chronologique** : mois par mois pour 1945 (le front bouge trop), puis au rythme qui convient à chaque période. Chaque changement trouvé = un nouvel état daté, jamais un écrasement.
3. **Couches ajoutées ensuite**, une par une, sur la même base : infrastructures (ports, ferries, grands axes routiers, postes-frontière et douanes, voies ferrées), puis flux (transport, migration, criminalité, accidentologie…).

**Répartition des rôles** : Ether ratisse, cherche et source. Claude intègre dans le dépôt, contrôle et tient le registre. Guizmo tranche et décide ce que l'Atlas raconte.

**Checklist d'un lot avant transmission** : IDs conformes au lexique · chaque source dans le registre · `parent_id` pour l'appartenance · acteurs courts · un changement = un nouvel état.

## Snapshot 0 — état par zone

| Zone | Lot | Entités | Tracés | Statut |
|---|---|---|---|---|
| Est / Nord | 01 | URSS, RSS kazakhe, Touva, Mongolie extérieure, Finlande, Petsamo, Porkkala, Laponie (zone allemande), front de Laponie | 9/9, provisoires (OHM) | intégré le 26/09/2026 ; points à sourcer, voir `docs/pour_ether/2026-09-26_traces_snapshot0_lot01.md` |
| Est / centre | 02 | Allemagne (1937), Autriche, Pologne, frontière Pologne–URSS, RSS d'Estonie, de Lettonie, de Lituanie, Courlande, Memel, Dantzig, front de l'Est | 11/11, provisoires (OHM ; Courlande et front : carte West Point n° 31 géoréférencée) | **verrouillé le 28/09/2026** ; voir `docs/pour_ether/2026-09-28_integration_lot02.md` |
| Est (suite) | — | autres RSS (Ukraine, Biélorussie, Caucase…) à préciser ; Hongrie, Slovaquie, Roumanie passent au lot 04 | — | à faire |
| Nord + Ouest | 03 | Danemark, Féroé, Norvège (+ Est-Finnmark), Suède, Islande, Royaume-Uni, Jersey, Guernesey, Irlande, France (+ poches, Colmar, nord-est), Belgique et Luxembourg (+ Ardennes), Pays-Bas (+ sud libéré), zones alliées en Allemagne, front de l'Ouest | 22/22, provisoires (OHM + cartes LOC et West Point géoréférencées) | intégré le 28/09/2026 ; voir `docs/pour_ether/2026-09-28_integration_lot03.md` |
| Sud + Centre + Balkans + Turquie | 04 | Espagne, Portugal, Andorre, Gibraltar, Suisse, Monaco, Vatican, Italie (+ zones nord/sud, Dodécanèse), Tchécoslovaquie (+ Ruthénie, Zaolzie, zone soviétique), Hongrie (+ zone soviétique, Budapest encerclée), Roumanie, Transylvanie du Nord, Bulgarie, Yougoslavie, Albanie, Grèce (+ Athènes, sans tracé), Turquie entière, Malte, Chypre, front d'Italie | 35/37 (OHM + West Point 31 et 51) ; Athènes et Crète sans tracé | intégré le 28/09, corrigé le 29/09/2026 ; voir `docs/pour_ether/2026-09-28_integration_lot04.md` |

*Les limites exactes de chaque zone seront fixées avec Ether (voir aussi le document de vision globale, pas encore versé dans le dépôt).*

## Décisions en attente

- **Porkkala, début du contrôle soviétique** : 19/09 (armistice), 29/09 (fermeture de la frontière, Yle) ou 03/10 (remise de la gare, Musée ferroviaire) ? Il faut une source A.

- **Laponie** : lien Doria du rapport cité par Ether (≈ 26 km de fortifications, ligne Lätäseno–Tankavaara–Petsamo) à ajouter au registre ; une source A/B pour les dates 29/11/1944 et 27/04/1945. *(Ether)*
- **Zones de contrôle derrière le front** (Pologne occupée à l'ouest de la Vistule, tête de pont de Memel, Prusse-Orientale, Hongrie…) : les dériver du front avec `controle_id`/`administration_id` ? *(proposition Claude, à valider par Ether)*
- **Estonie** : nouvel état juridique au 18/01/1945 (formalisation du transfert de la rive est de la Narva), à créer au ratissage de janvier. *(Ether)*
- **Zaolzie** : à traiter avec la Tchécoslovaquie. *(Ether)*
- **RSS baltes** : `souverainete_revendiquee_par` ne contient que l'URSS ; ajouter une revendication de continuité des États baltes si elle est sourcée. *(Ether)*

- **Lot 03** : île de Man et Svalbard / Jan Mayen (entités voulues, plus tard) ; Groix, Belle-Île, Ré, Oléron, Noirmoutier (source par île) ; carte du 6e groupe d'armées pour le secteur de Nordwind (Bitche) le 01/01 à 00:00. *(Ether)*
- **Janvier 1945 — états déjà repérés pour le ratissage** : front de l'Ouest jour par jour (cartes LOC du 12e groupe d'armées, une par jour, items 2004630304 → 2004630334 ; la première = 01/01 à 12:00) ; Nordwind (dès le 31/12 vers 23:00) et Sonnenwende (7-13/01) en Alsace ; réduction de la poche de Colmar (à partir du 20/01, West Point 75a) ; RSS d'Estonie (formalisation du 18/01) ; Memel (28/01). *(Claude)*

- **Avant de fermer la première passe territoriale** : Liechtenstein, Saint-Marin, île de Man, Svalbard / Jan Mayen (entités à sourcer) ; limites de l'enclave allemande de Crète ; carte yougoslave datée (côte dalmate, Monténégro) ; sources A/B pour Oujhorod, l'administration soviétique en Transylvanie du Nord, le Dodécanèse. *(Ether + Claude)*
- **Deuxième passe du Snapshot 0 : villes** (en cours). 1.0 France, Benelux, îles Britanniques : **73 villes intégrées le 30/09/2026** (61 + 12 après l'audit d'Ether ; 8 rôles déjà sourcés, les autres à sourcer par famille et par pays). 1.1 Nordiques : **65 villes intégrées le 30/09/2026** (56 + 9 après l'audit de zone ; 6 sources à revoir, voir le journal). 1.2 Allemagne + arc alpin : **73 villes intégrées le 01/10/2026** (v0.3, après deux audits d'Ether) ; preuves rôle par rôle ; 45 villes gardent un point « à renforcer » visible dans leur fiche ; **lot clôturé par Guizmo le 01/10/2026** avec ces réserves visibles. 1.3 Tchéquie, Slovaquie, Hongrie : **53 villes intégrées le 01/10/2026** (v0.3 : JSON d'Ether rapproché, puis noms à la date Cassovie et Aussig). 1.4 Pologne et pays baltes : **61 villes intégrées le 01/10/2026** (v0.1). Suite : 1.3 Tchécoslovaquie, Slovaquie, Hongrie → Baltique et Pologne → URSS et Mongolie → Caucase et Turquie → Balkans, Grèce, Italie → Ibérie (numéros à suivre) → **audit transversal** (ports, rail, frontières, industrie, capitales) avant de déclarer les villes terminées. *(Ether + Guizmo)*
- **À dater au ratissage de janvier 1945** : bombardement allié de Royan le 5 janvier 1945 (source : `src-shd-poches-atlantique-1945`).
- **Villes 1.4, états futurs à créer au ratissage du temps** : prise de Memel (28/01/1945) ; bombardement de Świnoujście (12/03/1945) ; prise de Gotenhafen (28/03/1945) ; nouveau complexe de Kohtla-Järve (1945) ; Bielsko-Biała (1951) ; Jēkabpils–Krustpils (1962) ; Kędzierzyn-Koźle (1975). *(Ether)*
- **Villes 1.3, états futurs à créer au ratissage du temps** : fusion Miskolc–Diósgyőr (01/01/1945, date confirmée par Ether, p. 102 du PDF municipal) ; retour aux noms Košice et Ústí nad Labem (dates à prouver) ; Grand Poprad (01/01/1946) ; Moravská Ostrava devient Ostrava (28/06/1946) ; fusion Dombóvár–Újdombóvár (1946) ; Grande Bratislava (1946) ; Párkány devient Štúrovo (26/06/1948) ; Zlín devient Gottwaldov (01/01/1949). Années seules : pas de 1er janvier inventé. *(Ether)*
- **Villes 1.2, états futurs à créer au ratissage du temps** : port de Magdebourg presque détruit le 16/01/1945 (`src-magdeburg-port` ; port, pas toute la ville) ; Vienne redevient capitale nationale (repère 27/04/1945, source dédiée à trouver) ; Leuna obtient le titre de ville (11/1945) ; Wesermünde devient Bremerhaven (1947). *(Ether)*
- **À dater au ratissage de février 1945** : Reims entre dans l'Atlas comme QG avancé du SHAEF (source : `src-defense-reims-shaef-1945`). *(Guizmo + Ether)*
- **Encore sans données au Snapshot 0** : Afrique du Nord et Proche-Orient au contact (« on montre par contact »), Irak, Iran, Caucase soviétique déjà dans l'URSS. *(à décider)*

## Couches suivantes (après le Snapshot 0 des frontières)

| Couche | Statut |
|---|---|
| Territoires et frontières | en cours (Snapshot 0) |
| Lignes de front / contrôle militaire | Snapshot 0 : fronts de l'Est, de Laponie et de l'Ouest tracés ; zones de contrôle faites à l'Ouest, à décider à l'Est |
| Ports, ferries | à faire |
| Grands axes routiers | à faire |
| Postes-frontière, douanes | à faire |
| Voies ferrées | à faire |
| Flux : transport, migration, criminalité, accidentologie | à faire |

## Repères à ajouter au Snapshot 0

- **Capitales et grandes villes** avec leur **nom de 1945** (Königsberg, Dantzig, Stalingrad, Lwów/Lviv…). Pas les noms modernes : ceux-là restent dans le calque « repères modernes ». Il faut un type d'entité `ville` (ou un calque dédié) et une liste sourcée. *(Ether pour la liste, Claude pour le type et l'affichage)*
  Affichage automatique selon le zoom, sans réglage pour l'utilisateur : Eurasie → pays ; continent → capitales ; pays → grandes villes structurantes ; région → nœuds ferroviaires, ports, villes frontalières et industrielles ; local → petites villes pertinentes et micro-histoire. *(Ether, validé le 30/09)*
- **Zones restantes** : Europe centrale (Tchécoslovaquie, Hongrie…), Balkans et Grèce, Europe de l'Ouest (France, Benelux…), péninsule Ibérique, Italie, Scandinavie, Turquie, Caucase, Asie centrale soviétique en détail.

## Idées d'interface (à discuter après le Snapshot 0)

Principe de Guizmo : **maximum d'informations, minimum de visibilité**. La carte doit être claire au premier coup d'œil ; on en apprend plus en cochant, en zoomant, en cliquant.

- **Fiches courtes** : un clic → une note rapide (ce qui s'est passé, en quelques lignes) + le lien vers la source. Pas une bibliothèque en vrac.
- **« Veines » de flux** : des tracés qui n'apparaissent que selon les couches / filtres cochés.
- **Moins de politique, plus de flux** : la politique n'explique que ce qui fait bouger les flux (règle éditoriale du récap).
- Exemple visé : on zoome sur la Finlande, on voit la Laponie, on comprend déjà l'essentiel ; on clique pour le détail (neutralité, guerre de Laponie, soutiens).
- Guizmo a d'autres idées dessinées à venir (affichage des fiches, interface générale).
