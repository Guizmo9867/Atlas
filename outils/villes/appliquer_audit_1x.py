"""Audit transversal villes 1.x d'Ether (05/10/2026) : 23 relations documentaires ajoutées à 22 villes déjà intégrées
(toutes du lot 1.0 : data/snapshot0/villes_1-0_france_benelux_iles_britanniques.json).

Opérations : data/sources/deltas_ether/2026-10-05_audit_1x_corrections_ether.json (toutes « completer_sources_sans_remplacer »),
appliquées par remise_ether_2026_10_05.appliquer_corrections : source ajoutée seulement si la ville ne la cite pas déjà ;
phrase d'Ether ajoutée à la note seulement si la source est confirmée par Claude pour cette ville ; rien n'est retiré.
Mention de preuve selon le registre (v1.30) : rien si « ok », sinon « (page relue par Claude pour cette ville) »,
« (lecture partielle) », « (non vérifiée par Claude) ».
Idempotent. À relancer après construire_villes_1_0.py si ce lot est reconstruit, avant appliquer_validations_guizmo.py.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from remise_ether_2026_10_05 import RACINE, appliquer_corrections
from confirmations_claude import confirmation
OPS = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_audit_1x_corrections_ether.json', encoding='utf-8'))['corrections']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
F = RACINE / 'data/snapshot0/villes_1-0_france_benelux_iles_britanniques.json'
L = json.load(open(F, encoding='utf-8'))
from remise_ether_2026_10_05 import roles_usage, confirmee
# Phrase d'Ether ajoutée à la note seulement si la relecture couvre TOUS les rôles que la phrase attribue à la ville
# (Cherbourg : la base navale n'est pas dite dans la page relue -> phrase non ajoutée).
_roles = {e['entite_id']: set(e['etats'][0]['proprietes']['roles']) for e in L['entites']}
for o in OPS:
    if not o.get('note_a_ajouter'): continue
    for a in o['sources_a_ajouter']:
        att = set(roles_usage(a['usage'])) & _roles.get(o['entite_id'], set())
        c = confirmee(REGISTRE.get(a['source_id']), o['entite_id'])
        if '*' not in c and not att <= c:
            o['note_a_ajouter'] = None
cibles = {o['entite_id'] for o in OPS}
journal = {}
for e in L['entites']:
    if e['entite_id'] not in cibles: continue
    avant = {s['source_id'] for s in e['etats'][0]['sources']}
    f = appliquer_corrections(e, OPS, REGISTRE, "Audit 1.x d'Ether")
    for s in e['etats'][0]['sources']:
        if s['source_id'] in avant: continue
        fiche = REGISTRE[s['source_id']]; st = fiche['verification_claude']
        cr, cm = confirmation(fiche, e['entite_id']) if st != 'ok' else (None, None)
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    journal[e['entite_id']] = f
assert cibles <= set(journal), cibles - set(journal)
MENTION = "Audit transversal 1.x d'Ether (05/10/2026) : 23 relations documentaires ajoutées à 22 villes (Ruppenthal, Logistical Support of the Armies I et II ; SNCF/patrimoine ferroviaire ; Hansard 1946 pour Portsmouth), relues par Claude (registre v1.30) ; rien n'est remplacé ni retiré ; phrases d'Ether ajoutées aux notes seulement pour les sources confirmées (outils/villes/appliquer_audit_1x.py)."
corr = L['metadata_lot'].setdefault('integration', {}).setdefault('corrections', [])
if MENTION not in corr: corr.append(MENTION)
F.write_text(json.dumps(L, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for k, v in journal.items(): print(' ', k, v)
