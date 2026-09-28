# Atlas — application (prototype V0)

Carte interactive : React + TypeScript + Vite + MapLibre GL. Le fond de carte vient de Natural Earth (dans `public/fond/`).
Les données ne sont **pas** ici : elles sont lues dans le dossier `data/` à la racine du dépôt.

## Lancer

Dans ce dossier `app/` :

```
npm install        (la première fois seulement)
npm run dev        → ouvre la carte dans le navigateur (http://localhost:5173)
```

Autres commandes :

- `npm run validate:data` : contrôle tout le corpus (IDs, dates, chevauchements d'états, sources, géométries).
- `npm run build` : fabrique la version à mettre en ligne (dossier `dist/`).

## Deux corpus au choix (panneau de gauche)

- **Snapshot 0 — 1er janvier 1945** : les vraies données du lot 01 (URSS, RSS kazakhe, Touva, Mongolie, Finlande, Petsamo, Porkkala). Tracés **provisoires** issus d'OpenHistoricalMap. Clique sur un territoire pour voir d'où vient son tracé et ce qu'il reste à vérifier.
- **Prototype V0 (fictif)** : sert à tester le moteur.

## Ce que le prototype V0 démontre (données 100 % fictives)

- Déplacer le curseur de date recalcule chaque territoire, frontière et pont à partir de ses états.
- **10 janvier** : la Kovalie est occupée par la Cordanie (la souveraineté ne change pas, le contrôle si).
- **15 janvier** : le traité de Valbourg déplace la frontière.
- **18 → 24 janvier** : parcours de réfugiés (pastille « archive » : visible seulement en zoomant).
- **20 janvier** : le pont de Trois-Pins est détruit.
- Clic sur une pastille → fiche de l'événement ; clic sur un territoire ou un pont → historique de ses états.

## Où est quoi

```
src/engine/temporal.ts   ← LA règle du temps (état actif si valid_from <= date < valid_to)
src/engine/features.ts   ← transforme le corpus en couches de carte pour une date
src/theme/palettes.ts    ← les couleurs (elles ne vivent QUE ici)
src/map/                 ← la carte MapLibre
src/timeline/            ← le curseur de date
src/ui/                  ← panneau de gauche, fiches
src/data/corpus.ts       ← quel corpus est chargé
scripts/validate-data.mjs
```
