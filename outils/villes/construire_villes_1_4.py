"""Ratissage villes 1.4 (Pologne, Estonie, Lettonie, Lituanie) -> data/snapshot0/villes_1-4_pologne_baltique.json

Villes, rangs, rôles, preuves rôle par rôle et notes : proposition JSON d'Ether du 01/10/2026
(data/sources/deltas_ether/2026-10-01_villes_1-4_proposition_ether.json ; document : villes_1-4_pologne_baltique_brief_ether.md).
Positions : Wikidata (CC0), outils/villes/wikidata_ratissage_1_4.json.
v0.2 : réponse d'Ether du 01/10/2026 (data/sources/deltas_ether/2026-10-01_villes_1-4_reponses_corrections.json) :
noms à la date portés dans l'état (fiche = nom actuel), Varsovie, renforts ferroviaires locaux, Koźle sur les bassins du port.
Relancer : python outils/villes/construire_villes_1_4.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-4_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_4.json', encoding='utf-8'))
CORRECTIONS = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-4_reponses_corrections.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

# Convention des capitales (Vienne, Prague) : capitale régionale = siège administratif de fait sous occupation ou RSS ;
# Varsovie nationale par continuité (aucun siège de gouvernement sur place) — proposition d'Ether, appliquée.
CAPITALES = {'ville-pl-warszawa': 'nationale', 'ville-pl-krakow': 'regionale', 'ville-ee-tallinn': 'regionale',
             'ville-lv-riga': 'regionale', 'ville-lt-vilnius': 'regionale'}
# Nom à la date : porté dans l'état (lu en premier par la carte) ; la fiche garde le nom actuel, l'ID ne change pas.
# 1) noms de 1945 déjà donnés par Ether dans sa proposition (Litzmannstadt, Breslau…) ; 2) réponse d'Ether (Posen, Kattowitz…), sur preuve individuelle.
NOM_A_LA_DATE = {c['entity_id']: c['nom_affiche_snapshot0'] for c in CORRECTIONS['nomenclature'] if c['operation'].startswith('fusionner')}
NOM_A_LA_DATE['ville-pl-kozle'] = 'Cosel'  # « Cosel — port » d'Ether, raccourci pour la carte
SOURCES_NOM = {c['entity_id']: c['sources'] for c in CORRECTIONS['nomenclature']}
ALIASES_NOM = {c['entity_id']: c['alias_a_conserver'] for c in CORRECTIONS['nomenclature']}
RENFORTS = {c['entity_id']: c['source'] for c in CORRECTIONS['renforts_locaux']}  # preuves locales de rail
SOURCES_CAPITALE = {CORRECTIONS['capitales']['entity_id']: CORRECTIONS['capitales']['sources']}
# Autres noms (allemand, polonais, russe…) : pour la recherche seulement, jamais un nom actif en 1945
ALIASES = {
    'ville-pl-warszawa': ['Warschau'], 'ville-pl-poznan': ['Posen'], 'ville-pl-wroclaw': ['Wrocław'], 'ville-pl-szczecin': ['Szczecin'],
    'ville-pl-gdynia': ['Gdynia'], 'ville-pl-swinoujscie': ['Swinemünde'], 'ville-pl-bydgoszcz': ['Bromberg'], 'ville-pl-torun': ['Thorn'],
    'ville-pl-tczew': ['Dirschau'], 'ville-pl-katowice': ['Kattowitz'], 'ville-pl-gliwice': ['Gliwice'], 'ville-pl-zabrze': ['Hindenburg'],
    'ville-pl-chorzow': ['Königshütte'], 'ville-pl-tarnowskie-gory': ['Tarnowitz'], 'ville-pl-walbrzych': ['Waldenburg'],
    'ville-pl-elblag': ['Elbing'], 'ville-pl-kedzierzyn': ['Heydebreck', 'Kędzierzyn-Koźle'], 'ville-pl-kozle': ['Cosel', 'Kędzierzyn-Koźle'],
    'ville-ee-tallinn': ['Reval'], 'ville-ee-tartu': ['Dorpat'], 'ville-lv-riga': ['Rīga'], 'ville-lv-liepaja': ['Libau'],
    'ville-lv-ventspils': ['Windau'], 'ville-lv-daugavpils': ['Dünaburg', 'Dvinsk'], 'ville-lv-jelgava': ['Mitau'],
    'ville-lt-vilnius': ['Wilno', 'Wilna'], 'ville-lt-kaunas': ['Kowno', 'Kauen'], 'ville-lt-siauliai': ['Schaulen'], 'ville-lt-klaipeda': ['Klaipėda'],
}
ROLES = {'port fluvial': 'port_fluvial'}
NOTES = {
    'ville-pl-warszawa': "Capitale nationale par continuité de l’État polonais (confirmé par Ether) : cela ne veut pas dire qu’un gouvernement siège à Varsovie au Snapshot 0. Gouvernement en exil à Londres ; PKWN siégeant à Lublin depuis le 27/07/1944, devenu gouvernement provisoire le 31/12/1944.",
    'ville-pl-gdansk': "Chantier Schichau : terrain acheté en 1889 près d'une voie existante, chantier construit 1890–1892, ouverture officielle en janvier 1892 (1889 n'est pas une date de raccordement).",
    'ville-ee-tapa': "Embranchement de Tartu : 1876 selon le musée de Tapa, 1877 (trafic régulier) selon les chemins de fer estoniens ; les deux dates sont gardées.",
    'ville-ee-kohtla-jarve': "Point sur le noyau historique de Järve ; statut de ville en 1946.",
    'ville-pl-kozle': "Position : gare du port (Wikidata Q16570466), au bord des bassins portuaires historiques (consigne d'Ether), pas le centre de Koźle.",
    'ville-pl-krakow': "Capitale « régionale » au Snapshot 0 : siège du Gouvernement général allemand (même convention que Vienne et Prague).",
    'ville-ee-tallinn': "Capitale « régionale » au Snapshot 0 : RSS d'Estonie (même convention que Vienne et Prague).",
    'ville-lv-riga': "Capitale « régionale » au Snapshot 0 : RSS de Lettonie (même convention que Vienne et Prague).",
    'ville-lt-vilnius': "Capitale « régionale » au Snapshot 0 : RSS de Lituanie (même convention que Vienne et Prague).",
    'ville-pl-kedzierzyn': "Position : quartier de Kędzierzyn (Wikidata), distinct de Koźle.",
    'ville-lv-krustpils': "Position : quartier de Krustpils (Wikidata), distinct de Jēkabpils.",
}

entites = []
for v in PROPOSITION['villes']:
    eid = v['entite_id']
    e0, audit = v['etat_snapshot0'], v['audit']
    q = QID[eid]
    nom = q['label_en'] if eid in NOM_A_LA_DATE or v['nom'] in ('Litzmannstadt', 'Breslau', 'Stettin', 'Dantzig', 'Gotenhafen', 'Gleiwitz', 'Memel') else v['nom']
    nom_date = NOM_A_LA_DATE.get(eid, v['nom'] if nom != v['nom'] else None)
    roles = list(dict.fromkeys(ROLES.get(r, r) for r in e0['roles']))
    prop = {}
    if nom_date: prop['nom'] = nom_date
    if v.get('nom_local') and v['nom_local'] not in (nom, nom_date): prop['nom_local'] = v['nom_local']
    prop['importance_atlas'] = e0['importance_atlas']
    if eid in CAPITALES: prop['capitale'] = CAPITALES[eid]
    prop['roles'] = roles
    statut = lambda s: REGISTRE[s]['verification_claude']
    preuves = {ROLES.get(r, r): list(p['sources']) for r, p in audit.get('preuves_roles', {}).items()}
    if eid in RENFORTS: preuves.setdefault('rail', []).append(RENFORTS[eid])
    # à renforcer : réserve d'Ether, ou rôle dont aucune preuve n'a été confirmée par la relecture de Claude
    a_renforcer = list(roles) if e0.get('source_role_a_renforcer') else []
    a_renforcer += [r for r in roles if r not in a_renforcer and not any(statut(s) == 'ok' for s in preuves.get(r, []))]
    note = f"Rôle dans l'Atlas (Ether, ratissage villes 1.4) : {audit.get('justification_importance', '')} {e0['note']}".strip()
    for vieux in (' La forme officielle Swinemünde doit être normalisée avec une preuve nomenclaturale dédiée.',
                  ' Libellé actuel de repérage ; forme historique Hindenburg O.S. à étayer dans le registre des noms avant import.'):
        note = note.replace(vieux, '')  # réglé par la réponse d'Ether (nom à la date sourcé)
    note = note.replace(' La convention capitale régionale/nationale doit être arbitrée séparément de la souveraineté territoriale.', '')  # tranché depuis
    if nom_date: note += f" Nom à la date : {nom_date} (aujourd'hui {nom})."
    if eid in NOTES: note += ' ' + NOTES[eid]
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    prop['note'] = note
    aliases = [a for a in dict.fromkeys([*v.get('aliases', []), *ALIASES_NOM.get(eid, []), *ALIASES.get(eid, []), q.get('label_en')]) if a and a not in (nom, nom_date)]
    roles_de = {}
    for r, ss in preuves.items():
        for s_ in ss: roles_de.setdefault(s_, []).append(r)
    def usage(s_):
        u = ('preuve locale : ' + ', '.join(roles_de[s_])) if s_ in roles_de else ('nom à la date' if nom_date else 'nom allemand attesté localement (ville non renommée : nom officiel non prouvé)') if s_ in SOURCES_NOM.get(eid, []) else 'contexte : gouvernements' if s_ in SOURCES_CAPITALE.get(eid, []) else 'contexte (situation, nom ou périmètre)'
        st = statut(s_)
        return u + ('' if st == 'ok' else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)')
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)'}]
    sources += [{'source_id': s_, 'locator': REGISTRE[s_].get('locator', ''), 'usage': usage(s_)} for s_ in dict.fromkeys([*e0['sources'], *SOURCES_NOM.get(eid, []), *SOURCES_CAPITALE.get(eid, []), *([RENFORTS[eid]] if eid in RENFORTS else [])])]
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
    'nom': 'snapshot0_villes_1-4_pologne_baltique', 'date_reference': '1945-01-01', 'heure_reference': '00:00',
    'version': '0.2', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
    'zone': ['Pologne actuelle', 'Estonie', 'Lettonie', 'Lituanie'],
    'hors_perimetre': PROPOSITION['metadata_lot'].get('hors_perimetre', []),
    'differes_par_ether': [c.get('nom') for c in PROPOSITION['candidats_differes']],
    'integration': {'date': '2026-10-01', 'par': 'Claude', 'corrections': [
      "Données : JSON d'Ether (rangs, rôles, preuves rôle par rôle, notes) ; noms au Snapshot 0 tels que proposés (Litzmannstadt, Breslau, Stettin, Dantzig, Gotenhafen, Gleiwitz, Memel…), autres formes en alias.",
      "Capitales : convention de Vienne et Prague — Cracovie (Gouvernement général), Tallinn, Riga, Vilnius (RSS) régionales ; Varsovie nationale par continuité ; Kaunas et Lublin sans capitale (Lublin : administration).",
      "Positions : Wikidata ; Kędzierzyn et Koźle distincts ; Krustpils distinct de Jēkabpils.",
      "« À renforcer » : réserves d'Ether et rôles dont aucune preuve n'a été confirmée par la relecture de Claude.",
      "v0.2 (01/10) : réponse d'Ether — nom de 1945 porté dans l'état et nom actuel sur la fiche, pour toutes les villes renommées (Litzmannstadt, Breslau, Stettin, Dantzig, Gotenhafen, Gleiwitz, Memel, puis Posen, Bromberg, Thorn, Kattowitz, Hindenburg, Königshütte, Swinemünde, Tarnowitz, Heydebreck, Cosel, Elbing) ; Tczew et Wałbrzych gardés (nom urbain non prouvé) ; note de Varsovie ; preuves locales de rail pour Tapa, Valga, Krustpils, Radviliškis ; Koźle placé sur les bassins du port.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-4_pologne_baltique.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
