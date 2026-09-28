# Atlas — Lexique des identifiants

Ce fichier trace chaque code et chaque mot-clé utilisé dans un ID ou un identifiant sémantique, pour éviter les synonymes involontaires (URSS / Union soviétique / USSR, ouverture / inauguration / mise-service…).

On le construit au fil de l'eau, jamais à l'avance. **Avant de créer un ID : chercher ici. Si le mot n'y est pas, l'ajouter.**

## 1. Formats d'ID (verrouillés)

- **Événement** : `annee-pays-motcle-titre` → `1945-de-partition-berlin`
- **Entité** : `type-pays-motcle[-precision]` → `territoire-su-kazakhstan`
- **Géométrie** : `geom-<entite_id>-<AAAA-MM-JJ>` → `geom-territoire-su-petsamo-1945-01-01`
- **Source** : `src-<institution>-<référence>` → `src-frus-1946-v04-d5`
- Minuscules, sans accents, sans apostrophes, séparés par `-`, courts. **Immuables** une fois intégrés.
- Un ID d'entité **commence par son `type_entite` exact** : `territoire-`, `frontiere-`, `ligne_front-`, `poste_frontiere-`… (vérifié par le validateur).
- L'ID désigne le **lieu ou la chose stable**, jamais son statut à une date.
- Le préfixe pays = le pays du **premier état** de l'entité dans le corpus. Il ne change jamais ensuite.

## 2. Codes pays (2 lettres, minuscules)

**Règle** : préfixe = code **ISO 3166-1 alpha-2**, en minuscules. Pour un État disparu, on prend son **ancien code alpha-2** quand il en a eu un (`su`, `yu`, `cs`, `dd`).

