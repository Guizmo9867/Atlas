# Subdivisions sans tracé sur la carte — suivi

*Mis à jour le 25/10/2026 par `outils/subdivisions/suivi_traces.py` (demande de Guizmo du 24/10/2026 : garder dans un coin les pays qui posent problème). Les fiches existent toujours (noms, rangs, sources) ; seul le dessin manque. À reprendre plus tard, pays par pays.*

**En tout : 428 subdivisions tracées sur 943.**

| Lot | Subdivisions | Tracées | État | Pourquoi | Pistes |
|---|---|---|---|---|---|
| 2.AD | 6 | 0 | aucun tracé | 6 paroisses sans tracé libre. | limites modernes ouvertes des paroisses + changements documentés depuis 1945 (réserve R2AD-01) |
| 2.BE | 50 | 0 | aucun tracé | aucun tracé de 1945 sous licence libre trouvé (R2BE-01). | limites modernes ouvertes (Statbel/NGI) + différences documentées depuis 1945, comme TRF-GIS pour la France |
| 2.DK | 30 | 0 | aucun tracé | piste DigDag (Rigsarkivet, CC BY 4.0) mais accès au service en échec (jeton, certificat expiré, disponibilité réduite), R2DK-01 ; Féroé : carte 2011 sous conditions propres, pas CC BY, R2DK-02. | DigDag « Amt og Region » (polygones historiques calculés depuis les ejerlav) via un accès avec jeton Dataforsyningen ; à transformer en EPSG:4326. |
| 2.ES | 57 | 0 | aucun tracé | aucun tracé de 1945 sous licence libre : l'IGN n'a que des scans de cartes, la base ouverte commence en 1998 (R2ES-01). | provinces quasi inchangées depuis 1927 : limites modernes ouvertes + différences documentées |
| 2.FI | 58 | 0 | aucun tracé | aucun contour de province ou de district au 01/01/1945 validé ; SAPO (communes historiques, CC BY 4.0) a des manques (84 des 547 communes de 1945 sans géométrie), des enclaves absentes et pas de jointure communes → districts de 1945 (R2FI-01). | SAPO via Sorvi/rOpenGov (révision 65a9a2c) : https://ropengov.github.io/sorvi/articles/finnish-historical-maps.html ; licence et auteurs : https://dev.hipla.fi/ (FinnONTO/SeCo Aalto, CC BY 4.0) ; reconstituer les communes de 1945 et leur rattachement, avec cessions et Porkkala. |
| 2.GB | 197 | 0 | aucun tracé | GB Historical GIS est sous CC BY-SA (refusée par notre liste) ; ONS 1921 (OGL) n'a pas le bon découpage ; rien pour l'Irlande du Nord ni l'Écosse (R2GB-01). | décider si on accepte CC BY-SA pour des tracés (question pour Guizmo) ; ou limites modernes + différences |
| 2.IE | 31 | 0 | aucun tracé | candidat Tailte 2024 (CC BY 4.0) mais pas encore rapproché des 31 unités de 1945 (R2IE-01). | comtés irlandais presque inchangés : utiliser Tailte avec les différences documentées |
| 2.NO | 20 | 0 | aucun tracé | cartes historiques Herredskart (Kartverket, 1918 mises à jour 1941, CC BY 4.0) disponibles, mais non géoréférencées ni vectorisées ; versions vectorielles officielles seulement depuis 1997 (R2NO-01). | géoréférencer et vectoriser les feuilles 6539 (Sør-Norge) et 6526 (Nord-Norge) : https://ws.geonorge.no/historiske-kart/v3/publiserte-kart/6539 et …/6526 ; crédit Kartverket. |
| 2.PT | 33 | 0 | aucun tracé | CAOP seulement moderne ; reconstitution REGIS annoncée CC BY-NC (refusée) ; droits des tracés d'Alves 2024 non établis (R2PT-01). | CAOP moderne + différences documentées ; demander la licence des tracés d'Alves |
| 2.SM | 8 | 0 | aucun tracé | aucun tracé historique ni licence propre trouvés ; le cadastre ne connaît que les paroisses, la carte des castelli date de la loi de 2020 (R2SM-03). | voir réserves R2SM ; un tracé ancien des castelli à licence libre reste à trouver |
| 2.FR | 108 | 103 | en partie | 5 régions (Angers, Bordeaux, Orléans, Poitiers, Toulouse) à la composition incomplète (R2FR-03). | compléter les compositions régionales, puis unir les départements déjà tracés |
| 2.IT | 93 | 80 | en partie | 11 provinces écartées par prudence par Ether (tracés jugés douteux pour 1945 : voir les réserves R2IT). | relire les réserves R2IT et lever la marque province par province |
| 2.LU | 15 | 11 | en partie | 4 cantons écartés par prudence par Ether (Vianden, Diekirch, Remich, Grevenmacher : rectifications de frontière). | vérifier les rectifications et lever la marque |
| 2.NL | 12 | 11 | en partie | Brabant-Septentrional écarté par prudence (enclaves de Baarle). | accepter le tracé avec réserve, ou découper les enclaves |
| 2.SE | 25 | 23 | en partie | 23 tracés intégrés (histmaps, CC0) ; seuls Stockholm ville et Stockholms län manquent : contour « county » de la ville de 192,53 km² contre 142,78 km² au tableau SCB, marqué « ne pas intégrer » par Ether (R2SE-02). | couche « municipal » 1916–1948 de histmaps (147,25 km²) à recouper avec le tableau SCB ; Spånga seulement après 1949. |
| 2.LI | 0 | 0 | rien à tracer | territoire Liechtenstein créé le 24/10 ; pas de découpage interne retenu (Landschaften surtout électorales, décision de Guizmo). |  |
| 2.MC | 0 | 0 | rien à tracer | pas de découpage utile en 1945 (rien à tracer). |  |
| 2.VA | 0 | 0 | rien à tracer | pas de découpage utile en 1945 (rien à tracer). |  |
| 2.CH | 200 | 200 | tout tracé | plus rien : 200 contours affichés depuis le 17/10 (licence opendata.swiss acceptée). |  |
