# Atlas — Corrections du lot 01 et règles pour les prochains ratissages

*De Claude, pour Ether. Transmis par Guizmo le 26/09/2026.*

Le lot 01 Nord/Est est **bon sur le fond** : sourçage solide, aucune géométrie inventée, dates propres. Les corrections ci-dessous portent sur la **forme**, pour que les prochains lots s'emboîtent sans doublons. Tout est déjà appliqué dans la version 0.2 du lot 01 : rien à refaire de ton côté, seulement à appliquer pour la suite.

À partir de maintenant, le dépôt GitHub `Atlas` est la **version officielle** de tous les fichiers (gabarits, registre, lots). Claude y range chaque nouvelle version et signale ce qui a changé. Plus besoin de renvoyer des copies « v2 » ou « final ».

---

## 1. La correction de 1947 (Petsamo, Porkkala, Finlande)

**Le fait** : l'armistice de Moscou du 19/09/1944 organise le retour de Petsamo à l'URSS et le bail de Porkkala-Udd. Le **traité de paix de Paris avec la Finlande**, signé le **10/02/1947** et **entré en vigueur le 15/09/1947**, **confirme** ces deux points :

- **art. 2** : « Finland confirms the return to the Soviet Union of the province of Petsamo (Pechenga)… » ;
- **art. 4** : la Finlande confirme le bail de 50 ans de Porkkala-Udd (base navale soviétique).

**Ce que ça change** : garder `souverainete_id: urss` pour Petsamo dès 1944 est correct, car le texte de 1947 parle bien d'une *confirmation*. Mais le **statut juridique change** le 15/09/1947 : on passe du régime d'armistice (provisoire) au traité de paix (définitif). Dans notre modèle, un changement = un nouvel état.

**À faire quand le ratissage atteindra septembre 1947** :

| Entité | Action au 15/09/1947 |
|---|---|
| `territoire-su-petsamo` | fermer `etat-01` (`valid_to` 1947-09-15, exacte), ouvrir `etat-02` avec `statut_administratif: territoire_cede_par_traite_de_paix` |
| `territoire-fi-porkkala` | fermer `etat-01`, ouvrir `etat-02` : bail confirmé par traité (souveraineté fi, contrôle su inchangés) |
| `territoire-fi-finlande` | fermer `etat-01`, ouvrir `etat-02` : frontières fixées par le traité de paix |

**Plus tard** : Porkkala revient à la Finlande le **26/01/1956** (accord du 19/09/1955) → nouvel état à ce moment-là.

**À vérifier avec une source A** : la remise *effective* de Porkkala aux Soviétiques daterait du **29/09/1944** (dix jours après l'armistice, le temps d'évacuer la population). Si c'est confirmé, `controle_id: urss` ne commence qu'au 29/09. Pour l'instant, seule Wikipédia le dit (niveau C).

**Source ajoutée au registre** : `src-uk-ts-1948-53-traite-paix-finlande` (texte officiel, UK Treaty Series n° 53 de 1948, vérifié sur le PDF).

---

## 2. Les IDs : préfixe pays = code ISO à 2 lettres

**Règle** : le préfixe pays est le **code ISO à 2 lettres, en minuscules**, y compris l'**ancien code alpha-2** des États disparus *(erratum du 28/09 : ce ne sont pas des codes ISO 3166-3, qui ont 4 lettres, voir LEXIQUE_ID.md)* : `su` = URSS, `yu` = Yougoslavie, `cs` = Tchécoslovaquie, `dd` = RDA.

- Le préfixe = le pays du **premier état** de l'entité dans le corpus. Il ne change **jamais**, même si le territoire change de pays ensuite (l'ID est immuable, la souveraineté vit dans les états).
- L'ID désigne le **lieu stable**, jamais son statut à une date. Pas de `post-armistice-1944`, `bail-sovietique` ou `republique-populaire` dans un ID : ces infos appartiennent aux états, et elles changeront.

