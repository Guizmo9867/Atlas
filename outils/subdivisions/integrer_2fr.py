"""Intégration du lot 2.FR — subdivisions de la France au 01/01/1945 (pilote de la phase 2).
Livré par Ether le 14/10/2026 dans 01_lots/2.FR/ ; intégré par Claude le 15/10/2026 en conversation avec Guizmo (mode manuel).
À lancer UNE fois, après outils/geo/decouper_2fr.py (registre v1.31 -> v1.32).

Décisions de Guizmo (15/10/2026) :
  1. les 90 départements s'affichent comme « tracé reconstitué » ; Hautes-Alpes, Alpes-Maritimes et Savoie aussi, avec la réserve R2FR-02 ;
  2. 18 circonscriptions régionales ; tracé seulement pour les 13 dont la composition est complète (Lyon et Marseille avec la réserve alpine) ;
  3. affichage sur la carte par échelons (1 = sous l'État, 2 = en dessous), selon des seuils de zoom fixes, calque « Découpage administratif » ;
  4. les chefs-lieux restent une référence 1940 (R2FR-05) ; les villes manquantes seront demandées à Ether en complément 1.x.
"""
import json, pathlib, copy
RACINE = pathlib.Path(__file__).resolve().parents[2]
DELTAS = RACINE / 'data/sources/deltas_ether'
GEOM = RACINE / 'data/geometries/snapshot0'
R = RACINE / 'data/sources/atlas_registre_sources.json'
VERIF = 'data/sources/verifications_claude/2026-10-15_2FR.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] in ('1.31', '1.32'), 'ordre des fusions ?'
DEJA_FUSIONNE = reg['metadata']['version'] == '1.32'  # relance : on refait seulement le fichier du corpus

