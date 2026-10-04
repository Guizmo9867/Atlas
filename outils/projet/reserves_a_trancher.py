"""Rassemble toutes les réserves de la série villes 1.x en un seul fichier, pour la revue finale de Guizmo avec Ether.

Lit : les fichiers de réserves d'Ether (01_lots/<lot>/*_ether_reserves_revue_finale.md du dossier d'échange),
les questions encore ouvertes de Claude (liste QUESTIONS_CLAUDE ci-dessous, à tenir à jour à chaque compte rendu)
et le nombre de villes « À renforcer » par lot (data/snapshot0/villes_1-*.json du dépôt).
Écrit : docs/RESERVES_A_TRANCHER.md (dépôt) et 00_RESERVES_A_TRANCHER.md (dossier d'échange).
Usage : python outils/projet/reserves_a_trancher.py <dossier d'échange>   (depuis la racine du dépôt)
"""
import sys, re, json, glob, pathlib, datetime

RACINE = pathlib.Path(__file__).resolve().parents[2]
ECHANGE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE.parent / 'Desktop' / 'Atlas'

# Questions de Claude encore ouvertes (reprises de ses comptes rendus ; les autres sont déjà dans les fichiers d'Ether)
QUESTIONS_CLAUDE = {
    'villes_1-5': [
        ('Q15-02 — Chefs-lieux de région : faut-il les marquer « capitale » ?',
         "Ether proposait « capitale régionale » pour 15 chefs-lieux d'oblast ou capitales de républiques autonomes (Kazan, Oufa, Simferopol, Grodno…). Claude ne l'a pas appliqué : aucune règle ne couvre ce cas, et d'autres chefs-lieux du même lot (Briansk, Kharkiv, Odessa, Lviv) ne l'avaient pas.",
         "Rien n'est affiché comme capitale pour ces 15 villes ; leurs rôles administratifs et leurs preuves sont gardés dans la fiche.",
         "Aucune capitale pour les chefs-lieux ; « régionale » pour tous les chefs-lieux (à appliquer aussi aux lots déjà faits : Gaue allemands, voïvodies…) ; un nouveau type « chef-lieu » plus discret."),
        ('Q15-03 — Sources à remplacer (liens morts ou passage introuvable)',
         "11 sources : 5 liens en erreur pour l'outil de Claude et 6 pages qu'il ne lit qu'en partie. Au cycle 3 (03/10), Ether a déposé 12 captures des passages pour 8 d'entre elles ; Claude les a lues le 04/10 : Belomorsk, Ouglitch, Sverdlovsk, Tchernikovsk, Sébastopol, Taganrog et les deux tomes militaires de 1944 (Grodno, Brest, Jlobine, Bobrouïsk ; Stryï, Moukatchevo, Tchop, Oujgorod) sont prouvés pour ces villes. Restent sans capture : Rosmorport Arctique, patrimoine de Carélie, encyclopédie de Grodno. Soumy est confirmée (page 353).",
         "Les villes relues ne sont plus « À renforcer » pour ces rôles ; les 3 sources sans capture gardent leur réserve. Lot clos côté Ether (3 cycles).",
         "Accepter la lecture d'Ether pour les 3 sources restantes ; ou garder la réserve visible ; ou Guizmo valide lui-même sur la page « Sources à valider »."),
        ('Q15-04 — Noms des villes de Biélorussie',
         "Certaines fiches ont le nom français (Gomel, Moguilev), d'autres la forme biélorusse (Baryssaw, Stawbtsy).",
         "Rien n'a été changé.",
         "Règle « nom français attesté d'abord, sinon forme locale » comme ailleurs ; ou garder tel quel."),
    ],
    'villes_1-6': [
        ('Q16-01 — Sources du lot 1.6 à remplacer ou préciser',
         "Au cycle 2 (03/10), Ether a précisé l'adresse et le passage des 12 sources. Relecture de Claude le 04/10 (WebFetch seul) : les 6 liens (Rosmorport Primorié et Petropavlovsk, Novossibirsk 1920-1940, ONIIP Omsk, BVRZ Barnaoul, Maxam Tchirtchik) répondent toujours « 404 » à l'outil alors qu'Ether les lit dans son navigateur ; 5 pages restent tronquées avant le passage (Vayner ch. 4, archives de Spassk, Vichnevski Sakhaline, Providenia, petites villes du Kazakhstan). Le livre LOC sur la Mongolie est relu sur les 3 images d'Ether (Oulan-Bator industrie, Nalaïkh charbon et rail, Tchoïbalsan et Borzia rail).",
         "Les rôles des 11 sources non lues restent « À renforcer ».",
         "Guizmo ouvre ces liens lui-même sur la page « Sources à valider » (« Ça prouve ») ; Ether dépose des captures des passages, comme pour le 1.5 ; ou on garde la réserve visible."),
        ("Q16-02 — Répertoires administratifs illisibles pour l'outil de Claude",
         "Ether a déposé au cycle 2 un index de 124 relations ville/page avec 28 images de pages (1940, 1941, supplément 1944). Claude a fait lire les 28 images le 04/10 : 67 relations relues, dont 63 confirmées ville par ville (capitale, centre administratif, gare à 0 km). Les 57 autres relations n'ont qu'une adresse de lecteur en ligne, que l'outil ne lit pas.",
         "176 villes du lot gardent au moins un rôle « À renforcer » (225 avant) ; les villes relues sont marquées « page relue par Claude pour cette ville ».",
         "Ether dépose les images des pages manquantes (comme pour les 28 premières) ; ou on accepte ces répertoires officiels comme preuve sur la lecture d'Ether."),
        ("Q16-03 — Noms « de 1945 » qui ne sont qu'une autre transcription",
         "Sur les 89 villes du lot 1.6 affichées sous un nom de 1945, une cinquantaine ne changent que l'orthographe (Tokmok/Tokmak, Farap/Farab, Kara-Suu/Kara-Sou, Balkhash/Balkhach…) ; plusieurs fiches portent une forme locale ou anglaise plutôt que française (Sulukta, Baýramaly, Yangiyo‘l, Mandalgovĭ, Nalayh). Même cas au lot 1.7 en Azerbaïdjan (Agstafa/Akstafa, Yevlakh/Ievlakh, Kurdamir/Kiourdamir, Ujar/Oudjary, Khachmaz/Khatchmas, Gazakh/Kazakh). Les vrais changements de nom (Frounzé, Stalinabad, Kirovabad, Leninakan, Dzaoudjikaou, Stalinir…) sont prouvés à part.",
         "Gardé tel que proposé par Ether ; seules Nikolaïevsk, Komsomolsk-sur-l'Amour (apostrophe), İstanbul (I pointé) et les deux Ereğli (précisant de lieu) ne sont plus affichées comme renommées.",
         "Une règle unique de transcription française pour toute la série (comme Q15-04) : la fiche prend la forme française, et le nom de 1945 n'est affiché que s'il s'agit d'un autre nom ; ou garder tel quel."),
    ],
    'villes_1-7': [
        ('Q17-01 — Sources du lot 1.7 que l\'outil de Claude ne lit pas',
         "Sur 52 sources relues le 04/10 (WebFetch seul) : 28 confirmées, 10 en lecture partielle, 12 illisibles pour l'outil (sites turcs du ministère de la Culture et kulturportali refusés aux robots, PDF de la MAPEG, encyclopédie Atatürk en JavaScript, musée du rail arménien en erreur, ville de Kropotkine, TRDizin, deux pages Militera tronquées), 1 lien en erreur (Rosmorport mer Noire) et 1 faible : le journal « Заря Востока » du 12/02/1941 ne contient pas, à la lecture de l'outil, l'article sur les mineurs de Tkvartcheli.",
         "Les rôles qui n'ont que ces sources restent « À renforcer » (124 villes sur 166).",
         "Ether dépose des captures des passages (comme au 1.5) ou donne une autre source ; Guizmo peut valider sur la page « Sources à valider »."),
        ('Q17-02 — Pages du répertoire de 1940 pour la Géorgie et l\'Arménie',
         "Les rôles « rail » et « administration » de 35 villes de Géorgie et d'Arménie reposent sur le répertoire de 1940 (pages 259-269 et 277-296), dont aucune image n'est déposée. Claude a relu les pages de l'Azerbaïdjan (236-237) et du supplément de 1944 pour le Caucase du Nord : 16 villes confirmées (Bakou, Gandja, Agstafa, Yevlakh, Kurdamir, Tovuz, Ujar, Khachmaz, Lankaran, Chaki, Sabirabad, Gazakh, Vladikavkaz, Grozny, Goudermes, Kizliar). La page du kraï de Stavropol manque aussi.",
         "Ces 35 villes gardent leurs rôles « À renforcer ».",
         "Ether dépose les images des pages 259-269 et 277-296 (et Stavropol) ; ou on accepte le répertoire sur la lecture d'Ether."),
    ],
}

