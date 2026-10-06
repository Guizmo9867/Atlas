# Réponse finale à Q19-03 — villes 1.9, cycle 3

6 octobre 2026 — Ether, Codex fondé sur GPT-6 ; aucun sous-agent. Dernier cycle autorisé, consacré aux sources de l’audit des villes 1.x. L’audit géographique est déjà livré ; aucune autre couche n’est ouverte.

Le compte rendu du 06/10 et le PRET de fin de Claude sont reçus. Q19-01 et Q19-02 sont closes ; leurs réserves restent à la revue finale. Cherbourg « base navale » n’est pas réintroduit. Les corrections Horta/Senglea et le vocabulaire de `usages_atlas` sont conservés.

La présente remise comporte **8 compléments de sources existantes**, **19 relations existantes à préciser sur 17 villes**, **15 captures originales** et **3 transcriptions de chapitres de l’U.S. Army** pour la recherche dans le texte. **Deux dossiers restent en réserve** : Hendaye frontalier et la pièce de Jeumont. Rien n’est déclaré confirmé par Claude avant sa relecture.

## Lecture et intégration

- `2026-10-06_ether_sources_reponses_cycle3_delta.json` : fusion additive, mêmes IDs ; conserver les autres cibles, passages, avis et validations.
- `2026-10-06_ether_corrections_cycle3.json` : relations déjà présentes, à enrichir sans les dupliquer. Les rôles, rangs, noms, positions et dates d’état restent inchangés.
- `2026-10-06_ether_index_preuves_cycle3.json` : URL, portée, fichiers et empreintes. Les trois essais/échecs exclus y sont signalés ; notamment le HTML Jeumont n’est pas son PDF.
- `2026-10-06_ether_reserves_complement_cycle3.json` et `2026-10-06_ether_index_reserves_avant_dernier_retour.json` : deux compléments, 301 dossiers au total avec les 299 historiques conservés. Ce total n’est pas un nombre d’erreurs indépendantes.

Après lecture seulement, lever « lecture partielle » ou « À renforcer » pour les rôles effectivement démontrés par les pièces. Ne pas supprimer une réserve de capacité/service, ni le signalement d’autres rôles non prouvés d’une même ville.

Les captures restent des pièces de lecture locales, hors dépôt public, conformément à la remise précédente. Les transcriptions de l’U.S. Army servent à retrouver les passages des ouvrages du domaine public ; elles ne remplacent pas la relecture des captures.

## 1. Ruppenthal, Logistical Support of the Armies, I, chapitre III

Source : `src-audit1x-ruppenthal-i3` — https://www.ibiblio.org/hyperwar/USA/USA-E-Logistics1/USA-E-Logistics1-3.html

Localisateur : I, chapitre III, §3 organisation des zones p.144–145 ; §4 Troop and Cargo Reception p.146–147 (pagination imprimée reproduite dans le HTML).

Les ports sont nommés dans le zonage de 1943 puis dans la réception américaine avant fin mai 1944. Glasgow appartient au groupe de la Clyde, Cardiff à celui du canal de Bristol, Liverpool et Manchester à celui de la Mersey ; Hull, Londres, Southampton et Plymouth sont mentionnés avec leur usage accru à partir de fin 1943.

Limites : Le localisateur précédent p.145–147 omettait p.144. Les tonnages et débarquements des groupes de ports ne sont pas attribuables à chaque ville. Aucune capacité ou continuité locale au 01/01/1945 déduite.

Pièces : [ruppenthal_i3_p144.jpg](2026-10-06_ether_C3_ruppenthal_i3_p144.jpg), [ruppenthal_i3_p146.jpg](2026-10-06_ether_C3_ruppenthal_i3_p146.jpg), [ruppenthal_i3_p147.jpg](2026-10-06_ether_C3_ruppenthal_i3_p147.jpg).

## 2. Ruppenthal, Logistical Support of the Armies, II, chapitre IV

Source : `src-audit1x-ruppenthal-ii4` — https://www.ibiblio.org/hyperwar/USA/USA-E-Logistics2/USA-E-Logistics2-4.html

Localisateur : II, chapitre IV, §3 Southern France, p.122–123.

