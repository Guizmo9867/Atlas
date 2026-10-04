"""Ratissage villes 1.8 (Balkans, Grèce et Italie : AL, BA, BG, GR, HR, IT, ME, MK, RO, RS, SI)
-> data/snapshot0/villes_1-8_balkans_grece_italie.json

Données : proposition JSON d'Ether du 04/10/2026, au format du gabarit
(data/sources/deltas_ether/2026-10-04_villes_1-8_proposition_ether.json ; note : villes_1-8_balkans_grece_italie_brief_ether.md ;
réserves R18-01 à R18-70 : villes_1-8_balkans_grece_italie_reserves_ether.md ; 15 candidats différés non importés).
Positions : QID Wikidata (CC0) proposés par Ether, recoupés par Claude par SPARQL (outils/villes/wikidata_ratissage_1_8.json ;
aucun écart > 1 km, aucun doublon avec les villes déjà intégrées).
Relancer : python outils/villes/construire_villes_1_8.py (depuis la racine du dépôt), après fusion_sources_1_8.py.
"""
import json, pathlib, copy, re
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-04_villes_1-8_proposition_ether.json', encoding='utf-8'))['proposition_ether']
WD = json.load(open(ICI / 'wikidata_ratissage_1_8.json', encoding='utf-8'))['villes']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Capitales d'États au 01/01/1945 (proposées par Ether). Zagreb (État indépendant de Croatie), Salò (RSI) et les futures
# capitales de républiques yougoslaves ne reçoivent pas de type d'affichage (réserves d'Ether, revue finale 1.x).
CAPITALES_ATTENDUES = {'ville-ro-bucarest': 'nationale', 'ville-bg-sofia': 'nationale', 'ville-rs-belgrade': 'nationale',
                       'ville-it-rome': 'nationale', 'ville-gr-athenes': 'nationale', 'ville-al-tirana': 'nationale'}
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
    'nom': 'snapshot0_villes_1-8_balkans_grece_italie', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.1', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'limites_ether': PROPOSITION['metadata_lot']['limites_ether'],
    'reserves_ether': 'R18-01 à R18-70 (data/snapshot0/villes_1-8_balkans_grece_italie_reserves_ether.md), revue finale 1.x',
    'integration': {'date': '2026-10-04', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (361 villes : IT 140, GR 49, BG 37, RO 34, BA 28, RS 24, HR 19, ME 9, AL 8, MK 7, SI 6), IDs déjà au code du pays actuel ; 8 noms de 1945 dans l'état (Fiume, Pola, Petrovgrad, Caribrod, Gorna Djoumaïa, Bosanski Brod, Bosanski Novi, Cluj), nom actuel sur la fiche ; aucun nom_local ; 15 candidats différés non importés ; Kosovo non couvert (Priština et Mitrovica réservés par Ether).",
      "Positions : QID Wikidata (CC0) d'Ether recoupés par SPARQL : libellé et pays cohérents, aucun écart > 1 km ; aucun QID ni ID commun avec les 945 villes déjà intégrées ; Côme à 5 km de Chiasso (villes distinctes) ; Rijeka/Sušak, Brod/Slavonski Brod, Herceg Novi/Zelenika, Agrigente/Porto Empedocle : paires voisines distinctes en 1945.",
      "Capitales « nationales » : Rome, Athènes, Belgrade, Sofia, Bucarest, Tirana ; aucune autre (Zagreb, futures capitales de républiques yougoslaves : réserves d'Ether).",
      "Preuves : 5 cartes OSS (1942-1944) lues par Claude sur les images déposées par Ether ; 271 villes relues une à une (confirmations_claude). Mentions « (non vérifiée par Claude) », « (lecture partielle) » ou « (page relue par Claude pour cette ville) » ; « À renforcer » = rôles sans aucune preuve confirmée."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-8_balkans_grece_italie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE), '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites),
      '; noms de 1945 :', sum(1 for e in entites if e['etats'][0]['proprietes'].get('nom')))
