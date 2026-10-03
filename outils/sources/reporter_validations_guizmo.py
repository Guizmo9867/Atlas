"""Reporte au registre les décisions de Guizmo sur les « Sources à valider ».

Lit, s'ils existent :
- <dossier d'échange>/decisions_sources_guizmo.json : fichier enregistré depuis 00_SOURCES_A_VALIDER.html (mode fichier) ;
- data/sources/validations_guizmo_claudeai.json : export de la collection « validations » de la page claude.ai
  (à écrire par Claude avec l'outil ArtifactData, action list, avant de lancer ce script).
Écrit dans chaque source concernée le champ verification_humaine = {decision, commentaire, par, date}.
Les sources ainsi tranchées sortent ensuite de la liste « Sources à valider ».
Décisions possibles : verifiee, verifiee_s0 (prouve pour 1945 ; la source dit aussi un changement plus tard, à reprendre
dans la chronologie : elle est gardée), ne_prouve_pas, lien_mort.
Écrit aussi docs/NOTES_GUIZMO_SOURCES.md : toutes les sources tranchées avec une note, et en tête celles « la suite plus tard »,
à relire quand on avancera dans le temps (ratissage des mois).
Usage : python outils/sources/reporter_validations_guizmo.py <dossier d'échange>   (puis relancer liste_sources_a_valider.py)
        python outils/sources/reporter_validations_guizmo.py --verifier <dossier d'échange>   (n'écrit rien ; dit combien de décisions sont nouvelles)
"""
import sys, json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
VERIFIER = '--verifier' in sys.argv
ECHANGE = pathlib.Path([a for a in sys.argv[1:] if a != '--verifier'][0])
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
if VERIFIER:
    print(n, 'décisions nouvelles à reporter'); sys.exit(0)
if n:
    R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(n, 'décisions de Guizmo reportées au registre', f'({len(decisions)} lues)')

# --- Notes de Guizmo (à relire plus tard) ---
tranchees = [s for s in reg['sources'] if s.get('verification_humaine')]
plus_tard = [s for s in tranchees if s['verification_humaine']['decision'] == 'verifiee_s0']
notes = [s for s in tranchees if s['verification_humaine']['decision'] != 'verifiee_s0' and s['verification_humaine'].get('commentaire')]
NOMS = {'verifiee': 'Ça prouve', 'verifiee_s0': 'Prouve pour 1945 (la suite plus tard)', 'ne_prouve_pas': 'Ne prouve pas', 'lien_mort': 'Lien mort'}
def ligne(s):
    v = s['verification_humaine']
    return (f"- **{s['source_id']}** — {s.get('titre', '')}\n  - Lien : {s.get('url', '')}\n"
            f"  - Décision : {NOMS.get(v['decision'], v['decision'])} (Guizmo, {v.get('date', '')})\n"
            f"  - Note de Guizmo : {v.get('commentaire') or '(aucune)'}")
md = ['# Notes de Guizmo sur les sources', '',
      '*Généré par `outils/sources/reporter_validations_guizmo.py`. Ne pas modifier à la main.*', '',
      f'{len(tranchees)} sources tranchées par Guizmo au total.', '',
      '## À reprendre plus tard dans la chronologie', '',
      'Ces sources sont **valides pour le Snapshot 0** (1945). Elles disent aussi un changement plus tard (nom, statut…) : '
      'elles restent au registre et seront relues quand le ratissage avancera dans le temps.', '']
md += [ligne(s) for s in plus_tard] or ['(aucune pour le moment)']
md += ['', '## Autres sources tranchées avec une note', '']
md += [ligne(s) for s in notes] or ['(aucune pour le moment)']
(RACINE / 'docs/NOTES_GUIZMO_SOURCES.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(len(plus_tard), 'sources « la suite plus tard » et', len(notes), 'autres notes dans docs/NOTES_GUIZMO_SOURCES.md')
