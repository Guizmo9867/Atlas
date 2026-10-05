"""Ratissage villes 1.7 (Caucase du Nord, Géorgie, Arménie, Azerbaïdjan et Nakhitchevan, Turquie)
-> data/snapshot0/villes_1-7_caucase_turquie.json

Données : proposition JSON d'Ether du 03/10/2026, au format du gabarit
(data/sources/deltas_ether/2026-10-03_villes_1-7_proposition_ether.json ; note : villes_1-7_caucase_turquie_brief_ether.md ;
réserves R17-01 à R17-27 : villes_1-7_caucase_turquie_reserves_ether.md ; 9 candidats différés non importés).
Positions : Ether proposait des repères GeoNames (CC BY 4.0) ; Claude prend les coordonnées Wikidata (CC0) de l'élément relié
à cet identifiant GeoNames (P1566), recoupées par SPARQL (outils/villes/wikidata_ratissage_1_7.json ; écart médian < 1 km,
au plus 5 km pour Bakou et Tbilissi). Le repère GeoNames reste cité comme identité.
Relancer : python outils/villes/construire_villes_1_7.py (depuis la racine du dépôt), après les fusions de sources.
"""
import json, pathlib, copy
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-03_villes_1-7_proposition_ether.json', encoding='utf-8'))['proposition_ether']
WD = json.load(open(ICI / 'wikidata_ratissage_1_7.json', encoding='utf-8'))['villes']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Capitales : convention du journal (capitale de RSS = « regionale » ; État souverain = « nationale »). Ether l'applique déjà.
# RSSA (Adjarie, Abkhazie, Nakhitchevan, Daghestan…), oblasts et provinces turques : pas de type d'affichage (Q15-02, revue finale).
CAPITALES_ATTENDUES = {'ville-tr-ankara': 'nationale', 'ville-ge-tbilissi': 'regionale', 'ville-am-erevan': 'regionale', 'ville-az-bakou': 'regionale'}
# Nom « de 1945 » qui n'est pas un autre nom : İstanbul (I pointé turc) et Ereğli (la fiche ne porte qu'un précisant de lieu).
# Gardé en alias, pas affiché comme renommage (règle du 03/10 : « un autre nom, pas une autre orthographe »).
# Les autres écarts de transcription (Akstafa, Ievlakh, Kiourdamir, Oudjary, Khatchmas, Kazakh, Taouz) restent tels que proposés (Q16-03).
PAS_UN_AUTRE_NOM = {'ville-tr-istanbul', 'ville-tr-eregli-konya', 'ville-tr-eregli-mer-noire'}
NON_PREUVE = ('src-wikidata', 'src-17-geonames-reperes')

# Corrections ciblées proposées par Ether et retenues par Claude après lecture de la page (İzmir : liste de 1944 et ouverture en 1947 de Halkapınar dans la même étude, contradiction relue sur les captures).
CORR = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-04_villes_1-7_corrections_cycle2_ether.json', encoding='utf-8'))['corrections']
def corriger(e):
    for c in CORR:
        if c['entite_id'] != e['entite_id']: continue
        p = e['etats'][0]['proprietes']
        p['roles'] = c['champs_seuls']['proprietes.roles']
        p['note'] = c['champs_seuls']['proprietes.note'].replace(' Position Wikidata Q35997, repère actuel ; centre exact de 1945 non certifié (R17-01).', '')
        for r in c['sources_usage_a_remplacer']:
            for s in e['etats'][0]['sources']:
                if s['source_id'] == r['source_id']: s['locator'], s['usage'] = r['locator'], r['usage']

