"""Autres liens et pièces jointes de Guizmo vérifiés par Claude le 04/10/2026 (BOUCLE_AUTOMATIQUE §3.5 bis). À lancer UNE fois.
src-13-hu-miskolc-histoire (Guizmo : « Prouve pour 1945, la suite plus tard », avec un nouveau lien et une capture) :
- lien https://miskolc.hu/…/miskolci-informacio/miskolc-tortenete : lu par WebFetch (sous-agent) -> src-guizmo-miskolc-tortenete ;
- capture (05_pieces_jointes_guizmo/src-13-hu-miskolc-histoire/…jpg, dossier d'échange, jamais dans le dépôt) : article de
  Kis József, « Miskolc és városrészei a kommunista hatalomátvétel sodrában », Régiónk története III, p. 193-212,
  DOI 10.46403/Akozigtortvalt.2022.193, lu par Claude -> src-guizmo-kis-miskolc-2022.
L'ancienne source, validée par Guizmo pour 1945, est GARDÉE telle quelle (jamais retirée) ; les deux nouvelles sont ajoutées aux
fiches de Miskolc et Diósgyőr par appliquer_validations_guizmo.py (complements_guizmo.sources_ajoutees).
"""
import json, pathlib
RACINE = pathlib.Path(__file__).resolve().parents[2]
R = RACINE / 'data/sources/atlas_registre_sources.json'
reg = json.load(open(R, encoding='utf-8'))
par_id = {s['source_id']: s for s in reg['sources']}
assert 'src-guizmo-kis-miskolc-2022' not in par_id, 'déjà fait'
CAPTURE = '05_pieces_jointes_guizmo/src-13-hu-miskolc-histoire/Image_ChatGPT_3_oct._2026_18_29_28.jpg'
ancienne = par_id['src-13-hu-miskolc-histoire']
nouvelles = [
 {'source_id': 'src-guizmo-miskolc-tortenete', 'niveau': 'B', 'type_source': 'notice_historique_institutionnelle',
  'titre': 'Miskolc története (nouvelle adresse)', 'institution': 'Ville de Miskolc',
  'url': 'https://miskolc.hu/elet-a-varosban/varosinformacio/miskolci-informacio/miskolc-tortenete', 'date_consultation': '2026-10-04',
  'periode_couverte': [], 'zones': [], 'usages_atlas': ['rail', 'perimetre_historique'], 'cibles': ['ville-hu-miskolc', 'ville-hu-diosgyor'],
  'locator': 'Chronologie : 1870 (ligne Hatvan–Miskolc) ; 1945 et 1950 (communes rattachées).',
  'resume_passage': '1870. január 9-én átadták a Hatvan–Miskolc vasútvonalat, amivel a város összeköttetésbe került Pesttel. … 1945-ben Diósgyőrt és Hejőcsabát, 1950-ben Görömbölyt, Szirmát és Hámort csatolták a városhoz.',
  'archive_locale': None, 'verification_claude': 'ok',
  'notes': "Lien proposé par Guizmo le 03/10/2026 pour src-13-hu-miskolc-histoire (ancienne adresse en erreur 404). Relu par Claude le 04/10/2026 (WebFetch, sous-agent) : ligne Hatvan–Miskolc ouverte le 9 janvier 1870 ; Diósgyőr et Hejőcsaba rattachées en 1945, Görömböly, Szirma et Hámor en 1950. La page ne donne que l'année 1945 (pas le jour)."},
 {'source_id': 'src-guizmo-kis-miskolc-2022', 'niveau': 'A', 'type_source': 'article_scientifique',
  'titre': 'Kis József : Miskolc és városrészei a kommunista hatalomátvétel sodrában (Régiónk története III, p. 193-212)',
  'institution': 'Régiónk története III (2022)', 'url': 'https://doi.org/10.46403/Akozigtortvalt.2022.193', 'date_consultation': '2026-10-04',
  'periode_couverte': [], 'zones': [], 'usages_atlas': ['perimetre_historique'], 'cibles': ['ville-hu-miskolc', 'ville-hu-diosgyor'],
  'locator': 'p. 193, section « Úton Nagy-Miskolc felé », premier paragraphe.',
  'resume_passage': 'A szovjet csapatok bevonulásakor a mai Miskolc még számos önálló településből állt. Így különálló községként működött Diósgyőr, Hámor, Hejőcsaba, Görömböly és Szirma. A Miskolci Nemzeti Bizottság már 1944. december 26-án határozatot hozott Nagymiskolc létrehozásáról. A Diósgyőrt, Hejőcsabát és Görömböly település Tapolca részét magába foglaló város bővülését az Ideiglenes Nemzetgyűlés 1945. január 1-től szentesítette.',
  'archive_locale': CAPTURE, 'verification_claude': 'ok',
  'notes': ("Pièce jointe de Guizmo (capture de la p. 193-194, 03/10/2026) pour src-13-hu-miskolc-histoire, lue par Claude le 04/10/2026. "
            "Prouve qu'à l'arrivée des troupes soviétiques (décembre 1944) Diósgyőr, Hámor, Hejőcsaba, Görömböly et Szirma étaient des communes distinctes, "
            "et que l'agrandissement de Miskolc (Diósgyőr, Hejőcsaba, Tapolca) vaut à compter du 1er janvier 1945 : changement daté du 1er janvier, "
            "appliqué APRÈS le Snapshot 0 (Diósgyőr reste une ville distincte au Snapshot 0 ; la fusion est pour le ratissage de janvier 1945). "
            "Capture dans le dossier d'échange seulement (droits d'auteur) ; DOI non ouvert par l'outil.")},
]
reg['sources'].extend(nouvelles)
c = ancienne['complements_guizmo']
c['a_verifier'] = False
c['resultat_claude'] = ("Vérifié le 04/10/2026 : le nouveau lien confirme le rail (1870) et les rattachements de 1945 ; la capture (article de Kis József, 2022) "
                        "confirme la décision du 26/12/1944 et l'effet au 1er janvier 1945 (après le Snapshot 0). Deux sources ajoutées : "
                        "src-guizmo-miskolc-tortenete et src-guizmo-kis-miskolc-2022 ; l'ancienne, validée par Guizmo, est gardée.")
c['sources_ajoutees'] = [
 {'source_id': 'src-guizmo-miskolc-tortenete', 'villes': {
   'ville-hu-miskolc': {'locator': '1870 : ligne Hatvan–Miskolc ; 1945 : Diósgyőr et Hejőcsaba rattachées', 'usage': 'preuve locale : rail'},
   'ville-hu-diosgyor': {'locator': '1945 : Diósgyőr rattachée à Miskolc', 'usage': 'contexte (situation, nom ou périmètre)'}}},
 {'source_id': 'src-guizmo-kis-miskolc-2022', 'villes': {
   'ville-hu-miskolc': {'locator': 'p. 193 : Grand Miskolc à compter du 1er janvier 1945 (après le Snapshot 0)', 'usage': 'date de la fusion (01/01/1945)'},
   'ville-hu-diosgyor': {'locator': 'p. 193 : commune distincte à l\'arrivée des troupes soviétiques ; rattachée au 1er janvier 1945', 'usage': 'date de la fusion (01/01/1945)'}}}]
ancienne['notes'] += " Autres liens et capture de Guizmo vérifiés par Claude le 04/10/2026 : voir complements_guizmo (sources ajoutées src-guizmo-miskolc-tortenete et src-guizmo-kis-miskolc-2022)."
R.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(reg['sources']), 'sources')
