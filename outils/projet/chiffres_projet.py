"""Fiche de chiffres du projet, tirée directement du dépôt (pour le dossier de financement d'Ether).

Sorties : data/chiffres_projet.json (machines) et docs/CHIFFRES_PROJET.md (lecture).
Relancer : python outils/projet/chiffres_projet.py (depuis la racine du dépôt). Lancé à chaque lot par la boucle automatique.
Aucun chiffre n'est estimé : tout est compté dans les fichiers ou dans l'historique git.
"""
import json, glob, pathlib, subprocess, collections, datetime

RACINE = pathlib.Path(__file__).resolve().parents[2]
os_ = lambda *a: str(RACINE.joinpath(*a))

def git(*args):
    try:
        return subprocess.run(['git', '-C', str(RACINE), *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ''

# --- Entités du Snapshot 0 ---
lots_frontieres, lots_villes = [], []
types = collections.Counter()
villes_rang, villes_capitale, villes_a_renforcer, villes_nom_date, roles = collections.Counter(), collections.Counter(), 0, 0, collections.Counter()
for f in sorted(glob.glob(os_('data/snapshot0/*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    m = d.get('metadata_lot', {})
    ents = d.get('entites', [])
    c = collections.Counter(e['type_entite'] for e in ents)
    types.update(c)
    info = {'fichier': pathlib.Path(f).name, 'version': m.get('version'), 'zone': m.get('zone'), 'entites': dict(c)}
    if c.get('ville'):
        lots_villes.append(info)
        for e in ents:
            p = e['etats'][0].get('proprietes', {})
            villes_rang[p.get('importance_atlas', '?')] += 1
            if p.get('capitale'): villes_capitale[p['capitale']] += 1
            if 'À renforcer' in p.get('note', ''): villes_a_renforcer += 1
            if p.get('nom'): villes_nom_date += 1
            roles.update(p.get('roles', []))
    else:
        lots_frontieres.append(info)

geometries = len(glob.glob(os_('data/geometries/snapshot0/*.geojson')))

# --- Sources ---
reg = json.load(open(os_('data/sources/atlas_registre_sources.json'), encoding='utf-8'))
src = reg['sources']
statuts = collections.Counter(s.get('verification_claude', 'non_renseigne') for s in src)
niveaux = collections.Counter(s.get('niveau', '?') for s in src)
a_valider = len(json.load(open(os_('data/sources/sources_a_valider.json'), encoding='utf-8'))['sources'])
humaines = sum(1 for s in src if s.get('verification_humaine'))

# --- Historique ---
commits = git('rev-list', '--count', 'HEAD')
premier = git('log', '--reverse', '--format=%ad', '--date=short').split('\n')[0] if commits else ''
dernier = git('log', '-1', '--format=%ad', '--date=short')

chiffres = {
    'genere_le': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
    'snapshot0': {
        'date_representee': '1945-01-01 00:00 (dernier état connu avant)',
        'territoires': types.get('territoire', 0), 'lignes_de_front': types.get('ligne_front', 0), 'frontieres_tracees': types.get('frontiere', 0),
        'geometries': geometries, 'villes': types.get('ville', 0),
        'villes_par_rang': dict(sorted(villes_rang.items())), 'capitales': dict(villes_capitale),
        'villes_avec_nom_de_1945_different': villes_nom_date, 'villes_avec_reserve_a_renforcer': villes_a_renforcer,
        'roles_de_villes': dict(roles.most_common()),
        'lots_frontieres': lots_frontieres, 'lots_villes': lots_villes,
    },
    'sources': {
        'registre_version': reg['metadata']['version'], 'total': len(src),
        'relecture_claude': dict(statuts), 'niveaux': dict(niveaux),
        'en_attente_de_validation_humaine': a_valider, 'validees_par_guizmo': humaines,
    },
    'historique': {'envois_github': int(commits) if commits else None, 'premier_envoi': premier, 'dernier_envoi': dernier,
                   'depot_public': 'https://github.com/Guizmo9867/Atlas'},
}
(RACINE / 'data/chiffres_projet.json').write_text(json.dumps(chiffres, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

S, Q, H = chiffres['snapshot0'], chiffres['sources'], chiffres['historique']
ok = Q['relecture_claude'].get('ok', 0)
md = f"""# Atlas Eurasie — chiffres du projet

*Généré automatiquement depuis le dépôt le {chiffres['genere_le']}. Aucun chiffre estimé : tout est compté dans les fichiers.
Version machine : `data/chiffres_projet.json`.*

## Snapshot 0 (Europe au 1er janvier 1945, 0 h)

| | |
|---|---|
| Territoires (souveraineté, contrôle, occupation) | {S['territoires']} |
| Lignes de front | {S['lignes_de_front']} |
| Géométries tracées | {S['geometries']} |
| Villes | {S['villes']} (rang A : {S['villes_par_rang'].get('A', 0)}, B : {S['villes_par_rang'].get('B', 0)}, C : {S['villes_par_rang'].get('C', 0)}, D : {S['villes_par_rang'].get('D', 0)}) |
| Capitales | {', '.join(f'{v} {k}' for k, v in S['capitales'].items())} |
| Villes affichées sous leur nom de 1945 | {S['villes_avec_nom_de_1945_different']} |
| Villes avec une réserve « à renforcer » visible | {S['villes_avec_reserve_a_renforcer']} |

Lots de frontières : {len(S['lots_frontieres'])}. Lots de villes : {len(S['lots_villes'])} ({', '.join(l['fichier'].replace('.json', '') for l in S['lots_villes'])}).

## Sources

| | |
|---|---|
| Sources au registre (v{Q['registre_version']}) | {Q['total']} |
| Confirmées par la relecture de Claude | {ok} ({round(100 * ok / Q['total'])} %) |
| Lecture partielle / faible / illisible / lien mort | {Q['relecture_claude'].get('limite', 0)} / {Q['relecture_claude'].get('faible', 0)} / {Q['relecture_claude'].get('non_verifiee', 0)} / {Q['relecture_claude'].get('lien_casse', 0)} |
| En attente de validation humaine | {Q['en_attente_de_validation_humaine']} |
| Validées par Guizmo | {Q['validees_par_guizmo']} |
| Niveaux (A primaire / B secondaire / C exploratoire) | {Q['niveaux'].get('A', 0)} / {Q['niveaux'].get('B', 0)} / {Q['niveaux'].get('C', 0)} |

## Historique

- Envois sur GitHub : {H['envois_github']} (du {H['premier_envoi']} au {H['dernier_envoi']}).
- Dépôt public : {H['depot_public']}
"""
(RACINE / 'docs/CHIFFRES_PROJET.md').write_text(md, encoding='utf-8')
print(md)
