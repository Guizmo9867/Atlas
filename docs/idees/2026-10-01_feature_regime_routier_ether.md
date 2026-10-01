# Atlas — Feature « Régime routier » / Permis / Immatriculation
## Note de conception à transmettre à Claude

### 1. Objectif

Ajouter à l’Atlas une couche consacrée à la **vie routière concrète d’un territoire**, sans surcharger la carte ni diluer le fil conducteur principal du projet.

Cette couche doit permettre de suivre dans le temps, depuis le **snapshot 0 au 1er janvier 1945**, l’évolution de sujets comme :

- les systèmes d’immatriculation ;
- les permis de conduire ;
- certaines règles générales de circulation ;
- la signalisation ;
- les contrôles routiers ;
- certains régimes professionnels, notamment poids lourds ;
- plus tard, par analogie, certaines règles propres au ferroviaire ou au maritime.

Le principe fondamental reste celui de l’Atlas : **tout doit être temporel, sourcé, rattaché au bon territoire et visible uniquement quand cela apporte quelque chose à la lecture de la carte.**

---

## 2. Principe UX général : une pastille « Régime routier »

L’idée centrale est de ne pas accrocher artificiellement ces informations à une ville, une autoroute ou une administration particulière.

On crée plutôt un objet cartographique abstrait de type :

**Régime routier**

Cette pastille sert de **porte d’entrée vers les informations routières applicables à un territoire donné à la date sélectionnée**.

Elle ne représente pas un lieu physique précis. Son ancrage sur la carte est donc principalement graphique.

Exemples de contenu dans la fiche :

- Immatriculation
- Permis de conduire
- Règles générales importantes
- Signalisation
- Particularités nationales ou régionales
- Sources
- Historique des changements

Les sujets professionnels très spécialisés, notamment poids lourds, peuvent être séparés pour ne pas transformer cette fiche en encyclopédie.

---

## 3. La pastille évolue avec le niveau de zoom

Le zoom peut résoudre une grande partie du problème de surcharge.

### Zoom faible — continent / plusieurs pays

Quand le filtre **Route** est actif :

- une seule pastille « Régime routier » par pays ou territoire majeur ;
- elle peut être ancrée visuellement **près de la capitale**, sans signifier que la réglementation concerne uniquement la capitale ;
- elle donne une vue générale du régime routier national à la date affichée.

Exemple :

**Allemagne — Régime routier — 1995**

La fiche peut présenter :

- système d’immatriculation général ;
- fonctionnement des permis ;
- conduite à droite ;
- règles nationales principales ;
- signalisation générale ;
- accès aux détails territoriaux si pertinents.

### Zoom intermédiaire — pays / grandes régions

La pastille nationale peut disparaître ou devenir secondaire.

Des pastilles plus fines apparaissent selon la structure du pays :

- Länder ;
- régions ;
- provinces ;
- districts ;
- départements ;
- zones d’immatriculation ;
- autre découpage historiquement pertinent.

La granularité ne doit pas être identique dans tous les pays.

**Règle importante : le système doit suivre la géographie réelle de la donnée, pas forcer tous les pays dans une hiérarchie administrative unique.**

### Zoom local

À fort zoom peuvent apparaître :

- zones précises de codes d’immatriculation ;
- particularités locales ;
- signalisation locale ou historique ;
- points de contrôle physiques ;
- péages ;
- postes douaniers ;
- autres objets routiers spécifiques.

Ainsi, l’Atlas évite d’afficher 300 codes allemands lorsque l’utilisateur regarde toute l’Europe.

---

## 4. Immatriculation

### But

Documenter l’évolution historique des plaques de chaque territoire à partir de l’état existant au 1er janvier 1945.

Il ne faut pas partir du principe que les plaques « apparaissent » après 1945 : beaucoup de systèmes existent déjà.

Le snapshot 0 doit donc chercher :

- quel système est en vigueur au 01/01/1945 ;
- quelles autorités l’utilisent ;
- quelles variantes existent ;
- quelles zones géographiques sont codées ;
- quelles plaques spéciales existent déjà.

### Contenu conseillé

Dans la fiche :

