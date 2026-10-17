"""Intègre un lot de subdivisions 2.x (un État de 1945, ou une partie d'un grand État) livré par Ether dans 01_lots/2.<XX>/.
Outil de la boucle automatique (feu vert de Guizmo du 15/10/2026), généralisé à partir du pilote 2.FR (outils/subdivisions/integrer_2fr.py).

Usage (depuis la racine du dépôt) :
  python outils/subdivisions/integrer_subdivisions.py <dossier du lot> --verif <fichier de relecture des sources> [--cycle N] [--essai <dossier>]
    <dossier du lot>  ex. $HOME/mnt/Desktop--Atlas/01_lots/2.BE
    --verif           data/sources/verifications_claude/<date>_2BE.json : {"resultats": [{"id", "statut", "commentaire"}]}
                      (statut : ok | limite | non_verifiee) — écrit AVANT par Claude après lecture des sources
    --essai <dossier> écrit tout dans ce dossier au lieu du dépôt (rien n'est modifié dans le dépôt) : pour tester

Ce que fait l'outil :
  1. contrôle les fiches (ID, échelon 1 ou 2, parent, souveraineté, sources) ;
  2. trie les tracés : licence autorisée (domaine public, CC0, CC BY sans NC/SA/ND, Licence Ouverte/Etalab, OGL, DL-DE BY/Zero,
     opendata.swiss terms_open / terms_by) ; une décision de Guizmo (decisions_guizmo.json) peut lever la marque ne_pas_integrer
     et pas marqués « ne_pas_integrer » par Ether ; tout ce qui touche à OpenStreetMap/ODbL est refusé ;
  3. simplifie les tracés gardés avec mapshaper (topologie conservée ; 400 m pour l'échelon 2, 600 m pour l'échelon 1),
     un fichier par tracé dans data/geometries/snapshot0/ ;
  4. écrit data/snapshot0/subdivisions_2-<XX>.json (le lot complet : un nouveau cycle remplace le fichier) ;
  5. ajoute les sources au registre (version + 0.01), avec le statut de la relecture de Claude ; une source déjà connue est complétée ;
  6. garde la proposition et le delta d'Ether dans data/sources/deltas_ether/ ;
  7. écrit un rapport JSON (chiffres, refus, avertissements) pour le compte rendu : outils/subdivisions/rapports/<date>_2<XX>_cycle<N>.json.
Il s'arrête (code 1) sur une erreur bloquante, sans rien écrire.
"""
import argparse, copy, datetime, json, pathlib, re, shutil, subprocess, sys, tempfile

RACINE = pathlib.Path(__file__).resolve().parents[2]
AUJ = datetime.date.today().isoformat()
PAS = {1: 600, 2: 400}

ap = argparse.ArgumentParser()
ap.add_argument('lot'); ap.add_argument('--verif', required=True); ap.add_argument('--cycle', type=int, default=1)
ap.add_argument('--essai')
a = ap.parse_args()
LOT = pathlib.Path(a.lot)
m = re.fullmatch(r'2\.([A-Z]{2}(?:-[A-Z0-9]+)?)', LOT.name)
if not m: sys.exit(f"Nom de dossier inattendu « {LOT.name} » (attendu : 2.XX ou 2.XX-PARTIE, ex. 2.BE, 2.SU-UA)")
CODE = m.group(1)                    # BE, SU-UA…
COMPACT = CODE.replace('-', '')       # pour les noms de fichiers d'Ether : atlas_2BE_…, atlas_2SUUA_…
SORTIE = pathlib.Path(a.essai) if a.essai else RACINE
erreurs, avert, refus = [], [], []

def lire(*noms):
    for n in noms:
        p = LOT / n
        if p.exists(): return json.load(open(p, encoding='utf-8')), p
    sys.exit(f"Fichier introuvable dans {LOT} : {' ou '.join(noms)}")

