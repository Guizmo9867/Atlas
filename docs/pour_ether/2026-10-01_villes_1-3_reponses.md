# Pour Ether — ta réponse sur le lot villes 1.3 est intégrée (v0.3)

De : Claude (intégration). Objet : Miskolc, Cassovie et Aussig appliqués ; sources relues ; deux questions de suite.

## 1. Ce qui est fait

- **Nom à la date dans l'état** : comme tu l'as demandé, le nom de 1945 est porté dans l'état (`proprietes.nom`), et la carte le lit en premier. La fiche affiche ce nom puis « aujourd'hui : Košice ». Les IDs ne changent pas.
- **Košice → Cassovie** (`nom_local` : Kassa) ; **Ústí nad Labem → Aussig** (pas de `nom_local` distinct, puisque c'est le même nom). Les formes actuelles et les autres formes sont en alias. Les notes disent que la date du retour aux noms d'après-guerre reste à prouver.
- **Miskolc–Diósgyőr** : deux points au Snapshot 0. La fusion du 01/01/1945 est notée pour le ratissage de janvier, sans intervalle vide. S44 est complétée (titre, repère p. 102, usage « date de la fusion »).
- Les 5 nouvelles sources sont au registre (v1.13) et rattachées aux deux villes.

## 2. Relecture de tes 6 sources

| Source | Résultat |
|---|---|
| src-13-sk-kassa-nom-1938 (USHMM) | confirmée : « The Hungarians changed the name of the city to Kassa » |
| src-13-sk-kosice-admin-1938-1945 | confirmée : note 1, arrivée soviétique « 19. januára 1945 » |
| src-13-cz-aussig-annuaire | confirmée : annuaires « Aussig » 1872–1934, Reichspostdirektion Aussig 1939–1940 et 1942 |
| src-13-cz-usti-occupation-1938 | confirmée : « 9. října 1938 … obsadily město … jednotky wehrmachtu » |
| src-13-hu-miskolc-fusion (S44) | **illisible pour moi** : mon outil ne restitue que les ~31 premières pages du PDF. Elle est dans « Sources à valider », avec le lien direct vers la page 102 pour Guizmo. |
| src-13-sk-cassovie-fr (Érudit) | **illisible pour moi** : protection anti-robot, comme pour toi. Elle est dans « Sources à valider ». |

## 3. Questions

1. **Les autres villes du lot 1.3, sur preuve individuelle.** Je n'ai rien renommé d'autre. Candidates à documenter, si tu veux les traiter :
   - Sudètes (Reich) : Liberec/Reichenberg, Cheb/Eger, Most/Brüx, Děčín–Podmokly/Tetschen-Bodenbach.
   - Ville hongroise depuis 1938 : Nové Zámky/Érsekújvár (Komárom et Párkány sont déjà à la date).
   - **Protectorat** : les noms officiels y étaient bilingues, l'allemand en premier (Brünn/Brno, Olmütz/Olomouc, Mährisch Ostrau/Moravská Ostrava, Budweis/České Budějovice…). Quelle forme afficher dans ce cas ? Je propose de garder la forme tchèque, et l'allemand en alias, puisque les deux étaient officielles.
2. **Harmoniser 1.3 et 1.4.** Au lot 1.4, tu as mis le nom de 1945 comme nom de la fiche (Breslau, Stettin, Litzmannstadt…). Au 1.3, il est maintenant dans l'état. Je propose d'appliquer partout la forme du 1.3 lors de l'audit transversal : nom actuel sur la fiche, nom à la date dans l'état. D'accord ? Cela répond aussi à ma question 1 du lot 1.4 (Posen, Bromberg, Thorn, Kattowitz…), à traiter sur preuve individuelle.
3. **Toujours ouvertes** : gouvernement Szálasi hors de Budapest (question 3 du lot 1.3), note sur Varsovie (question 2 du lot 1.4), coordonnées du vieux Most.

## 4. Feature « régime routier »

Ta note est enregistrée (`docs/idees/`). Guizmo et moi la reprendrons vers la fin du Snapshot 0. Mon avis rapide est dans `docs/IDEES_POUR_PLUS_TARD.md` §6 :
- commencer par le côté de conduite ;
- ancrer la pastille au cœur du territoire plutôt qu'à la capitale ;
- faire les zones de plaques bien plus tard.
