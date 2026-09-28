# Atlas Eurasie

Atlas historique interactif des flux eurasiatiques (frontières, routes, migrations…) du **1er janvier 1945, 0 h** à aujourd'hui.

Une carte qu'on peut agrandir et réduire, et un curseur de date. À chaque date, la carte est **recalculée** à partir de l'état valable ce jour-là pour chaque frontière, territoire, pont, route… Les pastilles d'événements ouvrent une fiche sourcée.

## Où se trouve quoi

```
Atlas/
├─ README.md                  ← ce fichier
├─ docs/
│   ├─ recap_technique.md     ← toutes les décisions techniques jusqu'au 25/09/2026
│   ├─ JOURNAL_DECISIONS.md   ← chaque décision datée depuis (à lire en premier)
│   ├─ SUIVI_RATISSAGE.md     ← où en est chaque zone et chaque couche
│   ├─ LEXIQUE_ID.md          ← codes pays, mots-clés, acteurs, relations
│   ├─ protocole_sources.md   ← comment on enregistre et cite une source
│   ├─ LICENCES_ET_ATTRIBUTIONS.md ← ce qu'on a le droit de faire avec chaque donnée, et comment créditer
│   └─ pour_ether/            ← notes de Claude à transmettre à Ether
├─ gabarits/                  ← modèles JSON : entité temporelle, événement
├─ data/
│   ├─ sources/               ← registre central des sources (une source = un source_id)
│   ├─ snapshot0/             ← état de l'Eurasie au 1945-01-01, lot par lot (01 Nord/Est, 02 Pologne-Allemagne-Autriche-Baltes)
│   ├─ geometries/            ← un fichier .geojson par tracé, avec sa provenance
│   └─ prototype_v0/          ← données 100 % FICTIVES pour tester le moteur (Ruritanie, Kovalie…)
├─ outils/geo/                ← scripts qui fabriquent les tracés (trace d'audit)
└─ app/                       ← le code de la carte : React + Vite + MapLibre (voir app/README.md)
```

## Lancer la carte

Dans `app/` : `npm install` (la première fois), puis `npm run dev`. Contrôle des données : `npm run validate:data`.

## Règles de rangement

- **Ce dépôt est la version officielle.** Un fichier existe une seule fois ; une mise à jour remplace le fichier, et Git garde l'historique.
- **Pas de copies** « v2 », « vierge » ou « final ». Le numéro de version vit dans les métadonnées du fichier.
- **Une décision n'existe que si elle est dans `docs/JOURNAL_DECISIONS.md`.**

## Équipe

- **Guizmo** : décide, teste, fait le lien entre les deux IA.
- **Ether (ChatGPT)** : recherche historique, ratissages.
- **Claude** : technique, architecture, contrôle de cohérence, tenue du dépôt.
