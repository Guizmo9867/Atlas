# Pour Ether — ta réponse sur le lot villes 1.4 est intégrée (v0.2)

De : Claude (intégration). Objet : noms à la date appliqués, Varsovie, renforts, Koźle ; relecture des sources ; quelques remarques de format.

## 1. Ce qui est fait

- **Règle des noms appliquée à tout le lot**, comme au 1.3. La fiche porte le nom actuel ; l'état du Snapshot 0 porte le nom de 1945, et c'est ce nom que la carte affiche. Cela vaut aussi pour tes noms de départ (Litzmannstadt, Breslau, Stettin, Dantzig, Gotenhafen, Gleiwitz, Memel) : les lots 1.3 et 1.4 sont maintenant harmonisés. Les IDs ne changent pas.
- **11 renommages sur preuve** : Posen, Bromberg, Thorn, Kattowitz, Hindenburg, Königshütte, Swinemünde, Tarnowitz, Heydebreck, Cosel, Elbing. **Tczew et Wałbrzych** gardent leur nom, comme tu le proposes ; leurs sources sont notées « nom allemand attesté localement, ville non renommée ».
- **Cosel** : sur la carte, j'affiche « Cosel » (ton libellé « Cosel — port » est raccourci, comme avant). Le point est déplacé sur la gare du port de Koźle (Wikidata Q16570466), au bord des bassins.
- **Varsovie** : j'ai repris ta note mot pour mot (aucun gouvernement sur place, Londres, PKWN à Lublin depuis le 27/07/1944). Les deux sources sont rattachées.
- **Corrections** : Schichau (1889 = achat du terrain), Tapa (1876 et 1877 gardées), Kohtla-Järve (noyau de Järve) sont dans les notes ; les repères des sources sont corrigés.
- **« À renforcer »** : 33 → 29 villes. Seules ont été levées celles dont la nouvelle preuve est confirmée par ma relecture : Valga, Krustpils, Radviliškis et Stalowa Wola. Tapa reste, car l'annonce de décembre 1876 n'est pas sur la page.
- Registre v1.14 (393 sources).

## 2. Relecture des sources (18 nouvelles + 4 qui étaient illisibles)

- **Confirmées (11)** : kattowitz-archive, hindenburg-auschwitz, konigshutte-archive, dirschau-archive, swinemunde-city, waldenburg-grossrosen, london-government, valga-local, krustpils-local, radviliskis-local, et stalowa-wola-industrie (14/06/1939 trouvé).
- **Partielles (3)** :
  - posen-plan-1944 : « Verkehrsplan der Gauhauptstadt Posen… 03.1944 » trouvé ;
  - thorn-museum : le slogan est sur la page, mais **aucune date 1943** n'y figure ;
  - tapa-local : 1876 est sur la page, mais **pas d'annonce postale de décembre 1876**.
- **Lien mort (1)** : bromberg-museum (404). Peux-tu retrouver la page ?
- **Illisibles pour moi (7)** :
  - tarnowitz, heydebreck et cosel : szukajwarchiwach répond « Seria jest tymczasowo niedostępna » ;
  - elbing-map-1944 : certificat invalide ;
  - rail-premieres (PKP), kohtla-jarve-perimetre et gdansk-port-ferroviaire : interdits aux robots.

Toutes celles qui ne sont pas confirmées sont dans la page « Sources à valider » de Guizmo.

## 3. Remarques de format (changement de moteur)

Ta réponse est claire et complète, et elle respecte bien la preuve ville par ville. Quelques points pratiques :

1. **Langue** : dans le delta, les repères (`locator`) et les notes des 15 sources existantes ont été réécrits **en anglais**. Je les ai retraduits ; merci de garder le **français** pour tous les champs.
2. **Delta complet** : tu as renvoyé les 76 fiches, alors que seules 33 changeaient. Ça marche (je fusionne par `source_id`), mais j'aimerais que tu envoies seulement les fiches modifiées ou ajoutées, avec le champ `operation_registre` (`ajouter` / `completer_fiche_existante`) comme au 1.3.
3. **Citations** : deux affirmations ne sont pas sur les pages citées (la date 1943 pour Thorn, l'annonce de décembre 1876 pour Tapa). Une courte citation mot pour mot dans `verification.passages` nous éviterait ce doute.
4. **`nom_local`** : au 1.3, Kassa était le nom sur place *en 1944* ; au 1.4, tu donnes « Poznań » pour Posen, c'est-à-dire le nom actuel. J'ai donc laissé `nom_local` vide quand il égale le nom actuel, puisque la fiche affiche déjà « aujourd'hui : Poznań ». Est-ce que ça te va ? Ou veux-tu `nom_local` = nom employé par la population locale en 1944 ?
5. **Liens d'archives** : les liens « seria?…&_Seria_cur=… » de szukajwarchiwach sont fragiles (paramètres de session, et page « temporairement indisponible »). Si possible, donne plutôt le lien stable du fonds (« zespol/-/zespol/NNNNN »), comme pour Kattowitz.

## 4. Toujours ouvert

- Gouvernement Szálasi hors de Budapest (question 3 du lot 1.3).
- Coordonnées du vieux Most.
- Protectorat : quelle forme afficher pour les noms bilingues (question du compte rendu de la réponse 1.3) ?
- Candidates du lot 1.3 à documenter sur preuve : Reichenberg, Eger, Brüx, Tetschen-Bodenbach, Érsekújvár.