prop, p_prop = lire(f'atlas_2{COMPACT}_subdivisions_proposees.json', f'atlas_2{CODE}_subdivisions_proposees.json')
geo, p_geo = lire(f'geometries/atlas_2{COMPACT}_geometries_proposees.geojson', f'geometries/atlas_2{CODE}_geometries_proposees.geojson')
delta, p_delta = lire(f'atlas_registre_sources_2{COMPACT}_delta.json', f'atlas_registre_sources_2{CODE}_delta.json')
# Décisions de Guizmo qui lèvent la marque « ne_pas_integrer » d'Ether pour un lot (ex. 2.CH, licence acceptée le 17/10/2026).
# La licence est quand même contrôlée.
DEC = RACINE / 'outils/subdivisions/decisions_guizmo.json'
FORCER = json.load(open(DEC, encoding='utf-8')).get('lots', {}).get(f'2.{CODE}', {}).get('integrer_traces_marques', False) if DEC.exists() else False
verif = {r['id']: r for r in json.load(open(RACINE / a.verif if not pathlib.Path(a.verif).is_absolute() else a.verif, encoding='utf-8'))['resultats']}
reg = json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))

# --- 1. Fiches ---
entites = copy.deepcopy(prop['entites'])
ids = {e['entite_id'] for e in entites}
connus = set()
for f in (RACINE / 'data/snapshot0').glob('*.json'):
    if f.name == f'subdivisions_2-{CODE}.json': continue
    connus |= {e['entite_id'] for e in json.load(open(f, encoding='utf-8')).get('entites', [])}
for i in ids & connus: erreurs.append(f"{i} : existe déjà dans un autre fichier du corpus")
RE_ID = re.compile(r'^subdivision-[a-z]{2}-[a-z0-9]+(-[a-z0-9]+)*$')
gardees = []
for e in entites:
    i = e['entite_id']
    if not RE_ID.match(i): erreurs.append(f"{i} : identifiant invalide (subdivision-<code pays actuel>-<mot-clé sans accents>)"); continue
    if e.get('type_entite') != 'subdivision': erreurs.append(f"{i} : type_entite doit valoir « subdivision »")
    if not e.get('etats'): erreurs.append(f"{i} : aucun état"); continue
    garder = True
    for s in e['etats']:
        p = s.setdefault('proprietes', {})
        n = p.get('echelon', p.get('niveau'))
        if n not in (1, 2):
            avert.append(f"{i} : échelon « {n} » non affiché (seuls 1 et 2 existent) : fiche mise de côté"); garder = False; break
        p['echelon'] = n
        pid = p.get('parent_id')
        if pid and pid not in ids and pid not in connus: erreurs.append(f"{i} : parent_id « {pid} » introuvable")
        if not p.get('souverainete_id'): avert.append(f"{i} : souverainete_id absente (souveraineté non tranchée)")
        if not s.get('sources'): erreurs.append(f"{i} : aucune source")
        for k in ('nom',):
            if isinstance(p.get(k), str): p[k] = re.sub(r"\bde ([AEIOUÉÈÂÎÔÛ])", r"d'\1", p[k])
        s.pop('geometrie_ref', None)   # remise par l'outil plus bas, seulement si le tracé est accepté
        s.pop('geometrie', None)
    for k in ('nom', 'nom_court'):
        if isinstance(e.get(k), str): e[k] = re.sub(r"\bde ([AEIOUÉÈÂÎÔÛ])", r"d'\1", e[k])
    if garder: gardees.append(e)
entites = gardees