Marseille : premier Liberty déchargé directement à quai le 15 septembre 1944. Toulon : utilisation à partir du 20 septembre ; décision de restitution aux Français fin octobre, emploi ensuite presque exclusivement pour les approvisionnements civils.

Limites : Les statistiques agrégées incluant janvier 1945 ne décrivent pas le Snapshot 0. Ne pas attribuer les totaux régionaux à une ville. Aucun changement demandé pour Le Havre, Rouen et Anvers déjà confirmés.

Pièces : [ruppenthal_ii4_p122.jpg](2026-10-06_ether_C3_ruppenthal_ii4_p122.jpg), [ruppenthal_ii4_p123.jpg](2026-10-06_ether_C3_ruppenthal_ii4_p123.jpg).

## 3. Ruppenthal, Logistical Support of the Armies, II, chapitre V

Source : `src-audit1x-ruppenthal-ii5` — https://www.ibiblio.org/hyperwar/USA/USA-E-Logistics2/USA-E-Logistics2-5.html

Localisateur : II, chapitre V, §2 The Railways, p.148–149, 155–156 ; §4 Inland Waterways, p.166.

Fin septembre 1944, les lignes à l’est de Paris passent par Charleroi et Namur vers Liège. Lyon accueille le quartier général ferroviaire le 14 septembre ; la ligne y est ouverte le 25, et fonctionne jusqu’à Dijon à la fin du mois. Les premières barges de charbon arrivent à Paris le 18 novembre 1944. Un pont ferroviaire sur la Meuse à Namur est détruit le 24 décembre 1944 et ne rouvre que le 5 janvier 1945.

Limites : La réouverture du 5 janvier et la fin du goulet de Liège fin janvier sont postérieures au Snapshot. La destruction concerne un pont de Namur, pas toute la ville ni tout son trafic. La photographie du canal Albert datée février 1945 sous p.166 ne sert pas de preuve au Snapshot. Le rôle port_fluvial de cette réponse concerne seulement Paris.

Pièces : [ruppenthal_ii5_p148.jpg](2026-10-06_ether_C3_ruppenthal_ii5_p148.jpg), [ruppenthal_ii5_p149.jpg](2026-10-06_ether_C3_ruppenthal_ii5_p149.jpg), [ruppenthal_ii5_p155.jpg](2026-10-06_ether_C3_ruppenthal_ii5_p155.jpg), [ruppenthal_ii5_p156.jpg](2026-10-06_ether_C3_ruppenthal_ii5_p156.jpg), [ruppenthal_ii5_p166.jpg](2026-10-06_ether_C3_ruppenthal_ii5_p166.jpg).

## 4. Gares et réseau ferré — Tours, Rennes, Limoges et Lyon Perrache

Source : `src-audit1x-fr-tours` — https://patrimoine.sncf.com/gares-et-reseau-ferre/

Localisateur : Sections Gare de Limoges ; Le poste d’aiguillage de Lyon Perrache (ligne PLM).

La gare de Limoges est inaugurée en 1929 ; le poste d’aiguillage de Lyon-Perrache est achevé en 1934.

Limites : Rôle ferroviaire historique seulement, sans certification du service au Snapshot. La modernisation de 1952 est future. Tours et Rennes, déjà confirmées, ne sont pas rouvertes.

Pièces : [sncf_limoges.jpg](2026-10-06_ether_C3_sncf_limoges.jpg), [sncf_lyon_perrache.jpg](2026-10-06_ether_C3_sncf_lyon_perrache.jpg).

## 5. Histoire du port de Bastia

Source : `src-audit1x-fr-bastia` — https://bastia-port.cci.corsica/histoire/

Localisateur : Frise Entre-deux-guerres : trois cartes 1920, 1943 et Décembre 1944, visibles ensemble dans la capture.

La concession du port à la Chambre de commerce est datée de 1920 ; les bombardements de 1943 détruisent presque toutes les installations ; en décembre 1944 trois épaves encombrent encore le port (Tibériade, Sidi Mabrouk, Mont Agel).

Limites : L’état endommagé n’équivaut pas à une preuve de fermeture totale. Ne pas anticiper les installations de 1975.

Pièces : [bastia_1920_1944.jpg](2026-10-06_ether_C3_bastia_1920_1944.jpg).

## 6. La gare — Dijon

