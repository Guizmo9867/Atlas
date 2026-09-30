import { useEffect, useState, type ReactNode } from 'react'
import type { Calques } from '../map/MapView'
import type { ModeLecture } from '../types'
import { LIBELLES, LISERES, couleurPour, SANS_VALEUR } from '../theme/palettes'
import { LISTE_CORPUS, type IdCorpus } from '../data/corpus'

// Commandes posées autour de la carte (remplacent l'ancien volet de gauche).
// Vocabulaire verrouillé : couche = sujet · calque = ce qui est dessiné · filtre = lesquels on garde
// · mode de lecture = comment on colorie (palette = sa légende) · fond de carte = l'image du dessous.

const MODES: { id: ModeLecture | string; nom: string; aide: string; pret: boolean }[] = [
  { id: 'souverainete', nom: 'Souveraineté', aide: 'À qui le territoire appartient légalement.', pret: true },
  { id: 'controle', nom: 'Contrôle effectif', aide: 'Qui tient réellement le terrain.', pret: true },
  { id: 'alignement', nom: 'Alignements', aide: 'Dans quel camp se trouve le territoire.', pret: true },
  { id: 'infrastructures', nom: 'Infrastructures', aide: 'plus tard', pret: false },
  { id: 'flux', nom: 'Flux', aide: 'plus tard', pret: false },
]
const COUCHES = [
  { nom: 'Territoires', aide: 'frontières, contrôle, fronts', pret: true },
  { nom: 'Infrastructures', aide: 'ponts, ports, rail, routes — plus tard', pret: false },
  { nom: 'Transport', aide: 'plus tard', pret: false },
  { nom: 'Migrations', aide: 'plus tard', pret: false },
  { nom: 'Criminalité', aide: 'plus tard', pret: false },
]
const CALQUES: { cle: keyof Calques | null; nom: string; aide?: string }[] = [
  { cle: 'territoires', nom: 'Territoires', aide: 'les aplats de couleur' },
  { cle: 'frontieres', nom: 'Frontières' },
  { cle: 'fronts', nom: 'Lignes de front' },
  { cle: null, nom: 'Villes', aide: 'capitales, puis grandes villes en zoomant — bientôt' },
  { cle: 'ponts', nom: 'Ponts' },
  { cle: 'evenements', nom: 'Pastilles d’événements' },
  { cle: 'parcours', nom: 'Parcours', aide: 'routes suivies' },
]
const FILTRES = [
  { nom: 'Événements militaires' }, { nom: 'Événements politiques' },
  { nom: 'Événements humains', aide: 'réfugiés, déportations…' },
  { nom: 'Micro-histoire', aide: 'petits événements locaux' }, { nom: 'Villes : capitales seulement' },
]
export type IdFond = 'plan' | 'relief' | 'naturel' | 'satellite' | 'reconstitue'
const FONDS: { id: IdFond; nom: string; aide: string; pret: boolean; apercu: string }[] = [
  { id: 'plan', nom: 'Plan', aide: 'terres et mers, sans frontières modernes', pret: true, apercu: 'linear-gradient(135deg,#dfe7ec 0 45%,#ebe5d4 45%)' },
  { id: 'relief', nom: 'Relief', aide: 'montagnes ombrées — bientôt', pret: false, apercu: 'radial-gradient(circle at 35% 40%,#f3efe6 0 18%,#c9c0ad 40%,#e8e2d2 70%)' },
  { id: 'naturel', nom: 'Vue naturelle', aide: 'forêts, déserts, glaciers — bientôt', pret: false, apercu: 'linear-gradient(135deg,#6f8f5a 0 35%,#c8b27e 35% 60%,#8aa8c4 60%)' },
  { id: 'satellite', nom: 'Satellite', aide: 'à partir de 1960 environ — plus tard', pret: false, apercu: 'linear-gradient(135deg,#2c3a2a,#5b6a4a 50%,#1f3448)' },
  { id: 'reconstitue', nom: 'Vue reconstituée', aide: 'l’époque recréée — projet', pret: false, apercu: 'linear-gradient(135deg,#8c7a5b,#b9a57f 50%,#6d7f8c)' },
]

type Pop = 'mode' | 'couches' | 'calques' | 'filtres' | null

