import type { RefSource, Selection } from '../types'
import type { Corpus } from '../data/corpus'
import { dateCourte, etatEstActif } from '../engine/temporal'
import { LIBELLES } from '../theme/palettes'

const NOMS_PROPRIETES: Record<string, string> = {
  souverainete_id: 'Souveraineté', souverainete_revendiquee_par: 'Souveraineté revendiquée par', controle_id: 'Contrôle effectif', administration_id: 'Administration civile', alignement_id: 'Alignement',
  regime_id: 'Régime', statut_administratif: 'Statut administratif', parent_id: 'Fait partie de', note: 'Note',
}
const NIVEAUX: Record<string, string> = { A: 'A · primaire', B: 'B · secondaire solide', C: 'C · exploratoire' }

function Sources({ refs, corpus }: { refs: RefSource[]; corpus: Corpus }) {
  if (!refs?.length) return <p className="muet">Aucune source.</p>
  return (
    <ul className="sources">
      {refs.map((r, i) => {
        const s = corpus.sources.find((x) => x.source_id === r.source_id)
        return (
          <li key={i}>
            {s ? <span className={`niveau niveau-${s.niveau}`}>{NIVEAUX[s.niveau]}</span> : <span className="niveau niveau-X">source absente du registre</span>}
            <div className="titre-source">{s?.url ? <a href={s.url} target="_blank" rel="noreferrer">{s.titre}</a> : (s?.titre ?? r.source_id)}</div>
            {s?.institution && <div className="muet">{s.institution}</div>}
            {(r.locator || s?.locator) && <div className="muet">📍 {r.locator || s?.locator}</div>}
            {r.usage && <div>{r.usage}</div>}
          </li>
        )
      })}
    </ul>
  )
}

interface MetaGeometrie {
  statut: string; operations: string[]; precision: string; surface_km2: number
  sources: RefSource[]; points_a_verifier?: string[]; script?: string
}

/** D'où vient le tracé affiché : sources, opérations, points à vérifier. */
function Trace({ meta, corpus }: { meta?: MetaGeometrie; corpus: Corpus }) {
  if (!meta) return <div className="trace"><h4>Tracé</h4><p className="muet">Pas encore de géométrie.</p></div>
  return (
    <div className="trace">
      <h4>Tracé {meta.statut.startsWith('provisoire') && <span className="provisoire">provisoire</span>}</h4>
      <p className="muet">{meta.surface_km2.toLocaleString('fr-FR')} km² · {meta.operations.join(' → ')}</p>
      <Sources refs={meta.sources} corpus={corpus} />
      {meta.points_a_verifier?.length ? <>
        <h4>À vérifier</h4>
        <ul className="a-verifier">{meta.points_a_verifier.map((p, i) => <li key={i}>{p}</li>)}</ul>
      </> : null}
    </div>
  )
}

export default function Fiche({ selection, date, corpus, onClose, onSelect }: {
  selection: Selection; date: string; corpus: Corpus; onClose: () => void; onSelect: (s: Selection) => void
}) {
  if (!selection) return null
  const entiteParId = (id: string) => corpus.entites.find((e) => e.entite_id === id)
  const evenementParId = (id: string) => corpus.evenements.find((e) => e.id === id)

  if (selection.kind === 'evenement') {
    const ev = evenementParId(selection.id)
    if (!ev) return null
    return (
      <aside className="fiche">
        <button className="fermer" onClick={onClose} aria-label="Fermer">✕</button>
        <div className="surtitre">Événement · {ev.categories.join(', ')}</div>
        <h2>{ev.titre}</h2>
        <div className="meta">{dateCourte(ev.date_precise)}{ev.date_fin ? ` → ${dateCourte(ev.date_fin)}` : ''} · {ev.lieu}</div>
        <div className="pastilles-info">
          <span>{ev.niveau_importance.replace('_', ' ')}</span><span>affichage : {ev.profondeur_affichage}</span>
          <span>certitude : {ev.certitude_evenement}</span><span>sources : {ev.etat_sources}</span>
        </div>
        <p className="resume">{ev.resume}</p>
        {ev.contexte && <><h3>Contexte</h3><p>{ev.contexte}</p></>}
        {ev.deroulement && <><h3>Déroulement</h3><p>{ev.deroulement}</p></>}
        {Object.keys(ev.consequences ?? {}).length > 0 && <>
          <h3>Conséquences</h3>
          <dl>{Object.entries(ev.consequences).filter(([, v]) => v).map(([k, v]) => <div key={k}><dt>{k}</dt><dd>{v}</dd></div>)}</dl>
        </>}
        {ev.notes_incertitude && <><h3>Incertitudes</h3><p>{ev.notes_incertitude}</p></>}
        {ev.relations.length > 0 && <>
          <h3>Liens</h3>
          <ul className="liens">{ev.relations.map((r, i) => {
            const nom = r.cible_type === 'entite' ? entiteParId(r.cible_id)?.nom : evenementParId(r.cible_id)?.titre
            return <li key={i}><em>{r.type}</em> → <button className="lien" onClick={() => onSelect({ kind: r.cible_type, id: r.cible_id })}>{nom ?? r.cible_id}</button></li>
          })}</ul>
        </>}
        <h3>Sources</h3>
        <Sources refs={ev.sources} corpus={corpus} />
      </aside>
    )
  }

  const ent = entiteParId(selection.id)
  if (!ent) return null
  const actif = ent.etats.find((e) => etatEstActif(e, date))
  return (
    <aside className="fiche">
      <button className="fermer" onClick={onClose} aria-label="Fermer">✕</button>
      <div className="surtitre">Entité · {ent.type_entite}</div>
      <h2>{ent.nom}</h2>
      <div className="meta"><code>{ent.entite_id}</code></div>
      <h3>Historique des états</h3>
      <ol className="etats">
        {ent.etats.map((e) => (
          <li key={e.etat_id} className={e === actif ? 'actif' : ''}>
            <div className="etat-tete">
              <strong>{e.statut.replace(/_/g, ' ')}</strong>
              {e === actif && <span className="badge">affiché</span>}
            </div>
            <div className="muet">{dateCourte(e.valid_from)} → {dateCourte(e.valid_to)}</div>
            {e === actif && <>
              <dl>{Object.entries(e.proprietes ?? {}).map(([k, v]) => (
                <div key={k}><dt>{NOMS_PROPRIETES[k] ?? k}</dt><dd>{Array.isArray(v) ? v.map((x) => LIBELLES[x] ?? x).join(', ') : k === 'parent_id' ? (entiteParId(v)?.nom ?? v) : (LIBELLES[v] ?? v)}</dd></div>
              ))}</dl>
              <Sources refs={e.sources} corpus={corpus} />
              {e.geometrie_ref && <Trace meta={corpus.geometries[e.geometrie_ref]?.properties as MetaGeometrie | undefined} corpus={corpus} />}
            </>}
          </li>
        ))}
      </ol>
    </aside>
  )
}
