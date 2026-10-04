# Atlas Eurasie — consignes pour Claude

Avant tout travail dans ce dépôt, lire **`docs/REPRISE.md`** (fiche de reprise : le projet, qui fait quoi, les règles, l'état actuel).
Ne lire le reste (`docs/JOURNAL_DECISIONS.md`, `docs/BOUCLE_AUTOMATIQUE.md`…) que si la tâche le demande.

En bref :
- Guizmo, le porteur du projet, a un niveau technique très faible : lui répondre en français simple, étape par étape, sans jargon.
- Jamais de secret dans le dépôt (il est public) ; jamais de données OSM/ODbL ; ne rien supprimer sans son accord.
- Ne pas modifier l'interface (`app/src`) sans décision de Guizmo ; le validateur `node app/scripts/validate-data.mjs` doit finir sans erreur.
- Les décisions vont dans `docs/JOURNAL_DECISIONS.md` (une section datée en haut).
- Une session cloud ne voit pas le dossier d'échange du Bureau (livraisons d'Ether) : elle travaille seulement sur ce qui est dans le dépôt, et ne doit pas tourner en même temps que la boucle automatique (la mettre en pause avant).
