# Atlas — Intégration du lot 02 et des décisions Finlande / Mongolie

*De Claude, pour Ether. Transmis par Guizmo le 28/09/2026.*

Le lot 02 est intégré dans le dépôt (`data/snapshot0/lot02_pologne_allemagne_autriche_baltique.json`), avec **9 tracés provisoires sur 11**. Le validateur ne signale aucune erreur. Il reste deux géométries à faire : la poche de Courlande et la ligne de front. Elles demandent de géoréférencer la carte de West Point.

## 1. Ce que j'ai corrigé en intégrant (à reprendre dans tes prochains lots)

| Problème | Correction |
|---|---|
| 5 `source_id` du lot ne correspondaient pas au delta du registre (`…-pl-su-border-…` / `…-urss-pkwn-frontiere-…`, `…-kozikowski-…` / `…-bialystok-delimitation`, `…-lithuania-memel-1939` / `…-lithuania`, `…-d88-memel`, `…-d380-eac-germany`) | Un seul ID par source, celui du registre. **Règle : l'ID d'une source se copie depuis le registre, il ne se réécrit pas.** |
| `src-frus-1944-v01-d380` pointait en réalité sur **FRUS 1945, vol. III, doc. 380** (et le titre était celui du protocole, pas du document) | ID corrigé en `src-frus-1945-v03-d380`. Titre réel : « Report on the Work of the European Advisory Commission ». La mention des frontières du 31/12/1937 y figure bien, vérifiée. |
| Deux sources citées mais absentes du delta : `src-frus-1939-v01-d88-memel`, `src-trames-2025-baltic-border-policy-1944` | Retrouvées et vérifiées : FRUS 1939 vol. I doc. 88 (télégramme du 23/03/1939 sur l'occupation de Memel) ; TRAMES 29(2), 2025, p. 107-131, T. Alatalu, DOI 10.3176/tr.2025.2.01. |
| `ligne-front-de-su-est-europe` : le préfixe n'était pas le type | Renommé `ligne_front-de-su-est-europe`. **Nouvelle règle du lexique : un ID d'entité commence par son `type_entite` exact** (`ligne_front-`, `poste_frontiere-`…). Le validateur le vérifie. |
| `controle_id: allemagne_nazie` alors que `souverainete_id: allemagne` | Ramené à `controle_id: allemagne`, le régime restant dans `regime_id: allemagne_nazie`. Sinon, la carte hachurait l'Allemagne comme « contrôlée par un autre acteur ». **Règle : un acteur = un seul ID ; le régime va dans `regime_id`.** |
| Ta note de lot dit « `souverainete_id` volontairement omis » pour les pays baltes, mais le JSON le contenait (`urss`) | J'ai suivi ta note : retiré pour l'Estonie, la Lettonie, la Lituanie et la Courlande. Sur la carte, « souveraineté non tranchée ». **À confirmer.** |
| `geometries_a_creer_ou_corriger` | Renommé `geometries_a_creer`, comme dans le lot 01. |

Les zones `territoire-pl-zone-ouest` et `territoire-pl-zone-est` annoncées dans ta note ne sont pas dans le JSON. Elles viendront avec le front.

## 2. Tracés : méthode et points à vérifier

Tout est rejouable : `outils/geo/deriver_snapshot0_lot02.py`. Chaque fichier de géométrie contient ses propres `points_a_verifier`.

| Entité | Surface | Méthode |
|---|---|---|
| Allemagne (1937) | 473 000 km² | Reich OHM 1936-1938 |
| Autriche | 84 000 km² | Autriche OHM 1922-1938. Le transfert de 316 km² à la Bavière n'est **pas** appliqué (lecture alliée) |
| Pologne | 208 900 km² | Pologne d'avant Munich ∩ Pologne 1945-1948 = ouest d'avant-guerre + est « Curzon » |
| Frontière Pologne–URSS | ligne | limite commune Pologne / URSS corrigée |
| RSS d'Estonie | 45 800 km² | après les transferts (Petseri, rive est de la Narva) |
| RSS de Lettonie | 64 700 km² | après le transfert d'Abrene |
| RSS de Lituanie | 62 500 km² | sans Klaipėda |
| Memel | 2 500 km² | Lituanie 1923 − Lituanie de mars 1939 |
| Dantzig | 2 000 km² | Ville libre 1920-1939 |

**L'URSS du lot 01 est corrigée** : on lui retire la Pologne du Snapshot 0. Białystok, Łomża et Przemyśl sont maintenant côté polonais. Aucun chevauchement entre territoires, et les trois RSS baltes sont bien contenues dans l'URSS.

**À sourcer / trancher :**

1. **Ligne du 27/07/1944.** Faute de carte vectorisée de l'accord, le tracé est celui du **traité du 16/08/1945**. Les écarts locaux sont possibles. Une carte annexée à l'accord, ou une étude qui décrit les écarts, serait idéale.
2. **Transferts baltes : quelle date ?** Tu les places en 1944. OHM les date du 16/01/1945. Wikipédia (niveau C) parle d'un décret de l'URSS de novembre 1944 pour la rive est de la Narva, d'une acceptation par la RSS d'Estonie le 18/01/1945, et, pour Abrene, de 1944 avec une formalisation en 1946. J'ai appliqué ta lecture (tracé d'après les transferts). Si une source A confirme janvier 1945, on ajoute simplement un nouvel état juridique à cette date, sans changer le tracé.
3. **Zaolzie** : absente de la Pologne, puisqu'on part de la Pologne d'avant Munich, ce qui colle avec la non-reconnaissance alliée des accords de 1938. À confirmer.
4. **Memel** : 2 500 km² de terres, contre environ 2 850 km² historiques. C'est le découpage de la côte (lagune de Courlande) qui explique l'écart. À vérifier avec une source.

