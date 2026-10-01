# Snapshot 0 — villes, ratissage 1.2 : Allemagne + arc alpin

Fichier : `villes_1-2_allemagne_alpes.json` (v0.2, 64 villes : Allemagne actuelle 33, Autriche actuelle 14, Suisse 15, Liechtenstein 2), intégré par Claude le 01/10/2026 à partir de la proposition d'Ether (`data/sources/deltas_ether/2026-10-01_villes_1-2_allemagne_alpes_proposition_ether.json`, brief : `villes_1-2_allemagne_alpes_brief_ether.md`).

- Même modèle que les lots 1.0 et 1.1 : `importance_atlas` A/B/C/D (affichage automatique par le zoom), `roles` en mots-clés, phrase d'Ether en `note`, `nom_local` et `aliases`.
- **Rôles** ramenés au vocabulaire de l'Atlas (aucun rôle nouveau) : Danube, Elbe, Rhin → `port_fluvial` ; corridors alpins, Brenner, nœud intérieur, fret → `rail` ; automobile, mécanique, chimie → `industrie`. Commerce, lac, front restent dans la note. Schaffhouse : pas de port (chutes du Rhin).
- **Capitales** : Berlin, Berne, Vaduz = nationales ; Vienne = régionale au 01/01/1945 (Autriche annexée). Vaduz est en priorité C : type de capitale et priorité sont indépendants.
- **Situation** : Aix-la-Chapelle « évacuée et détruite » au 01/01/1945 (source MWI, West Point).
- **Retour d'audit d'Ether (01/10)** : `villes_1-2_allemagne_alpes_audit_ether.md`. Le lot reste **ouvert** : 9 candidats à l'ajout et sources de remplacement attendus.
- **Rôle à sourcer localement** : écrit dans la note de chaque ville (53) sans source lue qui prouve son rôle. L'`usage` de chaque source dit ce qu'elle prouve vraiment (« contexte seulement », « non vérifiée lors de l'audit »).
- **Positions** : Wikidata (CC0), QID en locator (`outils/villes/wikidata_ratissage_1_2.json`), vérifiées contre Natural Earth.
- **Sources des rôles** : delta d'Ether fusionné au registre (v1.6, puis v1.7) après lecture de chaque lien ; `verification_claude` dit ce qui est confirmé (15), limité (11) ou non vérifié (8).
- Reportées volontairement à leur lot géographique : Breslau, Stettin, Königsberg, Dantzig.

Script rejouable : `outils/villes/construire_villes_1_2.py`. Questions : `docs/pour_ether/2026-10-01_villes_1-2.md`.
