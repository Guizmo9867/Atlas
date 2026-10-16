"""Fusion au registre des sources du lot villes 1.10 (complément France : chefs-lieux départementaux, Ether, remise du 16/10/2026)
et de la réponse documentaire Q2CH-05 (2.CH). À lancer UNE fois (v1.36 -> v1.37).
Delta : data/sources/deltas_ether/2026-10-16_villes_1-10_delta.json (63 ajouts, 2 compléments : TRF-GIS et réponse AN 1981).
Q2CH-05 : data/sources/deltas_ether/2026-10-16_2CH_Q2CH-05_delta.json (accès complémentaires, même source, mêmes cibles).
Relecture : data/sources/verifications_claude/2026-10-16_villes_1-10.json (WebFetch seul). Le champ verification_claude d'Ether est
ignoré (gardé sous verification_claude_ether). IDs de villes rapprochés du nom actuel (RENOMMAGE, voir construire_villes_1_10.py).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.36', 'ordre des fusions ?'
RENOMMAGE = {'ville-fr-bourg': 'ville-fr-bourg-en-bresse', 'ville-fr-digne': 'ville-fr-digne-les-bains',
             'ville-fr-le-puy': 'ville-fr-le-puy-en-velay', 'ville-fr-chalons-sur-marne': 'ville-fr-chalons-en-champagne'}
ren = lambda l: [RENOMMAGE.get(x, x) for x in l]
VERIF = 'data/sources/verifications_claude/2026-10-16_villes_1-10.json'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-16_villes_1-10_delta.json', encoding='utf-8'))['sources']
V = json.load(open(RACINE / VERIF, encoding='utf-8'))
verif = {r['id']: r for r in V['resultats']}
par_id = {s['source_id']: s for s in reg['sources']}
urls = {s['url'] for s in reg['sources']}
CONNUS = {'source_id', 'operation_registre', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation',
          'cibles', 'usage', 'usages_atlas', 'locator', 'note', 'verification_ether', 'verification_claude', 'resume_passage'}
ajouts, bilan = 0, {}
for s in delta:
    sid = s['source_id']
    if s['operation_registre'] == 'completer':
        x = par_id[sid]; c = s['complement_ether_villes_110']
        nv = ren(c['cibles'])
        x['cibles'] = list(dict.fromkeys([*x.get('cibles', []), *nv]))
        x['usages_atlas'] = list(dict.fromkeys([*x.get('usages_atlas', []), 'villes_snapshot0']))
        x['preuves_ether'] = x.get('preuves_ether', []) + [p for p in c.get('preuves_ether', []) if p not in x.get('preuves_ether', [])]
        if sid == 'src-trfgis-departements-1940':
            x['notes'] += (" Villes 1.10 (16/10/2026) : nom de référence 1940 et point de mairie moderne (CC BY 4.0, attribution Victor Gay) "
                           f"pour {len(nv)} villes ; ni preuve autonome de 1945, ni bâtiment préfectoral. Points recoupés par Claude avec Wikidata "
                           "(code INSEE P374, écart maximal 1,1 km ; outils/villes/wikidata_ratissage_1_10.json).")
        else:
            x['notes'] += (" Villes 1.10 (16/10/2026) : rôle régional de Nancy, Orléans et Poitiers (sièges de commissariats régionaux, p. 164) ; "
                           "pas de preuve autonome du siège départemental au jour exact (Ether). Avis « ok » de Claude inchangé.")
        continue
    assert sid not in par_id, sid
    v = verif[sid]
    usage = ' ; '.join(s['usage']) if isinstance(s['usage'], list) else s['usage']
    fiche = {
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': ['FR'],
        'usages_atlas': s.get('usages_atlas', []), 'cibles': ren(s['cibles']), 'locator': s['locator'],
        'resume_passage': v['citation'][:1500] if v['statut'] in ('ok', 'limite', 'faible') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s.get('verification_ether'),
        'notes': (f"Proposée par Ether (villes 1.10, 16/10/2026). Ce que la source prouve selon Ether : {usage}. "
                  f"Passage résumé par Ether : {s.get('resume_passage', '')} Limite annoncée par Ether : {s.get('note', '')} "
                  f"Relecture Claude 16/10/2026 : {v['commentaire']}"
                  + (" La page établit la fonction sur une période qui inclut le 01/01/1945." if v.get('couvre_1945') == 'oui' else '')
                  + (" URL déjà présente au registre sous un autre identifiant." if s['url'] in urls else '')),
    }
    if s.get('verification_claude'): fiche['verification_claude_ether'] = s['verification_claude']
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    reg['sources'].append(fiche); ajouts += 1; bilan[v['statut']] = bilan.get(v['statut'], 0) + 1
# Q2CH-05 : accès complémentaires de la même source (page de description Commons et permalien)
x = par_id['src-ch-constitution-1874-art1']
x['acces_complementaires'] = [
    {'url': 'https://commons.wikimedia.org/wiki/File:Constitution_Suisse,_1874.pdf', 'nature': 'page de description du fichier (Commons)'},
    {'url': 'https://commons.wikimedia.org/w/index.php?title=File:Constitution_Suisse,_1874.pdf&oldid=867653855', 'nature': 'permalien de cette page'}]
x['notes'] += (" Q2CH-05 (16/10/2026) : Ether donne la page de description Commons et son permalien ; la copie locale livrée a la même taille "
               "(7 873 000 octets) et le même SHA-1 que le fichier décrit (contrôle d'Ether). Ces deux pages n'ont pas pu être relues par Claude "
               "(WebFetch : URL_NOT_FOUND) ; l'avis « ok » sur la capture de l'article 1 est inchangé.")
reg['metadata']['version'] = '1.37'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(ajouts, 'ajouts', bilan, ';', len(reg['sources']), 'sources (v1.37)')
