// PALETTES — la couleur n'existe QUE ici, jamais dans les données historiques.
// Chaque mode de lecture associe des identifiants sémantiques (souverainete_id, controle_id…) à une couleur.
// Les identifiants viennent de docs/LEXIQUE_ID.md.
import type { ModeLecture } from '../types'

type Palette = Record<string, string>

const ACTEURS: Palette = {
  // réels
  urss: '#b5534b', finlande: '#4f7cac', republique_de_chine: '#c9a13a', republique_populaire_mongole: '#8a6fb0',
  allemagne: '#44444c', autriche: '#c49a6c', pologne: '#6f9f5f',
  danemark: '#a8505a', feroe: '#7a9a8a', norvege: '#4a6f9a', suede: '#d2b04c', islande: '#6fa3b8', royaume_uni: '#7d3c5a', couronne_britannique: '#9a5a7a',
  irlande: '#5f9a5a', france: '#5a6fb0', belgique: '#c98b3a', luxembourg: '#8fb3d1', pays_bas: '#d9822b', etats_unis: '#3d5a80',
  espagne: '#c9a24a', portugal: '#6f9a6a', andorre: '#9a7a5a', suisse: '#b84a4a', monaco: '#b06a8a', vatican: '#d8c06a', italie: '#4f8a6a',
  republique_sociale_italienne: '#5a5a3a', allies_occidentaux: '#3d5a80', tchecoslovaquie: '#5a7ab0', hongrie: '#7a8a4a', roumanie: '#b09a3a',
  bulgarie: '#6a9a7a', yougoslavie: '#8a5a8a', partisans_yougoslaves: '#a04a4a', albanie: '#9a3a3a', grece: '#4a8ab0', turquie: '#b04a3a',
  // fictifs (prototype)
  ruritanie: '#4f7cac', kovalie: '#c98b3a', cordanie: '#8a4f7d',
}

export const PALETTES: Record<ModeLecture | 'categorie', Palette> = {
  souverainete: ACTEURS,
  controle: ACTEURS,
  // Snapshot 0 (règle Ether/Guizmo, 28/09/2026) : 4 familles seulement.
  // Occupations = hachures, fronts = bande : jamais une 5e couleur politique.
  alignement: {
    allies_ww2: '#3a6ea5',          // bleu : Alliés (URSS comprise en 1945)
    axis_ww2: '#2e2e33',            // anthracite : Allemagne nazie et territoires qu'elle administre directement
    axis_associe_ww2: '#6b5f55',    // brun-gris sombre : États associés / satellites de l'Axe
    neutral_ww2: '#f6f1e2',         // ivoire : neutres ou hors du conflit affiché
    // Statuts particuliers (décision Ether/Guizmo du 28/09/2026) : fond ivoire, pas de 5e famille
    anti_axis_non_allied: '#f6f1e2',          // Finlande : hors coalitions, en guerre contre l'Allemagne en Laponie
    occupe_hors_coalitions: '#f6f1e2',
    pro_allied_armed_neutral: '#f6f1e2',      // Turquie : neutralité armée orientée vers les Alliés        // Danemark : occupé par l'Allemagne, sans gouvernement dans une coalition (hachures = occupant)
    pro_sovietique_non_belligerant: '#f6f1e2', // Mongolie : liée à l'URSS, non belligérante (+ liseré, voir LISERES)
    soviet_bloc: '#b5534b',         // pour plus tard (guerre froide)
    camp_fictif_a: '#3f8f6b', camp_fictif_b: '#a8483f', neutre_fictif: '#9a9a8a',
  },
  categorie: { migration: '#d9731a', territoire: '#6b4fa0', frontiere: '#6b4fa0', infrastructure: '#7a5a3a', transport: '#7a5a3a', autre: '#555555' },
}