memes_noms, entites = [], []
for v in PROPOSITION['entites']:
    e = copy.deepcopy(v); corriger(e); eid = e['entite_id']; et = e['etats'][0]; p = et['proprietes']
    assert p.get('capitale') == CAPITALES_ATTENDUES.get(eid), eid
    if eid in PAS_UN_AUTRE_NOM and p.get('nom'):
        e['aliases'] = list(dict.fromkeys([*e.get('aliases', []), p.pop('nom')])); memes_noms.append(eid)
    w = WD[eid]
    et['geometrie'] = {'type': 'Point', 'coordinates': [round(w['coord_wikidata'][0], 6), round(w['coord_wikidata'][1], 6)]}
    # sources : doublons exacts retirés (même source, même usage)
    vues, srcs = set(), []
    for s in et['sources']:
        cle = (s['source_id'], s.get('usage'), s.get('locator'))
        if cle in vues: continue
        vues.add(cle); srcs.append(s)
    srcs.append({'source_id': 'src-wikidata', 'locator': f"{w['qid']} (P625)", 'usage': 'position actuelle (repère), recoupée par Claude'})
    et['sources'] = srcs
    prouve = set()
    for s in srcs:
        if s['source_id'] in NON_PREUVE:
            continue
        st = REGISTRE[s['source_id']]['verification_claude']
        roles_usage = {t.strip() for t in s['usage'].split(',')} & set(p['roles'])
        cr, cm = confirmation(REGISTRE[s['source_id']], eid) if st != 'ok' else (None, None)
        if st == 'ok' or cr == 'usage': prouve |= roles_usage
        elif cr: prouve |= cr & roles_usage
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    note = p['note'].replace(' Repère urbain actuel ; centre exact de 1945 non certifié (R17-01).', '')
    note += f" Position : Wikidata ({w['qid']}), repère urbain actuel ; centre exact de 1945 non certifié (R17-01)."
    if p.get('capitale') == 'regionale':
        note += " Capitale « régionale » au Snapshot 0 : capitale de RSS (même convention que Tallinn, Riga, Minsk, Kiev ou Tachkent)."
    if p.get('nom'): note += f" Nom à la date : {p['nom']} (aujourd'hui {e['nom']})."
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    p['note'] = note
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-7_caucase_turquie', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.3', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': PROPOSITION['metadata_lot']['zone'],
    'limites_ether': PROPOSITION['metadata_lot']['limites'],
    'reserves_ether': 'R17-01 à R17-27 (data/snapshot0/villes_1-7_caucase_turquie_reserves_ether.md), revue finale 1.x',
    'integration': {'date': '2026-10-05', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (166 villes : TR 77, RU 36, GE 26, AZ 16, AM 11), IDs déjà au code du pays actuel ; noms de 1945 dans l'état, nom actuel sur la fiche ; aucun nom_local ; 9 candidats différés non importés.",
      "Positions : coordonnées Wikidata (CC0) de l'élément relié à l'identifiant GeoNames proposé par Ether (repère CC BY 4.0) ; 22 QID choisis à la main quand l'identifiant désignait un élément secondaire (district, localité homonyme) ou n'était pas relié (Koutaïssi, Hereke, Irmak) ; aucun QID ni ID commun avec les 779 villes déjà intégrées, aucune ville à moins de 10 km d'une ville existante.",
      "Capitales : Ankara « nationale » ; Tbilissi, Erevan, Bakou « régionales » (capitales de RSS) ; RSSA, oblasts et chefs-lieux de province sans type d'affichage (Q15-02).",
      "İstanbul et Ereğli : le « nom de 1945 » proposé n'était pas un autre nom (I pointé turc ; précisant de lieu de la fiche) : gardé en alias. Autres écarts de transcription conservés (Q16-03).",
      "Sources : doublons exacts retirés dans les fiches (même source et même usage cités deux fois, ex. Goudermes) ; référence Wikidata ajoutée.",
      "Preuves : mention « (non vérifiée par Claude) », « (lecture partielle) » ou « (page relue par Claude pour cette ville) » ; « À renforcer » = rôles sans aucune preuve confirmée.",
      "v0.2 (04/10/2026, réponses d'Ether cycle 2) : İzmir perd le rôle industrie (Halkapınar : liste de production 1944 et ouverture datée 1947 dans la même étude, contradiction relue par Claude sur les captures ; correction d'Ether, réserve R17-C2-01) ; 10 images de pages (Géorgie, Arménie, Stavropol) et 7 captures turques lues par Claude (registre v1.24) : rôles relus ville par ville, mentions de preuve et « À renforcer » recalculés.",
      "v0.3 (05/10/2026, réponses d'Ether cycle 3) : aucune correction de ville ; 3 pages du répertoire de 1940 (Alat, Nakhitchevan, Stepanakert, Choucha) et 3 captures (Ordu, Kropotkine, Kırklareli) lues par Claude (registre v1.26) ; Stepanakert et Choucha : gare à Yevlakh (96 et 112 km), pas de rail ajouté ; date du statut urbain de Kropotkine réservée (R17-C3-03)."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-7_caucase_turquie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ; même nom :', memes_noms, '->', out.relative_to(RACINE), '; à renforcer :', sum('À renforcer' in e['etats'][0]['proprietes']['note'] for e in entites),
      '; noms de 1945 :', sum(1 for e in entites if e['etats'][0]['proprietes'].get('nom')))
