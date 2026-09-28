# Atlas — Protocole de traçabilité des sources

## Règle générale

Aucun fait, changement de frontière, contrôle, flux, chiffre, tracé ou événement ne doit entrer dans le corpus canonique sans source enregistrée.

Le but n'est pas d'afficher une forêt de citations à l'utilisateur. Le but est que chaque élément de l'Atlas puisse être **audité** :
- d'où vient l'information ;
- quelle source la soutient ;
- où se trouve le passage pertinent ;
- à quelle date la source a été consultée ;
- comment une géométrie a été dérivée d'une carte ou d'un document.

## Registre central

Le fichier `data/sources/atlas_registre_sources.json` contient une entrée unique par source, avec un `source_id` stable.

Exemple :
`src-frus-1945-v07-d662`

Les entités et événements doivent idéalement référencer ce `source_id`. Pour compatibilité avec les gabarits actuels, on peut aussi conserver titre/url/date dans la fiche, mais le registre central reste la référence documentaire.

## Arborescence recommandée

```text
sources/
  registre/
    atlas_registre_sources.json
  raw/
    pdf/
    cartes/
    html/
  captures/
    captures_ecran/
  extraits/
    notes_de_lecture/
  derivations/
    geometries/
    georeferencement/
```

## Pour chaque source

Conserver au minimum :
- `source_id`
- niveau A/B/C
- type de source
- titre
- institution / auteur
- URL ou identifiant permanent
- date de consultation
- période couverte
- zone géographique
- usage dans l'Atlas
- page / section / document / carte précise (`locator`)
- résumé du passage réellement utilisé
- notes d'incertitude

## Copies locales

Quand les droits et les conditions d'utilisation le permettent :
- télécharger le PDF, la carte ou le fichier original ;
- conserver son nom original ;
- calculer un SHA-256 ;
- enregistrer le chemin local dans `archive_locale`.

Pour une page web :
- conserver au minimum l'URL, la date de consultation et le passage/section utilisé ;
- une capture d'écran peut être gardée **comme preuve de travail interne**, mais ne doit pas être publiée automatiquement ;
- éviter d'archiver ou redistribuer massivement du contenu protégé.

## Géométries historiques

Une géométrie ne doit jamais être seulement « tracée à la main ».

Pour chaque géométrie dérivée d'une carte :
- `source_id` de la carte ;
- date de la carte ;
- échelle si connue ;
- logiciel utilisé (QGIS, etc.) ;
- méthode : import direct / vectorisation / géoréférencement ;
- précision estimée ;
- points de contrôle éventuels ;
- date de création de la géométrie ;
- personne/outil ayant réalisé la dérivation.

Exemple de métadonnées :

```json
{
  "geometry_id": "geom-front-ouest-1945-01-01",
  "source_id": "src-loc-12th-army-group-1945-01-01",
  "method": "georeferencement_puis_vectorisation",
  "precision": "jour",
  "incertitude_m": null,
  "logiciel": "QGIS",
  "notes": ""
}
```

## Captures / extraits

Les captures servent à retrouver rapidement un passage, pas à remplacer la source.

Toujours conserver :
1. la référence originale ;
2. le locator précis ;
3. un court résumé du passage ;
4. éventuellement une capture interne.

Ne jamais considérer une capture sans provenance comme une source autonome.

## Hiérarchie de confiance

- **A** : source primaire / officielle / archive / traité / rapport / carte institutionnelle originale.
- **B** : source secondaire solide / universitaire / institution historique reconnue.
- **C** : source exploratoire / locale / témoignage / forum / presse locale, utile pour trouver une piste mais insuffisante seule pour une affirmation majeure.

## Workflow

```text
recherche
→ source trouvée
→ source enregistrée dans le registre
→ passage/locator sauvegardé
→ fait ou géométrie lié au source_id
→ validation
→ corpus canonique
```

Un lien trouvé dans une conversation mais non enregistré dans le registre est considéré comme **non intégré** au corpus.

## Règle éditoriale

L'interface utilisateur peut afficher une citation courte ou un bouton « Sources ». Le corpus interne, lui, conserve davantage de métadonnées que ce qui est montré visuellement.

L'utilisateur doit pouvoir apprendre simplement ; un historien doit pouvoir ouvrir le capot.