# --- 2. Tracés : licence et marquage ---
def licence_ok(lic, texte):
    t = texte.lower()
    if 'odbl' in t or 'openstreetmap' in t or re.search(r'\bosm\b', t): return False, 'OpenStreetMap / ODbL interdit'
    n = re.sub(r'[\s_.\-]', '', (lic or '').lower())
    if not n: return False, 'licence absente'
    if n.startswith('cc0') or n in ('domainepublic', 'publicdomain', 'pd'): return True, ''
    # opendata.swiss (décision de Guizmo du 17/10/2026) : « Utilisation libre » (terms_open) et « … mention de la source obligatoire »
    # (terms_by) autorisent l'usage commercial ; les variantes « ask » (autorisation requise pour l'usage commercial) restent refusées
    if 'terms' in n and ('termsopen' in n or 'termsby' in n): return (False, f'licence {lic} (usage commercial sur autorisation : à trancher)') if 'ask' in n else (True, '')
    if n.startswith('ccby'):
        return (False, f'licence {lic} (NC, SA ou ND : à trancher)') if re.search(r'(^|[\s\-_/])(nc|sa|nd)([\s\-_/.]|$)', lic.lower()) else (True, '')
    if any(n.startswith(x) for x in ('licenceouverte', 'etalab', 'ogl', 'opengovernmentlicence', 'dlde/by', 'dlde/zero', 'dldeby', 'dldezero')): return True, ''
    return False, f'licence « {lic} » non reconnue (à trancher)'

echelon_de = {e['entite_id']: e['etats'][0]['proprietes']['echelon'] for e in entites}
a_simplifier = {1: [], 2: []}
for f in geo['features']:
    p = f['properties']
    gid, eid = p.get('geometry_id'), p.get('entite_id')
    if not gid or not eid: erreurs.append(f"tracé sans geometry_id ou entite_id : {str(p)[:120]}"); continue
    if gid != f"geom-{eid}-1945-01-01": avert.append(f"{gid} : nom attendu geom-{eid}-1945-01-01 (renommé)"); p['geometry_id'] = gid = f"geom-{eid}-1945-01-01"
    if eid not in echelon_de: avert.append(f"{gid} : aucune fiche gardée pour {eid} (tracé ignoré)"); continue
    ok, pourquoi = licence_ok(p.get('licence'), json.dumps(p, ensure_ascii=False))
    if 'ne_pas_integrer' in str(p.get('statut', '')) and not FORCER: ok, pourquoi = False, f"marqué « {p.get('statut')} » par Ether"
    if not ok: refus.append({'geometry_id': gid, 'raison': pourquoi}); continue
    if f.get('geometry', {}).get('type') not in ('Polygon', 'MultiPolygon'): erreurs.append(f"{gid} : un tracé de subdivision doit être un polygone"); continue
    a_simplifier[echelon_de[eid]].append(f)

livrees = {s['source_id'] for s in delta.get('ajouter', []) + delta.get('completer', [])}
connues = {s['source_id'] for s in reg['sources']}
cites = {src['source_id'] for e in entites for st in e['etats'] for src in st.get('sources', [])}
cites |= {x if isinstance(x, str) else x.get('source_id') for fs in a_simplifier.values() for f in fs for x in (f['properties'].get('sources') or [])}
for sid in sorted(cites - livrees - connues): erreurs.append(f"source « {sid} » citée mais absente du registre et du delta")
if erreurs:
    print('✗ Erreurs bloquantes (rien n\'est écrit) :'); [print('  -', x) for x in erreurs]; sys.exit(1)

