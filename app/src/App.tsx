import { useCallback, useEffect, useMemo, useState } from 'react'
import MapView, { type Calques } from './map/MapView'
import Timeline, { type Marque } from './timeline/Timeline'
import Fiche from './ui/Fiche'
import Panneau from './ui/Panneau'
import { chargerCorpus, geometriesSeules, type Corpus, type IdCorpus } from './data/corpus'
import { construireCouches } from './engine/features'
import { couleurPour } from './theme/palettes'
import type { ModeLecture, Selection } from './types'

export default function App() {
  const [idCorpus, setIdCorpus] = useState<IdCorpus>('snapshot0')
  const [corpus, setCorpus] = useState<Corpus | null>(null)
  const [date, setDate] = useState('1945-01-01')
  const [mode, setMode] = useState<ModeLecture>('alignement')
  const [selection, setSelection] = useState<Selection>(null)
  const [zoom, setZoom] = useState(3)
  const [calques, setCalques] = useState<Calques>({
    territoires: true, frontieres: true, fronts: true, ponts: true, evenements: true, parcours: true, reperesModernes: false,
  })

  useEffect(() => {
    let annule = false
    setSelection(null)
    chargerCorpus(idCorpus).then((c) => { if (!annule) { setCorpus(c); setDate(c.debut) } })
    return () => { annule = true }
  }, [idCorpus])

  const couches = useMemo(() => corpus
    ? construireCouches(corpus.entites, corpus.evenements, date, mode, geometriesSeules(corpus))
    : null, [corpus, date, mode])
  const valeursPresentes = useMemo(() => [...new Set((couches?.territoires.features ?? [])
    .map((f) => String(f.properties?.valeur_mode ?? '')))].sort((a, b) => (a === '' ? 1 : b === '' ? -1 : a.localeCompare(b))), [couches])
  const marques: Marque[] = useMemo(() => (corpus?.evenements ?? []).map((e) => ({
    date: e.date_precise, titre: e.titre, couleur: couleurPour('categorie', e.categories[0] ?? 'autre'),
  })), [corpus])
  const changerDate = useCallback((d: string) => setDate(d), [])

  return (
    <div className="app">
      <Panneau corpus={idCorpus} setCorpus={setIdCorpus} fictif={corpus?.fictif ?? false}
        calques={calques} setCalques={setCalques} mode={mode} setMode={setMode} zoom={zoom}
        sansGeometrie={couches?.sansGeometrie ?? []} valeursPresentes={valeursPresentes} />
      <main className="zone-carte">
        {couches && corpus && <>
          <MapView couches={couches} calques={calques} selection={selection} emprise={corpus.emprise}
            onSelect={setSelection} onZoom={setZoom} />
          <Timeline date={date} debut={corpus.debut} fin={corpus.fin} marques={marques} onChange={changerDate}
            titre={!corpus.fictif && date === '1945-01-01' ? 'Snapshot 0 · 1er janvier 1945, 0 h 00' : undefined} />
          <Fiche selection={selection} date={date} corpus={corpus} onClose={() => setSelection(null)} onSelect={setSelection} />
        </>}
        {!corpus && <div className="chargement">Chargement des tracés…</div>}
      </main>
    </div>
  )
}