function Interrupteur({ on, actif = true, onClick }: { on: boolean; actif?: boolean; onClick?: () => void }) {
  return <button className={`interrupteur ${on ? 'on' : ''}`} disabled={!actif} onClick={onClick} role="switch" aria-checked={on} />
}
function Ligne({ nom, aide, children, actif = true }: { nom: string; aide?: string; children: ReactNode; actif?: boolean }) {
  return <div className={`cmd-ligne ${actif ? '' : 'bientot'}`}><span>{nom}{aide && <small>{aide}</small>}</span>{children}</div>
}
const Icone = ({ d, plein }: { d: string; plein?: string }) => (
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d={d} />{plein && <path d={plein} fill="currentColor" />}</svg>
)

export function Barre({ mode, setMode, calques, setCalques, valeursPresentes }: {
  mode: ModeLecture; setMode: (m: ModeLecture) => void; calques: Calques; setCalques: (c: Calques) => void; valeursPresentes: string[]
}) {
  const [pop, setPop] = useState<Pop>(null)
  useEffect(() => { const k = (e: KeyboardEvent) => { if (e.key === 'Escape') setPop(null) }; addEventListener('keydown', k); return () => removeEventListener('keydown', k) }, [])
  const basculer = (p: Pop) => setPop(pop === p ? null : p)
  const nbCalques = CALQUES.filter((c) => c.cle && calques[c.cle]).length
  const totalCalques = CALQUES.filter((c) => c.cle).length
  const nomMode = MODES.find((m) => m.id === mode)?.nom ?? mode
  const auj = calques.reperesModernes

  return <>
    {pop && <div className="cmd-pop">
      {pop === 'mode' && <>
        <h4>Mode de lecture : comment la carte est coloriée</h4>
        {MODES.map((m) => (
          <button key={m.id} className={`cmd-option ${mode === m.id ? 'choisi' : ''}`} disabled={!m.pret} onClick={() => setMode(m.id as ModeLecture)}>
            <span className="puce" /><span><b>{m.nom}</b><small>{m.aide}</small></span>
          </button>
        ))}
        <h4 className="espace">Légende de ce mode</h4>
        <ul className="cmd-legende">
          {valeursPresentes.map((id) => (
            <li key={id || 'vide'}><i style={{ background: id ? couleurPour(mode, id) : SANS_VALEUR }} />{id ? (LIBELLES[id] ?? id) : (mode === 'souverainete' ? 'souveraineté non tranchée (contestée)' : 'non renseigné')}</li>
          ))}
          {mode === 'alignement' && valeursPresentes.filter((v) => LISERES[v]).map((v) => (
            <li key={`lisere-${v}`}><i style={{ background: 'transparent', border: `3px solid ${LISERES[v]}` }} />liseré : {LIBELLES[v] ?? v}</li>
          ))}
          {mode !== 'controle' && <li><i className="hachure" />hachures : tenu par un autre acteur{mode === 'alignement' ? ' (couleur de son camp)' : ''}</li>}
          {mode !== 'controle' && <li><i className="croise" />rayures croisées : contrôle réel non tranché</li>}
          <li><i className="front" />bande rouge : ligne de front</li>
        </ul>
      </>}
      {pop === 'couches' && <>
        <h4>Couches : de quel sujet parle la carte</h4>
        {COUCHES.map((c) => <Ligne key={c.nom} nom={c.nom} aide={c.aide} actif={c.pret}><Interrupteur on={c.pret} actif={false} /></Ligne>)}
      </>}
      {pop === 'calques' && <>
        <h4>Calques : ce qui est dessiné</h4>
        {CALQUES.map((c) => (
          <Ligne key={c.nom} nom={c.nom} aide={c.aide} actif={!!c.cle}>
            <Interrupteur on={c.cle ? calques[c.cle] : false} actif={!!c.cle}
              onClick={() => c.cle && setCalques({ ...calques, [c.cle]: !calques[c.cle] })} />
          </Ligne>
        ))}
      </>}
      {pop === 'filtres' && <>
        <h4>Filtres : lesquels, parmi ce qui est dessiné</h4>
        <p className="cmd-note">Bientôt. Exemples à définir ensemble :</p>
        {FILTRES.map((f) => <Ligne key={f.nom} nom={f.nom} aide={f.aide} actif={false}><Interrupteur on={false} actif={false} /></Ligne>)}
      </>}
    </div>}

    <div className="cmd-barre">
      <button className={`cmd-btn ${pop === 'mode' ? 'ouvert' : ''}`} onClick={() => basculer('mode')}>
        <Icone d="M12 4a8 8 0 1 0 0 16a8 8 0 1 0 0-16" plein="M12 4a8 8 0 0 1 0 16z" />Mode<span className="etat">{nomMode}</span></button>
      <button className={`cmd-btn ${pop === 'couches' ? 'ouvert' : ''}`} onClick={() => basculer('couches')}>
        <Icone d="M4 6h16M4 12h16M4 18h16" />Couches<span className="etat">Territoires</span></button>
      <button className={`cmd-btn ${pop === 'calques' ? 'ouvert' : ''}`} onClick={() => basculer('calques')}>
        <Icone d="M12 4 3 9l9 5 9-5zM3 14l9 5 9-5" />Calques<span className="etat">{nbCalques} / {totalCalques}</span></button>
      <button className={`cmd-btn ${pop === 'filtres' ? 'ouvert' : ''}`} onClick={() => basculer('filtres')}>
        <Icone d="M4 5h16l-6 8v5l-4 2v-7z" />Filtres<span className="etat">aucun</span></button>
      <button className={`cmd-btn ${auj ? 'allume' : ''}`} onClick={() => { setPop(null); setCalques({ ...calques, reperesModernes: !auj }) }}
        title="Repères modernes (OpenStreetMap) par-dessus la carte historique">
        <Icone d="M12 4a8 8 0 1 0 0 16a8 8 0 1 0 0-16M12 8v4l3 2" />Aujourd’hui<span className="etat">{auj ? 'allumé' : 'éteint'}</span></button>
    </div>
  </>
}