- exemple visuel / photo réelle d’une plaque ;
- reproduction ou schéma si nécessaire ;
- format ;
- couleurs ;
- caractères ;
- signification des lettres/chiffres ;
- zone géographique codée ou non ;
- période de validité ;
- changements successifs ;
- variantes.

Variantes possibles :

- civile ;
- militaire ;
- diplomatique ;
- export ;
- transit ;
- provisoire ;
- police ;
- administration ;
- remorque ;
- véhicules commerciaux ;
- autres cas propres au pays.

### Relation avec la carte

Dans les pays où l’immatriculation code une origine territoriale :

- survol ou clic sur un code ;
- mise en évidence de la zone correspondante sur la carte.

Exemple allemand :

- KA → Karlsruhe ;
- HD → Heidelberg ;
- HN → Heilbronn.

Dans un système où la plaque ne code pas une origine locale, aucune subdivision artificielle ne doit être inventée.

---

## 5. Permis de conduire

Le permis est moins un objet géographique qu’un **régime réglementaire territorial**.

Il doit être accessible depuis la fiche du régime routier du territoire concerné.

Informations possibles :

- existence d’un permis obligatoire ;
- catégories ;
- âge minimal ;
- conditions particulières ;
- durée de validité ;
- examens ;
- permis professionnels ;
- apparition éventuelle d’un système à points ;
- capital initial ;
- retraits / accumulation de points ;
- réformes successives.

### Logique temporelle

Le permis ne doit pas être résumé par une simple date de réforme.

Chaque modification doit créer un nouvel état.

Exemple conceptuel :

- état A jusqu’à une date X ;
- événement de réforme ;
- état B à partir de X ;
- nouvel événement ;
- état C.

Ainsi, le curseur temporel restitue exactement ce qui était en vigueur à l’année ou au mois consulté.

---

## 6. État et événement doivent rester séparés

Il faut distinguer deux choses.

### Régime routier

Il représente **l’état applicable à un instant T**.

Exemple :

**France — 1994**
- plaques : système X ;
- permis : système Y ;
- règles nationales : Z.

### Événement routier

Il représente **le changement**.

Exemples :

- introduction d’un nouveau système d’immatriculation ;
- modification du format des plaques ;
- introduction du permis à points ;
- modification du capital de points ;
- réforme des catégories de permis ;
- modification importante d’une limitation générale ;
- changement majeur de signalisation.

L’événement explique la transition.

Le régime routier montre le résultat après la transition.

---

## 7. Poids lourds : séparer du régime routier général

Pour éviter une fiche gigantesque, les informations très professionnelles peuvent être rattachées à des objets physiques plus adaptés.

### Postes de douane / postes-frontières

Ils peuvent devenir le point principal d’accès à des informations telles que :

- règles poids lourds ;
- documents exigés ;
- contrôles douaniers ;
- transit ;
- restrictions spécifiques ;
- pesée ;
- contrôles techniques routiers ;
- obligations liées au fret ;
- régimes internationaux ;
- réglementation sociale ou professionnelle pertinente.

Cela sépare naturellement :

**Régime routier = utilisateur général**

et

**Poste frontalier / contrôle = usages professionnels et flux internationaux**

Ce choix doit rester souple : certaines règles poids lourds sont nationales et ne doivent pas être artificiellement limitées à un poste de douane. Le poste sert surtout de **point d’accès UX** à ces informations quand elles concernent le franchissement, le contrôle ou le transport international.

---

## 8. Même logique possible pour le ferroviaire et le maritime

Le principe peut être réutilisé sans tout mélanger.

### Ports

Les fiches de ports peuvent regrouper :

- règles propres aux navires ;
- contrôles ;
- douanes ;
- types de flux ;
- ferries ;
- formalités maritimes.

### Gares / points ferroviaires

Les fiches de gares, terminaux ou postes-frontières ferroviaires peuvent regrouper :

- règles de circulation ferroviaire ;
- changements de réseau ;
- changement d’écartement ;
- contrôles ;
- formalités ;
- régimes particuliers.

L’idée est de conserver une architecture cohérente :

- route → régime routier / douanes / contrôles ;
- rail → gares / terminaux / postes ferroviaires ;
- maritime → ports / ferries.

