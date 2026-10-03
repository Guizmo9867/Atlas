"""Exporte la liste « Sources à valider » en deux fichiers lisibles hors de claude.ai, dans le dossier d'échange :
- 00_SOURCES_A_VALIDER.md   : lisible par Ether (et par Guizmo), avec le lien de chaque source ;
- 00_SOURCES_A_VALIDER.html : la même page que sur claude.ai, à ouvrir dans un navigateur (lecture seule :
  les boutons n'enregistrent que sur la page publiée sur claude.ai).
Usage : python outils/sources/exporter_sources_a_valider.py <dossier d'échange>   (depuis la racine du dépôt)
"""
import sys, json, pathlib, datetime
RACINE = pathlib.Path(__file__).resolve().parents[2]
ECHANGE = pathlib.Path(sys.argv[1])
d = json.load(open(RACINE / 'data/sources/sources_a_valider.json', encoding='utf-8'))
S = d['sources']
GROUPES = {'a_lire': "Claude n'a pas pu lire la page", 'partielle': 'Lecture partielle ou faible', 'lien_mort': 'Lien mort', 'remplacee': 'Déjà remplacée (facultatif)'}
modele = (RACINE / 'outils/sources/page_sources_a_valider_modele.html').read_text(encoding='utf-8')
(ECHANGE / '00_SOURCES_A_VALIDER.html').write_text(modele.replace('__DONNEES__', json.dumps(d, ensure_ascii=False).replace('</', '<\\/')), encoding='utf-8')
out = ['# Atlas — sources à valider', '',
       f"*Généré le {datetime.datetime.now().strftime('%d/%m/%Y à %H h %M')} depuis le registre v{d.get('version_registre')} : {len(S)} sources que Claude n'a pas pu confirmer.*", '',
       "Pour chaque source : ouvrir le lien, chercher le passage indiqué, et dire si elle prouve ce qu'on lui fait dire.",
       "Guizmo enregistre sa décision avec les boutons de la page « Sources à valider » sur claude.ai ; ce fichier sert à la lire et à en discuter (avec Ether, par exemple).", '']
for g, titre in GROUPES.items():
    grp = [s for s in S if s['groupe'] == g]
    if not grp: continue
    out += [f'## {titre} ({len(grp)})', '']
    for s in grp:
        out += [f"### {s['titre'] or s['id']}", '',
                f"- **Identifiant** : `{s['id']}` · {'villes' if s['domaine'] == 'villes' else 'frontières'} · niveau {s.get('niveau') or '?'}"
                + (f" · {s['institution']}" if s.get('institution') else ''),
                f"- **Lien** : {s['url']}" if s.get('url') else '- **Lien** : (aucun)']
        if s.get('villes'): out.append(f"- **Villes** : {', '.join(s['villes'])}")
        if s.get('ou_regarder'): out.append(f"- **Où regarder** : {s['ou_regarder']}")
        if s.get('extrait'): out.append(f"- **Ce que Claude a pu lire** : « {s['extrait']} »")
        if s.get('remplacee_par'): out.append(f"- **Déjà remplacée par** : {', '.join(s['remplacee_par'])}")
        if s.get('notes'): out.append(f"- **Notes** : {s['notes']}")
        out += ['- **Décision de Guizmo** : …', '']
(ECHANGE / '00_SOURCES_A_VALIDER.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'sources -> 00_SOURCES_A_VALIDER.md et .html')
