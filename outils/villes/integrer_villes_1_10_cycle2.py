"""Villes 1.10, cycle 2 : applique au lot intégré (v0.1 -> v0.2) les 6 précisions d'Ether (notes et localisateurs : Valence, Grenoble,
Lons-le-Saunier, Vesoul, Mâcon, Auxerre ; data/sources/deltas_ether/2026-10-16_villes_1-10_cycle2_corrections.json, contrôle « avant »)
et la relecture de Claude (data/sources/verifications_claude/2026-10-16_villes_1-10_cycle2.json) : mentions des usages mises à jour,
« À renforcer : administration » retiré quand une source « ok » prouve le rôle. Aucun changement d'ID, de point, de date ou de rôle.
À lancer après fusion_sources_1_10_cycle2.py, une seule fois.
"""
import json, pathlib, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
F = RACINE / 'data/snapshot0/villes_1-10_complement_france.json'
lot = json.load(open(F, encoding='utf-8'))
assert lot['metadata_lot']['version'] == '0.1', 'déjà appliqué ?'
COR = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-16_villes_1-10_cycle2_corrections.json', encoding='utf-8'))['corrections']
REG = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
PAR_VILLE = json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-16_villes_1-10_cycle2.json', encoding='utf-8'))['par_ville']
MENTION = {'limite': ' (lecture partielle)', 'faible': ' (non confirmée par la relecture de Claude)', 'non_verifiee': ' (non vérifiée par Claude)'}
SUFFIXES = [' (lecture partielle)', ' (non confirmée par la relecture de Claude)', ' (non vérifiée par Claude)', ' (non vérifiée par Claude : lien cassé)',
            ' Précision Ether cycle2 ; avis de Claude à réexaminer sans validation implicite.']
NON_PREUVE = ('src-trfgis-departements-1940',)
par_id = {e['entite_id']: e for e in lot['entites']}
ecarts, corriges, levees = [], [], []
for c in COR:
    et = par_id[c['entite_id']]['etats'][0]; p = et['proprietes']
    if p['note'] != c['avant']['note']: ecarts.append(c['entite_id'])
    p['note'] = c['apres']['note']
    s = next(s for s in et['sources'] if s['source_id'] == c['apres']['source']['source_id'])
    s['locator'] = c['apres']['source']['locator']; s['usage'] = c['apres']['source']['usage']
    corriges.append(c['entite_id'])
for e in lot['entites']:
    et = e['etats'][0]; p = et['proprietes']; prouve = set()
    for s in et['sources']:
        if s['source_id'] in NON_PREUVE: continue
        st = PAR_VILLE.get(s['source_id'], {}).get(e['entite_id'], REG[s['source_id']]['verification_claude'])
        u = s['usage']
        for x in SUFFIXES:
            if u.endswith(x): u = u[:-len(x)].rstrip()
        s['usage'] = u + MENTION.get(st, '')
        if st == 'ok' and u.startswith('administration'): prouve.add('administration')
    if 'administration' in prouve and 'À renforcer : administration.' in p['note']:
        p['note'] = p['note'].replace(' À renforcer : administration.', '').replace('À renforcer : administration.', '').strip()
        levees.append(e['entite_id'])
m = lot['metadata_lot']; m['version'] = '0.2'
m['integration']['cycle2'] = {'date': '2026-10-16', 'par': 'Claude (boucle automatique)', 'corrections': [
  "Réponses d'Ether à Q110-01 et Q110-02 : 6 précisions de note et de localisateur (Valence, Grenoble, Lons-le-Saunier, Vesoul, Mâcon, Auxerre) ; 30 compléments de registre ; aucun changement d'ID, de point, de rôle ou de relation.",
  "Relecture de Claude sur les pièces locales d'Ether (21 copies HTML à empreinte contrôlée, 10 captures) : 4 sources « ok » (Tarbes, Besançon, Guéret, Cahors : continuité explicite de la préfecture), 22 « non vérifiées » et 1 « faible » deviennent « limite » (fait de 1944 ou indirect).",
  f"« À renforcer : administration » levé pour : {', '.join(levees)}."]}
F.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('corrigés', corriges, '; écarts « avant »', ecarts, '; levées', levees, '; à renforcer :',
      sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in lot['entites']))
