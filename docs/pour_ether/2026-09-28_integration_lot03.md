# Pour Ether — intégration du lot 03 (Nord et Ouest), 28/09/2026

De : Claude. Tout le lot est intégré et **tracé** (22 entités). Captures : `2026-09-28_lot03_*.png` dans ce dossier.

## 1. Les tracés

| Élément | Source | Précision |
|---|---|---|
| 13 États (frontières juridiques alliées : France 1918-1940 avec Alsace-Moselle, Belgique de 1920 avec Eupen-Malmedy…) | OpenHistoricalMap + côtes Natural Earth | ≈ 1 km |
| **Front de l'Ouest** (Zélande → Nimègue → Aix → saillant des Ardennes → Sarre → Rhin → Colmar) | **ta carte LOC du 01/01/1945** | géoréférencée **automatiquement** en calant ~9 900 points des fleuves sur les fleuves de la carte : écart ≈ 1-2 km, incertitude affichée 3 km |
| Ardennes belges (≈ 2 400 km²) et luxembourgeoises (≈ 620 km²), Pays-Bas libérés, poche de Colmar (≈ 2 000 km²) | pays ∩ côté allemand du front | idem |
| Sud de la poche de Colmar (Munster → Cernay → Mulhouse → Rhin) | **hors de la carte LOC** : West Point n° 75a, ligne du **20/01** | 1,8 km ; date différente, mais secteur figé de fin novembre au 20 janvier |
| Poches de l'Atlantique + Dunkerque (≈ 3 000 km² au total) | West Point n° 71, situation du **15/12/1944** | ≈ 5 km (carte au 1:5 000 000) : **sans doute sous-estimées**, surtout Saint-Nazaire |
| Est-Finnmark (≈ 11 000 km²) | Norvège à l'est de la Tana (ta source SNL) | cours aval de la Tana approché |

**Bonus pour janvier** : la LOC a **la même carte pour chaque jour de janvier 1945** (items 2004630304 à 2004630334). C'est la base idéale du ratissage mensuel à l'Ouest : je pourrai tracer le front jour par jour avec la même méthode.

## 2. Corrections d'intégration

1. `ligne_front-allies-de-ouest` → **`ligne_front-de-ouest-europe`** : après le type vient un code pays, pas « allies » (même forme que `ligne_front-de-su-est-europe`).
2. Danemark : `regime_id: occupation_militaire_allemande` retiré (une occupation n'est pas un régime) ; **`alignement_id: occupe_hors_coalitions`**, nouveau statut particulier : fond ivoire + hachures anthracite.
3. `administration_id` rempli : Féroé = `feroe` (contrôle `royaume_uni`), Est-Finnmark = `norvege` (contrôle `urss`), Pays-Bas libérés = `pays_bas`.
4. France : `regime_id: gprf`. `nom_court` ajouté partout ; précision « en_cours » → « inconnue » (convention des lots 01-02).
5. **Ta règle « pays occupé ≠ Axe » appliquée à tout le corpus** : un territoire garde le camp de son souverain, l'occupation se lit par des **hachures à la couleur du camp de l'occupant** (anthracite = Allemagne, bleu = Alliés, rayures claires si l'occupant est du même camp, comme l'Est-Finnmark). Du coup **la Courlande et la Laponie perdent `axis_ww2`** : Courlande = bleu hachuré anthracite, Laponie = ivoire hachuré anthracite. Tu confirmes ?

## 3. À valider

1. **Jersey et Guernesey** : j'ai ajouté `alignement_id: allies_ww2` (la Couronne est en guerre). OK ?
2. **Deux zones que j'ai tirées du même front** (proposition, comme pour l'Est) :
   - `territoire-de-zone-alliee-ouest` : Allemagne tenue par les Alliés (Aix-la-Chapelle, tête de pont de Sarrelouis, Bienwald) ≈ 1 300 km², `controle_id: etats_unis` ;
   - `territoire-fr-zone-allemande-nord-est` : secteur de Bitche tenu par les Allemands ≈ 200 km² (Nordwind commence le 31/12).
3. **Îles des poches** : Groix et Belle-Île (Lorient), Ré (La Rochelle), Oléron (Royan) rattachées sans source par île. **Noirmoutier** : pas inclus, tu sais ? (Groix n'existe pas dans le trait de côte Natural Earth : elle n'apparaît pas.)
4. **Trous volontaires** : île de Man (dépendance de la Couronne, pas dans le Royaume-Uni), Svalbard / Jan Mayen (garnison norvégienne + stations météo allemandes : ni « occupés » ni « libres »). Tu veux des entités ?
5. **Poches de l'Atlantique** : une carte française détaillée (même d'après-guerre) pour Saint-Nazaire et Lorient permettrait de corriger les surfaces.

## 4. Suite

Il reste le **Sud** (Ibérie, Italie) et le **Centre / Balkans** (Suisse, Tchécoslovaquie avec Zaolzie, Hongrie, Roumanie, Yougoslavie, Grèce…). Après ça, le Snapshot 0 des frontières sera complet.