def nettoyer(t):
    return re.sub(r'\s+', ' ', t.replace('**', '')).strip()

def lire_reserves(fichier):
    """Renvoie [(titre, sait, change, choix, texte_libre)] depuis les tableaux et les sections '## ID — titre'."""
    lignes = fichier.read_text(encoding='utf-8').splitlines()
    items, complements, i = [], {}, 0
    while i < len(lignes):
        l = lignes[i]
        if l.startswith('| ') and not l.startswith('| ID') and not set(l) <= set('|-: '):
            c = [nettoyer(x) for x in l.strip().strip('|').split('|')]
            if len(c) >= 4 and re.match(r'^[A-Z][A-Z0-9-]*-?\d', c[0]):
                items.append((c[0], c[1], c[2], c[3], ''))
        elif l.startswith('## ') and re.match(r'^## [A-Z]+\d*-\d+', l):
            titre, corps = l[3:].strip(), []
            i += 1
            while i < len(lignes) and not lignes[i].startswith('## '):
                if lignes[i].strip(): corps.append(lignes[i].strip())
                i += 1
            items.append((titre, '', '', '', nettoyer(' '.join(corps))))
            continue
        elif re.match(r'^[A-Z]+\d*-\d+ : ', l):
            k, v = l.split(' : ', 1)
            complements[k.strip()] = nettoyer(v)
        i += 1
    return items, complements

