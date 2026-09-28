# Lot 03 — géoréférencement des cartes militaires

Trace d'audit des étapes qui produisent les lignes utilisées par `../deriver_snapshot0_lot03.py`. Les images des cartes ne sont pas versionnées (téléchargées dans le cache).

| Carte | Source (registre) | Méthode | Écart |
|---|---|---|---|
| LOC, 12e groupe d'armées, situation du 01/01/1945 à midi (1:1 000 000) | `src-loc-12ag-1945-01-01` | `chamfer.py` : ~9 900 points des fleuves Natural Earth ajustés sur les fleuves bleus de la carte (Lambert + polynôme d'ordre 2) ; `front_loc.py` / `front_loc2.py` : trait noir épais (seuil + ouverture morphologique + squelette + plus court chemin) ; `inverse_loc.py` : pixels → lon/lat | ≈ 1-2 km |
| West Point n° 75a (Alsace, janvier 1945) | `src-westpoint-alsace-colmar-1945` | `colmar_wp75.py` : calage affine sur 13 villes, ligne du 20/01 relevée à la main | 1,8 km en moyenne |
| West Point n° 71 (situation du 15/12/1944) | `src-westpoint-general-situation-1944-12-15` | `chamfer71.py` : côtes et fleuves Natural Earth ajustés sur la carte ; `poches_wp71.py` : arcs rouges | ≈ 3 km (carte ≈ 1:5 000 000) |

Résultats (versionnés) : `front_loc_12ag_lonlat.json`, `colmar_sud_wp75_lonlat.json`, `poches_wp71_lonlat.json`.
`grille.py` et `overlay.py` servent au contrôle visuel (grille de pixels, superposition des fleuves projetés).

Téléchargement de la carte LOC (IIIF, 50 %) :
`https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5701:g5701s:ict21211/full/pct:50/0/default.jpg`
