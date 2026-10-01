# Route Atlas — réponses à Claude sur les villes 1.3

Complément préparé le 1er octobre 2026. Décisions à intégrer dans le dossier de Claude ; aucune modification du dépôt n’a été exécutée.

## 1. Fusion Miskolc–Diósgyőr : date confirmée

**La date d’effet à retenir est le 1er janvier 1945.** La source est déjà enregistrée dans le lot 1.3 sous `src-13-hu-miskolc-fusion` (S44).

Dans la stratégie culturelle municipale de Miskolc, page imprimée **102** — 102e page du PDF, index technique **101** — le passage porte la formule « 1945. január 1-től Nagy-Miskolc », soit, en français, Grand Miskolc à partir du 1er janvier 1945. Le texte traite ensuite des centres rattachés, dont Diósgyőr et Hejőcsaba. La page a été relue et inspectée visuellement.

[Ouvrir directement la page 102 du PDF municipal](https://www.miskolc.hu/sites/default/files/onkormanyzat/csatolmanyok/2024-11/169_1_mell._kult.strategia_2022-2032.pdf#page=102)

C’est une preuve **B**, une synthèse municipale rétrospective. Elle confirme la date d’effet ; elle ne constitue pas la lecture de l’acte administratif original et ne permet pas d’affirmer que le vote s’est tenu ce jour-là.

Application de la convention verrouillée du projet :

- **Snapshot 0, dernier état avant le 1er janvier à 00:00 :** conserver Miskolc et Diósgyőr distinctes.
- **Chronologie à compter du 1er janvier 1945 :** appliquer la fusion. L’histoire et la fonction industrielle de Diósgyőr restent conservées ; son site peut ensuite être décrit séparément sans simuler deux communes indépendantes.
- Dans les états normalisés, distinguer la date de l’échantillon Snapshot 0 des dates de validité historiques : aucun intervalle pré-fusion vide avec début et fin au même 1er janvier.

Le JSON de corrections joint donne une consigne de normalisation ; il ne prétend pas être un événement déjà conforme au gabarit d’import.

## 2. Košice/Kassa et Ústí/Aussig : corriger la nomenclature datée

**Claude a raison : ces formes historiques ne doivent pas rester seulement des clés de recherche.** Ma livraison 1.3 laissait des libellés actuels sans compléter suffisamment les noms au snapshot.

La règle déjà retenue pour l’Atlas distingue le nom français traditionnel, le nom local à la date, et les alias. Elle conduit ici à la proposition suivante :

| Repère actuel | Nom d’affichage français proposé | Nom local au snapshot | Alias à conserver |
|---|---|---|---|
| Košice | **Cassovie** | **Kassa** | Košice, Kassa, Cassovie |
| Ústí nad Labem | **Aussig** | **Aussig** | Ústí nad Labem, Aussig |

Cassovie est un exonyme français documenté par l’article de Jean Louis Vaxelaire. Son accès intégral étant bloqué, cette preuve est explicitement limitée à l’extrait indexé lu. Kassa, lui, est directement confirmé dans la notice du Musée mémorial de l’Holocauste des États-Unis décrivant le changement de novembre 1938.

Aussig est attesté dans le catalogue des archives municipales : noms d’annuaires anciens et répertoires officiels de la direction postale pour 1939–1940 et 1942. Le catalogue a été lu ; les volumes originaux n’ont pas été feuilletés. Le terme allemand existait déjà avant l’annexion.

### Chronologie à préciser dans la formulation

Ces villes sont examinées **à la date de 1945** ; les rattachements à la Hongrie et au Reich dont il est question remontent à **1938**. L’histoire municipale d’Ústí date l’occupation militaire du 9 octobre 1938. La notice du musée américain situe l’incorporation de Košice et le nom Kassa en novembre 1938.

L’article historique de Veronika Szeghy-Gayer atteste le cadre municipal hongrois et l’arrivée soviétique à Košice le 19 janvier 1945. **Une capture militaire ne suffit pas à dater au jour le changement administratif de nom.** Les dates exactes de retour aux formes locales de l’après-guerre devront donc recevoir leur preuve propre.

### Consigne technique

Conserver les IDs existants : `ville-sk-kosice` et `ville-cz-usti-nad-labem` sont des repères stables du dossier, à rapprocher des IDs canoniques. Le changement de nom ne crée pas une nouvelle ville et ne justifie pas de changer l’ID.

Porter les valeurs historiques dans **l’état temporel utilisé par le rendu**. Une fiche canonique peut conserver un libellé de repérage actuel, mais le rendu du snapshot doit consulter le nom daté. Les alias actuels restent disponibles pour la recherche et la reconnaissance.

La souveraineté et le contrôle restent hérités des territoires. Un nom hongrois ou allemand est une propriété linguistique et historique documentée, pas un substitut aux relations territoriales.

Appliquer cette même règle aux autres entrées concernées du lot 1.3, **sur preuve individuelle** ; aucun remplacement général des noms ne doit être déclenché par la seule couleur d’un territoire.

## Sources et limites de lecture

### 1. src-13-hu-miskolc-fusion

**B** — Miskolc Megyei Jogú Város Kulturális Stratégiája 2022–2032 — résumé historique

Institution : Ville de Miskolc.

[Ouvrir la source](https://www.miskolc.hu/sites/default/files/onkormanyzat/csatolmanyok/2024-11/169_1_mell._kult.strategia_2022-2032.pdf)

Repère : Page imprimée 102, 102e page du PDF, index technique 101. Section sur les décennies d’après-guerre : date d’effet de Grand Miskolc puis liste des centres rattachés.

Limite : Passage relu et page inspectée. Date d’effet du 1er janvier 1945 explicitement donnée ; ni date exacte du vote ni heure d’effet originale vérifiées. Document rétrospectif B ; acte administratif original non consulté.

Lecture : `passage_lu_et_page_verifiee`.

### 2. src-13-sk-kassa-nom-1938

**B** — Zuzana Gruenberger — récit biographique dans Deportations: ID Card/Oral History

Institution : United States Holocaust Memorial Museum — Musée mémorial de l’Holocauste des États-Unis.

[Ouvrir la source](https://encyclopedia.ushmm.org/content/en/gallery/deportations-stories)

Repère : Section Zuzana Gruenberger, paragraphe 1933–1939 : incorporation à la Hongrie et nom Kassa en novembre 1938.

Limite : Notice textuelle lue ; ne fixe pas à elle seule un jour de changement de nom ni le retour du nom slovaque en 1945.

Lecture : `passage_cible_lu`.

### 3. src-13-sk-kosice-admin-1938-1945

**B** — Veronika Szeghy-Gayer, Personálna kontinuita politickej elity v Košiciach po Viedenskej arbitráži [Continuité du personnel de l’élite politique de Košice après l’arbitrage de Vienne], Forum Historiae, 2018, 12(1)

Institution : Forum Historiae — revue de l’Institut d’histoire de l’Académie slovaque des sciences.

[Ouvrir la source](https://www.forumhistoriae.sk/sites/default/files/09-szeghy-gayer-veronika-personalna-kontinuita-politickej-elity-v-kosiciach.pdf)

Repère : Première page du PDF, note 1 et résumé : institutions municipales hongroises ; arrivée soviétique le 19 janvier 1945.

Limite : Début de l’article et passages ciblés lus. La capture du 19 janvier ne donne pas automatiquement la date administrative exacte du retour de Košice comme nom officiel.

Lecture : `passages_cibles_lus`.

### 4. src-13-sk-cassovie-fr

**B** — Jean Louis Vaxelaire, Pistes pour une nouvelle approche de la traduction automatique des noms propres, Meta, 51(4), 2006, p. 719–738

Institution : Les Presses de l’Université de Montréal — revue Meta ; diffusion Érudit.

[Ouvrir la source](https://www.erudit.org/fr/revues/meta/2006-v51-n4-meta1442/014337ar.pdf)

Repère : Extrait indexé comparant Košice, Kassa, Kaschau et Cassovie dans le contexte de 1937.

Limite : Métadonnées et extrait de recherche lus. Ouverture directe bloquée par une protection anti-robot ; l’article intégral n’est pas déclaré lu. Atteste l’exonyme français, pas un acte de nomination de 1944.

Lecture : `extrait_recherche_lu_article_non_ouvert`.

### 5. src-13-cz-aussig-annuaire

**B** — Adresáře, telefonní seznamy a uličnice [Annuaires, répertoires téléphoniques et répertoires de rues]

Institution : Archiv města Ústí nad Labem — Archives municipales d’Ústí nad Labem.

[Ouvrir la source](https://archiv.usti.cz/digitalni-archiv/adresare-telefonni-seznamy-ulicnice.html)

Repère : Annuaires de la ville portant Aussig avant 1938 ; répertoires officiels de la Reichspostdirektion Aussig de 1939–1940 et 1942.

Limite : Catalogue lu ; les ouvrages originaux n’ont pas été feuilletés. Les volumes de 1945 ne sont pas utilisés pour anticiper leur contenu au snapshot. Aussig est une forme allemande plus ancienne, pas un nom inventé en 1938.

Lecture : `notice_catalogue_lue_originaux_non_lus`.

### 6. src-13-cz-usti-occupation-1938

**B** — Dějiny města Ústí nad Labem — Začátek nacistické okupace [Histoire de la ville : début de l’occupation nazie]

Institution : Ville d’Ústí nad Labem / histoire municipale.

[Ouvrir la source](https://www.usti.cz/dejiny/1938-45/ul-7-1.htm)

Repère : Chapitre 1938–1945 : entrée des forces allemandes dans la ville le 9 octobre 1938.

Limite : Le 9 octobre est une date d’occupation militaire dans ce texte ; elle n’est pas assimilée à la date d’un acte légal de changement de nom. Contexte territorial à porter dans les territoires, pas dupliqué dans la ville.

Lecture : `passage_cible_lu`.

## Fichiers du complément

- `atlas_villes_1-3_reponses_claude_2026-10-01.md` : cette réponse, décisions et preuves.
- `atlas_villes_1-3_reponses_claude_corrections_2026-10-01.json` : deux corrections partielles de nomenclature, confirmation de la fusion et consignes communes.
- `atlas_villes_1-3_reponses_claude_sources_delta_2026-10-01.json` : six fiches, dont la mise à jour de S44 et cinq ajouts à réconcilier avec le registre canonique.

Les deux corrections de noms complètent la proposition 1.3 ; elles n’écrasent pas les autres décisions, preuves, rangs ou rôles.
