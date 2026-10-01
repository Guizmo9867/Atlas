"""Ratissage villes 1.2 (Allemagne + arc alpin) -> data/snapshot0/villes_1-2_allemagne_alpes.json

Liste, rôles, priorités et sources : proposition d'Ether (01/10/2026,
data/sources/deltas_ether/2026-10-01_villes_1-2_allemagne_alpes_proposition_ether.json), intégrée par Claude.
Positions : Wikidata (CC0), QID retenu dans outils/villes/wikidata_ratissage_1_2.json (tiré par SPARQL,
vérifié contre Natural Earth le 01/10/2026).
Retour d'audit d'Ether (01/10/2026) appliqué : voir IMPORTANCE, GENERALES, RETIREES, AJOUTS, SITUATION.
Relancer : python outils/villes/construire_villes_1_2.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_allemagne_alpes_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_2.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# --- Retour d'audit d'Ether (01/10/2026, data/snapshot0/villes_1-2_allemagne_alpes_audit_ether.md) ---
# Type de capitale et importance Atlas sont indépendants : Vaduz = capitale nationale mais C.
IMPORTANCE = {'ville-li-vaduz': 'C'}
# Sources générales : contexte seulement, jamais seule preuve d'un rôle local
GENERALES = {'src-db-museum-history', 'src-sbb-history'}
# Sources retirées d'une ville (page hors sujet)
RETIREES = {'ville-at-graz': {'src-graz-rail-industry'}}
# Sources ajoutées par Claude
AJOUTS = {
    'ville-li-vaduz': [{'source_id': 'src-vaduz-portrait', 'locator': 'Portrait > Vaduz', 'usage': 'statut : capitale, siège des autorités et du Parlement (capitale depuis 1719 selon la commune)'}],
    'ville-de-aachen': [{'source_id': 'src-mwi-aachen-1944', 'locator': 'Urban Warfare Project Case Study #10', 'usage': 'situation au 01/01/1945 : évacuation ordonnée, plus de 80 % des bâtiments détruits, ville prise le 21/10/1944'}],
}
SITUATION = {'ville-de-aachen': 'evacuee et detruite'}
NOTES_EN_PLUS = {
    'ville-de-aachen': " Situation au 01/01/1945 (source MWI) : évacuation des civils ordonnée par les autorités allemandes à l'automne 1944, il ne restait qu'environ 5 000 à 20 000 des 165 000 habitants au début des combats ; plus de 80 % des bâtiments détruits ; ville prise par les Américains le 21/10/1944. Cela ne prouve pas l'arrêt total du réseau ferroviaire.",
    'ville-at-wien': " Capitale régionale (Reichsgau Wien) au 01/01/1945. Retour au statut de capitale nationale : futur état daté, repère du 27/04/1945 à instruire avec une source dédiée (rétablissement politique, statut de capitale et contrôle effectif à distinguer).",
    'ville-de-magdeburg': " Destruction du port le 16/01/1945 : à traiter au ratissage de janvier (préciser l'objet touché : port, équipements ou ville).",
}

def usage_source(sid):
    if sid in GENERALES: return 'contexte national seulement (ne prouve pas le rôle local)'
    v = REGISTRE[sid]['verification_claude']
    if v == 'ok': return 'rôle de la ville au 01/01/1945'
    if v == 'non_verifiee': return 'rôle de la ville au 01/01/1945 (non vérifiée lors de l\'audit)'
    return 'contexte (ne prouve pas seule le rôle au 01/01/1945)'

def bien_sourcee(sources):
    return any(s['source_id'] not in GENERALES and REGISTRE[s['source_id']]['verification_claude'] == 'ok' for s in sources)

# Vocabulaire des rôles : mots-clés d'Ether -> rôles de l'Atlas (LEXIQUE_ID.md).
# None = information géographique, pas un rôle (elle reste dans la note).
ROLES = {
    'frontiere': 'frontalier',
    'danube': 'port_fluvial', 'elbe': 'port_fluvial', 'rhin': 'port_fluvial', 'confluence': 'port_fluvial',
    'port_lacustre': 'port_fluvial', 'industrie_navale': 'construction_navale',
    'automobile': 'industrie', 'mecanique': 'industrie', 'chimie': 'industrie',
    'fret': 'rail', 'noeud_interieur': 'rail', 'brenner': 'rail',
    'corridor_alpin': 'rail', 'corridor_simplon': 'rail', 'corridor_suisse': 'rail', 'corridor_italie': 'rail',
    'corridor_gothard': 'rail', 'corridor_autriche': 'rail', 'corridor_france': 'rail', 'corridor_autriche_suisse': 'rail',
    'commerce': None, 'lac': None, 'front': None,
}
# Exceptions ville par ville
ROLES_VILLE = {'ville-ch-schaffhausen': {'rhin': None}}  # chutes du Rhin : pas de navigation, la ville est un nœud ferroviaire/frontalier
CAPITALES = {'ville-de-berlin': 'nationale', 'ville-ch-bern': 'nationale', 'ville-li-vaduz': 'nationale',
             # Vienne au 01/01/1945 : l'Autriche est annexée (Reichsgau Wien) -> capitale régionale ; le détail juridique va dans la fiche
             'ville-at-wien': 'regionale'}
NOM_LOCAL = {
    'ville-de-hamburg': 'Hamburg', 'ville-de-bremen': 'Bremen', 'ville-de-hannover': 'Hannover', 'ville-de-duisburg': 'Duisburg',
    'ville-de-koeln': 'Köln', 'ville-de-frankfurt': 'Frankfurt am Main', 'ville-de-nuernberg': 'Nürnberg', 'ville-de-muenchen': 'München',
    'ville-de-dresden': 'Dresden', 'ville-de-magdeburg': 'Magdeburg', 'ville-de-saarbruecken': 'Saarbrücken', 'ville-de-kassel': 'Kassel',
    'ville-de-aachen': 'Aachen', 'ville-de-koblenz': 'Koblenz', 'ville-de-regensburg': 'Regensburg', 'ville-de-flensburg': 'Flensburg',
    'ville-at-wien': 'Wien', 'ville-at-salzburg': 'Salzburg', 'ville-ch-bern': 'Bern', 'ville-ch-zuerich': 'Zürich', 'ville-ch-basel': 'Basel',
    'ville-ch-luzern': 'Luzern', 'ville-ch-winterthur': 'Winterthur', 'ville-ch-st-gallen': 'St. Gallen', 'ville-ch-schaffhausen': 'Schaffhausen',
    'ville-ch-bellinzona': 'Bellinzona', 'ville-ch-brig': 'Brig',
}

def roles_atlas(eid, liste):
    table = {**ROLES, **ROLES_VILLE.get(eid, {})}
    out = []
    for r in liste:
        x = table.get(r, r)
        if x and x not in out: out.append(x)
    return out

# --- Second audit d'Ether (01/10/2026, data/snapshot0/villes_1-2_allemagne_alpes_audit2_ether.md) ---
# Patch : 9 villes ajoutées, preuves rôle par rôle pour les 64 autres, corrections de noms et de rôles.
PATCH = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_audit_patch.json', encoding='utf-8'))
CORR = {c['entite_id']: c for c in PATCH['corrections_villes']}
AJOUTEES = {a['entite_id']: a for a in PATCH['ajouts_villes']}
NOM_LOCAL.update({'ville-de-mainz': 'Mainz', 'ville-de-augsburg': 'Augsburg'})
VERS_ATLAS = {'frontiere': 'frontalier'}
# Romanshorn : bac vers Lindau arrêté en 1939, Friedrichshafen non daté en guerre -> le rôle ferry reste à renforcer
A_RENFORCER_EN_PLUS = {'ville-ch-romanshorn': ['ferry'], 'ville-ch-basel': ['industrie', 'port_fluvial']}  # Bâle : article DHS non confirmé par Claude
REMPLACEES = {x['source_id']: x['sources_remplacement'] for x in json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-2_audit_delta.json', encoding='utf-8'))['suivi_8_liens_signales_par_claude'] if x['sources_remplacement']}

def statut(sid): return REGISTRE[sid]['verification_claude']

def usage_preuve(sid, roles):
    u = 'preuve locale : ' + ', '.join(roles)
    st = statut(sid)
    return u if st == 'ok' else u + (' (non vérifiée par Claude)' if st == 'non_verifiee' else ' (lecture partielle)')

def usage_ancienne(sid):
    if sid in REMPLACEES: return f"remplacée par {', '.join(REMPLACEES[sid])} (ancienne page non relue)"
    return usage_source(sid)

entites = []
for v in [*PROPOSITION['villes'], *PATCH['ajouts_villes']]:
    eid, e0 = v['entite_id'], v['etat_snapshot0']
    nouvelle = eid in AJOUTEES
    c = CORR.get(eid, {})
    modif = c.get('modifications_proposees', {})
    q = QID[eid]
    nom = modif.get('nom_snapshot0', v['nom'])
    prop = {}
    if eid in NOM_LOCAL: prop['nom_local'] = NOM_LOCAL[eid]
    prop['importance_atlas'] = IMPORTANCE.get(eid, e0['importance_atlas'])
    if eid in CAPITALES: prop['capitale'] = CAPITALES[eid]
    roles = roles_atlas(eid, e0['roles'])
    # preuves rôle par rôle (patch d'audit) ; une ville ajoutée prouve ses rôles par ses sources
    preuves = [{'role': VERS_ATLAS.get(x['role'], x['role']), 'sources': x['sources']} for x in c.get('preuves_par_role', [])]
    if nouvelle: preuves = [{'role': r, 'sources': e0['sources']} for r in roles]
    if eid == 'ville-li-vaduz':  # source de la commune lue par Claude : « seat of the authorities and parliament »
        preuves += [{'role': r, 'sources': ['src-vaduz-portrait']} for r in ('capitale', 'administration')]
    for r in [*modif.get('roles_ajouter', []), *[x['role'] for x in preuves]]:
        if r not in roles: roles.append(r)
    roles = [r for r in roles if r not in modif.get('roles_retirer', [])]
    prop['roles'] = roles
    if eid in SITUATION: prop['situation'] = SITUATION[eid]
    # sources : anciennes (usage selon leur portée), puis preuves de l'audit
    roles_par_source = {}
    for x in preuves:
        for sid in x['sources']: roles_par_source.setdefault(sid, []).append(x['role'])
    retirees = RETIREES.get(eid, set()) | set(c.get('sources_retirer_des_preuves', []))
    anciennes = [] if nouvelle else [sid for sid in e0['sources'] if sid not in retirees]
    sources_role = [{'source_id': sid, 'locator': '', 'usage': usage_preuve(sid, roles_par_source[sid]) if sid in roles_par_source else usage_ancienne(sid)} for sid in anciennes]
    for sid in [*c.get('sources_ajouter', []), *(e0['sources'] if nouvelle else [])]:
        if sid not in anciennes and sid not in [x['source_id'] for x in sources_role]:
            sources_role.append({'source_id': sid, 'locator': REGISTRE[sid].get('locator', ''), 'usage': usage_preuve(sid, roles_par_source.get(sid, ['contexte']))})
    # ce qui reste à renforcer : réserves d'Ether + rôles dont aucune preuve n'a été confirmée par Claude
    a_renforcer = [VERS_ATLAS.get(r, r) for r in c.get('roles_a_renforcer', [])]
    a_renforcer += [x['role'] for x in preuves if not any(statut(sid) == 'ok' for sid in x['sources'])]
    a_renforcer += A_RENFORCER_EN_PLUS.get(eid, [])
    a_renforcer = [r for r in dict.fromkeys(a_renforcer) if r in roles]
    precisions = c.get('precisions_a_renforcer', []) + (v.get('complement_audit', {}).get('precisions_a_renforcer', []) if nouvelle else [])
    note = f"Rôle dans l'Atlas (Ether, ratissage villes 1.2) : {e0['note']}" + NOTES_EN_PLUS.get(eid, '')
    if c.get('note_historique_ajouter'): note += f" Audit du 01/10 : {c['note_historique_ajouter']}"
    if modif.get('roles_retirer'): note += f" Rôle retiré : {', '.join(modif['roles_retirer'])} ({modif.get('motif', '')})"
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    if precisions: note += ' Précisions à apporter : ' + ' ; '.join(p.rstrip('.') for p in precisions) + '.'
    prop['note'] = note.replace('..', '.')
    aliases = [a for a in dict.fromkeys([NOM_LOCAL.get(eid), *v.get('aliases', []), *modif.get('aliases_ajouter', []), q.get('label_en')]) if a and a != nom]
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)' + (' ; capitale du Liechtenstein' if eid == 'ville-li-vaduz' else '')}]
    sources += sources_role + AJOUTS.get(eid, [])
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

m = PROPOSITION['metadata_lot']
lot = {
  'metadata_lot': {
    'nom': 'snapshot0_villes_1-2_allemagne_alpes', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.3', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': m['perimetre'], 'note_perimetre': m['note_perimetre'],
    'exclusions_volontaires': PROPOSITION['exclusions_volontaires'],
    'audit_recommande': PROPOSITION['audit_recommande'],
    'integration': {'date': '2026-10-01', 'par': 'Claude', 'corrections': [
      "Format : champs d'Ether ramenés au modèle des lots 1.0/1.1 (etat-01 ; valid_from inconnu = ville déjà en place avant l'Atlas ; importance, rôles, note, nom local dans proprietes).",
      "Rôles : mots-clés d'Ether ramenés au vocabulaire de l'Atlas (voir ROLES dans le script) : fleuves (Danube, Elbe, Rhin) -> port_fluvial ; corridors, Brenner, nœud intérieur, fret -> rail ; automobile, mécanique, chimie -> industrie. Commerce, lac et front restent dans la note.",
      "Schaffhouse : le Rhin n'y est pas navigable (chutes) -> pas de rôle port_fluvial.",
      "Vienne : capitale « régionale » au 01/01/1945 (Autriche annexée) ; point soumis à Ether.",
      "Vaduz : aucune source fournie -> Wikidata (capitale du Liechtenstein) en attendant une source officielle.",
      "Villes marquées « à renforcer » par Ether : mention « Rôle à sourcer localement » dans la note.",
      "Positions : Wikidata (CC0), QID en locator ; vérifiées contre Natural Earth.",
      "v0.2 (01/10, retour d'audit d'Ether) : Vaduz A -> C (capitale nationale gardée : type de capitale et importance sont indépendants), source officielle de la commune ajoutée ; Vienne A et capitale régionale confirmées ; Aix-la-Chapelle « évacuée et détruite » (source MWI/West Point) ; Graz : page sur les pompiers retirée des preuves ; sources générales (DB Museum, CFF) et limitées = contexte seulement ; « Rôle à sourcer localement » sur chaque ville sans source lue qui prouve son rôle. Lot ouvert : 9 candidats à l'ajout et sources de remplacement attendus d'Ether.",
      "v0.3 (01/10, second audit d'Ether) : 9 villes ajoutées (Hamm, Ludwigshafen, Mayence, Schweinfurt, Augsbourg, Leuna, Watenstedt-Salzgitter, Leoben avec Donawitz, Osnabrück) ; Bremerhaven s'appelle Wesermünde au Snapshot 0 (même ID) ; Rostock : industrie au lieu d'aviation (Heinkel = fabrication) ; Bâle : + industrie ; Bregenz : + port (lac) ; preuves locales rôle par rôle (75 sources nouvelles, relues par Claude) ; la note dit précisément quels rôles restent à renforcer.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-2_allemagne_alpes.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
