# 2.SE — réserves cycle 1

## R2SE-01 — Portée des contours

Contours historiques reconstruits, périodes annuelles et généralisation d’origine ; comparaison aux superficies SCB et inspection régionale effectuées, sans validation cadastrale exhaustive. Des écarts de 0,01 à 2,25 % environ subsistent hors Stockholm.

Effet : 23 contours provisoires proposés ; aucun calage arbitraire sur les pays voisins.

## R2SE-02 — Stockholm ville et län

La couche county donne une ville de 192,53 km² contre 142,78 km² au tableau SCB. Une couche municipal 1916–1948 donne 147,25 km² ; elle ne suffit pas à certifier les limites et le complément du län. Spånga ne doit entrer qu’après 1945.

Effet : Les deux contours county restent livrés ne_pas_integrer pour examen ; fiches conservées, aucun faux lien. Aucun redécoupage automatique.

## R2SE-03 — Étiquettes modernes dans histmaps

Les géométries 12499, 12507, 12537 portent Skåne, Västra Götalands, Dalarnas ; leur extension et période sont historiques. Le tableau 1945 impose Malmöhus, Göteborgs och Bohus, Kopparbergs.

Effet : Correspondance explicite dans la preuve ; aucune fusion de Kristianstad/Malmöhus ou des comtés occidentaux.

## R2SE-04 — Traçabilité de la licence d’origine

Johan Junkka déclare explicitement CC0 pour les données suédoises Riksarkivet dans README et rapport technique ; notice originale non retrouvée au catalogue officiel actuel. Le logiciel MIT et les données européennes MPIDR ont des régimes distincts.

Effet : CC0 reconnue et retenue pour les données suédoises ; preuve du redistributeur conservée, limite documentaire signalée sans refuser cette licence acceptée. Pas de données MPIDR utilisées.

## R2SE-05 — Codes, chefs-lieux et échelon inférieur

L’annuaire distingue län, communes, ressorts judiciaires, fögderier fiscaux, conseils généraux et divisions ecclésiastiques. Le jeu SIG donne des centres et codes non datés spécifiquement de 1945.

Effet : Un seul niveau général retenu ; aucun code ni chef_lieu_propose. Pas de communes ordinaires ou de systèmes spécialisés ajoutés. Complément de sièges seulement sur preuve datée.

## R2SE-06 — Topologie de la reconstruction

Auto-intersections de Södermanland, Malmöhus, Värmland réparées par make_valid avec variation de surface inférieure à 0,02 m² chacune. Chevauchement Jönköping/Älvsborg d’environ 0,838 km² dans les données d’origine.

Effet : Réparations enregistrées ; chevauchement conservé et signalé pour relecture, sans attribuer arbitrairement la bande à un comté.