Source : `src-audit1x-fr-dijon` — https://www.caue-observatoire.fr/ouvrage/gare-dijon-observatoire-des-caue/

Localisateur : Description architecturale : premier paragraphe, inauguration Paris–Dijon en 1851 et destruction de la gare en 1944.

La gare est construite après l’inauguration de la ligne Paris–Dijon en 1851 et détruite par les bombardements alliés en 1944.

Limites : Destruction de la gare, pas de toute la ville. Les bâtiments de 1947–1962 sont futurs. Le fonctionnement de la ligne jusqu’à Dijon en septembre 1944 est documenté séparément par Ruppenthal II-5.

Pièces : [dijon_caue.jpg](2026-10-06_ether_C3_dijon_caue.jpg).

## 7. Le Connecting Europe Express fait escale à Hendaye, 4 septembre2021

Source : `src-audit1x-fr-hendaye` — https://www.hendaye.fr/fr/le-connecting-europe-express-fait-escale-a-hendaye/

Localisateur : Discours du maire de septembre 2021 : premier paragraphe historique, arrivée du train Madrid–Paris le 15 août 1864.

La page date explicitement une arrivée ferroviaire Madrid–Paris à Hendaye du 15 août 1864 ; elle fournit déjà la preuve ferroviaire admise par Claude.

Limites : Les phrases sur les deux pays et les ponts de la Bidassoa appartiennent au discours de 2021 ; elles ne datent pas un rôle frontalier ou douanier au Snapshot. Aucun renforcement du rôle frontalier proposé. Deux pistes municipales supplémentaires ont répondu 403 : non utilisées comme preuves.

Pièces : [hendaye_1864.jpg](2026-10-06_ether_C3_hendaye_1864.jpg).

**R19-C3-01 maintenue pour Guizmo**, sans nouvelle recherche automatique après ce cycle.

## 8. Présentation de la commune de Jeumont, dossierIA59001366

Source : `src-audit1x-fr-jeumont` — https://inventaire.hautsdefrance.fr/dossier/pdf/b944ab33-b2bb-4e71-8025-c755a10609ca/presentation-de-la-commune-de-jeumont.pdf

Localisateur : PDF annoncé de 17 pages, p.1, Historique ; dossier IA59001366. Texte du cache Web lu, original PDF local non obtenu.

Le texte de p.1 fourni par le cache Web évoque la ligne Paris–Erquelinnes en 1855, l’agrandissement de la gare vers 1881, l’industrie électrique, la métallurgie et des logements FACEJ de 1932.

Limites : Aucune capture authentique ni PDF local utilisable obtenu : la requête directe renvoie une page de contrôle d’accès, et la capture Web échoue. Ne pas présenter ce cache textuel comme une nouvelle vérification par Claude. La verrerie déplacée à Boussois et les logements ferroviaires de Marpent ne prouvent pas ces fonctions dans Jeumont en 1945.

**R19-C3-02 maintenue pour Guizmo**, sans nouvelle recherche automatique après ce cycle.

## Point de chronologie à conserver

La note proposée pour **Namur** est limitée à un pont ferroviaire sur la Meuse : destruction le 24 décembre 1944, toujours hors service au Snapshot ; la réouverture du 5 janvier 1945 appartient au futur. Le rôle ferroviaire historique de la ville n’implique pas un réseau entièrement opérationnel. Cette limite est dans le JSON de corrections.

## État de vérification et fin de boucle

Contrôle direct en lecture du canon reçu : **1 559 villes, 887 sources**, pas de doublon d’ID de ville. Le validateur à zéro erreur et l’envoi GitHub au commit `40d1e03` sont les annonces de Claude, pas des contrôles distants effectués par Ether. La présente remise reste une proposition locale jusqu’à sa relecture/intégration.

Merci de déposer le dernier compte rendu et le PRET de fin, avec les confirmations et réserves effectivement retenues. **Aucun quatrième cycle automatique.** Les points non conclusifs rejoindront le bilan final, sans demande au cas par cas. À réception de ce dernier retour : bilan et index final, phase `villes_terminees_attente_guizmo`, puis arrêt vérifié du réveil d’Ether. Aucune autre famille ni progression dans les mois sans choix et feu vert explicites de Guizmo. La planification propre à Claude demeure sous son contrôle.
