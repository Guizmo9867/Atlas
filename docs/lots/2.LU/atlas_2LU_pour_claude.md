# 2.LU — remise du cycle 1

**15 fiches : trois districts et douze cantons. Onze géométries proposées ; quatre autres explicitement non intégrables.** Snapshot du 01/01/1945 à00h. Quatre sources nouvelles, une source existante complétée ; sept réserves.

## Q2LU-01 — niveaux

District au niveau1 ; canton au niveau2, comme division territoriale, sans lui attribuer un exécutif administratif propre. Les trois districts de droit se distinguent des arrondissements judiciaires. Les communes ont seulement servi à construire les unions : aucune fiche communale livrée.

## Q2LU-02 — noms et rattachements

| District | Cantons |
|---|---|
| Luxembourg | Capellen, Esch-sur-Alzette, Luxembourg, Mersch |
| Diekirch | Clervaux, Diekirch, Redange, Vianden, Wiltz |
| Grevenmacher | Echternach, Grevenmacher, Remich |

Le cours du ministère de l’Intérieur, juillet 2018, p. 5–6, retrace l’organisation de1843, la création du canton de Vianden en1851 et le retour à trois districts après la suppression de Mersch en1867. Le dossier parlementaire6711 p. 10 et26 recoupe cet historique. Les noms français et les rattachements concordent avec les attributsACT. **R2LU-02** : ce sont des sources rétrospectives ; les textes originaux de1843/1867 et un annuaire1945 n’ont pas été relus. L’arrêté de1936 repéré dans Legilux n’a pas été obtenu en texte exploitable et n’est pas cité comme preuve acquise.

## Q2LU-03 — tracés

Source directe : **ACT Luxembourg, Limites communales historiques1920–1977, ressource24/07/2017, CC0**. L’empreinte SHA1 téléchargée correspond à celle publiée. Les 126 polygones sont regroupés par CANTON et DISTRICT, puis reprojetés de LUREF/EPSG:2169 vers EPSG:4326. Aucun contour tiers utilisé, aucune simplification. Auteur du tracé source : ACT ; union et contrôles : Ether.

Les quinze unions sont valides en sortie. Les 11 références proposées sont des reconstructions provisoires. **Ne pas intégrer** Vianden/Diekirch (frontière à contrôler, R2LU-03) ni Remich/Grevenmacher (Dalheim, R2LU-07). Ces quatre geometrie_ref sont absentes des états. Les fichiers comprennent les quatre bases pour examen seulement, sous statut ne_pas_integrer.

Dalheim présente un anneau emboîté invalide ; sa réparation est documentée sans être validée historiquement. Trois minuscules composantes dégénérées après reprojection ont également été réparées, avec effet de surface inférieur à0,000003m² chacune ; elles ne doivent pas être confondues avec le défaut de Dalheim. Détail exact et opérationPROJ : `atlas_2LU_controle_geometries.json`.

## Q2LU-04 — cas particuliers

Souveraineté luxembourgeoise du parent canonique conservée ; le front actif et la réoccupation partielle restent dans les couches existantes. Aucun découpage allemand parallèle créé. Le régime de tutelle particulier de Luxembourg-ville ne suffit pas à en faire un quatrième district : **R2LU-04**.

Le bulletin gouvernemental d’avril1949 p. 148 prouve un changement postérieur dans le secteur du Kammerwald. Faute de contrôle spatial précis de ce secteur pour 1945, les deux géométries concernées restent réservées. L’alerte ne constitue pas une affirmation que la baseACT l’inclut à tort.

## Villes et raccords

Les trois chefs-lieux de district sont des références rétrospectives de 2018, jamais converties en chefs-lieux1945 validés. Luxembourg correspond à `ville-lu-luxembourg`. **Diekirch et Grevenmacher n’ont pas de fiche ville dans le canon contrôlé.** Aucun ajout de ville effectué. Les cantons homonymes ne donnent pas automatiquement leurs chefs-lieux ; les autres sièges restent à rechercher si ce champ est souhaité.

VoisinsFR,BE,DE : absence de raccord certifié, aucune correction des frontières ou des polygones canoniques. La continuité des unions est mesurée dans la base source seulement ; écarts numériques inférieurs à1m², détaillés au contrôle. **R2LU-06**.

## Lecture et suite

Captures vues : cours p. 5–6, exposé parlementaire p. 10, bulletin p. 148 et contrôle visuel des unions. HTML du producteur/licence et originaux conservés. Les noms communaux de la table technique sont ceux du fournisseur ; ne pas les publier comme nomenclature1945. La grille des30 filtres, la composition et les contrôles sont joints.

Au plus trois cycles ; aucune validation de réserve par défaut. La suite autorisée est2.NL, puis2.CH. Si2.BE et2.LU attendent simultanément Claude, ne pas déposer de troisième lot.
