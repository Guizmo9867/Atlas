import type { Calques } from '../map/MapView'
import { ZOOM_MIN } from '../map/MapView'
import type { ModeLecture } from '../types'
import { LIBELLES, LISERES, couleurPour, SANS_VALEUR } from '../theme/palettes'
import { LISTE_CORPUS, type IdCorpus } from '../data/corpus'

const NOMS_CALQUES: Record<keyof Calques, string> = {
  territoires: 'Territoires', frontieres: 'Frontières', fronts: 'Lignes de front', ponts: 'Ponts', evenements: 'Pastilles d’événements',
  parcours: 'Parcours (routes suivies)', reperesModernes: 'Repères modernes (OpenStreetMap)',
}
const MODES: { id: ModeLecture; nom: string; aide: string }[] = [
  { id: 'souverainete', nom: 'Souveraineté', aide: 'À qui le territoire appartient légalement.' },
  { id: 'controle', nom: 'Contrôle effectif', aide: 'Qui tient réellement le terrain.' },
  { id: 'alignement', nom: 'Alignements', aide: 'Dans quel camp se trouve le territoire.' },
]

export default function Panneau({ corpus, setCorpus, fictif, calques, setCalques, mode, setMode, zoom, sansGeometrie, valeursPresentes }: {
  corpus: IdCorpus; setCorpus: (c: IdCorpus) => void; fictif: boolean
  calques: Calques; setCalques: (c: Calques) => void; mode: ModeLecture; setMode: (m: ModeLecture) => void
  zoom: number; sansGeometrie: string[]; valeursPresentes: string[]
}) {
  return (
    <nav className="panneau">
      <h1>Atlas Eurasie</h1>
      {fictif ? <div className="fictif">Données 100 % fictives</div> : <div className="provisoire-bandeau">Tracés provisoires (OpenHistoricalMap) à confirmer</div>}

      <h3>Corpus</h3>
      {LISTE_CORPUS.map((c) => (
        <label key={c.id} className="choix">
          <input type="radio" name="corpus" checked={corpus === c.id} onChange={() => setCorpus(c.id)} />
          <span><strong>{c.nom}</strong><small>{c.aide}</small></span>
        </label>
      ))}

      <h3>Mode de lecture</h3>
      {MODES.map((m) => (
        <label key={m.id} className="choix">
          <input type="radio" name="mode" checked={mode === m.id} onChange={() => setMode(m.id)} />
          <span><strong>{m.nom}</strong><small>{m.aide}</small></span>
        </label>
      ))}
      <ul className="legende">
        {valeursPresentes.map((id) => (
          <li key={id || 'vide'}><i style={{ background: id ? couleurPour(mode, id) : SANS_VALEUR }} />{id ? (LIBELLES[id] ?? id) : (mode === 'souverainete' ? 'souveraineté non tranchée (contestée)' : 'non renseigné')}</li>
        ))}
        {mode === 'alignement' && valeursPresentes.filter((v) => LISERES[v]).map((v) => (
          <li key={`lisere-${v}`} className="note"><i style={{ background: 'transparent', border: `3px solid ${LISERES[v]}` }} />liseré : {LIBELLES[v] ?? v}</li>
        ))}
        {mode !== 'controle' && <li className="note"><i className="hachure" />hachures : contrôlé par un autre acteur</li>}
        <li className="note"><i className="front" />bande : ligne de front</li>
      </ul>

      <h3>Calques</h3>
      {(Object.keys(NOMS_CALQUES) as (keyof Calques)[]).map((k) => (
        <label key={k} className="choix case">
          <input type="checkbox" checked={calques[k]} onChange={() => setCalques({ ...calques, [k]: !calques[k] })} />
          <span>{NOMS_CALQUES[k]}</span>
        </label>
      ))}

      <h3>Pastilles selon le zoom</h3>
      <ul className="zooms">
        {(Object.keys(ZOOM_MIN) as (keyof typeof ZOOM_MIN)[]).map((p) => (
          <li key={p} className={zoom >= ZOOM_MIN[p] ? 'visible' : ''}>
            <strong>{p}</strong> {ZOOM_MIN[p] === 0 ? 'toujours' : `à partir du zoom ${String(ZOOM_MIN[p]).replace('.', ',')}`}
          </li>
        ))}
      </ul>
      <div className="muet">Zoom actuel : {zoom.toFixed(1).replace('.', ',')}</div>
      {sansGeometrie.length > 0 && <div className="muet">{sansGeometrie.length} entité(s) sans géométrie à cette date.</div>}
    </nav>
  )
}
