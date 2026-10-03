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
         "5 liens morts (Arkhangelsk/Kandalakcha/Severodvinsk, Sverdlovsk, Tchernikovsk, Sébastopol, Taganrog) et 6 pages que l'outil de Claude ne lit qu'en partie (Carélie, Belomorsk, Ouglitch, deux tomes militaires sur 1944, Grodno). Le 03/10, Ether a retrouvé les passages dans son navigateur ; la relecture de Claude bute toujours sur les mêmes pages. Soumy est désormais confirmée (page 353 du recueil).",
         "Les rôles concernés restent marqués « À renforcer » dans les fiches.",
         "Accepter la lecture d'Ether pour ces 11 sources ; Ether fournit des copies lisibles (images de pages) ; ou on garde la réserve visible."),
        ('Q15-04 — Noms des villes de Biélorussie',
         "Certaines fiches ont le nom français (Gomel, Moguilev), d'autres la forme biélorusse (Baryssaw, Stawbtsy).",
         "Rien n'a été changé.",
         "Règle « nom français attesté d'abord, sinon forme locale » comme ailleurs ; ou garder tel quel."),
    ],
    'villes_1-6': [
        ('Q16-01 — Sources du lot 1.6 à remplacer ou préciser',
         "6 liens morts (Rosmorport Primorié et Petropavlovsk, histoire de Novossibirsk 1920-1940, ONIIP Omsk 1942, usine BVRZ, Maxam Tchirtchik) et 6 pages lisibles où le passage cité n'a pas été trouvé (Vayner ch. 4, Mongolie LoC 1991, archives du Primorié sur Spassk, Vichnevski Sakhaline 2000, Providenia 2022, petites villes du Kazakhstan 2011).",
         "Les rôles concernés restent marqués « À renforcer ».",
         "Ether donne une autre source ou l'adresse exacte du passage ; ou on garde la réserve visible."),
        ('Q16-02 — Répertoires administratifs illisibles pour Claude',
         "Les répertoires officiels de 1940, 1941 (Tadjikistan, Turkménistan) et le supplément de 1944 sont de gros PDF ou des pages de bibliothèque que l'outil de Claude ne lit pas. Claude a lu lui-même deux pages du supplément de 1944 (Astrakhan, Kemerovo et le Kouzbass) : elles concordent avec Ether.",
         "225 des 254 villes du lot gardent au moins un rôle « À renforcer » (surtout rail et administration), sans que la fonction soit mise en doute.",
         "Ether indique pour chaque ville l'adresse de l'image de la page (comme pour le supplément de 1944) ; ou on accepte ces répertoires comme preuve sur la lecture d'Ether."),
        ("Q16-03 — Noms « de 1945 » qui ne sont qu'une autre transcription",
         "Sur les 89 villes du lot affichées sous un nom de 1945, une cinquantaine ne changent que l'orthographe (Tokmok/Tokmak, Farap/Farab, Kara-Suu/Kara-Sou, Balkhash/Balkhach…) ; plusieurs fiches portent une forme locale ou anglaise plutôt que française (Sulukta, Baýramaly, Yangiyo‘l, Mandalgovĭ, Nalayh). Les vrais changements de nom (Frounzé, Stalinabad, Alma-Ata, Stalinsk, Akmolinsk, Djibkhalantou…) sont bien prouvés à part.",
         "Gardé tel que proposé par Ether ; seules Nikolaïevsk et Komsomolsk-sur-l'Amour (différence d'apostrophe) ne sont plus affichées comme renommées.",
         "Une règle unique de transcription française pour toute la série (comme Q15-04) : la fiche prend la forme française, et le nom de 1945 n'est affiché que s'il s'agit d'un autre nom ; ou garder tel quel."),
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
