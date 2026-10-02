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
         "5 liens morts (Arkhangelsk/Kandalakcha/Severodvinsk, Sverdlovsk, Tchernikovsk, Sébastopol, Taganrog) et 6 passages introuvables sur la page citée (Carélie, Belomorsk, Ouglitch, deux tomes militaires sur 1944, Grodno).",
         "Les rôles concernés restent marqués « À renforcer » dans les fiches.",
         "Ether cherche d'autres sources ; ou on garde la réserve visible."),
        ('Q15-04 — Noms des villes de Biélorussie',
         "Certaines fiches ont le nom français (Gomel, Moguilev), d'autres la forme biélorusse (Baryssaw, Stawbtsy).",
         "Rien n'a été changé.",
         "Règle « nom français attesté d'abord, sinon forme locale » comme ailleurs ; ou garder tel quel."),
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
       "- Les **sources** à vérifier (liens, passages) sont à part, dans la page « Sources à valider ».",
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
    for titre, sait, change, choix, libre in items:
        total += 1
        ident = titre.split(' ')[0]
        out += [f"### {titre}", ""]
        if libre: out += [libre, ""]
        if sait: out += [f"- **Ce qu'on sait** : {sait}"]
        if change: out += [f"- **Ce que ça change sur la carte** : {change}"]
        if choix: out += [f"- **Choix possibles** : {choix}"]
        if ident in comp: out += [f"- **Complément d'Ether** : {comp[ident]}"]
        out += ["- **Décision de Guizmo** : …", ""]
    for titre, sait, change, choix in qc:
        total += 1
        out += [f"### {titre} *(question de Claude)*", "", f"- **Ce qu'on sait** : {sait}",
                f"- **Ce que ça change sur la carte** : {change}", f"- **Choix possibles** : {choix}",
                "- **Décision de Guizmo** : …", ""]
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
