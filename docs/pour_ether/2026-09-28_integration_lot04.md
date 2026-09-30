# Pour Ether — intégration du lot 04 (Sud, Centre, Balkans, Turquie), 28/09/2026

De : Claude. Compte rendu d'intégration (ton brief est archivé dans `data/snapshot0/lot04_sud_centre_balkans_turquie_brief_ether.md`). Captures : `2026-09-28_lot04_*.png` dans ce dossier.

**Règle appliquée partout : dernière situation connue AVANT le 01/01/1945 à 00:00.** Rien de postérieur (armistice hongrois du 20/01, rupture turque avec le Japon le 06/01, trêve d'Athènes du 11/01, retour de la Transylvanie du Nord le 09/03) n'est appliqué.

## 1. Les tracés (28 sur 29)

| Élément | Source | Précision |
|---|---|---|
| 20 États et territoires, frontières juridiques alliées au 01/01/1945 | OpenHistoricalMap + côtes Natural Earth | ≈ 1 km |
| Front d'Italie (côte de Versilia → Apennins au sud de Bologne → Adriatique au nord de Ravenne) | West Point **51**, tireté « **31 Dec.** » | carte stylisée : ≈ 7 km en moyenne, incertitude affichée 10 km |
| Italie du Nord (≈ 125 000 km²) / Italie libérée (≈ 184 000 km²) | Italie ∩ chaque côté du front | idem |
| Hongrie soviétique (≈ 71 000 km²), Budapest encerclée (≈ 1 500 km²), est de la Slovaquie (≈ 12 500 km²) | front de l'Est du lot 02 (West Point **31**, « 31 Dec. »), qui descend jusqu'à la Yougoslavie | ≈ 9 km, incertitude 15 km |
| Dodécanèse allemand | OHM « German occupation of the Dodecanese » 1943-09-11 → 1945-05-08 | à doubler par une source A/B |
| Athènes–Le Pirée | — | **pas de géométrie** (comme tu le demandais) |

Choix de frontières (lecture alliée, à valider) :
- **Tchécoslovaquie** d'avant Munich ; **Hongrie** du Trianon (arbitrages de Vienne nuls) ; **Yougoslavie**, **Grèce** d'avant-guerre ; **Italie** de 1939 (Istrie, Fiume, Zara, Saseno, Dodécanèse italiens) ;
- **Roumanie** de septembre 1940 (sans Bessarabie, Bucovine du Nord, Dobroudja du Sud) + **Transylvanie du Nord à part** : l'armistice (art. 19) annule l'arbitrage de Vienne, mais le retour à l'administration roumaine n'a lieu que le 09/03/1945 ; entre-temps, administration militaire soviétique ;
- **Espagne / Portugal** : Europe + Baléares, Canaries, Açores, Madère ; possessions africaines hors périmètre.

## 2. Corrections d'intégration

1. **Format** : ton bloc « snapshot0 » converti en `etats[]`. Tu ne donnais pas de date de début : j'en ai proposé (ex. Espagne 01/04/1939, Monaco 03/09/1944, Albanie 29/11/1944, Hongrie 16/10/1944), précision indiquée. À vérifier au passage.
2. **Colonies** : `territoire-gb-gibraltar/malte/chypre` → **`territoire-gi-gibraltar`, `territoire-mt-malte`, `territoire-cy-chypre`** (code propre, comme Jersey et Guernesey).
3. **Un acteur = un ID** : `gouvernement_democratique_albanie` → controle/administration `albanie` + `regime_id` ; `gouvernement_grec_regence` → administration `grece` + `regime_id: regence` ; RSI seulement en `administration_id` de l'Italie du Nord.
4. `controle_id: allies` → **`allies_occidentaux`** (nouvel acteur) ; `controle_id: conteste` → **champ absent** (notre règle : non tranché = absent).
5. Les zones n'ont plus d'`alignement_id` propre : elles héritent de leur pays (fond) et l'occupant se lit par les hachures.

## 3. À valider

1. **Hongrie** : tu proposais `axis_ww2`. Comme `axis_ww2` est réservé à l'Allemagne nazie et à ce qu'elle administre directement, je propose **`axis_associe_ww2`** (État associé à l'Axe, gouvernement Szálasi). OK ?
2. **Roumanie** en `allies_ww2` mais **Bulgarie** en `anti_axis_non_allied` : les deux sont sous armistice avec les Alliés et combattent l'Allemagne sous commandement soviétique. Même statut pour les deux ? (Et l'Italie cobelligérante est en `anti_axis_non_allied`.)
3. **Monaco** : `hors_coalitions` → j'ai mis `neutral_ww2` pour éviter un statut de plus. OK ?
4. **Zones que j'ai tirées des fronts** (propositions) : Hongrie soviétique (administration : gouvernement provisoire de Debrecen, 22/12/1944), Budapest encerclée (26/12), est de la Slovaquie, Transylvanie du Nord, Dodécanèse. Il faut une source A/B pour Debrecen, Oujhorod (27/10/1944) et l'administration soviétique en Transylvanie du Nord.
5. **Yougoslavie** : j'ai gardé ton contrôle partisan pour tout le pays, et tracé seulement la ligne de front. Le nord-ouest (Croatie oustachie, Bosnie, Slovénie) est encore tenu par l'Allemagne : il faut **une carte datée d'avant le 01/01** pour découper les zones. Tu en as une ?
6. **Grèce** : garnisons allemandes encore en place (ouest de la Crète autour de La Canée, Milos) — à ajouter avec une source. Athènes reste sans tracé.
7. **Slovaquie** : l'État slovaque de Tiso (occupé par l'Allemagne depuis l'insurrection) et le sud annexé par la Hongrie en 1938 ne sont pas encore distingués dans la Tchécoslovaquie. On les ajoute ?
8. **Italie du Nord** : distinguer plus tard les zones d'opérations administrées directement par l'Allemagne (Alpes, littoral adriatique avec Trieste et l'Istrie) de la RSI ?

## 4. Suite

Avec ce lot, la **première passe territoriale du Snapshot 0 couvre toute l'Europe et la Turquie**. Restent les trous volontaires (Liechtenstein, Saint-Marin, île de Man, Svalbard / Jan Mayen) et la périphérie « par contact » (Afrique du Nord, Proche-Orient, Iran) à décider. Ensuite : villes, plaques, routes, rail, ports, ferries, postes-frontières, flux.

## 5. Suite après ton retour (29/09)

Tout est appliqué :
- **Roumanie** → `anti_axis_non_allied` (comme Bulgarie et Italie) ; **Hongrie** `axis_associe_ww2`, **Monaco** `neutral_ww2`, zones soviétiques, Debrecen et Transylvanie du Nord : validés et notés.
- **Yougoslavie** : plus de contrôle uniforme. Zone partisane (≈ 125 000 km², est) et zone allemande / oustachie (≈ 120 000 km², ouest), découpées par le front de la carte 31 déjà calée. Limites connues : la carte range toute la côte dalmate côté allemand (Split, Zadar, Šibenik étaient pourtant partisans) et s'arrête au Monténégro (au sud de son bord, rattachement partisan par défaut). Une carte yougoslave datée fin 1944 permettrait d'affiner.
- **État slovaque** (≈ 31 000 km², contrôle allemand, administration `republique_slovaque`) et **sud annexé par la Hongrie** (≈ 5 300 km², partie encore à l'ouest du front) dans la Tchécoslovaquie juridique.
- **Italie du Nord** : **OZAK** (≈ 15 500 km², Frioul, Trieste, Istrie, Fiume) et **OZAV** (≈ 17 200 km², Bolzano, Trente, Belluno), administration allemande directe, d'après OHM (1943-09-10 → 1945-05).
- **Grèce** : **Milos** tracée (garnison allemande du 09/05/1941 au 09/05/1945, source : Musée de la guerre de Milos) ; **Crète occidentale** en entité sans tracé (Wikipédia, niveau C : maintien allemand, est évacué pendant l'hiver, reddition le 12/05/1945 ; limites de l'enclave introuvables) ; la Grèce est en **« contrôle non tranché »** (nouvelles rayures croisées grises) : plus de bleu uniforme.

Il manque encore une source A/B pour : les limites de l'enclave de Crète, Oujhorod (27/10/1944), l'administration soviétique en Transylvanie du Nord, le Dodécanèse. Tu as les liens FRUS exacts pour Debrecen (21-22/12/1944) ? Je les ajouterai au registre.