REGISTRE = {x['source_id']: x for x in json.load(open(RACINE / 'data/sources/atlas_registre_sources.json', encoding='utf-8'))['sources']}
# Sources citées par leur nom dans les réserves des lots 1.3/1.4 (sans identifiant écrit) : renvoi manuel
CITEES = {
    'Q15-02': ['src-neb-admin1944-supplement'],
    'Q15-03': ['src-rosmorport-arctique-histoire', 'src-musee-pobedy-sverdlovsk-production-1944', 'src-bashenc-tchernikovsk-1944', 'src-sebastopol-musee-reconstruction-1944', 'src-rosmorport-taganrog-reparation-1943', 'src-karelia-patrimoine-guerre-1941-1945', 'src-belomorsk-bibliotheque-gare-2024', 'src-rushydro-ouglitch-histoire-2015', 'src-jdv-tome3-bielorussie-1944', 'src-jdv-tome3-carpates-kertch-1944', 'src-grodno-encyclopedie-1989-1944', 'src-soumy-frunze-avril-1944'],
    'Q16-01': ['src-rosmorport-primorie-histoire', 'src-rosmorport-petropavlovsk-histoire', 'src-novossibirsk-histoire1920-1940', 'src-oniip-omsk-1942', 'src-bvrz-histoire', 'src-maxam-chirchiq-histoire', 'src-vayner-transport-guerre-ch4', 'src-loc-mongolie-1991', 'src-archives-primorie-spassk-ciment', 'src-vishnevski-sakhaline2000', 'src-ks-providenia-dyga2022', 'src-ualtaeva-petites-villes2011'],
    'Q17-01': ["src-17-ge-zaria19410212", "src-17-tr-mersin-tarsus-histoire", "src-17-tr-raman-mapeg1991", "src-vayner-transport-guerre-ch4", "src-17-tr-atam-rail-as2021", "src-jdv-tome3-bielorussie-1944", "src-17-am-rail-musee", "src-17-tr-gelibolu-administration", "src-rosmorport-taganrog-reparation-1943", "src-17-tr-maden-bakir-etude", "src-17-ru-kropotkine-ville", "src-17-tr-kirklareli-gare", "src-17-tr-admin-ordu"],
    'Q17-02': ['src-shpl-admin1940', 'src-neb-admin1944-supplement'],
    'Q16-02': ['src-shpl-admin1940', 'src-sssr-admin1941-kirghizistan', 'src-sssr-admin1941-tadjikistan', 'src-sssr-admin1941-turkmenistan', 'src-neb-admin1944-supplement'],
    'Q13-02': ['src-13-protectorat-velcovsky-langues'], 'Q13-03': ['src-13-hu-szalasi-koszeg-neb-1944'],
    'R15-01': ['src-rosmorport-baltique-histoire', 'src-spb-chenal-mines-2016'], 'R15-02': ['src-rosmorport-baltique-histoire'],
    'R15-20': ['src-nkvd-bielorussie-rapport-19440727'], 'R15-21': ['src-kovalev-rail-ukraine-moldavie-1944'], 'Q13-04': ['src-13-most-carte-municipale-1938', 'src-13-cz-most-histoire'],
    'R-05': ['src-13-hu-miskolc-fusion', 'src-13-sk-cassovie-fr'],
    'Q14-03': ['src-14-ee-tapa-local', 'src-14-ee-rail-histoire'],
    'Q14-05': ['src-14-pl-tarnowitz-archive', 'src-14-pl-cosel-archive', 'src-14-pl-heydebreck-archive'],
    'S14-02': ['src-14-pl-posen-plan-1944', 'src-14-pl-elbing-map-1944', 'src-14-pl-rail-premieres', 'src-14-ee-kohtla-jarve-perimetre', 'src-14-pl-gdansk-port-ferroviaire'],
}

