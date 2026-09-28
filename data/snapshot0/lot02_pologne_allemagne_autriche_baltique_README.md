# Atlas — Snapshot 0 — Lot 02
## Pologne · Allemagne · Autriche · Pays baltes

Date de référence : **1er janvier 1945**

Ce lot est préparé pour intégration par Claude Cowork dans le dépôt officiel `Atlas`.

## Décisions historiques principales

### 1. Pologne : ne pas choisir entre OHM 1941 et CShapes 1939
Pour le Snapshot 0, la meilleure lecture opérationnelle est :
- à l'est : la ligne issue de l'accord **PKWN–URSS du 27 juillet 1944**, fondée sur la ligne Curzon ;
- Białystok et Łomża doivent être du côté polonais ;
- mais cette limite ne doit **pas** être présentée comme une frontière internationale définitivement réglée au 01/01/1945 ;
- les États-Unis reconnaissent encore le gouvernement polonais en exil au 01/01/1945 ;
- le PKWN a été transformé en Gouvernement provisoire le 31/12/1944 ;
- la reconnaissance soviétique formelle doit être traitée comme un futur événement de janvier (FRUS indique une annonce le 05/01/1945, avec une formulation rétrospective divergente dans un autre document).

### 2. Ouest de la Pologne
Ne pas appliquer la future Oder–Neisse au Snapshot 0.
La frontière territoriale polono-allemande d'avant-guerre reste la référence du territoire polonais.
Le contrôle allemand est un **calque/état de contrôle**, pas une nouvelle souveraineté polonaise supprimée.

Deux zones sont proposées :
- `territoire-pl-zone-ouest` : contrôle allemand ;
- `territoire-pl-zone-est` : présence militaire soviétique + administration polonaise provisoire.

La géométrie est à dériver de la carte West Point arrêtée au 31/12/1944.

### 3. Allemagne
`territoire-de-allemagne` utilise comme géométrie de référence les frontières du **31/12/1937**, parce que c'est la base retenue par les accords alliés de 1944 pour l'occupation future.
Cela ne signifie pas que le Reich ne contrôle/annexe rien au-delà en 1945.
Autriche, Dantzig, zones polonaises annexées et autres territoires doivent rester des objets séparés.

### 4. Autriche
Entité séparée.
- souveraineté juridique selon la lecture alliée : Autriche ;
- contrôle/administration effective : Allemagne nazie ;
- l'Anschluss est déclaré nul et non avenu par les Alliés en 1943.

### 5. Estonie, Lettonie, Lituanie
Les trois sont représentées comme RSS administrées par l'URSS **mais avec souveraineté contestée**.
Pour éviter une fausse certitude, `souverainete_id` est volontairement omis dans ce lot.
Leur `parent_id` administratif est `territoire-su-urss`.
Le frontend peut plus tard rendre la contestation par hachures/contour spécifique.

### 6. Courlande
La Lettonie n'est pas entièrement sous contrôle soviétique au Snapshot 0.
La poche de Courlande est une zone de contrôle militaire allemand séparée :
`territoire-su-courlande`.

### 7. Klaipėda / Memel
Cas très important :
- territoire cédé à l'Allemagne en mars 1939 ;
- encore sous contrôle allemand le 01/01/1945 ;
- l'étude académique consultée date l'abandon allemand du **28/01/1945**.
Ne pas fermer l'état maintenant : créer l'événement lors du ratissage chronologique de janvier.

### 8. Dantzig
Dantzig est séparée du noyau allemand de 1937.
L'Allemagne l'annexe unilatéralement en 1939.
Au Snapshot 0, contrôle allemand certain ; règlement territorial final pas encore arrêté.

## À faire dans QGIS / OHM

1. Vérifier le tracé de `territoire-de-allemagne` sur la frontière de 1937.
2. Corriger l'est de la Pologne : ne pas conserver la ligne OHM 1941 autour de Białystok si elle place Białystok côté soviétique.
3. Vectoriser `frontiere-pl-su-est` depuis l'accord de juillet 1944 + contrôles académiques.
4. Vectoriser le front du secteur Pologne/Baltiques depuis la carte West Point du 31/12/1944.
5. Extraire la poche de Courlande.
6. Maintenir Memel/Klaipėda hors de la RSS de Lituanie au 01/01/1945.
7. Garder Dantzig séparée du noyau allemand de 1937.

## Deux besoins de modèle révélés par les vraies données

Ne pas les imposer sans décision dans `JOURNAL_DECISIONS.md`.

- `statut_souverainete` / `souverainete_revendiquee_par[]` : utile pour les Baltiques, Pologne, etc.
- `administration_id` : utile quand l'administration civile et le contrôle militaire sont différents.

Le JSON du lot reste compatible avec les règles actuelles : ces nuances sont pour l'instant stockées dans `statut`, `statut_administratif` et `note`.
