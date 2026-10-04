# Villes 1.6 — compte rendu de Claude sur tes réponses (cycle 2)

*04/10/2026, réveil automatique de Claude. Livraison lue : `01_lots/villes_1-6/` (PRET_ether du 03/10 à 17 h 13 : `2026-10-03_ether_reponses_cycle2.md`, réponse par source Q16-01, index des pages administratives Q16-02 en .md et .json, delta de 17 compléments, complément de réserves). Remise commune avec 1.5 (cycle 3) et 1.7 (cycle 1).*

## 1. Intégré

- **17 compléments de sources** fusionnés (registre **v1.21**, `outils/villes/fusion_sources_1_6_reponses.py`) : union des cibles et usages, ton localisateur repris (l'ancien gardé dans les notes), `complement_ether_cycle2_documentaire` conservé. Les usages ajoutés pour le 1.7 sur les mêmes sources sont fusionnés à part (compte rendu 1.7), sans remplacer ceux-ci.
- **Q16-02 — répertoires administratifs** : j'ai fait lire les **28 images de pages** de ton index (1941 Kirghizie, Tadjikistan, Turkménistan ; supplément de 1944 ; répertoire de 1940). **67 relations ville/source relues, 63 confirmées ville par ville** (capitale, centre d'oblast ou de raïon, gare homonyme ou à 0 km). Exemples : Frounzé capitale et centre d'oblast p. 296/301 ; Kemerovo, Tomsk, Tioumen, Kourgan, Termez (centre d'okroug 1940, p. 261)… Ces villes ne sont plus « À renforcer » pour ces rôles ; leurs fiches disent « (page relue par Claude pour cette ville) ». Les 57 autres relations n'ont qu'une adresse de lecteur en ligne, que mon outil ne lit pas : elles restent en lecture partielle.
- Les statuts des répertoires 1940, 1941 Tadjikistan et Turkménistan passent de « illisible » à « lecture partielle ».
- **Livre LOC sur la Mongolie** : les 3 images (pages 6, 137, 164) confirment Oulan-Bator (combinat 1934), Nalaïkh (charbon, voie de 1938) et la liaison Tchoïbalsan–Borzia (1939). Statut : lecture partielle, villes relues notées une à une.
- Lot 1.6 reconstruit en **v0.2** : aucune ville, aucun nom, aucun rôle modifié. « À renforcer » : **176 villes** (225 avant).

## 2. Corrigé

- 5 sources passent de « faible » à « **non vérifiée** » : la relecture montre que mon outil n'atteint pas le passage (texte tronqué ou page d'accueil), le passage n'est donc pas absent : Vayner ch. 4 (s'arrête en 1943), archives du Primorié (menu seul), Vichnevski (s'arrête avant l'oblast de Sakhaline), Providenia (page d'accueil du journal), petites villes du Kazakhstan (PDF lu jusqu'à la p. 33).
- Ton contrôle de pagination (numéros imprimés distincts des indices d'image) est juste sur toutes les images relues.

## 3. Questions encore ouvertes

- **Q16-01** : tes adresses et localisateurs sont précis, mais mon outil répond toujours « 404 » aux 6 liens (Rosmorport Primorié et Petropavlovsk, Novossibirsk 1920-1940, ONIIP Omsk, BVRZ, Maxam Tchirtchik) alors que tu les lis dans ton navigateur, et 5 pages restent tronquées. Ce n'est pas un doute sur toi : c'est la limite de l'outil. Ce qui marche : **des captures des passages** (comme pour le 1.5, cycle 3). Sinon la réserve reste visible ; Guizmo peut aussi valider ces liens sur la page « Sources à valider ».
- **Q16-02** : 63 relations confirmées sur image. Pour les 57 autres, déposer les images des pages (même méthode que les 28 premières).
- **Q16-03** : en réserve pour la revue finale (avec Q15-04) ; le 1.7 ajoute quelques cas en Azerbaïdjan (voir son compte rendu).
- Q15-02 : en réserve, sans changement (aucun type de capitale RSSA/oblast imposé).

## 4. Réserves de source

- R16-01 à R16-69 gardées pour la revue finale 1.x, sans modification ; 49 candidats différés toujours non importés.
- Points relevés à la lecture des images, à garder en tête (aucun changement fait) : Khanty-Mansiïsk est un « рп » (bourg ouvrier) en 1944, pas un « г. » ; Asino est « с. » (village) avec gare à 0 km ; Anjero-Soudjensk, Kisselevsk, Stalinsk, Leninsk-Kouznetski et Prokopievsk ont leur gare à 0 km sous un autre nom (Анжерская, Акчурла, Новокузнецк, Кольчугино, Усяты) ; Kerki a sa gare (Керкичи) à 2 km ; Tachkent : capitale lue p. 259, le tableau p. 264 n'était pas sur l'image.

## 5. Décisions attendues de Guizmo

Aucune pendant la série 1.x.

## 6. Qualité de la livraison

- **Moteur** (selon PRET_ether) : Codex, fondé sur GPT-6 ; variante et effort non exposés ; aucun sous-agent.
- **Sources relues** : 17 ; Q16-01 : 1 relue en partie (LOC, sur image), 5 tronquées par l'outil, 6 liens « 404 » pour l'outil ; Q16-02 : 63 relations ville/source confirmées sur 67 relues.
- **Affirmations introuvables** : 0 sur les images lues. **Champs pas en français** : 0. **Manques au protocole** : aucun.
- **Corrections de Claude** : 5 statuts « faible » → « non vérifiée ». L'index des pages (fichier, page imprimée, empreinte) a rendu la vérification rapide et sûre : excellente méthode.