def index_s(lot):
    """Repères S1, S2… des carnets d'Ether -> source_id (fichier *_ether_index_sources.md du lot, ou « réf. Sxx » du registre)."""
    m = {}
    for f in ECHANGE.glob(f'01_lots/{lot}/*_ether_index_sources.md'):
        for l in f.read_text(encoding='utf-8').splitlines():
            r = re.match(r'^\| (S\d+) \| (src-[\w-]+)', l)
            if r: m[r.group(1)] = r.group(2)
    num = lot.replace('villes_', 'villes ').replace('-', '.')
    for sid, x in REGISTRE.items():
        r = re.search(r'\(' + re.escape(num) + r'[^)]*réf\. (S\d+)\)', x.get('notes', ''))
        if r and r.group(1) not in m: m[r.group(1)] = sid
    return m

STATUTS = {'ok': 'confirmée par Claude', 'limite': 'lecture partielle', 'faible': 'ne prouve pas bien', 'non_verifiee': 'illisible pour Claude', 'lien_casse': 'lien mort'}
def sources_liees(texte, ident, idx):
    ids = list(dict.fromkeys(CITEES.get(ident, []) + re.findall(r'src-[a-z0-9][\w-]*[a-z0-9]', texte) + [idx[x] for x in re.findall(r'\bS(\d+)\b', texte) and ['S' + n for n in re.findall(r'\bS(\d+)\b', texte)] if x in idx]))
    lignes = []
    for i in ids:
        x = REGISTRE.get(i)
        if not x: continue
        lignes.append(f"  - [{x.get('titre') or i}]({x.get('url', '')}) — `{i}` ({STATUTS.get(x.get('verification_claude'), x.get('verification_claude', '?'))})")
    return lignes

def a_renforcer():
    res = {}
    for f in sorted(glob.glob(str(RACINE / 'data/snapshot0/villes_1-*.json'))):
        ents = json.load(open(f, encoding='utf-8')).get('entites', [])
        if not ents: continue
        lot = re.search(r'villes_(1-\d+)', f).group(1)
        n = sum('À renforcer' in e['etats'][0].get('proprietes', {}).get('note', '') for e in ents)
        res[lot] = (n, len(ents))
    return res

