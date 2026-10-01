# Villes 1.3 — réponse à Claude, cycle 3

Livraison du 01/10/2026, Ether. Feu vert explicite consigné dans `coordination/AUTORISATIONS_RATISSAGE.json`. Snapshot 0 : dernière situation connue avant le 01/01/1945 à 00:00. Propositions à intégrer et vérifier par Claude ; aucune intégration au dépôt annoncée ici.

## Q13-01 — cinq noms, preuves individuelles

Le fichier `2026-10-01_ether_corrections_cycle3.json` propose cinq modifications de `proprietes.nom` dans l'état du Snapshot, avec rattachement de la source correspondante. Le nom actuel de fiche et les IDs sont conservés. Ne pas toucher à `nom_local`, aux rôles ou aux coordonnées. Les sources attestent des usages datés, pas des décrets ni toutes les bornes chronologiques.

| Ville / nom proposé | Preuve et limite |
|---|---|
| Liberec → Reichenberg | Reichsanzeiger du 18/05/1944, avis local signé le 11/05 ; OCR lu. |
| Cheb → Eger | Reichsanzeiger du 31/05/1944, avis 2536, nom du tribunal. L'entreprise de l'avis est à Asch : ne pas la situer à Eger. |
| Most → Brüx | Reichsanzeiger du 30/05/1942, registre du tribunal, avis daté du 12/05. Aucun déplacement du point. |
| Děčín → Tetschen-Bodenbach | Catalogue institutionnel SOA.141757 ouvert, annuaire de 1942, Dresden, Deutsche Reichs-Postreklame, cote R 800 /42. Exemplaire non feuilleté. Le titre atteste l'usage composé, pas une fusion : des annuaires antérieurs portent déjà cette forme. La réunion en une entité figure déjà dans le journal de Claude. |
| Nové Zámky → Érsekújvár | Journal local du 22/07/1944 conservé à l'OSZK, titre et avis municipaux ; texte du PDF lu. |

Les URL, repères et courts passages exacts sont dans les cinq fiches correspondantes du delta. Relecture de Claude attendue avant intégration ; conserver la distinction entre OCR, catalogue et original. Aucun retour au nom d'après-guerre n'est daté par extrapolation d'une prise militaire.

## Q13-02 — Protectorat : réserve explicite de Guizmo

Décision : « Laisser cette décision en réserve ». L'étude de Velčovský éclaire les règles linguistiques et les pratiques, mais ne suffit pas à imposer une forme uniforme ville par ville. Aucun changement global ni nouvel alias au titre de cet arbitrage. La source est livrée comme contexte de recherche uniquement.

## Q13-03 — Budapest / Szálasi : note réservée

La chronologie du Comité hongrois de la mémoire nationale situe le déplacement de Szálasi et de son entourage vers Kőszeg le 21/12/1944. Elle ne localise pas tous les ministères et ne prouve pas un siège gouvernemental unique. Guizmo : « Laisser la note en réserve ». Ne pas ajouter la note, créer de point ni modifier le statut de Budapest. Source conservée au registre avec son usage de recherche réservé, sans ajout narratif aux données.

## Q13-04 — vieux Most : relevé conservé, déplacement réservé

La carte municipale interactive a été consultée avec le fond **Lageplan der Stadt Brüx 1938**, signet **Staré město Most**, échelle 1:2500. L'outil Mesures > Localisation a donné **50,524968 N / 13,642034 E** pour un point choisi dans la première place, au sud de l'ancien hôtel de ville. Ce relevé désigne un centre représentatif, pas un monument précis ; la précision du géoréférencement n'est pas documentée. Il ne provient ni du centre moderne ni de l'emplacement actuel de l'église déplacée.

Guizmo : « Garder le déplacement en réserve ». **Aucune coordonnée à appliquer.** Les valeurs se trouvent uniquement dans la section réservée du JSON et dans la source documentaire. L'étude de 2025 a servi à trouver la carte ; la carte est la source du relevé. Aucun fond n'est redistribué.

## Éléments déjà traités et limites du cycle

R-01 (harmonisation fiche/état) et R-02 (Varsovie) sont intégrés selon CR2 1.4 et le journal : pas de nouvelle demande. S44 p.102, Cassovie/Érudit et les autres réserves historiques restent dans la file de validation ; cette livraison ne les valide pas.

Pièces : corrections ciblées, delta de **9 nouvelles sources**, présente réponse. Sources de contexte réservées explicitement distinguées des cinq preuves de nom. Préserver `verification_claude` et `verification_humaine` lors de la fusion ; une relecture Ether ne constitue pas validation humaine. Après ton retour du cycle 3, si des points restent ouverts : attente Guizmo, sans quatrième livraison automatique ni ouverture du lot 1.5.
