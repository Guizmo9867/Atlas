# Royaume-Uni — cycle1, état proposé au01/01/1945 à00h

**197 fiches, zéro contour, zéro chef-lieu proposé.** Les trois fichiers de données sont complets pour ce cycle. Huit réserves explicites ; la couverture administrative intégrale des territoires britanniques n’est pas revendiquée.

| Ensemble | Fiches |
|---|---:|
| Angleterre et pays de Galles : administrative counties | 62 |
| Angleterre et pays de Galles : county boroughs | 83 |
| Scilly, régime particulier | 1 |
| Écosse : counties / cities | 33 / 4 |
| Irlande du Nord : counties / county boroughs | 6 / 2 |
| Chypre : districts | 6 |
| Total | 197 |

## Réponses au lancement

- **Q2GB-01 — échelons.** Premier niveau de gouvernement local : administrative county et county borough en Angleterre/Galles ; county et city en Écosse ; county et county borough en Irlande du Nord. Scilly relève d’un régime spécial, avec assimilation fonctionnelle au comté dans l’Order1930. Chypre : district colonial. Ces catégories ne forment pas un régime juridique uniforme. Les municipal/metropolitan boroughs, urban/rural districts et les burghs/districts écossais plus fins ne sont pas livrés ; R2GB-06. Pas de paroisses ou communes.
- **Q2GB-02 — listes et noms.** Les62 comtés et83 county boroughs sont extraits de CR03, recensement1931, et rapprochés du Register1939 publié1944. York a son type distinct dans Nomis mais appartient aux83 ; ne pas l’omettre ni le compter deux fois. Noms officiels transcrits dans `proprietes.nom`, libellés français séparés. Les identifiantsH… de Nomis restent des repères de source. Écosse :33 counties du Register1939, quatre cities identifiées parNRS. NI : Table4 du recensement1937, six comtés et deuxCB. Chypre : six districts nommés par les ordres277–282 de la Gazette1943. Les actes1939/1944 renforcent la continuité britannique sans certifier tous les changements1940–1944 ; ils ne prouvent pas à eux seuls le maintien nord-irlandais. R2GB-02 et08.
- **Q2GB-03 — tracés.** GeoJSON vide et aucune `geometrie_ref`. ONS1921 sous OGL3.0 recevable, mais comtés historiques et correspondance1945 non établie. Boundary-LineOS moderne/historique n’est pas une restitution1945 démontrée. GBHGIS/UKDS9179 : documentation attribuée au projet de Portsmouth, README dePaula Aucott2022, renvoiCC-BY-SA hors liste acceptée. La licence d’un produitONS ne s’étend pas à ce jeu. Aucun OSM/ODbL ni tracé dégradé arbitrairement pour une licence autorisée. R2GB-01.
- **Q2GB-04 — cas particuliers.** London County historique ne signifie pas Greater London1965. La City et les28 metropolitan boroughs restent dans la preuve, sans création de county borough fictif. Scilly est séparée de l’agrégat statistique Cornouailles. Perth/Kinross et Moray/Nairn partagent certaines compétences selon art.10(7)1929, pas toutes : pas de fusion totale en31 counties. NI conserve son contexte constitutionnel propre. Parent et souveraineté sont repris du canon, sans modification du contrôle réel. Malte/Gozo et Gibraltar : notes ciblées, organisation interne1945 non entièrement établie ; aucune subdivision créée par défaut. Les territoires de Jersey et Guernesey ont une souveraineté canonique différente (`couronne_britannique`) et ne sont pas ajoutés à ce lot. Chypre : aucune partition actuelle ou base souveraine postérieure projetée sur1945.

## Q2GB-05 — représentation à relire

Confirmer le traitement de ces ensembles parallèles au rang local1, avec `systeme_administratif` distinct, particulièrement les33 counties et quatre cities écossais, les unions fonctionnelles de comtés et l’Irlande du Nord. Ce rang technique n’affirme ni une fédération britannique ni l’égalité de toutes les compétences. Un besoin d’arbitrage éditorial rejoint les réserves du groupe ; il ne valide pas implicitement un autre arbre.

## Chefs-lieux et raccords

Aucun siège n’est déduit du nom d’une circonscription. **Liste de chefs-lieux sans fiche ville : non établie**, faute de preuves homogènes sur les sièges ; cela ne signifie pas qu’il n’en manque aucun. Aucune nouvelle ville n’est demandée ou créée.

Sans contours, aucun raccord n’est déclaré vérifié : frontière irlandaise, côtes/îles, limites entreCB et comtés, séparation des cities écossais, Gibraltar/Espagne, Chypre entière et îles maltaises restent à contrôler avant toute cartographie. Les parents territoriaux existants ne sont pas modifiés.

## Portée des preuves

Lire `preuves/INDEX_PREUVES_ETHER.md`. Les listes sources sont datées1931,1937,1939 et1943 ; la fenêtre1945 n’est pas une date de création. Les publications officielles rétrospectives sont identifiées comme telles. Ni la liste statistique des régions du Register, ni les88 séries de valuation rolls écossaises, ni le total de28 boroughs métropolitains ne doivent être convertis sans examen en niveaux administratifs1945.

`atlas_2GB_controle_transcription.json` compare les145 entrées d’Angleterre/Galles au CSV original de l’archiveNomis. Le contrôle structurel porte sur les IDs, parents, sources et fichiers ; la relecture historique demeure distincte. Les fiches sont proposées, pas annoncées intégrées.