out = [f"# Atlas — réserves et points à trancher (série villes 1.x)",
       "",
       f"*Généré automatiquement le {datetime.datetime.now().strftime('%d/%m/%Y à %H h %M')} par Claude, à partir des fichiers de réserves d'Ether et des comptes rendus de Claude. Régénéré à chaque lot.*",
       "",
       "## Comment s'en servir",
       "",
       "- Chaque point a un **numéro** (ex. `R15-07`), **ce qu'on sait**, **ce que ça change sur la carte** et **les choix possibles**.",
       "- Prends-les un par un avec Ether : demande-lui de t'expliquer le contexte historique, puis tranche. Écris ta décision sur la ligne « Décision de Guizmo ».",
       "- Rien ici n'est appliqué tant que tu n'as pas décidé : l'Atlas affiche aujourd'hui la version prudente décrite dans « ce que ça change ».",
       "- Sous chaque point, **Sources liées** donne les liens des sources citées, avec leur état (confirmée, lecture partielle, illisible…).",
       "- Toutes les sources à vérifier (liens, passages) sont aussi dans `00_SOURCES_A_VALIDER.md` (même dossier).",
       ""]
total = 0
lots = sorted({p.parent.name for p in ECHANGE.glob('01_lots/*/*_ether_reserves_revue_finale.md')} | set(QUESTIONS_CLAUDE))
for lot in lots:
    fs = sorted(ECHANGE.glob(f'01_lots/{lot}/*_ether_reserves_revue_finale.md'))
    items, comp = ([], {})
    for f in fs:
        it, co = lire_reserves(f); items += it; comp.update(co)
    qc = QUESTIONS_CLAUDE.get(lot, [])
    out += [f"## Lot {lot.replace('villes_', 'villes ').replace('-', '.')} — {len(items) + len(qc)} points", ""]
    if fs: out += [f"*Fichier détaillé d'Ether : `01_lots/{lot}/{fs[-1].name}`*", ""]
    idx = index_s(lot)
    for titre, sait, change, choix, libre in items:
        total += 1
        ident = titre.split(' ')[0]
        out += [f"### {titre}", ""]
        if libre: out += [libre, ""]
        if sait: out += [f"- **Ce qu'on sait** : {sait}"]
        if change: out += [f"- **Ce que ça change sur la carte** : {change}"]
        if choix: out += [f"- **Choix possibles** : {choix}"]
        if ident in comp: out += [f"- **Complément d'Ether** : {comp[ident]}"]
        sl = sources_liees(' '.join([titre, sait, change, choix, libre, comp.get(ident, '')]), ident, idx)
        out += (["- **Sources liées** (cliquer pour ouvrir) :"] + sl) if sl else ["- **Sources liées** : aucune citée par identifiant ; voir le fichier détaillé d'Ether ou les sources des villes concernées dans `00_SOURCES_A_VALIDER.md`."]
        out += ["- **Décision de Guizmo** : …", ""]
    for titre, sait, change, choix in qc:
        total += 1
        out += [f"### {titre} *(question de Claude)*", "", f"- **Ce qu'on sait** : {sait}",
                f"- **Ce que ça change sur la carte** : {change}", f"- **Choix possibles** : {choix}"]
        sl = sources_liees(' '.join([titre, sait, change, choix]), titre.split(' ')[0], idx)
        if sl: out += ["- **Sources liées** (cliquer pour ouvrir) :"] + sl
        out += ["- **Décision de Guizmo** : …", ""]
ar = a_renforcer()
out += ["## Villes marquées « À renforcer » (rappel)", "",
        "Ce ne sont pas des décisions à prendre : ce sont des rôles (port, rail, industrie…) dont aucune preuve n'a encore été confirmée par la relecture de Claude. Ils se consolident au fil des lots et de la page « Sources à valider ».", "",
        "| Lot | Villes « À renforcer » | Villes du lot |", "|---|---|---|"]
out += [f"| {k.replace('-', '.')} | {v[0]} | {v[1]} |" for k, v in ar.items()]
out += ["", f"**Total : {total} points à trancher.**", ""]
texte = '\n'.join(out)
(RACINE / 'docs/RESERVES_A_TRANCHER.md').write_text(texte, encoding='utf-8')
(ECHANGE / '00_RESERVES_A_TRANCHER.md').write_text(texte, encoding='utf-8')
print(total, 'points ->', 'docs/RESERVES_A_TRANCHER.md et 00_RESERVES_A_TRANCHER.md')
