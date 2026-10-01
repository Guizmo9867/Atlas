"""Liste des sources à faire valider par un humain (Guizmo, plus tard la communauté).

Prend dans le registre toutes les sources que Claude n'a pas pu confirmer (non vérifiée, lecture partielle,
faible, lien cassé) et écrit data/sources/sources_a_valider.json. La page web « Sources à valider »
(artifact claude.ai) est générée à partir de ce fichier ; les validations faites sur la page sont ensuite
relues par Claude et reportées au registre (champ verification_humaine).
Relancer : python outils/sources/liste_sources_a_valider.py (depuis la racine du dépôt).
"""
import json, glob, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
reg = json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))
noms = {}
for f in glob.glob(str(RACINE / 'data/snapshot0/*.json')):
    for e in json.load(open(f, encoding='utf-8')).get('entites', []):
        noms[e['entite_id']] = e.get('nom_court') or e['nom']

GROUPE = {'non_verifiee': 'a_lire', 'limite': 'partielle', 'faible': 'partielle', 'lien_casse': 'lien_mort'}
liste = []
for s in reg['sources']:
    v = s.get('verification_claude')
    if v not in GROUPE: continue
    groupe = 'remplacee' if s.get('statut_usage') == 'non_verifiee_remplacee' else GROUPE[v]
    liste.append({
        'id': s['source_id'], 'groupe': groupe, 'statut_claude': v, 'niveau': s.get('niveau'),
        'titre': s.get('titre'), 'institution': s.get('institution'), 'url': s.get('url'),
        'ou_regarder': s.get('locator') or '', 'extrait': s.get('resume_passage') or '',
        'notes': s.get('notes') or '',
        'villes': [noms.get(c, c) for c in s.get('cibles', [])],
        'remplacee_par': s.get('sources_remplacement', []),
    })
ordre = {'a_lire': 0, 'partielle': 1, 'lien_mort': 2, 'remplacee': 3}
liste.sort(key=lambda x: (ordre[x['groupe']], x['id']))
sortie = RACINE / 'data/sources/sources_a_valider.json'
sortie.write_text(json.dumps({'version_registre': reg['metadata']['version'], 'sources': liste}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(liste), 'sources à valider ->', sortie.relative_to(RACINE))
