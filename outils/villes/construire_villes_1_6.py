"""Ratissage villes 1.6 (URSS d'Asie hors Caucase : Sibérie, Extrême-Orient, Kazakhstan, Asie centrale ; Mongolie)
-> data/snapshot0/villes_1-6_asie_sovietique_mongolie.json

Données : proposition JSON d'Ether du 03/10/2026, au format du gabarit
(data/sources/deltas_ether/2026-10-03_villes_1-6_proposition_ether.json ; note : villes_1-6_asie_sovietique_mongolie_brief_ether.md ;
réserves R16-01 à R16-69 : villes_1-6_asie_sovietique_mongolie_reserves_ether.md).
Positions : Wikidata (CC0) pour les 254 villes, recoupées par requête SPARQL (outils/villes/wikidata_ratissage_1_6.json).
v0.2 (04/10/2026) : preuves relues ville par ville (outils/villes/confirmations_claude.py) après les réponses d'Ether (cycle 2).
Relancer : python outils/villes/construire_villes_1_6.py (depuis la racine du dépôt), après les fusions de sources.
"""
import json, pathlib, copy
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-6_proposition_ether.json', encoding='utf-8'))['proposition_ether']
QID = json.load(open(ICI / 'wikidata_ratissage_1_6.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Capitales : Ether applique déjà la convention du journal (RSS = « regionale » : Alma-Ata, Tachkent, Frounzé, Stalinabad,
# Achkhabad ; Oulan-Bator = « nationale »). Chefs-lieux d'oblast et capitales de RSSA (Iakoutsk, Oulan-Oudé, Noukous) :
# rôle capitale sans type d'affichage (Q15-02 / R16-02, revue finale). Rien n'est changé ici.
CAPITALES_ATTENDUES = {'ville-kz-almaty': 'regionale', 'ville-uz-tachkent': 'regionale', 'ville-kg-bichkek': 'regionale',
                       'ville-tj-douchanbe': 'regionale', 'ville-tm-achgabat': 'regionale', 'ville-mn-oulan-bator': 'nationale'}

# Nom « de 1945 » identique au nom de la fiche à l'apostrophe près (Nikolaïevsk-sur-l’Amour, Komsomolsk-sur-l’Amour) :
# ce n'est pas un autre nom, il n'est pas affiché comme tel (règle : « nom » seulement s'il diffère du nom actuel).
# Les autres écarts de pure transcription (Tokmok/Tokmak, Farap/Farab…) sont gardés tels que proposés : Q16-03, revue finale.
# Corrections ciblées proposées par Ether et retenues par Claude après lecture de la page (Tchirtchik : gare à 32 km, p. 265 du répertoire de 1940).
CORR = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-04_villes_1-6_corrections_cycle3_ether.json', encoding='utf-8'))['corrections']
def corriger(e):
    for c in CORR:
        if c['entite_id'] != e['entite_id']: continue
        p = e['etats'][0]['proprietes']
        p['roles'] = c['champs_seuls']['proprietes.roles']
        p['note'] = c['champs_seuls']['proprietes.note']
        for r in c['sources_usage_a_remplacer']:
            for s in e['etats'][0]['sources']:
                if s['source_id'] == r['source_id']: s['locator'], s['usage'] = r['locator'], r['usage']

memes_noms = []
entites = []
for v in PROPOSITION['entites']:
    e = copy.deepcopy(v); corriger(e); eid = e['entite_id']; et = e['etats'][0]; p = et['proprietes']
    assert p.get('capitale') == CAPITALES_ATTENDUES.get(eid), eid
    if p.get('nom') and p['nom'].replace('’', "'") == e['nom'].replace('’', "'"):
        e['aliases'] = list(dict.fromkeys([*e.get('aliases', []), p.pop('nom')])); memes_noms.append(eid)
    assert eid in QID and QID[eid]['ecart_km_wikidata'] == 0.0, eid
    prouve = set()
    for s in et['sources']:
        if s['source_id'] == 'src-wikidata':
            continue
        st = REGISTRE[s['source_id']]['verification_claude']
        cr, cm = confirmation(REGISTRE[s['source_id']], eid) if st != 'ok' else (None, None)
        if st == 'ok' or cr == 'usage': prouve |= {t.strip() for t in s['usage'].split(',')} & set(p['roles'])
        elif cr: prouve |= cr & set(p['roles'])
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    note = p['note']
    if p.get('capitale') == 'regionale':
        note += " Capitale « régionale » au Snapshot 0 : capitale de RSS (même convention que Tallinn, Riga, Vilnius, Minsk et Kiev)."
    if p.get('nom'): note += f" Nom à la date : {p['nom']} (aujourd'hui {e['nom']})."
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    p['note'] = note
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-6_asie_sovietique_mongolie', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.3', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'limites_ether': PROPOSITION['metadata_lot']['limites'],
    'reserves_ether': 'R16-01 à R16-69 (data/snapshot0/villes_1-6_asie_sovietique_mongolie_reserves_ether.md), revue finale 1.x',
    'integration': {'date': '2026-10-03', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (254 villes : RU 135, KZ 41, UZ 23, MN 19, KG 16, TM 12, TJ 8), IDs déjà au code du pays actuel ; noms de 1945 dans l'état (91), nom actuel sur la fiche ; aucun nom_local.",
      "Positions : Wikidata pour les 254 villes (QID et coordonnées recoupés par Claude, écart nul, pays actuel concordant, aucun QID ni ID commun avec les 525 villes déjà intégrées).",
      "Capitales : 5 capitales de RSS « régionales », Oulan-Bator « nationale » (convention du journal) ; RSSA et oblasts sans type d'affichage (Q15-02, R16-02).",
      "Preuves : mention « (non vérifiée par Claude) » ou « (lecture partielle) » selon la relecture de Claude ; « À renforcer » = rôles sans aucune preuve confirmée.",
      "Nikolaïevsk-sur-l'Amour et Komsomolsk-sur-l'Amour : le « nom de 1945 » proposé ne différait de la fiche que par l'apostrophe ; gardé en alias, pas affiché comme nom à la date. Autres écarts de transcription conservés (Q16-03).",
      "Sükhbaatar : roles vide, tel que proposé (transit routier en note).",
      "v0.2 (04/10/2026, réponses d'Ether cycle 2, Q16-01 et Q16-02) : aucune donnée de ville modifiée ; Claude a lu les 28 images de pages des répertoires administratifs (1940, 1941, supplément 1944) et les 3 pages LOC : 67 relations ville/source relues, rôles comptés comme prouvés pour ces villes seulement (registre v1.21, champ confirmations_claude) ; mentions de preuve et « À renforcer » recalculés.",
      "v0.3 (04/10/2026, réponses d'Ether cycle 3) : Tchirtchik perd le rôle rail (la page 265 du répertoire de 1940, relue par Claude, met la gare à 32 km ; correction d'Ether) ; 37 images de pages et 9 captures lues par Claude (registre v1.24) : rôles relus ville par ville, mentions de preuve et « À renforcer » recalculés."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-6_asie_sovietique_mongolie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ; même nom :', memes_noms, '->', out.relative_to(RACINE), '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites))
