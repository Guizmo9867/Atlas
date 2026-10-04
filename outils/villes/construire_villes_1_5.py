"""Ratissage villes 1.5 (Russie d'Europe et Oural, Biélorussie, Ukraine/Crimée, Moldavie, Prusse-Orientale aujourd'hui russe)
-> data/snapshot0/villes_1-5_europe_orientale.json

Données : proposition JSON d'Ether du 02/10/2026, déjà au format du gabarit
(data/sources/deltas_ether/2026-10-02_villes_1-5_proposition_ether.json ; note : villes_1-5_europe_orientale_brief_ether.md ;
réserves R15-01 à R15-36 : villes_1-5_europe_orientale_reserves_ether.md).
Positions : Wikidata (CC0) pour 195 villes, recoupées par requête SPARQL (outils/villes/wikidata_ratissage_1_5.json) ;
GeoNames (CC BY 4.0) pour 5 villes (Ivanovo, Rodniki, Teïkovo, Kokhma, Tchernikovsk), repères actuels proposés par Ether (R15-17, R15-28).
v0.2 (03/10/2026) : mêmes données, mentions de preuve recalculées après les réponses d'Ether (cycle 2).
v0.3 (04/10/2026) : idem après le cycle 3 (captures Q15-03 lues par Claude ; preuves relues ville par ville, outils/villes/confirmations_claude.py).
Relancer : python outils/villes/construire_villes_1_5.py (depuis la racine du dépôt).
"""
import json, pathlib, copy
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-02_villes_1-5_proposition_ether.json', encoding='utf-8'))['proposition_ether']
QID = json.load(open(ICI / 'wikidata_ratissage_1_5.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Capitales de RSS : convention du journal (01/10/2026, Vienne/Prague) déjà appliquée à Tallinn, Riga et Vilnius :
# capitale « régionale » = siège administratif de fait en RSS. Ether avait laissé l'attribut vide (R15-36) en lisant
# les capitales baltes comme « nationales », ce qui n'est pas le cas dans le dépôt : la convention existante est appliquée,
# R15-36 reste dans la revue finale pour la typologie d'ensemble des RSS.
CAPITALE_RSS = {'ville-by-minsk', 'ville-ua-kiev', 'ville-md-chisinau', 'ville-ru-petrozavodsk'}
# Chefs-lieux d'oblast et capitales de RSS autonomes : Ether proposait « regionale » pour 15 d'entre eux, mais pas pour
# d'autres chefs-lieux du même lot (Briansk, Ijevsk, Kharkiv, Odessa, Lviv…), et aucune règle du journal ne couvre ce cas.
# Attribut non appliqué (point incertain, Q15-02 / revue finale) ; rôles, preuves et notes d'Ether conservés.
MOTS_ROLES = {  # libellés d'usage d'Ether -> rôles prouvés
    'rôle ferroviaire': ['rail'], 'rôle industriel': ['industrie'], 'rôle portuaire fluvial': ['port_fluvial'],
    'chef-lieu': ['administration', 'capitale'], 'capitale': ['capitale', 'administration'], 'administration': ['administration', 'capitale'],
    'ateliers industriels': ['industrie'],
}

def roles_prouves(usage, roles):
    out = {r for r in roles if r in usage}
    for mot, rs in MOTS_ROLES.items():
        if mot in usage: out |= {r for r in rs if r in roles}
    return out

retires_capitale, entites = [], []
for v in PROPOSITION['entites']:
    e = copy.deepcopy(v); eid = e['entite_id']; et = e['etats'][0]; p = et['proprietes']
    if eid in CAPITALE_RSS: p['capitale'] = 'regionale'
    elif p.get('capitale') == 'regionale':
        del p['capitale']; retires_capitale.append(eid)
    statut = lambda s: 'ok' if s == 'src-wikidata' else REGISTRE[s]['verification_claude']
    prouve = set()
    for s in et['sources']:
        if s['source_id'].startswith(('src-wikidata', 'src-geonames')):
            continue
        st = statut(s['source_id'])
        cr, cm = confirmation(REGISTRE.get(s['source_id']), eid) if st != 'ok' else (None, None)
        if st == 'ok' or cr == 'usage': prouve |= roles_prouves(s['usage'], p['roles'])
        elif cr: prouve |= cr & set(p['roles'])
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    note = p['note']
    if eid in CAPITALE_RSS:
        note += " Capitale « régionale » au Snapshot 0 : capitale de RSS (même convention que Tallinn, Riga et Vilnius)."
    if eid in retires_capitale:
        note += " Chef-lieu : type de capitale non affiché, convention des chefs-lieux d'oblast et de RSSA en réserve (revue finale 1.x)."
    if p.get('nom'): note += f" Nom à la date : {p['nom']} (aujourd'hui {e['nom']})."
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    p['note'] = note
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-5_europe_orientale', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.3', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'limites_ether': PROPOSITION['metadata_lot']['limites'],
    'reserves_ether': 'R15-01 à R15-36 (data/snapshot0/villes_1-5_europe_orientale_reserves_ether.md), revue finale 1.x',
    'integration': {'date': '2026-10-02', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (200 villes : RU 105, UA 66, BY 24, MD 5), IDs déjà au code du pays actuel ; noms de 1945 dans l'état (67), nom actuel sur la fiche ; aucun nom_local.",
      "Positions : Wikidata pour 195 villes (QID et coordonnées recoupés par Claude, écart nul, pays actuel concordant) ; GeoNames pour 5 repères actuels (R15-17, R15-28).",
      "Capitales : Moscou nationale ; Minsk, Kiev, Kichinev, Petrozavodsk régionales (capitales de RSS, convention du journal du 01/10) ; attribut « regionale » non appliqué aux 15 chefs-lieux d'oblast ou de RSSA proposés par Ether (convention non établie, Q15-02).",
      "Preuves : mention « (non vérifiée par Claude) » ou « (lecture partielle) » selon la relecture de Claude ; « À renforcer » = rôles sans aucune preuve confirmée.",
      "Tilsit, Insterburg, Gumbinnen, Ragnit et Béjitsa : roles vide, tel que proposé (R15-07).",
      "v0.2 (03/10/2026, réponses d'Ether cycle 2) : aucune donnée de ville modifiée ; mentions de preuve recalculées d'après le registre v1.18 (Soumy confirmée sur la page 353 du recueil ; six sources Q15-03 passent de « faible » à « non vérifiée », l'outil de Claude n'ayant lu que le début des pages).",
      "v0.3 (04/10/2026, réponses d'Ether cycle 3, Q15-03) : aucune donnée de ville modifiée ; Claude a lu les 12 captures déposées par Ether : 8 sources relues, leurs villes passent en « page relue par Claude pour cette ville » (registre v1.20, champ confirmations_claude) ; mentions de preuve et « À renforcer » recalculés."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-5_europe_orientale.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE), '; capitale retirée :', len(retires_capitale),
      '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites))
