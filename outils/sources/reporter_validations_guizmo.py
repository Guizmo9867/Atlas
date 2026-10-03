"""Reporte au registre les décisions de Guizmo sur les « Sources à valider ».

Lit, s'ils existent :
- <dossier d'échange>/decisions_sources_guizmo.json : fichier enregistré depuis 00_SOURCES_A_VALIDER.html (mode fichier),
  avec ses compléments : autres liens proposés par Guizmo et pièces jointes (captures, PDF, en base64) ;
- data/sources/validations_guizmo_claudeai.json : export de la collection « validations » de la page claude.ai
  (à écrire par Claude avec l'outil ArtifactData, action list, avant de lancer ce script ; liens possibles, pas de pièces jointes).
Écrit dans chaque source concernée :
- verification_humaine = {decision, commentaire, par, date} (la source sort alors de la liste « Sources à valider ») ;
- complements_guizmo = {liens, pieces_jointes, date, a_verifier} si Guizmo a donné d'autres liens ou des pièces jointes.
  Les pièces jointes sont écrites dans <dossier d'échange>/05_pieces_jointes_guizmo/<source_id>/ et JAMAIS dans le dépôt
  (dépôt public : droits d'auteur des documents). a_verifier = true tant que Claude ne les a pas vérifiés (BOUCLE_AUTOMATIQUE §3.5).
Décisions possibles : verifiee, verifiee_s0 (prouve pour 1945 ; la source dit aussi un changement plus tard, à reprendre
dans la chronologie : elle est gardée), ne_prouve_pas, lien_mort.
Écrit aussi docs/NOTES_GUIZMO_SOURCES.md : compléments à vérifier, sources « la suite plus tard », autres notes.
Usage : python outils/sources/reporter_validations_guizmo.py <dossier d'échange>   (puis relancer liste_sources_a_valider.py)
        python outils/sources/reporter_validations_guizmo.py --verifier <dossier d'échange>   (n'écrit rien ; dit combien de changements sont nouveaux)
"""
import sys, json, pathlib, base64, re
RACINE = pathlib.Path(__file__).resolve().parents[2]
VERIFIER = '--verifier' in sys.argv
ECHANGE = pathlib.Path([a for a in sys.argv[1:] if a != '--verifier'][0])
PJ = '05_pieces_jointes_guizmo'
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
par_id = {s['source_id']: s for s in reg['sources']}

decisions, complements, donnees = {}, {}, {}
for f in [ECHANGE / 'decisions_sources_guizmo.json', RACINE / 'data/sources/validations_guizmo_claudeai.json']:
    if not f.exists(): continue
    d = json.load(open(f, encoding='utf-8'))
    for sid, v in (d.get('decisions', d)).items():
        if isinstance(v, dict) and v.get('decision'):
            if sid not in decisions or (v.get('le') or '') > (decisions[sid].get('le') or ''):
                decisions[sid] = v
    if isinstance(d.get('complements'), dict):
        complements.update(d['complements'])
    if isinstance(d.get('pieces_donnees'), dict):
        donnees.update(d['pieces_donnees'])

def propre(nom):
    return re.sub(r'[^\w.-]+', '_', nom)[:80] or 'piece'

n, fichiers = 0, []
for sid in sorted(set(decisions) | set(complements)):
    s = par_id.get(sid)
    if not s: continue
    v = decisions.get(sid)
    if v:
        nouveau = {'decision': v['decision'], 'commentaire': v.get('commentaire', ''), 'par': 'Guizmo', 'date': (v.get('le') or '')[:10]}
        if s.get('verification_humaine') != nouveau:
            s['verification_humaine'] = nouveau; n += 1
    c = complements.get(sid) or {}
    liens = list(dict.fromkeys((v or {}).get('liens') or c.get('liens') or []))
    pieces = []
    for p in c.get('pieces') or []:
        chemin = f"{PJ}/{propre(sid)}/{propre(p.get('nom', 'piece'))}"
        if p.get('cle') in donnees:
            fichiers.append((ECHANGE / chemin, donnees[p['cle']]))
            pieces.append(chemin)
    if not liens and not pieces: continue
    ancien = s.get('complements_guizmo') or {}
    if ancien.get('liens') == liens and ancien.get('pieces_jointes') == pieces: continue
    s['complements_guizmo'] = {'liens': liens, 'pieces_jointes': pieces, 'date': ((v or {}).get('le') or '')[:10],
                               'a_verifier': True, 'resultat_claude': ''}
    n += 1

