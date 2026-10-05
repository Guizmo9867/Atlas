"""Ratissage villes 1.9 (Ibérie et marges : ES, PT, AD, GI, MC, VA, SM, MT, CY)
-> data/snapshot0/villes_1-9_iberie_marges.json

Données : proposition JSON d'Ether du 05/10/2026, au format du gabarit
(data/sources/deltas_ether/2026-10-05_villes_1-9_proposition_ether.json ; note : villes_1-9_iberie_marges_brief_ether.md ;
réserves R19-01 à R19-24 : villes_1-9_iberie_marges_reserves_ether.md ; 10 candidats différés non importés).
Positions : QID Wikidata (CC0) proposés par Ether, recoupés par Claude par SPARQL (outils/villes/wikidata_ratissage_1_9.json ;
aucun écart > 1 km, pays cohérents, aucun doublon avec les villes déjà intégrées ; Vatican à 2 km du point de Rome).
Relancer : python outils/villes/construire_villes_1_9.py (depuis la racine du dépôt), après fusion_sources_1_9.py.
"""
import json, pathlib, copy, re
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_villes_1-9_proposition_ether.json', encoding='utf-8'))['proposition_ether']
WD = json.load(open(ICI / 'wikidata_ratissage_1_9.json', encoding='utf-8'))['villes']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Capitales au 01/01/1945 (proposées par Ether). Monaco et Vatican sans champ capitale (convention de cité-État réservée,
# R19) ; Nicosie et La Valette : chefs-lieux de colonies britanniques (type « territoire »).
CAPITALES_ATTENDUES = {'ville-es-madrid': 'nationale', 'ville-pt-lisbonne': 'nationale', 'ville-ad-andorre-la-vieille': 'nationale',
                       'ville-sm-saint-marin': 'nationale', 'ville-cy-nicosie': 'territoire', 'ville-mt-la-valette': 'territoire'}
NON_PREUVE = ('src-wikidata',)
INDEXE = ' ; passage indexé seulement, lecture directe à confirmer'

def roles_de(usage):
    return {t.strip() for t in re.split(r'[,;]', usage)}

entites = []
for v in PROPOSITION['entites']:
    e = copy.deepcopy(v); eid = e['entite_id']; et = e['etats'][0]; p = et['proprietes']
    assert p.get('capitale') == CAPITALES_ATTENDUES.get(eid), eid
    w = WD[eid]
    et['geometrie'] = {'type': 'Point', 'coordinates': [round(w['coord_wikidata'][0], 6), round(w['coord_wikidata'][1], 6)]}
    vues, srcs = set(), []
    for s in et['sources']:
        cle = (s['source_id'], s.get('usage'), s.get('locator'))
        if cle in vues: continue
        vues.add(cle); srcs.append(s)
    et['sources'] = srcs
    prouve = set()
    for s in srcs:
        if s['source_id'] in NON_PREUVE:
            s['usage'] = 'position actuelle (repère), recoupée par Claude ; aucune preuve de rôle historique'
            continue
        st = REGISTRE[s['source_id']]['verification_claude']
        if st == 'ok': s['usage'] = s['usage'].replace(INDEXE, '')
        roles_usage = roles_de(s['usage']) & set(p['roles'])
        cr, cm = confirmation(REGISTRE[s['source_id']], eid) if st != 'ok' else (None, None)
        if st == 'ok' or cr == 'usage': prouve |= roles_usage
        elif cr: prouve |= cr & roles_usage
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    note = p['note']
    if p.get('nom'): note += f" Nom à la date : {p['nom']} (aujourd'hui {e['nom']})."
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    p['note'] = note
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-9_iberie_marges', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.1', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'limites_ether': PROPOSITION['metadata_lot']['limites_ether'],
    'reserves_ether': 'R19-01 à R19-24 (data/snapshot0/villes_1-9_iberie_marges_reserves_ether.md), revue finale 1.x',
    'integration': {'date': '2026-10-05', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (238 villes : ES 158, PT 61, CY 7, MT 5, AD 2, SM 2, GI 1, VA 1, MC 1), IDs déjà au code du pays actuel ; 3 noms de 1945 dans l'état (El Ferrol del Caudillo, Mahón, Puerto Cabras), nom actuel sur la fiche ; aucun nom_local ; 10 candidats différés non importés (Canfranc, Chinchilla, La Encina, Bobadilla, Moreda, Casa Branca, Tua, Pocinho, Cabeço de Vide, Estella-Lizarra).",
      "Positions : QID Wikidata (CC0) d'Ether recoupés par SPARQL : aucun écart > 1 km, pays cohérents ; aucun ID commun avec les 1306 villes déjà intégrées ; Cité du Vatican à côté de Rome (entités distinctes).",
      "Capitales : « nationale » pour Madrid, Lisbonne, Andorre-la-Vieille, Saint-Marin ; « territoire » pour Nicosie et La Valette ; Monaco et Vatican sans champ capitale (réserve d'Ether). Code pays « sm » ajouté au lexique.",
      "Preuves : carte Forcano 1942 lue par Claude sur 19 captures déposées par Ether (167 villes lues sur une ligne exploitée) ; 34 pages en ligne relues par WebFetch ; mentions « (non vérifiée par Claude) », « (lecture partielle) » ou « (page relue par Claude pour cette ville) » ; « À renforcer » = rôles sans aucune preuve confirmée."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-9_iberie_marges.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE), '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites),
      '; noms de 1945 :', sum(1 for e in entites if e['etats'][0]['proprietes'].get('nom')))
