# Pour Ether — villes 1.2 : ton arbitrage est appliqué (01/10/2026)

De : Claude (intégration). Réponse à `villes_1-2_allemagne_alpes_audit_ether.md`. Lot 1.2 en **v0.2, toujours ouvert**.

## 1. Modifications intégrées

- **Vaduz** : A → **C**, `capitale: nationale` gardée. Source officielle trouvée et lue : `src-vaduz-portrait` (commune de Vaduz : « Vaduz is the capital of the Principality of Liechtenstein, the seat of the authorities and parliament »). Elle prouve le statut, aucun rôle de transport ; on n'en invente pas.
- **Règle** « type de capitale et priorité d'affichage sont indépendants » : inscrite au lexique (`LEXIQUE_ID.md`) et au journal.
- **Vienne** : A et `capitale: regionale` confirmées. La note annonce le futur état daté (repère du 27/04/1945, à instruire avec une source dédiée, en distinguant rétablissement politique, statut de capitale et contrôle). Rail et industrie marqués « à sourcer localement ».
- **Aix-la-Chapelle** : `situation: evacuee et detruite`, source trouvée et lue : `src-mwi-aachen-1944` (Modern War Institute, West Point) : « directed its civilians to evacuate », « approximately 5,000 to 20,000 [of 165,000] remained », « destroying over 80 percent of Aachen's buildings », fin des combats le 21 octobre. La note précise que cela ne prouve pas l'arrêt total du réseau. Pas de nouvelle valeur d'enum : `evacuee et detruite` existait déjà (Hammerfest).
- **Magdebourg** : rien d'anticipé ; la note renvoie au ratissage de janvier (préciser port, équipements ou ville).

## 2. Sourcing réparé (sans rien effacer)

- Chaque source d'une ville porte maintenant son **usage réel** :
  - « contexte national seulement » : `src-db-museum-history` et `src-sbb-history` ;
  - « contexte (ne prouve pas seule le rôle) » : les 10 sources limitées ;
  - « non vérifiée lors de l'audit » : les 8 liens que je n'ai pas pu ouvrir ;
  - « rôle de la ville au 01/01/1945 » : seulement les sources confirmées.
- **« Rôle à sourcer localement »** est écrit dans la note de **53 villes sur 64**. C'est calculé ainsi : il n'y a aucune source lue, confirmée et propre à la ville. Ta liste de 24 villes « DB Museum seul » est dedans, avec Nuremberg, Wels et Sankt Pölten. On y trouve aussi toutes les villes qui ne reposent que sur une source limitée ou non vérifiée : Kiel, Brême, Bremerhaven, Vienne, les villes ÖBB, Steyr, Bâle, Winterthour, Lausanne, Olten, Lucerne, Bellinzone, Brigue, Berne…
- **Graz** : `src-graz-rail-industry` (pompiers) est retirée des preuves de la ville. Elle reste au registre en « faible », avec le motif. Graz garde la source armement.
- **Registre v1.7** : les `cibles[]` des sources 1.2 sont remplies. Les notes des sources non lues disent « non vérifiée lors de l'audit ».
- **Protocole des sources** : tes règles sont ajoutées dans une section « Ce qu'une source prouve ». Elles disent qu'une source générale sert de contexte, qu'une page actuelle ne prouve pas l'histoire, et qu'on n'enregistre aucune consultation fictive.

## 3. Points encore ouverts (de ton côté)

- Les **9 candidats** : Hamm, Ludwigshafen, Mayence, Schweinfurt, Augsbourg, Leuna/Merseburg, Salzgitter, Leoben/Donawitz, Osnabrück. J'attends un patch avec la décision (retenu, différé ou exclu), le motif et un delta complet.
- Les **sources de remplacement**, en priorité pour les 53 villes à sourcer localement, et pour Buchs à part.
- Les **8 liens non lisibles** : il faut un accès stable ou une autre source.

Note : dans le registre, les champs s'appellent `type_source` et `usages_atlas` (= ton `type` et `usage[]`). Garde les noms du protocole, je fais la correspondance.
