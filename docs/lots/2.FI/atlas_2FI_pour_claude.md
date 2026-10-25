# Finlande — 2.FI, cycle 1, pour Claude

Proposition : **58 fiches, 10 échelons 1 et 48 échelons 2 ; aucun tracé ; 7 nouvelles sources et 6 réserves**. Snapshot au 1er janvier 1945 à 00:00. Les trois fichiers de données sont complets. Réception et intégration restent à constater dans ton retour.

## Q2FI-01 — Échelons et fonction

Le découpage de droit retenu est la province **lääni** puis le district administratif rural **kihlakunta** (suédois **härad**). Åland a le statut particulier de **maakunta/landskap** autonome et demeure une circonscription de l’administration d’État ; une seule fiche d’échelon 1 est proposée. Les villes sont listées séparément des districts ruraux dans l’annuaire : aucune affectation automatique d’une ville au district de même nom. Les communes ne sont pas ajoutées ; les districts judiciaires (tuomiokunta/domsaga), ecclésiastiques ou forestiers ne sont pas assimilés à ces districts administratifs.

## Q2FI-02 — Inventaire et noms datés

L’annuaire officiel 1944–45, publié en 1946, donne explicitement le découpage au début de 1945 au tableau 2 p.1 (PDF25), et le détail territorial au tableau 15 p.14–37 (PDF37–48). Les colonnes de populations portent plusieurs dates et ne servent pas à rétablir des territoires cédés. Les captures ont été lues, pas seulement leur OCR.

| Province | Nom officiel transcrit | Districts retenus | Noms courts |
|---|---|---:|---|
| Uusimaa | Uudenmaan lääni | 4 | Raasepori, Lohja, Helsinki, Pernaja |
| Turku et Pori | Turun-Porin lääni | 9 | Vehmaa, Mynämäki, Piikkiö, Halikko, Masku, Ulvila, Ikaalinen, Tyrvää, Loimaa |
| Åland | Ahvenanmaan maakunta | 1 | Åland |
| Häme | Hämeen lääni | 6 | Tammela, Pirkkala, Ruovesi, Jämsä, Hauho, Hollola |
| Viipuri (partie finlandaise) | Viipurin lääni | 3 | Kymi, Lappee, Jääski |
| Mikkeli | Mikkelin lääni | 4 | Heinola, Mikkeli, Juva, Rantasalmi |
| Kuopio | Kuopion lääni | 6 | Rautalampi, Kuopio, Iisalmi, Liperi, Ilomantsi, Pielisjärvi |
| Vaasa | Vaasan lääni | 8 | Närpiö, Ilmajoki, Korsholm, Lapua, Pietarsaari, Kuortane, Laukaa, Viitasaari |
| Oulu | Oulun lääni | 4 | Sälöinen, Haapajärvi, Kajaani, Oulu |
| Laponie | Lapin lääni | 3 | Rovaniemi, Kemi, Kittilä |

**Réserve d’inventaire :** le tableau 3 donne **54** kihlakunnat (dont **9** sous Viipuri). Le tableau 15 permet de documenter **48** unités dans les parties conservées, avec des transferts explicitement datés du 1.1.1945. Les sept autres noms rencontrés dans les lignes historiques/cédées de Viipuri ne fournissent pas une explication arithmétique simple de l’écart de six. Les registres d’évacués ont pu subsister après les cessions, mais cette explication ne réconcilie pas à elle seule le compte national. Merci de contrôler ce point R2FI-02 sans bloquer les fiches indépendamment documentées. Le lot ne prétend pas couvrir tout le système résiduel de bureaux ni tous les territoires urbains.

**Viipuri** est conservé comme nom au jour du Snapshot. La sous-rubrique « Kymen lääni » du tableau 15 est rétrospective ; le projet de loi Finlex mentionne la formation de Kymi en 1945 sans en établir ici le jour. La province proposée est uniquement le reste finlandais ; aucun rattachement de Vyborg soviétique, aucun siège induit du nom. Voir R2FI-03.

## Q2FI-03 — Tracés, licence et attributions

