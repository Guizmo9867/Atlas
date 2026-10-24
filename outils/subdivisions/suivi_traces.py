"""Tableau des États dont les subdivisions de 1945 n'ont pas (ou pas toutes) de tracé sur la carte (demande de Guizmo du 24/10/2026).
Calcule les chiffres à partir de data/snapshot0/subdivisions_2-*.json et du dernier rapport de chaque lot ; le « pourquoi » et les
« pistes » viennent de outils/subdivisions/suivi_traces_notes.json (à compléter par Claude à chaque lot 2.x).
Usage : python outils/subdivisions/suivi_traces.py [dossier d'échange]   → docs/SUBDIVISIONS_SANS_TRACE.md (+ 00_SUBDIVISIONS_SANS_TRACE.md)"""
import json, pathlib, sys, datetime
R = pathlib.Path(__file__).resolve().parents[2]
notes = json.load(open(R / 'outils/subdivisions/suivi_traces_notes.json', encoding='utf-8')).get('lots', {})
lignes, tot, tot_t = [], 0, 0
for f in sorted((R / 'data/snapshot0').glob('subdivisions_2-*.json')):
    lot = '2.' + f.stem.split('_2-')[1]
    ents = json.load(open(f, encoding='utf-8'))['entites']
    n = len(ents); t = sum(1 for e in ents if any(s.get('geometrie_ref') for s in e['etats']))
    tot += n; tot_t += t
    no = notes.get(lot, {})
    etat = ('en attente' if 'attend' in no.get('pourquoi', '') else 'rien à tracer') if n == 0 else 'tout tracé' if t == n else 'aucun tracé' if t == 0 else 'en partie'
    if etat == 'tout tracé' and not no: continue
    lignes.append((lot, n, t, etat, no.get('pourquoi', '— (à compléter)'), no.get('pistes', '')))
ordre = {'aucun tracé': 0, 'en partie': 1, 'en attente': 2, 'rien à tracer': 3, 'tout tracé': 4}
lignes.sort(key=lambda x: (ordre[x[3]], x[0]))
md = [f"# Subdivisions sans tracé sur la carte — suivi\n",
      f"*Mis à jour le {datetime.date.today().strftime('%d/%m/%Y')} par `outils/subdivisions/suivi_traces.py` (demande de Guizmo du 24/10/2026 : garder dans un coin les pays qui posent problème). "
      f"Les fiches existent toujours (noms, rangs, sources) ; seul le dessin manque. À reprendre plus tard, pays par pays.*\n",
      f"**En tout : {tot_t} subdivisions tracées sur {tot}.**\n",
      "| Lot | Subdivisions | Tracées | État | Pourquoi | Pistes |", "|---|---|---|---|---|---|"]
md += [f"| {a} | {n} | {t} | {e} | {p} | {s} |" for a, n, t, e, p, s in lignes]
texte = '\n'.join(md) + '\n'
(R / 'docs/SUBDIVISIONS_SANS_TRACE.md').write_text(texte, encoding='utf-8')
if len(sys.argv) > 1: (pathlib.Path(sys.argv[1]) / '00_SUBDIVISIONS_SANS_TRACE.md').write_text(texte, encoding='utf-8')
print(f'{len(lignes)} lots suivis ; {tot_t}/{tot} subdivisions tracées')
