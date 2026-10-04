"""Liste des sources à faire valider par un humain (Guizmo, plus tard la communauté).

Prend dans le registre toutes les sources que Claude n'a pas pu confirmer (non vérifiée, lecture partielle,
faible, lien cassé) et écrit data/sources/sources_a_valider.json. La page web « Sources à valider »
(artifact claude.ai) est générée à partir de ce fichier ; les validations faites sur la page sont ensuite
relues par Claude et reportées au registre (champ verification_humaine).
Relancer : python outils/sources/liste_sources_a_valider.py (depuis la racine du dépôt).
"""
import json, glob, pathlib, re, collections

RACINE = pathlib.Path(__file__).resolve().parents[2]
reg = json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))
noms = {}
for f in glob.glob(str(RACINE / 'data/snapshot0/*.json')):
    for e in json.load(open(f, encoding='utf-8')).get('entites', []):
        noms[e['entite_id']] = e.get('nom_court') or e['nom']

# Priorité : une source est « importante » si sa validation changerait la carte, c'est-à-dire si elle est
# la preuve d'un rôle encore « À renforcer » dans une ville, ou la preuve d'un nom de 1945.
# Les autres (rôle déjà prouvé par une autre source confirmée, simple contexte) sont « facultatives » :
# elles restent marquées « non vérifiée » sans rien changer à la carte.
RENF = re.compile(r'À renforcer : ([^.]*)\.')
IMPACT = collections.defaultdict(list)
for f in glob.glob(str(RACINE / 'data/snapshot0/*.json')):
    for e in json.load(open(f, encoding='utf-8')).get('entites', []):
        nom_v = e.get('nom_court') or e['nom']
        for et in e.get('etats', []):
            m = RENF.search(et.get('proprietes', {}).get('note', ''))
            renf = {r.strip() for r in m.group(1).split(',')} if m else set()
            for s in et.get('sources', []):
                u = s.get('usage', '')
                if u.startswith('preuve locale : '):
                    roles = sorted({r.strip() for r in re.sub(r' \(.*\)$', '', u[16:]).split(',')} & renf)
                    if roles: IMPACT[s.get('source_id')].append(f"{nom_v} ({', '.join(roles)})")
                elif u.startswith('nom à la date'):
                    IMPACT[s.get('source_id')].append(f"{nom_v} (nom de 1945)")
                else:
                    # Format des lots 1.5 et suivants : l'usage est la liste des rôles (« rail, industrie (lecture partielle) »).
                    # Correction du 04/10/2026 : ces lots n'étaient pas comptés.
                    roles = sorted({r.strip() for r in re.split(r'[,;]', re.sub(r' \(.*$', '', u))} & renf)
                    if roles: IMPACT[s.get('source_id')].append(f"{nom_v} ({', '.join(roles)})")

GROUPE = {'non_verifiee': 'a_lire', 'limite': 'partielle', 'faible': 'partielle', 'lien_casse': 'lien_mort'}
liste = []
for s in reg['sources']:
    v = s.get('verification_claude')
    if v not in GROUPE: continue
    if s.get('verification_humaine'): continue  # déjà tranchée par Guizmo
    groupe = 'remplacee' if s.get('statut_usage') == 'non_verifiee_remplacee' else GROUPE[v]
    liste.append({
        'id': s['source_id'], 'groupe': groupe, 'statut_claude': v, 'niveau': s.get('niveau'),
        'titre': s.get('titre'), 'institution': s.get('institution'), 'url': s.get('url'),
        'ou_regarder': s.get('locator') or '', 'extrait': s.get('resume_passage') or '',
        'notes': s.get('notes') or '',
        'domaine': 'villes' if any(c.startswith('ville-') for c in s.get('cibles', [])) else 'frontieres',
        'villes': [noms.get(c, c) for c in s.get('cibles', [])],
        'remplacee_par': s.get('sources_remplacement', []),
        'priorite': 'importante' if IMPACT.get(s['source_id']) and groupe != 'remplacee' else 'facultative',
        'impact': IMPACT.get(s['source_id'], []),
    })
ordre = {'a_lire': 0, 'partielle': 1, 'lien_mort': 2, 'remplacee': 3}
liste.sort(key=lambda x: (x['priorite'] != 'importante', ordre[x['groupe']], x['id']))
sortie = RACINE / 'data/sources/sources_a_valider.json'
sortie.write_text(json.dumps({'version_registre': reg['metadata']['version'], 'sources': liste}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(liste), 'sources à valider ->', sortie.relative_to(RACINE), '; importantes :', sum(x['priorite'] == 'importante' for x in liste))
