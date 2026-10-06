"""Audit transversal villes 1.x d'Ether (05/10/2026) : 15 villes ajoutées pour compléter la couverture du lot 1.0
(France et Grande-Bretagne : nœuds ferroviaires, frontières, ports corses)
-> data/snapshot0/villes_1-x_audit_complements.json

Données : data/sources/deltas_ether/2026-10-05_audit_1x_complements_villes_ether.json (bilan : villes_1x_audit_bilan_ether.md).
Positions : QID Wikidata (CC0) proposés par Ether, recoupés par Claude par SPARQL (outils/villes/wikidata_ratissage_audit_1x.json).
Preuves : registre v1.30 (relecture data/sources/verifications_claude/2026-10-05_villes_audit_1x.json).
Relancer : python outils/villes/construire_villes_audit_1x.py (depuis outils/villes), après fusion_sources_audit_1x.py.
"""
import json, pathlib, copy, re
from confirmations_claude import confirmation

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROP = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-05_audit_1x_complements_villes_ether.json', encoding='utf-8'))['proposition_ether']
WD = json.load(open(ICI / 'wikidata_ratissage_audit_1x.json', encoding='utf-8'))['villes']
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
NON_PREUVE = ('src-wikidata',)

def roles_de(usage):
    tete = re.split(r' — ', usage)[0]
    return {t.strip() for t in re.split(r'[,;]', tete)}

entites = []
for v in PROP['entites']:
    e = copy.deepcopy(v); eid = e['entite_id']; et = e['etats'][0]; p = et['proprietes']
    assert not p.get('capitale'), eid
    w = WD[eid]
    et['geometrie'] = {'type': 'Point', 'coordinates': [round(w['coord_wikidata'][0], 6), round(w['coord_wikidata'][1], 6)]}
    prouve = set()
    for s in et['sources']:
        if s['source_id'] in NON_PREUVE:
            s['locator'] = w['qid']
            s['usage'] = 'position actuelle (repère), recoupée par Claude ; aucune preuve de rôle historique'
            continue
        fiche = REGISTRE[s['source_id']]; st = fiche['verification_claude']
        roles_usage = roles_de(s['usage']) & set(p['roles'])
        if not roles_usage:  # usage sans rôle en tête (« Gare de Limoges ») : rôles de la ville attendus de la source
            roles_usage = set(p['roles']) & set(fiche.get('usages_atlas', []))
            s['usage'] = ', '.join(r for r in p['roles'] if r in roles_usage) + ' ; ' + s['usage']
        cr, cm = confirmation(fiche, eid) if st != 'ok' else (None, None)
        if st == 'ok' or cr == 'usage': prouve |= roles_usage
        elif cr: prouve |= cr & roles_usage
        s['usage'] += '' if st == 'ok' else cm if cm else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)'
    a_renforcer = [r for r in p['roles'] if r not in prouve]
    if a_renforcer: p['note'] += f" À renforcer : {', '.join(a_renforcer)}."
    entites.append(e)

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-x_audit_complements', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.1', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': "Compléments de couverture du lot 1.0 (France, Grande-Bretagne) proposés par l'audit transversal 1.x d'Ether",
    'limites_ether': PROP['metadata_lot']['integration'],
    'reserves_ether': "Index des réserves de l'audit (data/snapshot0/villes_1x_audit_index_reserves_ether.md), revue finale 1.x",
    'integration': {'date': '2026-10-05', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (15 villes : FR 12, GB 3), IDs au code du pays actuel ; aucun nom de 1945 différent, aucune capitale ; gares et ports non séparés des villes. Lens différée par Ether (non importée).",
      "Positions : QID Wikidata (CC0) d'Ether recoupés par SPARQL : libellé et pays cohérents, écart < 100 m ; aucun QID ni ID déjà dans le corpus ; Hendaye/Irun, Cerbère/Portbou et Tours/Saint-Pierre-des-Corps sont des paires de villes voisines distinctes.",
      "Preuves : 18 sources de l'audit relues par sous-agents (WebFetch seul) : 7 confirmées, 8 en lecture partielle, 2 illisibles pour l'outil (Jeumont, Dijon), 1 faible (Ruppenthal I-3) ; mentions « (non vérifiée par Claude) », « (lecture partielle) » ou « (page relue par Claude pour cette ville) » ; « À renforcer » = rôles sans aucune preuve confirmée."]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-x_audit_complements.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE), '; à renforcer :', [(e['entite_id'], e['etats'][0]['proprietes']['note'].split('À renforcer : ')[-1]) for e in entites if 'À renforcer' in e['etats'][0]['proprietes']['note']])