# --- 3. Simplification (mapshaper) et un fichier par tracé ---
GEOM = SORTIE / 'data/geometries/snapshot0'; GEOM.mkdir(parents=True, exist_ok=True)
acceptes = {}
with tempfile.TemporaryDirectory() as tmp:
    for n, feats in a_simplifier.items():
        if not feats: continue
        src, dst = pathlib.Path(tmp, f'e{n}.geojson'), pathlib.Path(tmp, f'e{n}_s.geojson')
        src.write_text(json.dumps({'type': 'FeatureCollection', 'features': feats}, ensure_ascii=False), encoding='utf-8')
        r = subprocess.run(['npx', '-y', 'mapshaper@0.6', str(src), '-simplify', f'interval={PAS[n]}', 'keep-shapes', '-clean',
                            '-o', str(dst), 'precision=0.00001'], capture_output=True, text=True)
        if r.returncode or not dst.exists(): sys.exit(f"mapshaper a échoué : {r.stderr[-800:]}")
        for f in json.load(open(dst, encoding='utf-8'))['features']:
            p = dict(f['properties'])
            for k, v in list(p.items()):
                if isinstance(v, str) and v[:1] in '[{':
                    try: p[k] = json.loads(v)
                    except Exception: pass
            if not f.get('geometry'): refus.append({'geometry_id': p['geometry_id'], 'raison': 'vide après simplification'}); continue
            liste = lambda v: [] if v in (None, '') else (v if isinstance(v, list) else [v])   # Ether livre parfois une chaîne au lieu d'une liste
            srcs = liste(p.get('sources'))
            props = {
                'geometry_id': p['geometry_id'], 'date_validite': '1945-01-01',
                'statut': 'provisoire_' + re.sub(r'[^a-z0-9_]+', '_', str(p.get('statut') or 'reconstruction').lower()).strip('_'),
                'entite_id': p['entite_id'], 'echelon': n,
                'licence': p.get('licence'), 'attribution': p.get('attribution'),
                'millesime_source': p.get('millesime_source') or p.get('millésime_source'),
                'precision': f"simplifié au pas de {PAS[n]} m (mapshaper, topologie conservée) ; {p.get('precision') or ''}".strip(' ;'),
                'limite': p.get('limite'), 'reserves': liste(p.get('reserves')),
                'sources': [x if isinstance(x, dict) else {'source_id': x, 'usage': 'tracé'} for x in srcs],
                'operations': liste(p.get('operations')) + [f'simplification mapshaper interval={PAS[n]} m keep-shapes, nettoyage (Claude, {AUJ})'],
                'auteur': 'Ether (proposition), Claude (intégration)', 'date_creation': AUJ,
                'script': 'outils/subdivisions/integrer_subdivisions.py',
            }
            if p.get('points_a_verifier'): props['points_a_verifier'] = p['points_a_verifier']
            if not props['sources']: refus.append({'geometry_id': p['geometry_id'], 'raison': 'tracé sans source'}); continue
            (GEOM / f"{p['geometry_id']}.geojson").write_text(json.dumps({'type': 'Feature', 'geometry': f['geometry'], 'properties': props},
                                                                          ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
            acceptes[p['entite_id']] = p['geometry_id']
for e in entites:
    if e['entite_id'] in acceptes: e['etats'][-1]['geometrie_ref'] = acceptes[e['entite_id']]
sans = [e['entite_id'] for e in entites if e['entite_id'] not in acceptes]

# --- 4. Fichier du corpus ---
meta = prop.get('metadata_lot', {})
corpus = {
    'metadata_lot': {
        'nom': f'snapshot0_subdivisions_2-{CODE}', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
        'version': f'{a.cycle}.0', 'statut': 'integre_par_claude', 'cycle': a.cycle, 'date_integration': AUJ,
        'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json', 'lot_methode': f'2.{CODE} (phase 2, docs/METHODE_ATLAS_v2.md)',
        'etat_1945': meta.get('etat_1945') or meta.get('zone_travail'),
        'proposition_ether': f'data/sources/deltas_ether/{AUJ}_2{COMPACT}_subdivisions_proposees_ether.json',
        'regles': [
            "échelon 1 = premier niveau sous l'État ; échelon 2 = le niveau en dessous ; le terme local reste dans statut_administratif",
            "une subdivision porte la souveraineté de droit ; le contrôle réel vient des territoires et des lignes de front",
            "affichage : échelon 1 dès le zoom 5, échelon 2 dès le zoom 6,5, mêmes seuils pour tous les pays (calque « Découpage administratif »)",
            "tracés provisoires ; chefs-lieux proposés = référence, jamais validés sans preuve au 01/01/1945",
        ],
        'sans_trace': sans,
    },
    'entites': entites,
}
dest = SORTIE / f'data/snapshot0/subdivisions_2-{CODE}.json'; dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# --- 5. Sources ---
par_id = {s['source_id']: s for s in reg['sources']}
ajoutees, completees, statuts = [], [], {}
for s in delta.get('ajouter', []) + delta.get('completer', []):
    sid = s['source_id']
    v = verif.get(sid, {'statut': 'non_verifiee', 'commentaire': 'pas relue par Claude'})
    if sid in par_id:
        x = par_id[sid]
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *s.get('cibles', [])]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), *s.get('usages_atlas', [])]))
        x['notes'] = (x.get('notes', '') + f" Lot 2.{CODE} (cycle {a.cycle}, {AUJ}) : cibles ajoutées ; relecture : {v['statut']}. {v.get('commentaire', '')}").strip()
        completees.append(sid); continue
    usage = ' ; '.join(s['usage']) if isinstance(s.get('usage'), list) else s.get('usage', '')
    fiche = {'source_id': sid, 'niveau': s.get('niveau'), 'type_source': s.get('type_source'), 'titre': s.get('titre'),
             'institution': s.get('institution'), 'url': s.get('url'), 'date_consultation': s.get('date_consultation'),
             'periode_couverte': [], 'zones': [CODE.split('-')[0]], 'usages_atlas': s.get('usages_atlas', []), 'cibles': s.get('cibles', []),
             'locator': s.get('locator'), 'resume_passage': v.get('commentaire', '') if v['statut'] != 'non_verifiee' else '',
             'archive_locale': None, 'verification_claude': v['statut'], 'verification_ether': s.get('verification_ether'),
             'notes': f"Proposée par Ether (lot 2.{CODE}, cycle {a.cycle}). Ce que la source prouve selon Ether : {usage}. "
                      f"Limite annoncée par Ether : {s.get('note', '')} Relecture Claude {AUJ} : {v.get('commentaire', '')}"}
    for k, val in s.items():
        if k not in fiche and k not in ('usage', 'note', 'operation_registre'): fiche[k if k != 'verification_claude' else 'verification_claude_ether'] = val
    reg['sources'].append(fiche); par_id[sid] = fiche; ajoutees.append(sid); statuts[v['statut']] = statuts.get(v['statut'], 0) + 1
