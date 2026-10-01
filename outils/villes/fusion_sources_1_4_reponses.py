"""Fusion au registre de la réponse d'Ether au lot villes 1.4 (01/10/2026). À lancer UNE fois.
Delta : data/sources/deltas_ether/2026-10-01_villes_1-4_reponses_delta.json (76 fiches : 58 reprises, 18 nouvelles ; fusion par source_id).
Statut : relecture de Claude (data/sources/verifications_claude/2026-10-01_villes_1-4_reponses.json).
Les repères (locator) réécrits en anglais par Ether sont traduits ici en français ; les autres champs existants ne changent pas.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.13', 'fusion déjà faite ?'
delta = json.load(open(RACINE / 'data/sources/deltas_ether/2026-10-01_villes_1-4_reponses_delta.json', encoding='utf-8'))['sources']
verif = {r['id']: r for r in json.load(open(RACINE / 'data/sources/verifications_claude/2026-10-01_villes_1-4_reponses.json', encoding='utf-8'))['resultats']}
LOCATORS_FR = {
    'src-14-ee-rail-histoire': "EVR : trafic régulier Tapa–Tartu en 1877 ; Valga 1887 ; liaison régulière vers Riga 1889. Le musée de Tapa donne 1876.",
    'src-14-lv-rail-chronologie': "Tableau : Riga–Daugavpils 1861 ; Riga–Jelgava 1868 ; Liepāja–Vaiņode 1871 ; Sita–Rēzekne 1934 ; ligne Krustpils–Jēkabpils fermée en 1944.",
    'src-14-lt-rail-ministere': "Le ministère date de 1861 la première ligne de Lituanie ; Liepāja–Romny par Radviliškis 1871–1874 ; embranchements de 1873.",
    'src-14-lt-rail-vle': "VLE : Kaunas–Kybartai en service en 1861 ; ligne Saint-Pétersbourg–Varsovie achevée à travers la Lituanie (par Vilnius) en 1862 ; Liepāja–Romny par Radviliškis 1871–1873.",
    'src-14-pl-rail-premieres': "Histoire PKP : Wrocław–Oława 1842 ; premier tronçon Varsovie–Vienne 1845 ; Cracovie reliée en 1847.",
    'src-14-pl-lublin-administration': "Archives d'État de Lublin : siège du PKWN à Lublin dès le 27 juillet 1944 ; transformation en gouvernement provisoire le 31 décembre.",
    'src-14-pl-katowice-gare': "Fiche d'inventaire de l'Institut national du patrimoine : ensemble de l'ancienne gare ; bâtiment voyageurs daté de 1906.",
    'src-14-pl-stalowa-wola-industrie': "Histoire municipale : Zakłady Południowe inaugurées le 14 juin 1939 ; cité ouvrière et équipements déjà construits.",
    'src-14-pl-czestochowa-industrialisation': "Histoire culturelle municipale : chemin de fer Varsovie–Vienne en 1846 ; usines historiques citées ; aciérie Hantke à Raków, alors en périphérie.",
    'src-14-pl-gdansk-schichau': "Gedanopedia : terrain acheté en 1889 le long d'une voie ferrée existante ; chantier construit 1890–1892 ; premiers travaux navals 1891 ; ouverture officielle en janvier 1892.",
    'src-14-ee-kohtla-jarve-industrie': "VKG : industrie du schiste bitumineux dès 1916 ; usine d'essai 1921 ; quatre usines Kiviter 1924–1943 ; nouveau complexe daté de 1945.",
    'src-14-ee-kohtla-jarve-perimetre': "Encyclopédie : statut de ville en 1946 ; bourg de Järve d'avant-guerre et ajouts d'après-guerre décrits.",
    'src-14-ee-tallinn-histoire': "Notice : chemin de fer 1870 ; capitale de la RSS d'Estonie dès 1940 ; bombardement des 9–10 mars 1944 ; entrée de l'Armée rouge le 22 septembre 1944.",
    'src-14-lv-liepaja-port': "Histoire municipale (extrait indexé) : port bombardé le 2 août 1914 ; rôle maritime au début du XXe siècle.",
    'src-14-pl-gdansk-port-ferroviaire': "Gedanopedia : ferry ferroviaire Gedania construit en 1926 pour le service du port ; saisi en 1939, il garde son trajet sous le nom « Danzig ».",
}
par_id = {s['source_id']: s for s in reg['sources']}
for s in delta:
    sid = s['source_id']; v = verif.get(sid)
    if sid in par_id:
        x = par_id[sid]
        if sid in LOCATORS_FR and LOCATORS_FR[sid] != x.get('locator'):
            x['locator'] = LOCATORS_FR[sid]
            x['notes'] += f" Repère corrigé par Ether le 01/10/2026 (réponse au lot 1.4)."
        if v:  # relue à nouveau par Claude
            x['verification_claude'] = v['statut']
            if v['statut'] in ('ok', 'limite'): x['resume_passage'] = v['citation']
            x['notes'] += f" Relecture Claude 01/10/2026 (2e passe) : {v['commentaire']}"
        continue
    reg['sources'].append({
        'source_id': sid, 'niveau': s['niveau'], 'type_source': s['type_source'], 'titre': s['titre'],
        'institution': s['institution'], 'url': s['url'], 'date_consultation': s['date_consultation'], 'periode_couverte': [], 'zones': [],
        'usages_atlas': s['usages_atlas'], 'cibles': s['cibles'], 'locator': s['locator'],
        'resume_passage': v['citation'] if v['statut'] in ('ok', 'limite') else '', 'archive_locale': None,
        'verification_claude': v['statut'], 'verification_ether': s['verification'],
        'notes': f"Proposée par Ether (réponse au lot villes 1.4, 01/10/2026). Limite annoncée par Ether : {s['note']} Relecture Claude 01/10/2026 : {v['commentaire']}",
    })
reg['metadata']['version'] = '1.14'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources (v1.14)')
