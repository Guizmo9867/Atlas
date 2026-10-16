"""Villes 1.10, cycle 2 : 4 raccords de chefs-lieux 2.FR de plus (même règle que raccorder_chefs_lieux_1_10.py : preuve « ok » qui établit
explicitement la fonction sur une période incluant le 01/01/1945 ; chef_lieu_propose gardé). Relecture de Claude sur pièces locales d'Ether :
Creuse -> Guéret (siège constamment affecté depuis 1802), Doubs -> Besançon (services de l'État dans ces bâtiments depuis plus de 200 ans),
Lot -> Cahors (bâtiment partagé avec le département de 1800 à 2011), Hautes-Pyrénées -> Tarbes (préfecture installée depuis 1800). Idempotent.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
F = RACINE / 'data/snapshot0/subdivisions_2-FR.json'
VILLES = {e['entite_id']: e for e in json.load(open(RACINE / 'data/snapshot0/villes_1-10_complement_france.json', encoding='utf-8'))['entites']}
REG = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
RACCORDS = {'subdivision-fr-creuse': ('ville-fr-gueret', 'src-v110-gueret-histoire'), 'subdivision-fr-doubs': ('ville-fr-besancon', 'src-v110-besancon-histoire'),
            'subdivision-fr-lot': ('ville-fr-cahors', 'src-v110-cahors-exposition'), 'subdivision-fr-hautes-pyrenees': ('ville-fr-tarbes', 'src-v110-tarbes-histoire')}
texte = F.read_text(encoding='utf-8'); d = json.loads(texte); fait = []
for e in d['entites']:
    if e['entite_id'] not in RACCORDS: continue
    vid, src = RACCORDS[e['entite_id']]; assert vid in VILLES and REG[src]['verification_claude'] == 'ok', (vid, src)
    p = e['etats'][0]['proprietes']; assert p['chef_lieu_propose']['nom'] == VILLES[vid]['nom'], vid
    if p.get('chef_lieu_id') != vid:
        p['chef_lieu_id'] = vid
        p['note'] = p.get('note', '') + f" Chef-lieu raccordé à {vid} le 16/10/2026 (villes 1.10, cycle 2 ; preuve valable au 01/01/1945 : {src})."
    fait.append(e['entite_id'])
assert len(fait) == len(RACCORDS)
F.write_text(json.dumps(d, ensure_ascii=False, indent=1 if '\n "' in texte[:200] else 2) + '\n', encoding='utf-8')
print(len(fait), 'raccords ;', sum(1 for e in d['entites'] if e['etats'][0]['proprietes'].get('chef_lieu_id')), 'subdivisions 2.FR avec chef_lieu_id')