---

## 9. Signalisation

La signalisation peut être très intéressante historiquement, mais elle risque de devenir extrêmement volumineuse.

Approche proposée :

- au zoom faible : uniquement le système général en vigueur ;
- au zoom intermédiaire : grandes réformes ;
- au zoom local : panneaux particuliers, variantes régionales, signalisation de frontière, péages, restrictions locales, etc.

Les changements de panneaux importants peuvent aussi être enregistrés comme événements historiques.

---

## 10. Contrôles routiers

Les contrôles sont plus pertinents quand ils sont liés à des points physiques.

Exemples :

- postes de contrôle ;
- zones de pesée ;
- péages ;
- postes douaniers ;
- contrôles permanents ;
- points de contrôle historiques connus.

Ils peuvent ensuite contenir :

- type de contrôle ;
- véhicules concernés ;
- période d’activité ;
- organisme responsable ;
- technologie utilisée ;
- sources.

Il vaut mieux éviter une pastille nationale « contrôle » qui mélangerait tout.

---

## 11. Intégration dans les filtres

Approche simple au départ :

**Route**

Le filtre Route active :

- infrastructures routières ;
- événements routiers ;
- régime routier ;
- autres objets routiers pertinents.

Si la densité devient trop importante, ajouter ensuite des sous-filtres.

Exemple futur :

- Routes physiques
- Régime routier
- Immatriculation
- Permis
- Signalisation
- Contrôles
- Professionnels / poids lourds

Il vaut mieux créer les sous-filtres quand le volume réel le justifie plutôt que construire dès maintenant une interface immense.

---

## 12. Photos et exemples visuels

Les photos sont particulièrement importantes pour les plaques et la signalisation.

Principe :

- ne pas charger automatiquement toutes les images directement sur la carte ;
- afficher plutôt un exemple visuel dans la fiche ouverte ;
- éventuellement utiliser une miniature légère ;
- charger les images détaillées seulement à l’ouverture de la fiche.

Pour une plaque :

- photo d’époque si disponible et librement utilisable ;
- photo moderne si le système est contemporain ;
- reproduction graphique lorsque cela apporte plus de lisibilité ;
- source de l’image ;
- date approximative ou exacte ;
- territoire.

On peut imaginer une petite galerie temporelle :

**1945 | 1955 | 1970 | 1990 | aujourd’hui**

si plusieurs grands formats se succèdent.

---

## 13. Snapshot 0 — 1er janvier 1945

Cette feature doit être amorcée dès le snapshot 0.

Le ratissage final du snapshot 0 devra donc inclure, pour chaque territoire :

### Immatriculation
- système en vigueur au 01/01/1945 ;
- format ;
- administration responsable ;
- découpage territorial éventuel ;
- exemples ;
- variantes importantes.

### Permis
- régime en vigueur ;
- catégories principales ;
- conditions générales ;
- éventuelles particularités.

### Signalisation
- système général en vigueur, si suffisamment documenté.

### Règles routières majeures
- uniquement celles qui sont importantes pour comprendre la circulation à cette date.

Si aucune donnée fiable n’est trouvée :

- ne pas inventer ;
- distinguer `absent`, `non applicable` et `inconnu/non documenté`.

---

## 14. Méthode de ratissage

Cette couche devra probablement être faite **pays par pays**, et non uniquement par grandes zones géographiques.

Pourquoi :

- chaque pays possède sa propre histoire réglementaire ;
- les subdivisions pertinentes diffèrent ;
- les régimes d’immatriculation ne suivent pas tous les mêmes structures ;
- certaines périodes comportent occupations, partitions, administrations concurrentes ou transitions.

Le snapshot 0 nécessite donc :

1. définir l’état initial au 01/01/1945 ;
2. sourcer cet état ;
3. identifier les subdivisions pertinentes ;
4. créer les entités nécessaires ;
5. ensuite, dans le ratissage chronologique mois par mois, enregistrer seulement les changements.

---

## 15. Schéma de données suggéré

### Entité générique de régime routier

