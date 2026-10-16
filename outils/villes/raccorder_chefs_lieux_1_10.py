"""Raccord des chefs-lieux 2.FR aux villes du lot 1.10 (16/10/2026, boucle automatique, mode d'emploi §0 « Complément villes_1-10 »).
Règle : chef_lieu_id ajouté seulement si la preuve vaut pour le 01/01/1945 ; chef_lieu_propose (référence 1940) est gardé.
- 8 circonscriptions régionales : même base que les 10 raccords du pilote 2.FR (réponse ministérielle AN 1981, « ok »,
  ressorts des commissaires de la République modifiés jusqu'au 29/11/1944), maintenant que leur ville existe.
- 3 départements : source relue « ok » qui établit explicitement la fonction sur une période incluant le 01/01/1945
  (Mézières : préfecture depuis 1800 ; Rodez : mêmes locaux depuis 1823 ; Albi : lettre au préfet du Tarn à Albi du 31/10/1944).
Les 63 autres départements gardent leur chef-lieu de 1940 non validé (R2FR-05, R110-02). Relancer sans risque (idempotent).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
F = RACINE / 'data/snapshot0/subdivisions_2-FR.json'
VILLES = {e['entite_id']: e for e in json.load(open(RACINE / 'data/snapshot0/villes_1-10_complement_france.json', encoding='utf-8'))['entites']}
RACCORDS = {
  'subdivision-fr-commissariat-angers': ('ville-fr-angers', 'AN 1981'), 'subdivision-fr-commissariat-chalons-sur-marne': ('ville-fr-chalons-en-champagne', 'AN 1981'),
  'subdivision-fr-commissariat-clermont-ferrand': ('ville-fr-clermont-ferrand', 'AN 1981'), 'subdivision-fr-commissariat-laon': ('ville-fr-laon', 'AN 1981'),
  'subdivision-fr-commissariat-montpellier': ('ville-fr-montpellier', 'AN 1981'), 'subdivision-fr-commissariat-nancy': ('ville-fr-nancy', 'AN 1981'),
  'subdivision-fr-commissariat-orleans': ('ville-fr-orleans', 'AN 1981'), 'subdivision-fr-commissariat-poitiers': ('ville-fr-poitiers', 'AN 1981'),
  'subdivision-fr-ardennes': ('ville-fr-mezieres', 'src-v110-mezieres-histoire'), 'subdivision-fr-aveyron': ('ville-fr-rodez', 'src-v110-rodez-histoire'),
  'subdivision-fr-tarn': ('ville-fr-albi', 'src-v110-albi-prefet')}
d = json.load(open(F, encoding='utf-8'))
fait = []
for e in d['entites']:
    if e['entite_id'] not in RACCORDS: continue
    vid, base = RACCORDS[e['entite_id']]; assert vid in VILLES, vid
    p = e['etats'][0]['proprietes']
    nom_attendu = (p.get('chef_lieu_propose') or {}).get('nom') or p.get('chef_lieu_nom')
    noms_ville = {VILLES[vid]['nom'], VILLES[vid]['etats'][0]['proprietes'].get('nom')}
    assert nom_attendu in noms_ville, (e['entite_id'], nom_attendu, noms_ville)
    if p.get('chef_lieu_id') != vid:
        p['chef_lieu_id'] = vid
        p['note'] = p.get('note', '') + f" Chef-lieu raccordé à {vid} le 16/10/2026 (villes 1.10 ; preuve valable au 01/01/1945 : {base})."
    fait.append(e['entite_id'])
assert len(fait) == len(RACCORDS), set(RACCORDS) - set(fait)
F.write_text(json.dumps(d, ensure_ascii=False, indent=1 if '\n "' in F.read_text(encoding='utf-8')[:200] else 2) + '\n', encoding='utf-8')
print(len(fait), 'raccords ;', sum(1 for e in d['entites'] if e['etats'][0]['proprietes'].get('chef_lieu_id')), 'subdivisions 2.FR avec chef_lieu_id')