if VERIFIER:
    print(n, 'décisions nouvelles à reporter'); sys.exit(0)
for chemin, b64 in fichiers:
    contenu = base64.b64decode(b64)
    if not (chemin.exists() and chemin.read_bytes() == contenu):
        chemin.parent.mkdir(parents=True, exist_ok=True); chemin.write_bytes(contenu)
if n:
    R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(n, 'décisions ou compléments de Guizmo reportés au registre', f'({len(decisions)} décisions lues, {len(fichiers)} pièces jointes)')

# --- Notes de Guizmo (à relire plus tard) ---
tranchees = [s for s in reg['sources'] if s.get('verification_humaine')]
avec_compl = [s for s in reg['sources'] if s.get('complements_guizmo')]
PLUS_TARD = re.compile(r'plus tard|chronologie', re.I)  # aussi les « Ça prouve » dont la note parle d'un changement plus tard
plus_tard = [s for s in tranchees if s['verification_humaine']['decision'] == 'verifiee_s0' or PLUS_TARD.search(s['verification_humaine'].get('commentaire') or '')]
notes = [s for s in tranchees if s not in plus_tard and s['verification_humaine'].get('commentaire')]
NOMS = {'verifiee': 'Ça prouve', 'verifiee_s0': 'Prouve pour 1945 (la suite plus tard)', 'ne_prouve_pas': 'Ne prouve pas', 'lien_mort': 'Lien mort'}
def ligne(s):
    v = s.get('verification_humaine') or {}
    l = [f"- **{s['source_id']}** — {s.get('titre', '')}", f"  - Lien : {s.get('url', '')}"]
    if v:
        l += [f"  - Décision : {NOMS.get(v['decision'], v['decision'])} (Guizmo, {v.get('date', '')})",
              f"  - Note de Guizmo : {v.get('commentaire') or '(aucune)'}"]
    c = s.get('complements_guizmo')
    if c:
        l += [f"  - Autre lien proposé par Guizmo : {u}" for u in c.get('liens', [])]
        l += [f"  - Pièce jointe (dossier Atlas) : {p}" for p in c.get('pieces_jointes', [])]
        l.append(f"  - Vérifié par Claude : {'non, à faire' if c.get('a_verifier') else 'oui — ' + (c.get('resultat_claude') or '')}")
    return '\n'.join(l)
md = ['# Notes de Guizmo sur les sources', '',
      '*Généré par `outils/sources/reporter_validations_guizmo.py`. Ne pas modifier à la main.*', '',
      f'{len(tranchees)} sources tranchées par Guizmo au total.', '',
      '## Autres liens et pièces jointes donnés par Guizmo', '',
      'Quand une source ne prouve pas (ou a un lien mort), Guizmo peut proposer d\'autres liens ou joindre une capture ou un PDF. '
      'Claude les vérifie, puis ajoute les bonnes preuves au registre comme nouvelles sources (l\'ancienne est marquée « remplacée »). '
      'Les pièces jointes restent dans le dossier Atlas du PC (`05_pieces_jointes_guizmo/`), jamais dans le dépôt public.', '']
md += [ligne(s) for s in avec_compl] or ['(aucun pour le moment)']
md += ['', '## À reprendre plus tard dans la chronologie', '',
       'Ces sources sont **valides pour le Snapshot 0** (1945). Elles disent aussi un changement plus tard (nom, statut…) : '
       'elles restent au registre et seront relues quand le ratissage avancera dans le temps.', '']
md += [ligne(s) for s in plus_tard] or ['(aucune pour le moment)']
md += ['', '## Autres sources tranchées avec une note', '']
md += [ligne(s) for s in notes if not s.get('complements_guizmo')] or ['(aucune pour le moment)']
(RACINE / 'docs/NOTES_GUIZMO_SOURCES.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(len(avec_compl), 'sources avec compléments,', len(plus_tard), '« la suite plus tard »,', len(notes), 'autres notes -> docs/NOTES_GUIZMO_SOURCES.md')