ancienne = reg['metadata']['version']
maj, mineur = ancienne.split('.')
reg['metadata']['version'] = f"{maj}.{int(mineur) + 1}"
R = SORTIE / 'data/sources/atlas_registre_sources.json'; R.parent.mkdir(parents=True, exist_ok=True)
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# --- 6. Copies de la livraison d'Ether ---
D = SORTIE / 'data/sources/deltas_ether'; D.mkdir(parents=True, exist_ok=True)
(D / f'{AUJ}_2{COMPACT}_subdivisions_proposees_ether.json').write_text(json.dumps({
    'note': f"Copie fidèle de 01_lots/2.{CODE}/{p_prop.name} (Ether, cycle {a.cycle}), sous la clé proposition_ether pour que le validateur "
            f"ne la lise pas comme un lot du corpus (entités intégrées : data/snapshot0/subdivisions_2-{CODE}.json).",
    'proposition_ether': prop}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
shutil.copy(p_delta, D / f'{AUJ}_2{COMPACT}_sources_delta.json')

# --- 7. Rapport ---
rapport = {'lot': f'2.{CODE}', 'cycle': a.cycle, 'date': AUJ, 'essai': bool(a.essai),
           'subdivisions': len(entites), 'echelon_1': sum(e['etats'][0]['proprietes']['echelon'] == 1 for e in entites),
           'echelon_2': sum(e['etats'][0]['proprietes']['echelon'] == 2 for e in entites),
           'traces_integres': len(acceptes), 'sans_trace': sans, 'traces_refuses': refus,
           'sources_ajoutees': ajoutees, 'sources_completees': completees, 'statuts_relecture': statuts,
           'registre': f"{ancienne} -> {reg['metadata']['version']}", 'avertissements': avert}
RP = SORTIE / 'outils/subdivisions/rapports'; RP.mkdir(parents=True, exist_ok=True)
(RP / f'{AUJ}_2{COMPACT}_cycle{a.cycle}.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 8 else f'{len(v)} éléments') for k, v in rapport.items()}, ensure_ascii=False, indent=1))
