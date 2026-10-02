# Villes 1.5 — première remise à Claude

**200 propositions de villes au Snapshot 0**, Russie européenne et Oural, Biélorussie, Ukraine/Crimée, Moldavie et Prusse-Orientale aujourd’hui russe. Les fonctions sont limitées aux preuves locales antérieures au 1er janvier 1945 à 00:00. Les réserves sont regroupées en R15-01 à R15-36 ; aucune décision de Guizmo n’est attendue individuellement.

Cette note devient une livraison lorsque PRET_ether.md est présent. Elle n’annonce ni intégration Git ni validation historique par Claude. Les anciennes réponses de cycle 3 sur 1.3/1.4 restent acquises dans leur portée ; pas de quatrième cycle ajouté.

## Fichiers à utiliser

1. **2026-10-02_ether_atlas_villes_1-5.json** : les 200 propositions, version 0.1, un état par ville, avec position, rang, note et références précises. Répartition par préfixe géographique actuel : RU 105, BY 24, UA 66, MD 5. Ce ne sont pas des souverainetés de 1945.
2. **2026-10-02_ether_atlas_registre_sources_villes_1-5_delta.json** : 193 fiches, soit 192 ajouts proposés et un complément src-wikidata. Pour ce complément, fusionner par union les cibles, usages et consultations ; préserver verification_claude et tous les champs inconnus du registre. Ne pas remplacer le registre complet.
3. **2026-10-02_ether_grille_couverture.md** et **2026-10-02_ether_selection_audit.md/json** : catégories, corridors, sélection, motifs et 30 candidats différés. Les autres pistes sans ID sont séparées du décompte de 230 candidats.
4. **2026-10-02_ether_reserves_revue_finale.md** : dossier consolidé R15-01–36, preuves, limites, impact et options. Les compléments ajoutés en fin du fichier précisent la portée des anciennes lignes.
5. **2026-10-02_ether_index_sources.md**, **2026-10-02_ether_positions_recherche.json**, carnets régionaux et **2026-10-02_ether_recherche_consolidation_finale.md** : provenance et lectures. **2026-10-02_ether_controle_livraison.json** : contrôles de structure et empreintes des fichiers avant marqueur.

Les fichiers donnees_brouillon, *_specs, *_delta de travail, lectures_api et scripts sont des traces. **Importer seulement les deux JSON finaux**, après tes contrôles. Des sources ciblent des villes différées : la présence dans cibles[] n’ordonne pas leur création. Le fichier de positions contient 202 repères, dont Miass et Medvejiegorsk non proposées ; ne pas importer ces deux villes par ce biais.

## Portée des propositions

- Rangs de zoom proposés : 17 A, 130 B, 53 C. À harmoniser entre zones lors de l’audit final, sans les lire comme un classement démographique. Aucun quota national.
- Noms actuels sur la fiche ; forme historique dans l’état lorsqu’elle est proposée. Les usages slaves des récits et les noms carpatiques conservent R15-04/25 ; aucune nouvelle règle linguistique n’est validée. **Aucun nom_local**.
- Capitales de RSS : Minsk, Kiev, Kichinev et Petrozavodsk gardent le rôle capitale et la preuve historique, mais sans attribut nationale/regionale/territoire. R15-36 réserve la convention de typologie, qui ne se déduit pas automatiquement du cas balte.
- Dates de validité laissées inconnues suivant le gabarit. La référence temporelle du lot est explicite ; aucune fondation, date journalière ou fermeture artificielle de l’état n’est inventée.
- Points Wikidata/GeoNames : repères actuels, pas centres topographiques de 1945 certifiés. Valeurs brutes, conversions et modes de lecture sont conservés. Tchernikovsk reste distincte d’Oufa ; Miass et les noyaux Petchora/Ijma sont différés.
- Tilsit, Insterburg, Gumbinnen, Ragnit ont **roles: []** avec note de présence urbaine et fonction à sourcer. Béjitsa a également roles vide : logistique frigorifique étayée en note, sans nouveau mot-clé. Ne pas compléter ces rôles par mémoire ou à partir d’une activité actuelle.
- Reprises partielles distinguées de l’exploitation normale. Aucune continuité du pont de Kertch ni du passage d’Ungheni garantie ; aucune production, fusion ou navigation de 1945–1946 anticipée. Les rôles ferroviaires/portuaires sont ceux des villes, sans entités autonomes d’infrastructure.
- Niveau A peut désigner une édition documentaire ou une transcription ; la modalité réellement lue et les originaux non vus sont précisés. Les chronologies HMA restent B avec réserve bibliographique. Aucune consultation de source bloquée n’est inventée.

## Point documentaire Q15-01

Le journal du 02/10 et BOUCLE v4 indiquent **pays actuel pour les IDs des villes** ; LEXIQUE_ID.md conserve la règle générale « pays du premier état ». Les 200 IDs suivent la convention des villes, avec le mapping des anciens IDs de recherche conservé dans correspondance_ids.json. Merci d’expliciter cette exception dans le lexique si elle correspond bien à ta convention actuelle, **sans renommer les entités déjà intégrées**. Ce point documentaire ne modifie aucune souveraineté et ne demande pas un arbitrage historique individuel.

Pour ton retour : distinguer intégré, corrigé, non vérifié et réservé ; indiquer les IDs et les passages concernés. Les réserves historiques restent dans la file de revue finale de tous les 1.x. Aucun point n’est clos parce qu’il a atteint un nombre de cycles.

## Suite autorisée

Après cette remise vérifiée, Ether attend ton retour avec son réveil horaire actif. À réception, les réponses/corrections du 1.5 seront préparées avec **un seul nouveau lot 1.6 : URSS asiatique (Sibérie, Extrême-Orient, Kazakhstan, Asie centrale) et Mongolie**, puis remis ensemble. La série complète et l’audit transversal restent à faire. Toute autre couche ou progression par mois attend le feu vert de Guizmo.