export function FondCarte({ fond, setFond }: { fond: IdFond; setFond: (f: IdFond) => void }) {
  const [ouvert, setOuvert] = useState(false)
  const actuel = FONDS.find((f) => f.id === fond)!
  return (
    <div className="fond-carte">
      {ouvert && <div className="fond-liste">
        <h4>Fond de carte</h4>
        {FONDS.map((f) => (
          <button key={f.id} className={`fond-choix ${f.id === fond ? 'choisi' : ''}`} disabled={!f.pret} onClick={() => { setFond(f.id); setOuvert(false) }}>
            <i style={{ background: f.apercu }} /><span><b>{f.nom}</b><small>{f.aide}</small></span>
          </button>
        ))}
      </div>}
      <button className="fond-carre" onClick={() => setOuvert(!ouvert)} aria-expanded={ouvert} title="Fond de carte">
        <i style={{ background: actuel.apercu }} /><span>Fond</span>
      </button>
    </div>
  )
}

export function Entete({ fictif, corpus, setCorpus, zoom, sansGeometrie }: {
  fictif: boolean; corpus: IdCorpus; setCorpus: (c: IdCorpus) => void; zoom: number; sansGeometrie: string[]
}) {
  const [ouvert, setOuvert] = useState(false)
  return (
    <div className="entete">
      <div className="entete-logo">
        <b>Atlas Eurasie</b>
        {fictif && <span className="entete-fictif">fictif</span>}
        <button className="entete-i" onClick={() => setOuvert(!ouvert)} aria-expanded={ouvert} aria-label="À propos de l’Atlas">i</button>
      </div>
      {ouvert && <div className="entete-info">
        <p>{fictif ? <span className="badge-fictif">Données 100 % fictives</span> : <span className="badge-provisoire">Tracés provisoires</span>}</p>
        {!fictif && <p>Frontières d’après OpenHistoricalMap et des cartes militaires datées, à confirmer par des sources de niveau A ou B.</p>}
        <h4>Petit lexique</h4>
        <dl className="lexique">
          <div><dt>Mode de lecture</dt><dd>comment la carte est coloriée</dd></div>
          <div><dt>Couche</dt><dd>le sujet (territoires, transport…)</dd></div>
          <div><dt>Calque</dt><dd>ce qui est dessiné (frontières, villes…)</dd></div>
          <div><dt>Filtre</dt><dd>lesquels on garde parmi ce qui est dessiné</dd></div>
          <div><dt>Fond de carte</dt><dd>l’image du dessous (plan, relief…)</dd></div>
        </dl>
        <h4>Pour l’équipe</h4>
        {LISTE_CORPUS.map((c) => (
          <label key={c.id} className="entete-corpus">
            <input type="radio" name="corpus" checked={corpus === c.id} onChange={() => setCorpus(c.id)} />
            <span>{c.nom}</span>
          </label>
        ))}
        <p className="cmd-note">Zoom : {zoom.toFixed(1).replace('.', ',')}{sansGeometrie.length > 0 ? ` · ${sansGeometrie.length} entité(s) sans tracé à cette date` : ''}</p>
      </div>}
    </div>
  )
}