| Ancien ID | Nouvel ID |
|---|---|
| `territoire-urss` | `territoire-su-urss` |
| `territoire-urss-kazakhstan` | `territoire-su-kazakhstan` |
| `territoire-urss-rsfsr-touva` | `territoire-su-touva` |
| `territoire-mn-republique-populaire-mongole` | `territoire-mn-mongolie` |
| `territoire-fi-finlande-post-armistice-1944` | `territoire-fi-finlande` |
| `territoire-urss-petsamo` | `territoire-su-petsamo` |
| `territoire-fi-porkkala-bail-sovietique` | `territoire-fi-porkkala` |

Les `geometrie_ref` suivent maintenant une règle fixe : `geom-` + entite_id + `-` + date (ex. `geom-territoire-su-petsamo-1945-01-01`).

Pour les événements, c'est pareil : `pays` = liste de codes (`["fr", "ch"]`), plus de noms en toutes lettres.

Chaque mot-clé et chaque code utilisé est tracé dans `docs/LEXIQUE_ID.md`. **Avant de créer un ID, vérifier le lexique.**

---

## 3. L'appartenance territoriale : `parent_id`, pas `explique`

Dans le lot, `explique` servait à dire « le Kazakhstan fait partie de l'URSS ». Ça posait deux problèmes : `explique` est réservé aux liens narratifs, et pour Petsamo → Finlande, ça laissait croire que Petsamo était encore finlandais.

**Nouvelle règle** :

- **Appartenance** → dans chaque état : `proprietes.parent_id` = l'entité qui contient ce territoire **à cette date**. C'est datable : quand la Crimée passe de la RSFSR à la RSS d'Ukraine en 1954, on ferme l'état et on en ouvre un avec le nouveau `parent_id`.
- **Territoire retiré à un autre** → relation `detache_de` (ex. Petsamo `detache_de` Finlande).
- **`explique`** → uniquement pour un lien de cause ou de récit.

Appliqué au lot 01 : Kazakhstan, Touva et Petsamo → `parent_id: territoire-su-urss` ; Porkkala → `parent_id: territoire-fi-finlande`. Pour Touva, le vrai parent est la RSFSR : on pointera vers elle quand l'entité RSFSR existera.

---

## 4. Les sources : le registre d'abord, puis un simple renvoi

Ton registre est une excellente idée, on en fait la **référence unique**. Chaque source est écrite **une seule fois**, dans le registre, et les fiches ne font plus que pointer vers elle :

```json
"sources": [
  { "source_id": "src-frus-1946-v04-d5", "locator": "", "usage": "clauses territoriales de l'armistice" }
]
```

- `locator` : où exactement (page, article…) ; vide si c'est le même que dans le registre ;
- `usage` : ce que la source prouve **ici**, en une phrase.

Ordre de travail : **source trouvée → ajoutée au registre → référencée dans la fiche**.

Deux sources étaient citées dans le lot mais absentes du registre, je les ai ajoutées : `src-britannica-russia` et `src-encyclopedia-com-mongolia`.

---

## 5. Identifiants d'acteurs courts

`souverainete_id: republique_de_chine_revendication_de_jure` devient `republique_de_chine`. La nuance « revendication de jure » reste dans `note`. Même règle pour `controle_id` et `alignement_id` : **un acteur = un identifiant court, toujours le même** (voir la liste dans le lexique).

---

## 6. Ce qui ne change PAS (confirmé)

- **`valid_to` vide** = état toujours ouvert, jusqu'à ce qu'un document trouvé pendant le ratissage le ferme. C'est voulu, on garde.
- Les `geometrie_ref` non résolues restent une file d'attente de vectorisation. On n'invente aucune géométrie.
- Pas de couleur dans les données, uniquement des identifiants sémantiques.
- Ratissage mensuel pour 1945.

---

## 7. Checklist pour chaque nouveau lot

1. IDs : préfixe ISO, lieu stable, mots-clés présents dans le lexique (ou signalés comme nouveaux).
2. Chaque source présente dans le registre ; les fiches pointent par `source_id`.
3. Appartenance → `parent_id` ; retrait de territoire → `detache_de` ; `explique` = narratif seulement.
4. Acteurs et alignements : identifiants courts, nuances dans `note`.
5. Un changement = un nouvel état ; on n'écrase jamais un état existant.
