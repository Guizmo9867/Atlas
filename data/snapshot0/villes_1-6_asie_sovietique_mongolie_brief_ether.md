# Villes 1.6 — première remise, avec réponses 1.5

**254 propositions de villes**, URSS asiatique hors Caucase et Mongolie, au **1er janvier 1945 à 00:00**. **303 candidats examinés, 49 différés**, dont deux doublons de recherche. **114 fiches de sources : 113 ajouts et un complément Wikidata.** 69 réserves numérotées pour la revue finale 1.x ; aucune décision de Guizmo sollicitée individuellement.

Cette note est une remise seulement avec `PRET_ether.md`. Elle ne signifie ni intégration Git ni confirmation de source par Claude. Le même envoi comprend les réponses du cycle 2 au lot 1.5 dans son propre dossier.

## Fichiers à intégrer après contrôle

1. `2026-10-03_ether_atlas_villes_1-6.json` : seules les 254 entités proposées. RU135, KZ41, KG16, TJ8, TM12, UZ23, MN19 ; codes actuels sans valeur de souveraineté en1945. Rangs : A13, B54, C187, D0.
2. `2026-10-03_ether_atlas_registre_sources_villes_1-6_delta.json` : delta ciblé. Ajouter les113 sources après contrôle ; **fusionner src-wikidata par union**, sans remplacer les cibles/consultations/usages antérieurs ni `verification_claude` ni aucun champ inconnu. Des sources documentent des candidats différés : elles ne créent pas de villes.

Les JSON de candidats, les relevés API et les scripts sont des traces de recherche, **pas d’autres imports**. Ne pas copier les propositions sous une clé `entites` supplémentaire que le validateur traiterait comme un second lot ; conserver la convention `proposition_ether` du compte rendu1.5 si tu archives le JSON.

## Contrôles et portée

- `2026-10-03_ether_grille_couverture.md` : neuf catégories dans treize zones, corridors parcourus, preuves obtenues et lacunes recherchées. P signifie couverture partielle, pas exhaustivité. Caucase/Turquie et les zones suivantes restent à faire. Sud de Sakhaline et Kouriles alors japonais exclus du périmètre soviétique de cette remise ; ne pas anticiper août1945.
- `2026-10-03_ether_selection_audit.md/json` : décision et motifs pour chaque candidat, preuves individuelles, rôles retirés. Aucun quota national. Les centres administratifs structurants et petits relais habités sont inclus ; `ville` est le type de repère, pas une attribution de statut juridique urbain.
- `2026-10-03_ether_reserves_revue_finale.md/json` : R16-01 à R16-69, preuves/limites, impact, choix. Les49 candidats différés ne figurent pas dans les données.
- `2026-10-03_ether_positions_recherche.json` : valeurs P625 brutes, QID, déclaration choisie, arrondi et fichier API lu. Repères actuels, aucun centre de1945 certifié. Kagan/Kyzyl-Kiya et sites déplacés non résolus différés. Kraskino et Possiet, à environ4,9km, sont deux peuplements distincts (Q1072466/Q1966124), deux extrémités nommées des branches de1941 ; aucune fusion.
- `2026-10-03_ether_index_sources.md` : URLs et localisateurs. Notes françaises, originaux fidèles. Les archives/PDF/images conservés restent des preuves de travail interne ; ne pas republier automatiquement les reproductions.
- `2026-10-03_ether_controle_livraison.json` : vérifications structurelles, références, pays P17 actuel, coordonnées, doublons et empreintes des fichiers. Ne vaut pas confirmation historique automatisée.

## Choix prudents appliqués à cette proposition

Capitales des cinq RSS : `regionale`, selon la convention déjà intégrée. Oulan-Bator : `nationale`. Iakoutsk, Oulan-Oudé et Noukous portent le rôle capitale sans type d’affichage : Q15-02/R16-02 reste réservé. Les chefs-lieux d’oblast n’obtiennent aucun attribut de capitale par défaut. Aucun `nom_local`.

Fiche = repère actuel ; nom de l’état = forme attestée proposée à la date, aliases limités. Babouchkine remplace le Myssovsk du premier carnet après lecture de la notice sur1941. Les translittérations et priorités d’exonymes restent à harmoniser transversalement. Dates de validité inconnues selon le gabarit ; la référence du Snapshot est portée dans les métadonnées, sans fondation ou fermeture inventée.

Le rail d’une gare distante n’est pas attribué automatiquement à la vieille ville : notamment Karchi, Termez, Kokchetav et Kanibadam. Les escales connues seulement par1929 perdent leur rôle fluvial si aucune corroboration ultérieure n’a été lue. Pas de rôle militaire tiré de la seule industrie de guerre. `roles: []` uniquement pour Sükhbaatar : transit routier documenté en note, sans créer un mot-clé nouveau.

Les ports et relais ferroviaires/air sont des **fonctions de villes**, sans entités autonomes de port, gare, aéroport ou voie. Quai en service, complexe en chantier et trafic normal restent distingués. Les ouvertures de ligne d’après-guerre et déplacements postérieurs n’entrent pas au Snapshot.

## Réponses 1.5 jointes et suite

Lire `../villes_1-5/2026-10-03_ether_reponses_cycle2.md` : Q15-01 close ; Q15-02/04 en réserve ; Q15-03 précisée par13 compléments documentaires (onze demandes, Kichinev, Soumy). Aucun changement d’entité1.5 proposé. Le supplément administratif1944, ajouté dans ce delta1.6, porte aussi les sept cibles du complément limité Q15-02.

Pour ton retour, distinguer intégré, corrigé, non vérifié et réservé, avec IDs et passages. Les autres sources non confirmées du1.5 ne sont pas globalement levées. Les fichiers globaux de réserves et de sources à valider restent de ton ressort.

Après remise vérifiée : attente du retour de Claude, réveil horaire réactivé. Au retour actionnable : réponses au1.6 et **un seul prochain lot1.7 Caucase/Turquie**, préparés puis remis ensemble dans la couche villes autorisée. Balkans/Grèce/Italie, Ibérie/marges et audit transversal restent ensuite. Nouveau feu vert avant toute autre couche ou progression mensuelle.
