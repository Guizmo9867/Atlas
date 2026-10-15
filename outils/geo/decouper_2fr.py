"""Lot 2.FR : écrit une géométrie par fichier (data/geometries/snapshot0/<geometry_id>.geojson) à partir des
tracés d'Ether simplifiés avec mapshaper (simplification topologique : les limites partagées restent communes).
  npx mapshaper@0.6 atlas_2FR_geometries_proposees.geojson -filter "geometry_id.indexOf('commissariat')<0" -simplify interval=400 keep-shapes -clean -o dep.geojson precision=0.00001
  npx mapshaper@0.6 atlas_2FR_geometries_proposees.geojson -filter "geometry_id.indexOf('commissariat')>=0" -simplify interval=600 keep-shapes -clean -o reg.geojson precision=0.00001
Usage : python decouper_2fr.py dep.geojson reg.geojson <dossier de sortie>
"""
import json, sys, pathlib
sortie = pathlib.Path(sys.argv[3]); sortie.mkdir(parents=True, exist_ok=True)
n = 0
for fichier, pas in ((sys.argv[1], 400), (sys.argv[2], 600)):
    for f in json.load(open(fichier, encoding='utf-8'))['features']:
        p = dict(f['properties'])
        for k, v in list(p.items()):
            if isinstance(v, str) and v[:1] in '[{':
                try: p[k] = json.loads(v)
                except Exception: pass
        alpin = p.get('statut') == 'reserve_alpine_ne_pas_integrer'
        props = {
            'geometry_id': p['geometry_id'], 'date_validite': '1945-01-01',
            'statut': 'provisoire_reconstruction_trfgis_1940' + ('_reserve_alpine' if alpin else ''),
            'entite_id': p.get('entite_id'), 'millesime_source': p.get('millésime_source', '1940'),
            'licence': 'CC BY 4.0', 'attribution': p.get('attribution'),
            'precision': f"reconstruction nationale (~1:1 000 000), simplifiée au pas de {pas} m (mapshaper, topologie conservée)",
            'limite': p.get('limite'),
            'reserves': ['R2FR-01'] + (['R2FR-02'] if alpin else []),
            'sources': p.get('sources'), 'operations': (p.get('operations') or []) + [f'simplification mapshaper interval={pas} m keep-shapes, nettoyage (Claude, 15/10/2026)'],
            'auteur': 'Ether (proposition), Claude (intégration)', 'date_creation': '2026-10-15',
            'script': 'outils/geo/decouper_2fr.py',
        }
        if alpin:
            props['points_a_verifier'] = "Frontière alpine d'avant 1947 non restituée : les petites cessions italiennes de 1947 (traité de Paris, art. 2) ne sont pas retirées. Affiché par décision de Guizmo (15/10/2026), avec réserve R2FR-02."
        (sortie / f"{p['geometry_id']}.geojson").write_text(json.dumps({'type': 'Feature', 'geometry': f['geometry'], 'properties': props}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        n += 1
print(n, 'géométries écrites')
