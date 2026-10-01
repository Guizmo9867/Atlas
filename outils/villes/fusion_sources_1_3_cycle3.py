"""Fusion au registre du cycle 3 d'Ether sur le lot villes 1.3 (01/10/2026). À lancer UNE fois.
Delta : data/sources/deltas_ether/2026-10-01_villes_1-3_cycle3_delta.json (9 sources nouvelles ; fusion par source_id).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-3_cycle3.json).
Cinq preuves de nom (Q13-01) ; quatre sources de contexte gardées EN RÉSERVE par décision de Guizmo (Q13-02, Q13-03, Q13-04) :
elles entrent au registre mais ne modifient aucune donnée.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.14', 'fusion déjà faite ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_cycle3_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-3_cycle3.json', encoding='utf-8'))['resultats']}
USAGES = {
    'src-13-cz-reichenberg-reichsanzeiger-1944': ['nom_historique'], 'src-13-cz-eger-reichsanzeiger-1944': ['nom_historique'],
    'src-13-cz-brux-reichsanzeiger-1942': ['nom_historique'], 'src-13-sk-ersekujvar-presse-1944': ['nom_historique'],
    'src-13-cz-tetschen-telephone-1942': ['nom_historique'],
    'src-13-hu-szalasi-koszeg-neb-1944': ['administration'], 'src-13-protectorat-velcovsky-langues': ['nomenclature'],
    'src-13-most-toponymes-2025': ['implantation_historique'], 'src-13-most-carte-municipale-1938': ['implantation_historique'],
}
RESERVE = {  # décision de Guizmo du 01/10/2026 (coordination/AUTORISATIONS_RATISSAGE.json)
    'src-13-hu-szalasi-koszeg-neb-1944': "Q13-03 : « Laisser la note en réserve » (Guizmo, 01/10/2026) — aucune note ni nouveau siège dans les données.",
    'src-13-protectorat-velcovsky-langues': "Q13-02 : « Laisser cette décision en réserve » (Guizmo, 01/10/2026) — aucune règle de noms nouvelle pour le Protectorat.",
    'src-13-most-toponymes-2025': "Q13-04 : « Garder le déplacement en réserve » (Guizmo, 01/10/2026) — aucun déplacement du point.",
    'src-13-most-carte-municipale-1938': "Q13-04 : « Garder le déplacement en réserve » (Guizmo, 01/10/2026) — relevé d'Ether 50,524968 N / 13,642034 E conservé ici seulement, aucun déplacement du point.",
}
par_id = {s['source_id']: s for s in reg['sources']}
n = 0
for s in delta:
    sid = s['source_id']; v = verif[sid]
    assert sid not in par_id, sid
    notes = f"Proposée par Ether (cycle 3 du lot villes 1.3, 01/10/2026). Ce que la source prouve selon Ether : {'; '.join(s['usage'])}. Limite annoncée par Ether : {s['note']}"
    if sid in RESERVE: notes += f" SOURCE DE CONTEXTE EN RÉSERVE — {RESERVE[sid]}"
    notes += f" Relecture Claude 01/10/2026 : {v['commentaire']}"
    reg['sources'].append({
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': USAGES[sid], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s['verification'], 'notes': notes,
    }); n += 1
reg['metadata']['version'] = '1.15'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(n, 'ajoutées ;', len(reg['sources']), 'sources (v1.15)')