export const LIBELLES: Record<string, string> = {
  // rôles des villes
  capitale: 'capitale', rail: 'nœud ferroviaire', port_maritime: 'port maritime', port_fluvial: 'port fluvial', industrie: 'industrie', frontalier: 'ville frontalière',
  administration: 'administration', aviation: 'aviation', base_navale: 'base navale', ferry: 'ferries', detroit: 'détroit', charbon: 'charbon',
  construction_navale: 'construction navale', siderurgie: 'sidérurgie', transatlantique: 'lignes transatlantiques',
  base_sous_marine: 'base sous-marine', quartier_general: 'quartier général',
  minerai: 'minerai', peche: 'pêche', navigation_cotiere: 'navigation côtière', militaire: 'importance militaire',
  urss: 'URSS', finlande: 'Finlande', republique_de_chine: 'République de Chine', republique_populaire_mongole: 'Rép. populaire mongole',
  allies_ww2: 'Alliés', axis_ww2: 'Allemagne nazie', axis_associe_ww2: 'États associés à l’Axe', neutral_ww2: 'Neutres / hors conflit', soviet_bloc: 'Bloc soviétique', anti_axis_non_allied: 'Hors coalitions, en guerre contre l’Axe', pro_sovietique_non_belligerant: 'Liée à l’URSS, non belligérante', occupe_hors_coalitions: 'Occupé, hors coalitions', pro_allied_armed_neutral: 'Neutre armé, orienté vers les Alliés',
  allemagne: 'Allemagne', autriche: 'Autriche', pologne: 'Pologne',
  danemark: 'Danemark', feroe: 'autorités féroïennes', norvege: 'Norvège', suede: 'Suède', islande: 'Islande', royaume_uni: 'Royaume-Uni', couronne_britannique: 'Couronne britannique',
  irlande: 'Irlande', france: 'France', belgique: 'Belgique', luxembourg: 'Luxembourg', pays_bas: 'Pays-Bas', etats_unis: 'États-Unis', gprf: 'Gouvernement provisoire',
  espagne: 'Espagne', portugal: 'Portugal', andorre: 'Andorre', suisse: 'Suisse', monaco: 'Monaco', vatican: 'Saint-Siège', italie: 'Italie',
  republique_sociale_italienne: 'République sociale italienne', allies_occidentaux: 'Alliés occidentaux', tchecoslovaquie: 'Tchécoslovaquie', hongrie: 'Hongrie',
  gouvernement_provisoire_hongrois: 'Gouvernement provisoire hongrois (Debrecen)', roumanie: 'Roumanie', bulgarie: 'Bulgarie', yougoslavie: 'Yougoslavie',
  partisans_yougoslaves: 'Partisans yougoslaves', republique_slovaque: 'État slovaque (Tiso)', albanie: 'Albanie', grece: 'Grèce', turquie: 'Turquie',
  franquisme: 'régime franquiste', estado_novo: 'Estado Novo', royaume_italie: 'royaume d’Italie', croix_flechees: 'Croix fléchées (Szálasi)', regence: 'régence', gouvernement_democratique_albanie: 'gouvernement démocratique (Hoxha)', allemagne_nazie: 'régime nazi', republique_populaire: 'république populaire',
  ruritanie: 'Ruritanie', kovalie: 'Kovalie', cordanie: 'Cordanie (occupant)',
  camp_fictif_a: 'Camp A', camp_fictif_b: 'Camp B', neutre_fictif: 'Neutre',
  migration: 'Migration', territoire: 'Territoire', frontiere: 'Frontière', infrastructure: 'Infrastructure', transport: 'Transport',
}

/** Liseré (contour intérieur) propre à certains statuts particuliers, en mode Alignements */
export const LISERES: Record<string, string> = {
  pro_sovietique_non_belligerant: '#3a6ea5', // liseré « soviétique » (l'URSS est bleue dans ce mode)
}

/** Camp d'acteurs qui ne sont souverains d'aucun territoire « racine » du corpus (armées étrangères, coalitions, mouvements), pour colorer leurs hachures.
 *  Les autres acteurs prennent le camp de leur territoire dans les données du jour. */
export const CAMP_HORS_CORPUS: Record<string, string> = { etats_unis: 'allies_ww2', allies_occidentaux: 'allies_ww2', partisans_yougoslaves: 'allies_ww2' }

export const SANS_VALEUR = '#bdb7aa'
/** Couleur des hachures quand on ne connaît pas la couleur de l'occupant dans le mode affiché */
export const HACHURE_NEUTRE = '#333333'
/** Hachures claires : contrôle par un autre acteur du MÊME camp (ex. Est-Finnmark norvégien tenu par les Soviétiques) */
export const HACHURE_CLAIRE = '#f6f1e2'
/** Rayures croisées : souverain connu, contrôle réel non tranché (disputé entre plusieurs acteurs) */
export const HACHURE_NON_TRANCHE = '#6e6a62'
export function couleurPour(mode: ModeLecture | 'categorie', valeur: string): string {
  return PALETTES[mode][valeur] ?? SANS_VALEUR
}
