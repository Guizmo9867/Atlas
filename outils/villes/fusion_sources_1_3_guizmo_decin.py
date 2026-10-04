"""Ajoute au registre la source trouvée par Guizmo pour Děčín (Tetschen-Bodenbach), le 04/10/2026.

Page sudetengebiete.de « Tetschen » : fusion du 01/10/1942 sous le nom Tetschen-Bodenbach, Landkreis Tetschen-Bodenbach
(Regierungsbezirk Aussig, Reichsgau Sudetenland) en 1945 ; chemin de fer en 1869 ; navigation sur l'Elbe.
Relecture Claude (WebFetch) : passages 1939, 1869 et Elbe lus ; la section sur 1942-1945 n'est pas restituée par l'outil
(page derrière une fenêtre d'abonnement) : elle est lue sur les deux captures de Guizmo (dossier d'échange).
Usage : python outils/villes/fusion_sources_1_3_guizmo_decin.py (une seule fois), puis construire_villes_1_3.py.
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
assert reg['metadata']['version'] == '1.22', 'ordre des fusions ?'
SID = 'src-guizmo-sudetengebiete-tetschen'
assert SID not in {s['source_id'] for s in reg['sources']}
PJ = '05_pieces_jointes_guizmo/src-guizmo-sudetengebiete-tetschen/'
reg['sources'].append({
    'source_id': SID, 'niveau': 'C', 'type_source': 'site_patrimoine_prive',
    'titre': 'Tetschen — Städte und Gemeinden bis heute (Deutsche in Böhmen & Mähren)',
    'institution': 'sudetengebiete.de (auteur indiqué : Thomas)',
    'url': 'https://sudetengebiete.de/tetschen/#Zugehoerigkeit_zum_Deutschen_Reich_bis_1945',
    'date_consultation': '2026-10-04', 'periode_couverte': '1838-1945', 'zones': ['cz'],
    'usages_atlas': ['nom_historique', 'perimetre_historique', 'rail', 'port_fluvial'],
    'cibles': ['ville-cz-decin'],
    'locator': "Section « Zugehörigkeit zum Deutschen Reich bis 1945 » (fusion du 01/10/1942 avec Altstadt sous le nom Tetschen-Bodenbach ; en 1945, Landkreis Tetschen-Bodenbach, Regierungsbezirk Aussig, Reichsgau Sudetenland) ; passages sur le recensement du 17/05/1939, le chemin de fer (1869) et la navigation sur l'Elbe.",
    'resume_passage': "Die Stadt Tetschen erhielt ihren Anschluss an das Eisenbahnnetz im Jahre 1869, als die Böhmische Nordbahn den Betrieb von Bodenbach über Tetschen, Bensen und Böhmisch-Kamnitz nach Warnsdorf aufnahm",
    'archive_locale': [PJ + 'capture_1_fusion_1942.jpg', PJ + 'capture_2_rail_elbe_1939.jpg'],
    'verification_claude': 'limite',
    'verification_humaine': {'decision': 'verifiee',
                             'commentaire': "Le 1er octobre 1942, Tetschen et Bodenbach fusionnent avec Altstadt pour former la ville de Tetschen-Bodenbach ; en 1945, elle appartient au district de Tetschen-Bodenbach (Regierungsbezirk Aussig, Reichsgau Sudetenland). Chemin de fer en 1869, navigation sur l'Elbe importante.",
                             'par': 'Guizmo', 'date': '2026-10-04'},
    'notes': "Trouvée par Guizmo le 04/10/2026 (captures de la page traduite en français, section 22). Relecture Claude 04/10/2026 (WebFetch) : passages 1939 (12 647 habitants), 1869 (Böhmische Nordbahn) et Elbe (1er vapeur en 1838) lus ; la section sur 1942-1945 n'est pas restituée par l'outil (fenêtre d'abonnement), lue sur les captures de Guizmo. Site privé (niveau C) : confirme l'annuaire de 1942 (src-13-cz-tetschen-telephone-1942) ; l'acte officiel est le Verordnungsblatt 1942, n° 40, p. 353 (référence trouvée par Ether, à ajouter avec sa capture).",
})
reg['metadata']['version'] = '1.23'
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('registre v1.23 :', len(reg['sources']), 'sources')
