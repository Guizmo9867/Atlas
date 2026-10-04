"""Ratissage villes 1.3 (Tchéquie, Slovaquie, Hongrie) -> data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json

Villes, rangs, rôles, preuves rôle par rôle et notes : proposition JSON d'Ether du 01/10/2026
(data/sources/deltas_ether/2026-10-01_villes_1-3_proposition_ether.json ; document : villes_1-3_..._brief_ether.md).
v0.1 avait été faite depuis le document seul (extrait gardé dans ..._extrait_du_brief.json) ; v0.2 lit le JSON.
Positions : Wikidata (CC0), outils/villes/wikidata_ratissage_1_3.json.
v0.3 : réponse d'Ether du 01/10/2026 (data/sources/deltas_ether/2026-10-01_villes_1-3_reponses_corrections.json) :
noms à la date Cassovie/Kassa et Aussig portés dans l'état ; fusion Miskolc–Diósgyőr datée (01/01/1945, après le Snapshot 0).
v0.4 : cycle 3 d'Ether du 01/10/2026 (data/sources/deltas_ether/2026-10-01_villes_1-3_cycle3_corrections.json) :
cinq noms à la date sur preuve individuelle (Reichenberg, Eger, Brüx, Tetschen-Bodenbach, Érsekújvár) ;
Protectorat, note Budapest et déplacement de Most laissés en réserve par Guizmo (aucune donnée modifiée pour ces points).
Relancer : python outils/villes/construire_villes_1_3.py (depuis la racine du dépôt).
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
ICI = pathlib.Path(__file__).parent
PROPOSITION = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_proposition_ether.json', encoding='utf-8'))
QID = json.load(open(ICI / 'wikidata_ratissage_1_3.json', encoding='utf-8'))
CORRECTIONS = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_reponses_corrections.json', encoding='utf-8'))
REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}

ROLES = {'port fluvial': 'port_fluvial'}
# Prague : siège du Protectorat -> régionale, par cohérence avec Vienne (arbitrage laissé ouvert par Ether ; validé par Guizmo le 01/10/2026)
CAPITALES = {'ville-cz-prague': 'regionale', 'ville-sk-bratislava': 'nationale', 'ville-hu-budapest': 'nationale'}
NOM_LOCAL = {'ville-cz-prague': 'Praha', 'ville-cz-plzen': 'Plzeň'}
# Nom à la date (réponse d'Ether) : porté dans l'état, lu en premier par la carte ; la fiche garde le repère actuel (même ID)
NOM_A_LA_DATE = {c['entite_id']: c for c in CORRECTIONS['corrections_nomenclature']}
# Sources de la réponse d'Ether ajoutées à l'état (nom à la date)
SOURCES_EN_PLUS = {c['entite_id']: c['sources'] for c in CORRECTIONS['corrections_nomenclature']}
SOURCES_EN_PLUS['ville-cz-decin'] = SOURCES_EN_PLUS.get('ville-cz-decin', []) + ['src-guizmo-sudetengebiete-tetschen']  # trouvée par Guizmo, 04/10/2026
# Cycle 3 (Q13-01) : nom à la date dans l'état seulement ; fiche, ID, nom_local, rôles et coordonnées inchangés
CYCLE3 = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-3_cycle3_corrections.json', encoding='utf-8'))
NOM_CYCLE3 = {c['entite_id']: c for c in CYCLE3['corrections'] if c['operation'] == 'nom_dans_etat_snapshot0'}
for eid_, c_ in NOM_CYCLE3.items(): SOURCES_EN_PLUS[eid_] = SOURCES_EN_PLUS.get(eid_, []) + c_['source_ids']
PREUVE_NOM = {
    'ville-cz-liberec': "avis local daté « Reichenberg, den 11. Mai 1944 » (Reichsanzeiger, OCR)",
    'ville-cz-cheb': "tribunal d'Eger, inscription du 13/05/1944 (Reichsanzeiger, OCR)",
    'ville-cz-most': "registre du tribunal de Brüx, avis du 12/05/1942 (Reichsanzeiger, OCR)",
    'ville-cz-decin': "titre d'un annuaire téléphonique de 1942 (notice d'archives), confirmé par la page sudetengebiete.de (fusion du 01/10/1942 sous ce nom ; Landkreis Tetschen-Bodenbach en 1945 ; captures de Guizmo) ; acte officiel : Verordnungsblatt 1942, n° 40, p. 353 (référence trouvée par Ether)",
    'ville-sk-nove-zamky': "journal local et avis municipal de juillet 1944",
}
NOMS = {'ville-cz-bohumin': 'Nový Bohumín', 'ville-sk-komarno-komarom': 'Komárom', 'ville-sk-sturovo': 'Párkány'}  # libellés d'Ether raccourcis pour la carte
# Autres noms (allemand, hongrois, slovaque, nom plus récent) : pour la recherche seulement, jamais un nom actif en 1945
ALIASES = {
    'ville-cz-prague': ['Praha', 'Prag'], 'ville-cz-brno': ['Brünn'], 'ville-cz-plzen': ['Plzeň'], 'ville-cz-ostrava': ['Ostrava', 'Mährisch Ostrau'],
    'ville-cz-usti-nad-labem': ['Aussig'], 'ville-cz-pardubice': ['Pardubitz'], 'ville-cz-olomouc': ['Olmütz'], 'ville-cz-prerov': ['Prerau'],
    'ville-cz-breclav': ['Lundenburg'], 'ville-cz-decin': ['Děčín', 'Podmokly', 'Bodenbach-Tetschen', 'Tetschen', 'Tetschen-Bodenbach'], 'ville-cz-cheb': ['Eger'],
    'ville-cz-liberec': ['Reichenberg'], 'ville-cz-zlin': ['Gottwaldov'], 'ville-cz-mlada-boleslav': ['Jungbunzlau'],
    'ville-cz-ceske-budejovice': ['Budweis'], 'ville-cz-ceska-trebova': ['Böhmisch Trübau'], 'ville-cz-most': ['Brüx'],
    'ville-cz-bohumin': ['Bohumín', 'Neu Oderberg'],
    'ville-sk-bratislava': ['Pressburg', 'Pozsony'], 'ville-sk-kosice': ['Kaschau'], 'ville-sk-zilina': ['Zsolna', 'Sillein'],
    'ville-sk-zvolen': ['Zólyom', 'Altsohl'], 'ville-sk-banska-bystrica': ['Besztercebánya', 'Neusohl'], 'ville-sk-presov': ['Eperjes'],
    'ville-sk-trnava': ['Nagyszombat', 'Tyrnau'], 'ville-sk-nove-zamky': ['Érsekújvár'], 'ville-sk-komarno-komarom': ['Komárno'],
    'ville-sk-sturovo': ['Parkan', 'Štúrovo'], 'ville-sk-trencin': ['Trencsén', 'Trentschin'],
    'ville-hu-gyor': ['Raab'], 'ville-hu-pecs': ['Fünfkirchen'], 'ville-hu-szekesfehervar': ['Stuhlweißenburg'], 'ville-hu-sopron': ['Ödenburg'],
    'ville-hu-ujdombovar': ['Dombóvár'], 'ville-hu-vac': ['Waitzen'], 'ville-hu-szombathely': ['Steinamanger'],
}
# Compléments de Claude à la note d'Ether (positions, arbitrage de Prague)
NOTES = {
    'ville-cz-prague': "Capitale « régionale » au Snapshot 0 (siège du Protectorat de Bohême-Moravie), par cohérence avec Vienne : validé par Guizmo le 01/10/2026.",
    'ville-cz-most': "Position provisoire : Wikidata donne la ville reconstruite ; à déplacer sur le vieux Most. Un relevé d'Ether sur le plan municipal de 1938 existe (registre des sources) mais le déplacement est laissé en réserve par Guizmo (01/10/2026) : point non déplacé.",
    'ville-cz-bohumin': "Position : gare de Bohumín (Nový Bohumín).",
    'ville-sk-komarno-komarom': "Position : rive nord (Komárno) ; l'entité couvre les deux rives.",
    'ville-hu-miskolc': "Date confirmée par Ether (S44, p. 102). Page 102 pas encore relue par Claude (document trop long pour l'outil) : dans « Sources à valider ».",
    'ville-hu-diosgyor': "Date confirmée par Ether (S44, p. 102) ; son rôle industriel restera décrit après la fusion.",
    'ville-sk-kosice': "Nom à la date : Cassovie (nom français traditionnel ; Kassa sur place, ville hongroise depuis novembre 1938). Date du retour au nom Košice en 1945 encore à prouver (pas automatiquement la prise du 19/01/1945). Source de « Cassovie » (Érudit) bloquée pour Claude : dans « Sources à valider ».",
    'ville-cz-usti-nad-labem': "Nom à la date : Aussig (forme allemande ancienne, en usage officiel 1939–1942 d'après les archives municipales ; ville occupée le 9/10/1938). Date du retour au nom Ústí nad Labem encore à prouver.",
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
    if eid in NOM_A_LA_DATE: prop['nom'] = NOM_A_LA_DATE[eid]['nom_propose']
    if eid in NOM_CYCLE3: prop['nom'] = NOM_CYCLE3[eid]['valeur']
    if eid in NOM_A_LA_DATE:
        if NOM_A_LA_DATE[eid]['nom_local_snapshot_propose'] != prop['nom']: prop['nom_local'] = NOM_A_LA_DATE[eid]['nom_local_snapshot_propose']
    elif v.get('nom_local') and v['nom_local'] != nom: prop['nom_local'] = v['nom_local']
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
    note = note.replace(' Le nom d’affichage slovaque ne prétend pas être la forme administrative officielle de 1944.', '')  # remplacé par le nom à la date
    note = note.replace(' ; graphie administrative de guerre à normaliser séparément', '')  # réglé au cycle 3 (Reichenberg)
    note = note.replace(' Libellé descriptif historique ; la forme officielle allemande reste à normaliser.', '')  # réglé au cycle 3 (Tetschen-Bodenbach)
    if eid in NOM_CYCLE3: note += f" Nom à la date : {prop['nom']} (aujourd'hui {'Děčín' if eid == 'ville-cz-decin' else nom}) — preuve : {PREUVE_NOM[eid]}. Date du retour au nom d'après-guerre non établie."
    if eid in NOTES: note += ' ' + NOTES[eid]
    if a_renforcer: note += f" À renforcer : {', '.join(a_renforcer)}."
    prop['note'] = note
    aliases = [a for a in dict.fromkeys([*v.get('aliases', []), *NOM_A_LA_DATE.get(eid, {}).get('aliases_a_ajouter', []), *ALIASES.get(eid, []), q.get('label_en')]) if a and a != nom]
    roles_de = {}
    for r, ss in preuves.items():
        for s_ in ss: roles_de.setdefault(s_, []).append(r)
    def usage(s_):
        u = ('preuve locale : ' + ', '.join(roles_de[s_])) if s_ in roles_de else 'nom à la date' if s_ in SOURCES_EN_PLUS.get(eid, []) else 'date de la fusion (01/01/1945)' if s_ == 'src-13-hu-miskolc-fusion' else 'contexte (situation, nom ou périmètre)'
        st = statut(s_)
        return u + ('' if st == 'ok' else ' (non vérifiée par Claude)' if st in ('non_verifiee', 'lien_casse') else ' (lecture partielle)')
    sources = [{'source_id': 'src-wikidata', 'locator': q['qid'], 'usage': 'position (coordonnées)'}]
    sources += [{'source_id': s_, 'locator': REGISTRE[s_].get('locator', ''), 'usage': usage(s_)} for s_ in dict.fromkeys([*e0['sources'], *SOURCES_EN_PLUS.get(eid, [])])]
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
    'version': '0.4', 'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
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
      "v0.3 (01/10) : réponse d'Ether — Cassovie (Kassa sur place) et Aussig portés comme nom à la date dans l'état (lu en premier par la carte ; la fiche garde Košice et Ústí nad Labem comme repères actuels, mêmes IDs) ; fusion Miskolc–Diósgyőr datée du 01/01/1945 (S44 complétée) ; 5 sources ajoutées. Les autres villes ne sont renommées que sur preuve individuelle.",
      "v0.4 (01/10) : cycle 3 d'Ether — Reichenberg (Liberec), Eger (Cheb), Brüx (Most), Tetschen-Bodenbach (Děčín) et Érsekújvár (Nové Zámky) portés comme nom à la date dans l'état, chacun sur une preuve individuelle relue par Claude ; fiches, IDs, nom_local, rôles et positions inchangés. Protectorat (noms bilingues), note Budapest/Szálasi et déplacement du vieux Most laissés en réserve par Guizmo : sources au registre, aucune donnée modifiée.",
    ]},
  },
  'entites': entites,
}
out = RACINE / 'data/snapshot0/villes_1-3_tchequie_slovaquie_hongrie.json'
out.write_text(json.dumps(lot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(len(entites), 'villes ->', out.relative_to(RACINE))