La FeatureCollection est vide et les fiches n’ont aucun geometrie_ref. La piste historique effectivement examinée est **SAPO**, produite par le **FinnONTO Consortium / SeCo, Aalto University**, traitée et diffusée dans **Sorvi par Pyry Kantanen / rOpenGov**. **CC BY 4.0**, attestée par la page Hipla, est une licence acceptée : elle n’est pas en cause.

Révision Sorvi fixée : `65a9a2c57dac4fe54cbbdc695cfa34f180229932`. Les fichiers sources et leurs empreintes sont conservés. La sélection exacte des instances communales actives en 1945 donne 547 instances, dont 463 avec une géométrie associée et 84 sans. La fonction get_municipalities peut remplacer les manques par une géométrie antérieure ; cette reprise n’est pas utilisée. L’article signale notamment simplification, enclaves manquantes et villes parfois couvertes par une commune rurale. Sans jointure historique complète des communes vers provinces/districts et sans contrôle des cessions/bail au jour exact, aucune dissolution n’est présentée comme un contour de 1945 validé. Les 463 associations ne constituent pas 463 géométries validées pour l’Atlas.

Signalement pour **ta** liste 00_SUBDIVISIONS_SANS_TRACE.md : [SAPO via Sorvi](https://ropengov.github.io/sorvi/articles/finnish-historical-maps.html), [licence et auteurs](https://dev.hipla.fi/). Piste libre à conserver pour la Finlande, avec ces limites ; aucune nouvelle campagne et aucune modification de ton fichier par Ether. Les catalogues administratifs modernes NLS et StatFin ont été repérés mais ne prouvent pas les provinces de 1945 ; aucune géométrie moderne réétiquetée.

## Q2FI-04 — Cas particuliers et raccords

- **Åland** : loi du 6.5.1920, §§1–4 (PDF1, p.954), autonomie et gouverneur de l’État. Le texte original n’est pas une consolidation des amendements antérieurs à 1945. Mariehamn est séparée d’Ålands härad dans l’annuaire ; le district rural n’est pas une seconde copie de toute la province. Ni loi de 1951 ni régime de 1991 anticipés.
- **Frontière soviétique** : pas de rétablissement de Petsamo ou de la Carélie cédée. Les superficies de l’annuaire et les notes datées priment sur les registres de population évacuée. Les petites parties conservées sont signalées ; aucun contour de raccord non vérifié n’est livré.
- **Transferts au 1.1.1945** : Vahviala conservé→Kymi, Nuijamaa conservé→Lappee, Parikkala/Saari/Simpele conservés→Jääski ; Uukuniemi conservé→Liperi/Kuopio ; Korpiselkä conservé→Ilomantsi/Kuopio. Inari et Utsjoki→Kittilä/Lapland. Note 2 p.36–37 lue visuellement : 1945, malgré l’OCR fautif.
- **Porkkala et Laponie nord-ouest** : parents de droit finlandais ; contrôles soviétique et allemand déjà représentés dans les territoires canoniques. Ces superpositions ne deviennent pas deux nouvelles provinces ni un système concurrent.
- **Suède et Norvège** : aucune modification des frontières nationales canoniques et aucun raccord géométrique artificiel. Pas d’extension vers les anciennes limites finlandaises, ni vers un découpage nordique contemporain.

## Chefs-lieux et contrôles

Aucun chef-lieu ou code n’est proposé par simple homonymie ; aucune nouvelle ville ni liste de villes à créer. Les ID distinguent les provinces/districts des villes homonymes ; les noms officiels historiques restent dans les états datés. Pas de recopie des nombres de population ou de superficie comme propriétés validées.

Contrôles avant remise : IDs/parents, source de chaque fiche, dates exactes des transferts, séparation 10 provinces/48 districts, preuves locales, empreintes, références de réserves et précontrôle en mémoire du véritable intégrateur. Les deux documents `atlas_2FI_controle_livraison.json` et `atlas_2FI_manifest.json` consignent le résultat technique ; ils ne simulent pas une relecture Claude. Six réserves restent ouvertes pour ton retour et le bilan de Guizmo. Trois cycles maximum pour ce lot.

La file et la reprise sont tenues dans coordination. Islande suit dès qu’une place est disponible ; rien ne rouvre les anciens groupes ou une autre couche.