*Précision (correction d'Ether, 28/09/2026)* : ces anciens codes ne sont PAS des codes ISO 3166-3. La norme ISO 3166-3 donne aux pays disparus des codes à **4 lettres** (`SUHH`, `YUCS`, `CSHH`, `DDDE`). On garde les 2 lettres pour des IDs courts. Pour un État qui n'a jamais eu de code alpha-2, on décidera au cas par cas et on le notera ici.

| Code | Pays | Utilisé dans |
|---|---|---|
| `su` | URSS (ancien alpha-2 ; ISO 3166-3 : SUHH) | lot 01 |
| `fi` | Finlande | lot 01 |
| `mn` | Mongolie | lot 01 |
| `yu` | Yougoslavie (ancien alpha-2 ; ISO 3166-3 : YUCS) | réservé |
| `cs` | Tchécoslovaquie (ancien alpha-2 ; ISO 3166-3 : CSHH) | réservé |
| `dd` | RDA, à partir de 1949 (ancien alpha-2 ; ISO 3166-3 : DDDE) | réservé |
| `xa`, `xb`, `xc`… | **FICTIF** — codes alpha-2 réservés par l'ISO à l'usage privé | prototype V0 uniquement |
| `de` | Allemagne | lot 02 |
| `at` | Autriche | lot 02 |
| `pl` | Pologne | lot 02 |
| `fr` | France | lot 03 |
| `ch` | Suisse | exemple du gabarit |
| `dk` | Danemark (Féroé comprises : `territoire-dk-feroe`) | lot 03 |
| `no` | Norvège | lot 03 |
| `se` | Suède | lot 03 |
| `is` | Islande | lot 03 |
| `gb` | Royaume-Uni | lot 03 |
| `je` | Jersey (dépendance de la Couronne : code propre) | lot 03 |
| `gg` | Guernesey (idem) | lot 03 |
| `ie` | Irlande | lot 03 |
| `be` | Belgique | lot 03 |
| `lu` | Luxembourg | lot 03 |
| `nl` | Pays-Bas | lot 03 |

## 3. Types d'entités

`frontiere` · `route` · `pont` · `port` · `ferry` · `poste_frontiere` · `territoire` · `voie_ferree` · `ligne_front` · `autre`

## 4. Mots-clés utilisés dans les IDs

| Domaine | Mot-clé | Sens | Premier usage |
|---|---|---|---|
| territoire | `urss` | l'État fédéral soviétique dans son ensemble | `territoire-su-urss` |
| territoire | `kazakhstan` | RSS kazakhe | `territoire-su-kazakhstan` |
| territoire | `touva` | Touva (oblast autonome en 1945) | `territoire-su-touva` |
| territoire | `mongolie` | Mongolie extérieure | `territoire-mn-mongolie` |
| territoire | `finlande` | l'État finlandais dans son ensemble | `territoire-fi-finlande` |
| territoire | `petsamo` | Petsamo / Pechenga | `territoire-su-petsamo` |
| territoire | `porkkala` | Porkkala-Udd (zone de la base navale) | `territoire-fi-porkkala` |
| territoire | `allemagne` | l'Allemagne, frontières du 31/12/1937 | `territoire-de-allemagne` |
| territoire | `autriche` | l'Autriche, frontières de 1937 | `territoire-at-autriche` |
| territoire | `pologne` | l'État polonais | `territoire-pl-pologne` |
| territoire | `estonie`, `lettonie`, `lituanie` | les RSS baltes | `territoire-su-estonie`… |
| territoire | `courlande` | poche de Courlande (contrôle allemand) | `territoire-su-courlande` |
| territoire | `memel` | territoire de Memel / Klaipėda | `territoire-de-memel` |
| territoire | `dantzig` | Ville libre de Dantzig / Gdańsk | `territoire-de-dantzig` |
| frontiere | `su-est` | frontière orientale Pologne–URSS | `frontiere-pl-su-est` |
| territoire | `laponie-nord-ouest` | bras nord-ouest de la Laponie finlandaise tenu par les Allemands (1944-1945) | `territoire-fi-laponie-nord-ouest` |
| ligne_front | `su-est-europe` | front germano-soviétique en Europe orientale | `ligne_front-de-su-est-europe` |
| ligne_front | `laponie` | front germano-finlandais de Laponie (Lätäseno) | `ligne_front-de-fi-laponie` |
| ligne_front | `ouest-europe` | front occidental Alliés / Allemagne | `ligne_front-de-ouest-europe` |
| territoire | `danemark`, `feroe`, `norvege`, `suede`, `islande`, `royaume-uni`, `jersey`, `guernesey`, `irlande`, `belgique`, `luxembourg`, `pays-bas` | l'État ou le territoire dans son ensemble | `territoire-dk-danemark`… |
| territoire | `est-finnmark` | Finnmark à l'est de la Tana (libéré, 1944-1945) | `territoire-no-est-finnmark` |
| territoire | `poches-atlantiques` | poches allemandes du littoral français (Dunkerque → Royan) | `territoire-fr-poches-atlantiques` |
| territoire | `poche-colmar` | poche de Colmar | `territoire-fr-poche-colmar` |
| territoire | `zone-allemande-ardennes` | partie d'un pays tenue par les Allemands dans le saillant des Ardennes | `territoire-be-zone-allemande-ardennes`, `territoire-lu-…` |
| territoire | `zone-allemande-nord-est` | secteur français tenu par les Allemands au nord-est (Bitche) | `territoire-fr-zone-allemande-nord-est` |
| territoire | `zone-liberee-sud` | partie libérée d'un pays occupé | `territoire-nl-zone-liberee-sud` |
| territoire | `zone-alliee-ouest` | territoire allemand tenu par les Alliés à l'ouest | `territoire-de-zone-alliee-ouest` |
| territoire | `partition` | partage d'un territoire | `1945-de-partition-berlin` (exemple) |

## 5. Identifiants sémantiques (acteurs, alignements)

Valeurs de `souverainete_id`, `controle_id`, `alignement_id`. Courts, toujours les mêmes. La nuance va dans `note`.

**Acteurs** — un acteur = un seul ID ; le régime politique va dans `regime_id` (`allemagne_nazie`, `republique_populaire`).

| ID | Acteur |
|---|---|
| `urss` | Union soviétique |
| `finlande` | Finlande |
| `republique_de_chine` | République de Chine (gouvernement nationaliste) |
| `republique_populaire_mongole` | République populaire mongole |
| `allemagne` | Allemagne (l'État ; le régime nazi va dans `regime_id: allemagne_nazie`) |
| `autriche` | Autriche |
| `pologne` | Pologne |
| `danemark`, `norvege`, `suede`, `islande`, `irlande`, `france`, `belgique`, `luxembourg`, `pays_bas` | les États du lot 03 |
| `royaume_uni` | Royaume-Uni |
| `couronne_britannique` | la Couronne, souveraine de Jersey et Guernesey (pas le Royaume-Uni) |
| `feroe` | autorités féroïennes (Løgting, préfet) — `administration_id` des Féroé |
| `etats_unis` | États-Unis (armées américaines) — acteur sans territoire dans le corpus : son camp est donné dans `CAMP_HORS_CORPUS` (palettes.ts) |

**Régimes** (`regime_id`) : `allemagne_nazie`, `republique_populaire`, `gprf` (Gouvernement provisoire de la République française).

**Alignements** — Snapshot 0 : **4 familles principales + statuts particuliers quand les faits l'exigent** (règle du 28/09/2026). Occupation = hachures, front = bande. Les couleurs vivent dans `app/src/theme/palettes.ts`, jamais dans les données.

| ID | Sens | Famille visuelle |
|---|---|---|
| `allies_ww2` | puissances alliées dans la guerre en cours (URSS comprise) | bleu |
| `axis_ww2` | **Allemagne nazie** et territoires administrés directement par son appareil d'État | anthracite |
| `axis_associe_ww2` | États alliés, satellites ou gouvernements associés à l'Axe (ex. Slovaquie) | gris / brun sombre |
| `neutral_ww2` | neutres ou hors du conflit affiché | blanc / ivoire |
| `anti_axis_non_allied` | statut particulier : hors des coalitions, mais en guerre contre l'Axe (Finlande au 01/01/1945) | ivoire |
| `pro_sovietique_non_belligerant` | statut particulier : lié à l'URSS, non belligérant (Mongolie jusqu'au 10/08/1945) | ivoire + liseré bleu |
| `occupe_hors_coalitions` | statut particulier : pays occupé dont le gouvernement n'est dans aucune coalition (Danemark au 01/01/1945) | ivoire + hachures de l'occupant |
| `soviet_bloc` | bloc soviétique (guerre froide, plus tard) | — |

**Règle « pays occupé ≠ Axe »** (lot 03, 28/09/2026) : un territoire garde le camp de son souverain (hérité du parent pour une zone) ; l'occupation se lit par des **hachures à la couleur du camp de l'occupant** (anthracite = Allemagne, bleu = Alliés ; rayures claires si l'occupant est du même camp, ex. Est-Finnmark).

## 6. Types de relations

| Type | Usage |
|---|---|
| `precede` / `suit` | ordre chronologique |
| `entraine` | cause directe |
| `modifie` | un événement modifie une entité |
| `explique` | lien narratif ou causal **uniquement** |
| `detache_de` | ce territoire a été retiré à la cible (cession, annexion…) |

L'appartenance à un territoire parent ne passe **pas** par une relation mais par `proprietes.parent_id` dans chaque état (datable).

## 7. Propriétés d'un état (rappel)

| Propriété | Sens |
|---|---|
| `souverainete_id` | à qui le territoire appartient légalement — **absent** si contesté / non tranché |
| `souverainete_revendiquee_par` | liste des acteurs qui le revendiquent quand la souveraineté est contestée (ex. `["urss"]`) |
| `controle_id` | qui le tient réellement (militairement) |
| `administration_id` | qui l'administre civilement, si différent du contrôle militaire |
| `alignement_id` | famille ou statut particulier (mode Alignements) |
| `regime_id` | régime politique (`allemagne_nazie`, `republique_populaire`…) |
| `parent_id` | territoire qui le contient à cette date |
| `statut_administratif`, `note` | précisions libres |

**Dans un fichier de géométrie** (`data/geometries/…`), en plus de la provenance : `reference_temporelle` = `{snapshot, observation_source, ecart, statut: "derniere_situation_connue_avant_snapshot", etat_suivant?, note?}` quand le tracé vient d'une source datée. Règle : on prend la **dernière situation connue avant** l'état représenté (ex. carte du 31/12/1944 à 12:00 pour le Snapshot du 01/01 à 00:00) ; ce qui est observé après devient un état suivant.
