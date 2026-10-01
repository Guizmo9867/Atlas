"""Ratissage villes 1.3 (Tchéquie, Slovaquie, Hongrie) -> data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json

Villes, rangs, rôles, preuves rôle par rôle et notes : proposition JSON d'Ether du 01/10/2026
(data/sources/deltas_ether/2026-10-01_villes_1-3_proposition_ether.json ; document : villes_1-3_..._brief_ether.md).
v0.1 avait été faite depuis le document seul (extrait gardé dans ..._extrait_du_brief.json) ; v0.2 lit le JSON.
Positions : Wikidata (CC0), outils/villes/wikidata_ratissage_1_3.json.
Relancer : python outils/villes/construire_villes_1_3.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_3.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

ROLES = {'port fluvial': 'port_fluvial'}
# Prague : siège du Protectorat -> régionale, par cohérence avec Vienne (arbitrage laissé ouvert par Ether ; validé par Guizmo le 01/10/2026)
CAPITALES = {'ville-cz-prague': 'regionale', 'ville-sk-bratislava': 'nationale', 'ville-hu-budapest': 'nationale'}
NOM_LOCAL = {'ville-cz-prague': 'Praha', 'ville-cz-plzen': 'Plzeň'}
NOMS = {'ville-cz-bohumin': 'Nový Bohumín', 'ville-sk-komarno-komarom': 'Komárom', 'ville-sk-sturovo': 'Párkány'}  # libellés d'Ether raccourcis pour la carte
# Autres noms (allemand, hongrois, slovaque, nom plus récent) : pour la recherche seulement, jamais un nom actif en 1945
ALIASES = {
    'ville-cz-prague': ['Praha', 'Prag'], 'ville-cz-brno': ['Brünn'], 'ville-cz-plzen': ['Plzeň'], 'ville-cz-ostrava': ['Ostrava', 'Mährisch Ostrau'],
    'ville-cz-usti-nad-labem': ['Aussig'], 'ville-cz-pardubice': ['Pardubitz'], 'ville-cz-olomouc': ['Olmütz'], 'ville-cz-prerov': ['Prerau'],
    'ville-cz-breclav': ['Lundenburg'], 'ville-cz-decin': ['Děčín', 'Podmokly', 'Bodenbach-Tetschen', 'Tetschen'], 'ville-cz-cheb': ['Eger'],
    'ville-cz-liberec': ['Reichenberg'], 'ville-cz-zlin': ['Gottwaldov'], 'ville-cz-mlada-boleslav': ['Jungbunzlau'],
    'ville-cz-ceske-budejovice': ['Budweis'], 'ville-cz-ceska-trebova': ['Böhmisch Trübau'], 'ville-cz-most': ['Brüx'],
    'ville-cz-bohumin': ['Bohumín', 'Neu Oderberg'],
    'ville-sk-bratislava': ['Pressburg', 'Pozsony'], 'ville-sk-kosice': ['Kassa', 'Kaschau'], 'ville-sk-zilina': ['Zsolna', 'Sillein'],
    'ville-sk-zvolen': ['Zólyom', 'Altsohl'], 'ville-sk-banska-bystrica': ['Besztercebánya', 'Neusohl'], 'ville-sk-presov': ['Eperjes'],
    'ville-sk-trnava': ['Nagyszombat', 'Tyrnau'], 'ville-sk-nove-zamky': ['Érsekújvár'], 'ville-sk-komarno-komarom': ['Komárno'],
    'ville-sk-sturovo': ['Parkan', 'Štúrovo'], 'ville-sk-trencin': ['Trencsén', 'Trentschin'],
    'ville-hu-gyor': ['Raab'], 'ville-hu-pecs': ['Fünfkirchen'], 'ville-hu-szekesfehervar': ['Stuhlweißenburg'], 'ville-hu-sopron': ['Ödenburg'],
    'ville-hu-ujdombovar': ['Dombóvár'], 'ville-hu-vac': ['Waitzen'], 'ville-hu-szombathely': ['Steinamanger'],
}
# Compléments de Claude à la note d'Ether (positions, arbitrage de Prague)
NOTES = {
    'ville-cz-prague': "Capitale « régionale » au Snapshot 0 (siège du Protectorat de Bohême-Moravie), par cohérence avec Vienne : validé par Guizmo le 01/10/2026.",
    'ville-cz-most': "Position provisoire : Wikidata donne la ville reconstruite ; à déplacer sur le vieux Most.",
    'ville-cz-bohumin': "Position : gare de Bohumín (Nový Bohumín).",
    'ville-sk-komarno-komarom': "Position : rive nord (Komárno) ; l'entité couvre les deux rives.",
    'ville-hu-miskolc': "Date de la fusion avec Diósgyőr (01/01/1945) non confirmée par la relecture de Claude.",
}
A_RENFORCER = {'ville-hu-csepel': ['industrie']}  # seule source C (Ether)

entites = []
for v in PROPOSITION['villes']:
    eid = v['entite_id']
    e0, audit = v['etat_snapshot0'], v['audit']
    q = QID[eid]
    nom = NOMS.get(eid, v['nom'])
    roles = list(dict.fromkeys(ROLES.get(r, r) for r in e0['roles']))
    prop = {}
    if v.get('nom_local') and v['nom_local'] != nom: prop['nom_local'] = v['nom_local']
    elif eid in NOM_LOCAL: prop['nom_local'] = NOM_LOCAL[eid]
    prop['importance_atlas'] = e0['importance_atlas']
    if eid in CAPITALES: prop['capitale'] = CAPITALES[eid]
    prop['roles'] = roles
    statut = lambda s: REGISTRE[s]['verification_claude']
    preuves = {ROLES.get(r, r): p['sources'] for r, p in audit.get('preuves_roles', {}).items()}
    # à renforcer : réserve d'Ether, ou rôle dont aucune preuve n'a été confirmée par la relecture de Claude
    a_renforcer = list(A_RENFORCER.get(eid, []))
    a_renforcer += [r for r in roles if r not in a_renforcer and not any(statut(s) == 'ok' for s in preuves.get(r, []))]
    note = f"Rôle dans l'Atlas (Ether, ratissage villes 1.3) : {audit.get('justification_importance', '')} {e0['note']}".strip()
    note = note.replace(' Le statut de capitale dans l’Atlas reste à arbitrer ; aucun statut national ou régional n’est imposé dans l’état proposé.', '')  # tranché depuis
    if eid in NOTES: note += ' ' + NOTES[eid]
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    prop['note'] = note
    aliases = [a for a in dict.fromkeys([*v.get('aliases', []), *ALIASES.get(eid, []), q.get('label_en')]) if a and a != nom]
    roles_de = {}
    for r, ss in preuves.items():
        for s_ in ss: roles_de.setdefault(s_, []).append(r)
    def usage(s_):
        u = ('preuve locale : ' + ', '.join(roles_de[s_])) if s_ in roles_de else 'contexte (situation, nom ou périmètre)'
        st = statut(s_)
        return u + ('' if st == 'ok' else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)')
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)'}]
    sources += [{'source_id': s_, 'locator': REGISTRE[s_].get('locator', ''), 'usage': usage(s_)} for s_ in e0['sources']]
    entites.append({
        'entite_id': eid, 'type_entite': 'ville', 'nom': nom, 'nom_court': nom, **({'aliases': aliases} if aliases else {}),
        'etats': [{
            'etat_id': 'etat-01',
            'valid_from': {'date': '', 'precision': 'inconnue'},
            'valid_to': {'date': '', 'precision': 'inconnue'},
            'statut': 'ville_au_snapshot0',
            'proprietes': prop,
            'geometrie': {'type': 'Point', 'coordinates': [q['lon'], q['lat']]},
            'sources': sources,
        }],
        'relations': [],
    })

lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-3_tchequie_slovaquie_hongrie', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.2', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': ['Tchéquie actuelle', 'Slovaquie actuelle', 'Hongrie actuelle'],
    'differes_par_ether': ['Dunapentele (argument industriel de 1950 exclu)', 'Esztergom (pont à traiter à part)', 'Tatabánya', 'Kazincbarcika', 'Otrokovice / Baťov', 'Karlovy Vary'],
    'integration': {'date': '2026-10-01', 'par': 'Claude', 'corrections': [
      "Données tirées du document d'Ether (le JSON n'avait pas été transmis) : rangs, rôles, sources et corrections de la section 2.",
      "Noms au Snapshot 0 : Moravská Ostrava, Děčín–Podmokly, Nový Bohumín, Komárom (les deux rives), Párkány ; noms allemands, hongrois et plus récents en alias (recherche seulement).",
      "Capitales : Bratislava et Budapest nationales ; Prague régionale par cohérence avec Vienne (à confirmer).",
      "Miskolc et Diósgyőr : deux points (fusion du 01/01/1945 à appliquer au ratissage du temps).",
      "Positions : Wikidata ; Nový Bohumín = gare ; Most à déplacer sur le vieux Most ; Komárom = rive nord (Komárno).",
      "« À renforcer » : Csepel (source C) et les villes dont aucune source n'a été confirmée par la relecture de Claude.",
      "v0.2 (01/10) : JSON d'Ether reçu et rapproché (aucune différence de villes, rangs, rôles ou sources) ; notes d'Ether et preuves rôle par rôle reprises ; « à renforcer » calculé rôle par rôle ; Prague régionale validée par Guizmo.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
