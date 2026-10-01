"""Fusion au registre du cycle 3 d'Ether sur le lot villes 1.4 (01/10/2026). À lancer UNE fois, après fusion_sources_1_3_cycle3.py.
Delta : data/sources/deltas_ether/2026-10-01_villes_1-4_cycle3_delta.json (6 fiches existantes complétées ; fusion par source_id).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-4_cycle3.json).
Repère (locator), adresse et relecture d'Ether mis à jour ; l'ancienne adresse est gardée dans les notes ; les notes et relectures
antérieures sont conservées (on ajoute, on n'efface pas). Tarnowitz : réserve de provenance maintenue (Q14-05).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.15', 'lancer d’abord fusion_sources_1_3_cycle3.py (ou fusion déjà faite ?)'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-4_cycle3_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-4_cycle3.json', encoding='utf-8'))['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
for s in delta:
    sid = s['source_id']; x = par_id[sid]; v = verif[sid]
    assert s['operation_registre'] == 'completer_fiche_existante'
    ajout = f" Cycle 3 d'Ether (01/10/2026) : {s['note']}"
    if s['url'] != x['url']:
        ajout += f" Adresse précédente (conservée pour l'historique) : {x['url']}"
        x['url'] = s['url']
    if s['locator'] != x.get('locator'):
        ajout += f" Repère précédent : {x.get('locator', '')}"
        x['locator'] = s['locator']
    x['verification_ether'] = s['verification']
    x['date_consultation'] = s['date_consultation']
    x['verification_claude'] = v['statut']
    if v['statut'] in ('ok', 'limite') and v['citation']: x['resume_passage'] = v['citation']
    x['notes'] += ajout + f" Relecture Claude 01/10/2026 (3e passe) : {v['commentaire']}"
reg['metadata']['version'] = '1.16'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(delta), 'complétées ;', len(reg['sources']), 'sources (v1.16)')
