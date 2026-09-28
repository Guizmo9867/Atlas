// PALETTES — la couleur n'existe QUE ici, jamais dans les données historiques.
// Chaque mode de lecture associe des identifiants sémantiques (souverainete_id, controle_id…) à une couleur.
// Les identifiants viennent de docs/LEXIQUE_ID.md.
import type { ModeLecture } from '../types'

type Palette = Record<string, string>

const ACTEURS: Palette = {
  // réels
  urss: '#b5534b', finlande: '#4f7cac', republique_de_chine: '#c9a13a', republique_populaire_mongole: '#8a6fb0',
  allemagne: '#44444c', autriche: '#c49a6c', pologne: '#6f9f5f',
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
    pro_sovietique_non_belligerant: '#f6f1e2', // Mongolie : liée à l'URSS, non belligérante (+ liseré, voir LISERES)
    soviet_bloc: '#b5534b',         // pour plus tard (guerre froide)
    camp_fictif_a: '#3f8f6b', camp_fictif_b: '#a8483f', neutre_fictif: '#9a9a8a',
  },
  categorie: { migration: '#d9731a', territoire: '#6b4fa0', frontiere: '#6b4fa0', infrastructure: '#7a5a3a', transport: '#7a5a3a', autre: '#555555' },
}

export const LIBELLES: Record<string, string> = {
  urss: 'URSS', finlande: 'Finlande', republique_de_chine: 'République de Chine', republique_populaire_mongole: 'Rép. populaire mongole',
  allies_ww2: 'Alliés', axis_ww2: 'Allemagne nazie', axis_associe_ww2: 'États associés à l’Axe', neutral_ww2: 'Neutres / hors conflit', soviet_bloc: 'Bloc soviétique', anti_axis_non_allied: 'Hors coalitions, en guerre contre l’Axe', pro_sovietique_non_belligerant: 'Liée à l’URSS, non belligérante',
  allemagne: 'Allemagne', autriche: 'Autriche', pologne: 'Pologne', allemagne_nazie: 'régime nazi', republique_populaire: 'république populaire',
  ruritanie: 'Ruritanie', kovalie: 'Kovalie', cordanie: 'Cordanie (occupant)',
  camp_fictif_a: 'Camp A', camp_fictif_b: 'Camp B', neutre_fictif: 'Neutre',
  migration: 'Migration', territoire: 'Territoire', frontiere: 'Frontière', infrastructure: 'Infrastructure', transport: 'Transport',
}

/** Liseré (contour intérieur) propre à certains statuts particuliers, en mode Alignements */
export const LISERES: Record<string, string> = {
  pro_sovietique_non_belligerant: '#3a6ea5', // liseré « soviétique » (l'URSS est bleue dans ce mode)
}

export const SANS_VALEUR = '#bdb7aa'
/** Couleur des hachures quand on ne connaît pas la couleur de l'occupant dans le mode affiché */
export const HACHURE_NEUTRE = '#333333'
export function couleurPour(mode: ModeLecture | 'categorie', valeur: string): string {
  return PALETTES[mode][valeur] ?? SANS_VALEUR
}
