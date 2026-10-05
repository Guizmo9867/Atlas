"""Recoupement par Claude (SPARQL Wikidata, CC0) des 238 QID proposés par Ether pour le lot villes 1.9 (Ibérie et marges).
Écrit outils/villes/wikidata_ratissage_1_9.json (même format que wikidata_ratissage_1_8.json).
Relancer : python outils/villes/wikidata_recouper_1_9.py (depuis la racine du dépôt ; réseau requis)."""
import json, math, pathlib, urllib.parse, urllib.request
RACINE = pathlib.Path(__file__).resolve().parents[2]
POS = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_positions_wikidata_ether.json', encoding='utf-8'))['positions']
PAYS = {'es': 'Q29', 'pt': 'Q45', 'cy': 'Q229', 'mt': 'Q233', 'ad': 'Q228', 'sm': 'Q238', 'gi': 'Q145', 'va': 'Q237', 'mc': 'Q235'}
qids = sorted({p['qid'] for p in POS.values()})
res = {}
for i in range(0, len(qids), 60):
    lot = ' '.join('wd:' + q for q in qids[i:i + 60])
    q = f"""SELECT ?q ?c ?p ?l WHERE {{ VALUES ?q {{ {lot} }} OPTIONAL {{?q wdt:P625 ?c}} OPTIONAL {{?q wdt:P17 ?p}}
            OPTIONAL {{?q rdfs:label ?l FILTER(lang(?l)='fr')}} }}"""
    url = 'https://query.wikidata.org/sparql?format=json&query=' + urllib.parse.quote(q)
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'AtlasEurasie/0.1'}), timeout=60))
    for b in d['results']['bindings']:
        k = b['q']['value'].rsplit('/', 1)[1]; r = res.setdefault(k, {'c': set(), 'p': set(), 'l': None})
        if 'c' in b: r['c'].add(b['c']['value'])
        if 'p' in b: r['p'].add(b['p']['value'].rsplit('/', 1)[1])
        if 'l' in b: r['l'] = b['l']['value']
def km(a, b):
    return 6371 * math.acos(min(1, math.sin(math.radians(a[1])) * math.sin(math.radians(b[1])) + math.cos(math.radians(a[1])) * math.cos(math.radians(b[1])) * math.cos(math.radians(a[0] - b[0]))))
villes, alertes = {}, []
for eid, p in POS.items():
    r = res.get(p['qid'], {'c': set(), 'p': set(), 'l': None})
    pts = [tuple(map(float, c.split('(')[1].rstrip(')').split())) for c in r['c']]
    eth = p['coordinates_retenues']
    if not pts: alertes.append(f'{eid} : aucun P625'); continue
    best = min(pts, key=lambda c: km(c, eth)); e = round(km(best, eth), 3)
    pays_attendu = PAYS[eid.split('-')[1]]
    if e > 1: alertes.append(f'{eid} : écart {e} km')
    if pays_attendu not in r['p']: alertes.append(f"{eid} : pays Wikidata {sorted(r['p'])} (attendu {pays_attendu})")
    villes[eid] = {'qid': p['qid'], 'label_fr': r['l'], 'pays': sorted(r['p']), 'coord_wikidata': list(best), 'ecart_km_ether': e, 'nb_p625': len(pts)}
out = {'metadata': {'date': '2026-10-05', 'source': 'Wikidata (CC0), SPARQL query.wikidata.org, User-Agent AtlasEurasie/0.1',
                    'methode': "QID proposés par Ether recoupés par Claude : P625 relu (point le plus proche de celui d'Ether quand plusieurs), pays (P17) comparé au préfixe actuel.",
                    'alertes': alertes}, 'villes': villes}
(RACINE / 'outils/villes/wikidata_ratissage_1_9.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(villes), 'villes ;', len(alertes), 'alertes'); print('\n'.join(alertes))
