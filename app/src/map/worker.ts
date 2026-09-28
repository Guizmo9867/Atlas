// MapLibre v6 lance un « worker » (un fichier de calcul séparé) pour découper les données.
// Vite doit l'emballer lui-même, sinon le navigateur ne le trouve pas : on lui donne l'adresse ici.
import { setWorkerUrl } from 'maplibre-gl'
import workerUrl from 'maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url'

setWorkerUrl(workerUrl)
