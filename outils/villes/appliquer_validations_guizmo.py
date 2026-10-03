"""Applique aux fiches des villes les décisions de Guizmo sur les sources (champ verification_humaine du registre).

Pour chaque source utilisée par une ville :
- « Ça prouve » (verifiee) : la mention « (non vérifiée par Claude) » ou « (lecture partielle) » devient « (validée par Guizmo) » ;
- « Prouve pour 1945 (la suite plus tard) » (verifiee_s0) : « (validée par Guizmo pour 1945) ». Seule la partie de la source
  qui vaut au 01/01/1945 est appliquée ; ce qu'elle dit d'après (changement de nom, etc.) n'est PAS appliqué au Snapshot 0
  et reste listé dans docs/NOTES_GUIZMO_SOURCES.md pour le ratissage des années suivantes ;
- dans ces deux cas, les rôles que la source prouve (« preuve locale : rail, industrie… ») sortent de « À renforcer » ;
- « Ne prouve pas » / « Lien mort » : mention « (ne prouve pas, selon Guizmo) » / « (lien mort, selon Guizmo) » ; rien d'autre ne change.
Idempotent : à relancer après chaque construction ou mise à jour d'un lot de villes (BOUCLE_AUTOMATIQUE §3, étape 4).
Usage : python outils/villes/appliquer_validations_guizmo.py   (depuis la racine du dépôt)
"""
import json, glob, pathlib, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
reg = json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))
PLUS_TARD = re.compile(r'plus tard|chronologie', re.I)  # « Ça prouve » dont la note de Guizmo parle d'une suite plus tard = validée pour 1945
def decision(v):
    return 'verifiee_s0' if v['decision'] == 'verifiee' and PLUS_TARD.search(v.get('commentaire') or '') else v['decision']
H = {s['source_id']: decision(s['verification_humaine']) for s in reg['sources'] if s.get('verification_humaine')}
MENTION = {'verifiee': ' (validée par Guizmo)', 'verifiee_s0': ' (validée par Guizmo pour 1945)',
           'ne_prouve_pas': ' (ne prouve pas, selon Guizmo)', 'lien_mort': ' (lien mort, selon Guizmo)'}
ANCIENNES = [' (non vérifiée par Claude)', ' (lecture partielle)', *MENTION.values()]
RENF = re.compile(r' À renforcer : ([^.]*)\.')
total_usages, total_roles = 0, 0
for f in sorted(glob.glob(str(RACINE / 'data/snapshot0/villes_1-*.json'))):
    brut = open(f, encoding='utf-8').read(); d = json.loads(brut); change = False
    retrait = len(brut.split('\n')[1]) - len(brut.split('\n')[1].lstrip(' ')) or 1  # garder la mise en forme du fichier
    for e in d.get('entites', []):
        for et in e.get('etats', []):
            prouves = set()
            for s in et.get('sources', []):
                dec = H.get(s.get('source_id'))
                if not dec: continue
                u = s.get('usage', ''); base = u
                for m in ANCIENNES:
                    if base.endswith(m): base = base[:-len(m)]; break
                nouveau = base + MENTION.get(dec, '')
                if nouveau != u: s['usage'] = nouveau; change = True; total_usages += 1
                if dec in ('verifiee', 'verifiee_s0') and base.startswith('preuve locale : '):
                    prouves.update(r.strip() for r in base[len('preuve locale : '):].split(','))
            p = et.get('proprietes', {}); note = p.get('note', '')
            m = RENF.search(note)
            if m and prouves:
                reste = [r.strip() for r in m.group(1).split(',') if r.strip() not in prouves]
                note2 = note.replace(m.group(0), f" À renforcer : {', '.join(reste)}." if reste else '')
                if note2 != note: p['note'] = note2; change = True; total_roles += 1
    if change:
        pathlib.Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=retrait) + ('\n' if brut.endswith('\n') else ''), encoding='utf-8')
print(len(H), 'décisions de Guizmo ;', total_usages, 'mentions de preuve mises à jour ;', total_roles, 'fiches avec « À renforcer » allégé')