## 3. Décisions Finlande / Mongolie appliquées

- **Finlande** : `alignement_id: anti_axis_non_allied`, rendu **ivoire**, sans bleu territorial. J'ai suivi ton dernier message : le premier proposait un bleu-gris, le suivant l'ivoire.
- **Mongolie** : `controle_id: republique_populaire_mongole`, `alignement_id: pro_sovietique_non_belligerant`, `regime_id: republique_populaire`, `statut_administratif: etat_de_facto`, **pas** de `souverainete_id` ni de `parent_id`. Rendu ivoire avec un **liseré bleu** (lien avec l'URSS). Le passage à `allies_ww2` au 10/08/1945 sera créé pendant le ratissage d'août.
- La règle devient « **4 familles principales + statuts particuliers** » (lexique mis à jour). `pro_sovietique_hors_urss` est remplacé par `pro_sovietique_non_belligerant`.
- **Chine et périphérie** : principe noté au journal, « on montre par contact, pas par exhaustivité » (Mandchoukouo, Mengjiang, Xinjiang seulement là où ils touchent l'espace de l'Atlas).

## 4. Ce qu'il me faut pour la suite

1. **Carte West Point « map 31 »** (campagnes balkaniques et baltes, 19/08-31/12/1944) : le lien exact vers l'image haute définition. Je la géoréférence pour tracer **la poche de Courlande et la ligne de front**, avec une marge d'incertitude.
2. **Laponie** (ta demande du 28/09) : une entité pour la **zone tenue par les Allemands dans le « bras » nord-ouest** (vers Kilpisjärvi), rendue en anthracite, et une **ligne de front vers Lätäseno** avec une zone d'incertitude. Il me faut l'entité + la source (la référence Doria que tu cites) + si possible une carte datée proche du 01/01/1945. Je n'invente pas le tracé.
3. **Modèle — MIS À JOUR** : Guizmo a validé tes deux champs. `souverainete_revendiquee_par` (liste) et `administration_id` sont dans le gabarit entité et le lexique. Appliqués : Mongolie `["republique_de_chine"]`, RSS baltes et Courlande `["urss"]`. Pour les pays baltes, ajoute une revendication de continuité (légations, gouvernements en exil) si tu la sources. `administration_id` servira pour les zones polonaises (Armée rouge + administration polonaise provisoire) quand on tracera le front.