# 1. La proposition d'Ether, rangée sous « proposition_ether » pour que le validateur ne la lise pas comme un lot du corpus
P = DELTAS / '2026-10-14_2FR_subdivisions_proposees_ether.json'
brut = json.load(open(P, encoding='utf-8'))
if 'proposition_ether' not in brut:
    P.write_text(json.dumps({'note': "Copie fidèle de 01_lots/2.FR/atlas_2FR_subdivisions_proposees.json (Ether, 14/10/2026), placée sous la clé "
                             "proposition_ether pour que le validateur ne la lise pas comme un lot du corpus (les entités intégrées sont dans "
                             "data/snapshot0/subdivisions_2-FR.json).", 'proposition_ether': brut}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lot = brut
else:
    lot = brut['proposition_ether']

# 2. Géométries : sources au format du corpus (objets avec source_id)
for f in sorted(GEOM.glob('geom-subdivision-fr-*.geojson')):
    g = json.load(open(f, encoding='utf-8'))
    s = g['properties'].get('sources', [])
    if s and isinstance(s[0], str):
        region = '-commissariat-' in f.name
        g['properties']['sources'] = [{'source_id': x, 'locator': 'COG_DEPARTEMENTS_1940' + (' ; union des départements de la composition régionale' if region else ''),
                                       'usage': 'tracé reconstitué (millésime 1940)'} for x in s]
        f.write_text(json.dumps(g, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

# 3. Le fichier du corpus
ALPINS = {'subdivision-fr-hautes-alpes', 'subdivision-fr-alpes-maritimes', 'subdivision-fr-savoie',
          'subdivision-fr-commissariat-lyon', 'subdivision-fr-commissariat-marseille'}
entites = []
for e in lot['entites']:
    e = copy.deepcopy(e)
    s = e['etats'][0]
    p = s['proprietes']
    p['echelon'] = p['niveau']
    if p['niveau'] == 1:
        # « de Angers » -> « d'Angers » ; nom court lisible sur la carte (« Région de Lyon » plutôt que « CRR Lyon »)
        ville = e['nom'].split('République de ', 1)[1]
        de = "d'" if ville[0] in 'AEIOUÉÈ' else 'de '
        e['nom'] = p['nom'] = f"Commissariat régional de la République {de}{ville}"
        e['nom_court'] = f"Région {de}{ville}"
    if e['entite_id'] in ALPINS:
        ref = f"geom-{e['entite_id']}-1945-01-01"
        assert (GEOM / f'{ref}.geojson').exists(), ref
        s['geometrie_ref'] = ref
        p['note'] = (p.get('note', '') + " Tracé affiché avec la réserve alpine R2FR-02 (décision de Guizmo du 15/10/2026) : "
                     "limite de 1940, petites cessions antérieures à 1947 non vérifiées.").strip()
    entites.append(e)
sans = [e['entite_id'] for e in entites if not e['etats'][0].get('geometrie_ref')]
corpus = {
    'metadata_lot': {
        'nom': 'snapshot0_subdivisions_2-FR', 'date_reference': '1945-01-01', 'heure_reference': '00:00', 'version': '1.0',
        'statut': 'integre_par_claude', 'gabarit_source': 'gabarits/gabarit_entite_temporelle_atlas.json',
        'lot_methode': '2.FR (pilote de la phase 2, docs/METHODE_ATLAS_v2.md)',
        'proposition_ether': 'data/sources/deltas_ether/2026-10-14_2FR_subdivisions_proposees_ether.json',
        'regles': [
            "échelon 1 = premier niveau sous l'État (ici les 18 circonscriptions des commissaires régionaux de la République) ; échelon 2 = le niveau en dessous (les 90 départements). Le terme local reste dans statut_administratif.",
            "une subdivision porte la souveraineté de droit ; le contrôle réel (poches, Alsace occupée, fronts) vient des territoires et des lignes de front déjà intégrés",
            "affichage : échelon 1 à partir du zoom 5, échelon 2 à partir du zoom 6,5, les mêmes seuils pour tous les pays (calque « Découpage administratif »)",
            "tracés : reconstitution TRF-GIS millésime 1940 (CC BY 4.0, Victor Gay), statut provisoire ; R2FR-01",
            "chef_lieu_propose = référence 1940, jamais publiée comme chef-lieu 1945 validé (R2FR-05)",
        ],
        'sans_trace': sans,
        'decision_guizmo': '15/10/2026 : tracés reconstitués affichés, réserve alpine, 18 régions dont 13 tracées, affichage par échelons et zoom fixe',
    },
    'entites': entites,
}
(RACINE / 'data/snapshot0/subdivisions_2-FR.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# 4. Relecture des sources par Claude et fusion au registre
if DEJA_FUSIONNE:
    print(len(entites), 'subdivisions (corpus refait) ;', len(sans), 'sans tracé'); raise SystemExit
V = {
 'src-trfgis-departements-1940': ('non_verifiee', "La page Harvard Dataverse n'est pas lisible par l'outil de lecture de Claude (accès refusé aux robots). Les tracés livrés par Ether ont été contrôlés à l'intégration (90 départements, codes 01–90, topologie conservée) ; licence CC BY 4.0 annoncée, à confirmer."),
 'src-gay-trfgis-methodologie-2020': ('limite', "Document de travail de la Toulouse School of Economics : décrit la méthode de reconstruction des départements à partir des communes. Explique le tracé, mais ne prouve pas à lui seul l'état au 01/01/1945."),
 'src-an-reponse-regions-1981-01-12': ('ok', "Page 164 lue par Claude sur la capture d'Ether : commissaires régionaux de la République créés par l'ordonnance du 10/01/1944 ; Strasbourg au 29/09/1944 ; pouvoirs du préfet de la Moselle ; Corse non rattachée au 09/11/1944 ; Lot-et-Garonne rattaché à Bordeaux le 29/11/1944."),
 'src-rhone-inventaire-283w-2001': ('ok', "Inventaire 283W des archives du Rhône : circonscription du commissariat régional de la République de Lyon, huit départements après le décret du 27/06/1944."),
 'src-insee-annuaire-1940-1945-1946': ('ok', "Page 6 lue par Claude sur la capture d'Ether : tableau « au 1er janvier 1945 » avec les noms de l'époque (Charente-Maritime, Loire-Inférieure, Côtes-du-Nord, Alpes (Basses-)…)."),
 'src-lang-histoire-cog-1943': ('ok', "Histoire du Code officiel géographique : codes 01–90 de 1943 et maintien en droit des trois départements annexés de fait (Bas-Rhin, Haut-Rhin, Moselle)."),
 'src-haute-vienne-fonds-boursicot-9j': ('non_verifiee', "PDF des archives de la Haute-Vienne non lisible par l'outil de Claude ; Ether l'a lu par l'index seulement (R2FR-04)."),
 'src-memorial-alsace-moselle-malgre-nous': ('ok', "Page du Mémorial de l'Alsace-Moselle : annexion de fait et incorporation de force ; sert de note de contexte, pas de limite."),
 'src-manche-halais-prefecture-1944': ('non_verifiee', "PDF des archives de la Manche non lisible par l'outil de Claude."),
 'src-an-reponse-regions-militaires-1981-08-03': ('non_verifiee', "PDF du Journal officiel non relu par Claude dans ce lot ; utilisé seulement en appui (régions militaires)."),
 'src-onu-traite-italie-1947-art2': ('limite', "Traité de paix avec l'Italie (1947), article 2 : changements de frontière postérieurs au Snapshot. Sert seulement d'alerte, rien n'est appliqué au 01/01/1945."),
}
(RACINE / VERIF).write_text(json.dumps({'lot': '2.FR', 'date': '2026-10-15', 'auteur': 'Claude',
    'methode': "Lecture des pages accessibles et des captures déposées par Ether dans 01_lots/2.FR/preuves/ ; ce qui n'a pas pu être lu reste « non_verifiee » et va dans « Sources à valider ».",
    'resultats': [{'id': k, 'statut': v[0], 'commentaire': v[1]} for k, v in V.items()]}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
delta = json.load(open(DELTAS / '2026-10-14_2FR_sources_delta.json', encoding='utf-8'))
par_id = {s['source_id'] for s in reg['sources']}
CONNUS = {'source_id', 'niveau', 'type_source', 'titre', 'institution', 'url', 'date_consultation', 'cibles', 'usage', 'usages_atlas',
          'locator', 'note', 'verification_ether', 'verification_claude', 'preuves'}
for s in delta['ajouter']:
    sid = s['source_id']
    assert sid not in par_id, sid
    statut, com = V[sid]
    usage = ' ; '.join(s['usage']) if isinstance(s.get('usage'), list) else s.get('usage', '')
    fiche = {'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'], 'institution': s['institution'],
             'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': ['FR'],
             'usages_atlas': s.get('usages_atlas', []), 'cibles': s['cibles'], 'locator': s['locator'],
             'resume_passage': com if statut != 'non_verifiee' else '', 'archive_locale': None,
             'verification_claude': statut, 'verification_ether': s.get('verification_ether'),
             'notes': f"Proposée par Ether (lot 2.FR, 14/10/2026). Ce que la source prouve selon Ether : {usage}. Limite annoncée par Ether : {s.get('note', '')} Relecture Claude 15/10/2026 : {com}"}
    if s.get('preuves'): fiche['preuves_ether'] = s['preuves']
    if s.get('verification_claude'): fiche['verification_claude_ether'] = s['verification_claude']
    for k, val in s.items():
        if k not in CONNUS: fiche[k] = val
    reg['sources'].append(fiche)
reg['metadata']['version'] = '1.32'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(entites), 'subdivisions ;', len(sans), 'sans tracé :', sans)
print(len(delta['ajouter']), 'sources ajoutées ;', len(reg['sources']), 'au registre (v1.32)')
