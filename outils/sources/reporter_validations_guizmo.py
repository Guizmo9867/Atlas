"""Reporte au registre les décisions de Guizmo sur les « Sources à valider ».

Lit, s'ils existent :
- <dossier d'échange>/decisions_sources_guizmo.json : fichier enregistré depuis 00_SOURCES_A_VALIDER.html (mode fichier) ;
- data/sources/validations_guizmo_claudeai.json : export de la collection « validations » de la page claude.ai
  (à écrire par Claude avec l'outil ArtifactData, action list, avant de lancer ce script).
Écrit dans chaque source concernée le champ verification_humaine = {decision, commentaire, par, date}.
Les sources ainsi tranchées sortent ensuite de la liste « Sources à valider ».
Usage : python outils/sources/reporter_validations_guizmo.py <dossier d'échange>   (puis relancer liste_sources_a_valider.py)
"""
import sys, json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
ECHANGE = pathlib.Path(sys.argv[1])
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
par_id = {s['source_id']: s for s in reg['sources']}
decisions = {}
for f in [ECHANGE / 'decisions_sources_guizmo.json', RACINE / 'data/sources/validations_guizmo_claudeai.json']:
    if f.exists():
        d = json.load(open(f, encoding='utf-8'))
        for sid, v in (d.get('decisions', d)).items():
            if isinstance(v, dict) and v.get('decision'):
                if sid not in decisions or (v.get('le') or '') > (decisions[sid].get('le') or ''):
                    decisions[sid] = v
n = 0
for sid, v in decisions.items():
    s = par_id.get(sid)
    if not s: continue
    nouveau = {'decision': v['decision'], 'commentaire': v.get('commentaire', ''), 'par': 'Guizmo', 'date': (v.get('le') or '')[:10]}
    if s.get('verification_humaine') != nouveau:
        s['verification_humaine'] = nouveau; n += 1
if n:
    R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(n, 'décisions de Guizmo reportées au registre', f'({len(decisions)} lues)')
