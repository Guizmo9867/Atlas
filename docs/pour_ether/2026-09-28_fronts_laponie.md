# Pour Ether — fronts, Courlande, Laponie (28/09/2026)

De : Claude (intégration). Objet : ce qui est fait après ton dernier retour, et 3 questions.

## 1. Ce qui est intégré

| Élément | Fichier / ID | Source | Précision |
|---|---|---|---|
| Front de l'Est au 31/12/1944 (Courlande, tête de pont de Memel, front principal Baltique → Yougoslavie, anneau de Budapest) | `ligne_front-de-su-est-europe` | `src-westpoint-russian-balkan-baltic-1944` (carte n° 31, trait rouge « 31 Dec. ») | carte géoréférencée sur 23 points d'appui, erreur ≈ 9 km en moyenne, 19 km au pire → incertitude affichée **15 km** |
| Poche de Courlande | `territoire-su-courlande` | idem | ≈ 15 200 km² ; `alignement_id: axis_ww2` (anthracite, comme la Laponie) |
| Zone allemande de Laponie (bras de Käsivarsi) | `territoire-fi-laponie-nord-ouest` (nouveau) | `src-piirainen-lapland-war` (C), `src-metsahallitus-schutzwall-2002` (B) | ≈ 3 100 km² ; du 29/11/1944 à… (retrait vers Kilpisjärvi le 27/04/1945, à dater au ratissage) |
| Front de Laponie (Lätäseno, « Sturmbock ») | `ligne_front-de-fi-laponie` (nouveau) | idem | tracé = cours de la rivière (OHM) |

Tes nuances sont appliquées :

- **Estonie / Lettonie** : note « transfert soviétique effectif, formalisation incomplète » (Petserimaa et Abrene août 1944, rive est de la Narva 24/11/1944). Le 18/01/1945 deviendra un nouvel état juridique au ratissage de janvier, sans changement de tracé.
- **Zaolzie** : reste hors de la Pologne (contesté, contrôle allemand), avec la source `src-frus-1945-v04-d432` (mémo du 11/01/1945 : retour à la frontière d'avant 1938 pour Teschen, Spiš, Orava). À reprendre avec la Tchécoslovaquie.
- **Memel** : polygone inchangé (≈ 2 500 km²), drapeau « 2 657 contre 2 828 km² » dans les points à vérifier.
- **Registre** : v0.6, lien exact de la carte West Point, + 2 sources Laponie.

Aperçu : `2026-09-28_fronts_baltique.png`, `2026-09-28_fronts_europe.png`, `2026-09-28_laponie.png` (dans ce dossier).

## 2. Questions

1. **Laponie — ton rapport Doria** : je ne l'ai pas retrouvé. J'ai trouvé à la place le rapport de Metsähallitus (Postila 2002, série A 71) qui donne bien le nom « Sturmbock » pour la Lätäseno, mais parle d'une position d'environ **20 km**, pas 26. Peux-tu m'envoyer ton lien Doria (URN ou URL) ? Et si tu as une source A/B pour les deux dates (29/11/1944 et 27/04/1945), c'est le moment.
2. **Zones de contrôle derrière le front** : aujourd'hui la Pologne est entièrement bleue alors qu'à l'ouest de la Vistule c'est l'Allemagne qui tient le terrain (idem pour la Prusse-Orientale côté soviétique, la tête de pont de Memel, la Hongrie). Je propose de **découper ces zones à partir du front** : nouvelle entité « zone d'occupation » avec `souverainete_id` inchangé, `controle_id` = qui tient le terrain, et `administration_id` si l'administration civile diffère. Tu valides le principe ?
3. **Balayage** : on reprend où ? Ma proposition, dans la continuité du front : Hongrie, Slovaquie/Tchécoslovaquie (avec Zaolzie), Roumanie, Yougoslavie. Ou tu préfères finir d'abord le Nord (Norvège, Suède, Danemark) ?
