"""Preuves relues par Claude ville par ville (04/10/2026).

Certaines sources ne sont lisibles qu'en partie par l'outil de Claude, mais Claude a lu lui-même la page utile pour
certaines villes (images de pages de répertoires administratifs, captures déposées par Ether). Le registre garde alors
un statut de source « limite » (lecture partielle) et note, dans `confirmations_claude`, les villes et les rôles
effectivement relus :
    "confirmations_claude": {"ville-tm-mary": {"roles": ["administration", "rail"], "lecture": "...", "date": "2026-10-04",
                                              "verification": "data/sources/verifications_claude/2026-10-04_villes_1-6_cycle2.json"}}
`roles` vaut "usage" quand la page relue prouve tout ce que la ville attend de cette source.
Les constructeurs de lots (construire_villes_1_5/1_6/1_7.py) comptent ces rôles comme prouvés pour CETTE ville seulement
et écrivent la mention MENTION au lieu de « (lecture partielle) ».
"""
MENTION = ' (page relue par Claude pour cette ville)'
MENTION_PARTIELLE = ' (page relue par Claude pour cette ville : {roles})'


def confirmation(fiche, entite_id):
    """Renvoie (roles, mention) : roles = None (rien), 'usage' (tous les rôles de l'usage) ou un ensemble de rôles."""
    c = (fiche or {}).get('confirmations_claude', {}).get(entite_id)
    if not c:
        return None, None
    if c['roles'] == 'usage':
        return 'usage', MENTION
    return set(c['roles']), MENTION_PARTIELLE.format(roles=', '.join(c['roles']))
