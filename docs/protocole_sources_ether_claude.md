# Protocole sources — Atlas Eurasie

## Principe

Le dépôt **Atlas** géré par Claude reste la **source de vérité**. Ether ne maintient pas un second registre canonique parallèle.

À partir de maintenant, chaque ratissage ou recherche qui introduit de nouvelles sources doit produire un **delta de sources transférable à Claude**, avec les URL brutes et les relations vers les objets concernés.

## Fichiers à produire par lot

- `atlas_<lot>_...json` : données proposées.
- `atlas_registre_sources_<lot>_delta.json` : uniquement les sources nouvelles / à fusionner.
- éventuellement `atlas_<lot>_pour_claude.md` : décisions, incertitudes, géométries et points à valider.

## Structure minimale d'une source

Chaque entrée doit contenir :
`source_id`, `niveau`, `type_source`, `titre`, `institution`, `url`, `date_consultation`, `cibles[]`, `usage[]`, `locator`, `note`.

## Règle anti-chaos

Une source trouvée ne doit pas rester uniquement dans une citation de chat.

Dès qu'elle sert à créer une entité, justifier un rôle, tracer une géométrie, dater un changement, raconter un événement ou définir un flux, elle doit entrer dans le delta de sources du lot correspondant.

Claude fusionne ensuite le delta au registre officiel et remplace les IDs provisoires par les IDs canoniques existants en cas de doublon.

## Ce qu'une source prouve (audit villes 1.2, 01/10/2026)

- Une source générale (histoire du rail d'un pays, d'une compagnie) sert au **contexte** ; elle n'est jamais la seule preuve d'un rôle local (port, industrie, nœud, militaire).
- La source doit établir le rôle **avant la date représentée** : une page officielle qui décrit la situation actuelle ne vaut pas preuve historique. Le niveau ne découle pas du seul caractère officiel du site.
- Le `locator` doit permettre de retrouver le passage ; `usage[]` dit ce qui est démontré (rôle, nom, statut, situation, date de changement).
- Une source qu'on n'a pas pu lire reste « non vérifiée » : son contenu n'est pas présenté comme confirmé. On n'enregistre jamais une consultation qui n'a pas eu lieu, et on n'efface pas une réserve pour qu'un lot paraisse complet.
- Dans les fichiers de villes, l'`usage` de chaque source le dit (« contexte seulement », « non vérifiée lors de l'audit »), et la note porte « Rôle à sourcer localement » tant qu'aucune source lue ne prouve le rôle.

## Important

Les citations enrichies de ChatGPT sont pratiques pour lire une réponse, mais elles ne sont pas notre archivage de provenance : lors d'un copier-coller vers Claude, leurs URL peuvent disparaître.

Les fichiers `*_sources_*_delta.json` deviennent donc le canal officiel Ether → Claude pour les sources.