```json
{
  "id": "road_regime_xxx",
  "type": "road_regime",
  "territory_id": "xxx",
  "valid_from": "1945-01-01",
  "valid_to": null,
  "scope_level": "country",
  "anchor_strategy": "capital_nearby",
  "categories": {
    "registration": [],
    "driving_licence": [],
    "general_rules": [],
    "signage": []
  },
  "sources": []
}
```

### Immatriculation

```json
{
  "type": "vehicle_registration_system",
  "territory_id": "xxx",
  "valid_from": "1945-01-01",
  "valid_to": null,
  "geographic_encoding": true,
  "format": "...",
  "plate_types": [
    "civil",
    "military",
    "diplomatic"
  ],
  "examples": [],
  "sources": []
}
```

### Permis

```json
{
  "type": "driving_licence_system",
  "territory_id": "xxx",
  "valid_from": "1945-01-01",
  "valid_to": null,
  "licence_categories": [],
  "points_system": {
    "active": false,
    "model": null,
    "initial_points": null
  },
  "sources": []
}
```

Le format exact devra bien sûr être adapté à l’architecture existante de l’Atlas.

---

## 16. Garde-fous anti-surcharge

1. Une seule pastille de régime routier par territoire au zoom faible.
2. Les subdivisions apparaissent uniquement quand le zoom les rend utiles.
3. Pas d’images lourdes chargées directement sur la carte.
4. Pas de pastille séparée pour chaque micro-catégorie.
5. Les informations professionnelles restent séparables.
6. Les objets physiques restent attachés aux lieux physiques.
7. Les données abstraites sont clairement différenciées visuellement des objets géographiques.
8. Le niveau de détail doit suivre le zoom.
9. Les sous-filtres ne sont ajoutés que lorsque le volume réel le justifie.
10. Toujours privilégier la lisibilité de la carte.

---

## 17. Questions ouvertes à poser à Claude

1. Comment intégrer une entité `road_regime` sans casser l’architecture actuelle ?
2. Peut-on faire évoluer automatiquement le niveau de granularité selon le zoom ?
3. Comment gérer proprement le remplacement :
   - pastille nationale → pastilles régionales → pastilles locales ?
4. Quel système d’ancrage visuel utiliser pour une donnée territoriale abstraite ?
5. Peut-on rattacher une pastille à une capitale sans créer une fausse relation géographique ?
6. Comment éviter les collisions visuelles avec les villes et futurs objets routiers ?
7. Peut-on charger les images à la demande dans les fiches pour limiter les performances ?
8. Comment représenter les zones de plaques allemandes ou autres systèmes territoriaux ?
9. Comment gérer des découpages d’immatriculation qui ne correspondent pas exactement aux frontières administratives déjà présentes ?
10. Faut-il créer un type générique `territorial_regime` réutilisable plus tard pour route, rail et maritime ?
11. Comment articuler les événements de réforme avec l’état courant du régime ?
12. Comment garder une interface simple lorsque Route contiendra à terme autoroutes, ponts, ferries, règles, plaques, permis, signalisation et contrôles ?
13. Quelle structure est la plus adaptée pour les photos et exemples historiques ?
14. Est-il préférable d’avoir un filtre `Route` unique au départ puis de créer dynamiquement des sous-filtres à mesure que la densité augmente ?
15. Comment rattacher les régimes poids lourds nationaux aux postes de douane sans donner l’impression qu’ils ne valent qu’au poste-frontière ?

---

## 18. Résumé conceptuel

La feature peut être résumée ainsi :

**Le filtre Route ne montre pas seulement où l’on circule. Il doit aussi pouvoir montrer comment on circule à une date donnée.**

Le « régime routier » devient donc une couche temporelle et territoriale qui évolue avec le zoom :

**pays → région / subdivision pertinente → zone locale**

Elle regroupe les informations utiles à l’usager général :

**immatriculation + permis + règles principales + signalisation**

Tandis que les informations professionnelles ou de contrôle sont davantage rattachées aux objets physiques pertinents :

**douanes, postes-frontières, péages, contrôles, ports, gares, terminaux.**

Cette architecture permet d’intégrer beaucoup d’informations sans transformer la carte en tableau de bord saturé, tout en restant fidèle au fil conducteur principal de l’Atlas : **la route, les circulations physiques et leur évolution depuis 1945.**
