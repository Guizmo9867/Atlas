import { useEffect, useRef, useState } from 'react'
import { ajouterJours, ecartJours } from '../engine/temporal'
import type { Marque } from './Timeline'

// Règle du temps « à effet loupe », posée en haut de la carte.
// - glisser (doigt/souris) ou molette pour voyager ; toucher un trait pour y sauter ;
// - accélérateur par paliers (« tempo ») : coups 1-2 = jours, 3-5 = mois, 6 et plus = années ;
// - toucher la date ouvre le sélecteur : année, puis mois et jour facultatifs.

interface Props {
  date: string
  debut: string
  fin: string
  marques: Marque[]
  onChange: (d: string) => void
  titre?: string
}

const MOIS = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
const MOIS_LONG = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
const JOURS_SEM = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']

// Œil de poisson : ±D jours visibles, M = force de la loupe.
const D = 150, M = 14
// Tempo : vitesse (jours par image) selon le nombre de coups enchaînés.
const FROTTEMENT = 0.96, BASE_MOLETTE = 0.5, ENCHAINEMENT_MS = 1500
const VITESSES = [0, 0.5, 1.2, 2.5, 4, 6, 16, 32, 64, 128, 256]

const iso = (d: Date) => d.toISOString().slice(0, 10)
const parse = (s: string) => new Date(`${s}T00:00:00Z`)
const jourLisible = (s: string) => { const d = parse(s); return `${d.getUTCDate() === 1 ? '1er' : d.getUTCDate()} ${MOIS_LONG[d.getUTCMonth()]} ${d.getUTCFullYear()}` }

export default function RegleTemps({ date, debut, fin, marques, onChange, titre }: Props) {
  const regleRef = useRef<HTMLDivElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const total = ecartJours(debut, fin)
  const etat = useRef({ pos: ecartJours(debut, date), cible: ecartJours(debut, date), elan: 0, coups: 0, dernierElan: 0, emis: ecartJours(debut, date), emisA: 0 })
  const tirRef = useRef<null | { x: number; depart: number; bouge: boolean; elanAvant: number; hist: [number, number][] }>(null)
  const [affiche, setAffiche] = useState(date)
  const [vitesse, setVitesse] = useState('')
  const [ouvert, setOuvert] = useState(false)
  const rappel = useRef(onChange); rappel.current = onChange
  const marquesRef = useRef(marques); marquesRef.current = marques

  // Date changée de l'extérieur (sélecteur, fiche…) → la règle y va.
  useEffect(() => {
    const e = etat.current, i = ecartJours(debut, date)
    if (i !== e.emis) { e.elan = 0; e.cible = Math.min(total, Math.max(0, i)); e.emis = i }
  }, [date, debut, total])

  useEffect(() => {
    const regle = regleRef.current!, c = canvasRef.current!, ctx = c.getContext('2d')!
    const e = etat.current
    let W = 0, H = 0, raf = 0, dernierAffiche = '', derniereVitesse = ''
    const taille = () => { const r = regle.getBoundingClientRect(), d = devicePixelRatio || 1
      W = r.width; H = r.height; c.width = W * d; c.height = H * d; ctx.setTransform(d, 0, 0, d, 0, 0) }
    const ro = new ResizeObserver(taille); ro.observe(regle); taille()
    const borne = (v: number) => Math.min(total, Math.max(0, v))
    const demi = () => W / 2
    const X = (d: number) => { const u = Math.min(1, Math.abs(d) / D); return demi() + Math.sign(d) * demi() * ((M + 1) * u) / (M * u + 1) }
    const pente = (d: number) => { const u = Math.min(1, Math.abs(d) / D); return demi() / D * (M + 1) / ((M * u + 1) ** 2) }
    const ecartDe = (x: number) => { const g = Math.min(0.999, Math.abs(x - demi()) / demi()); return Math.sign(x - demi()) * D * g / ((M + 1) - M * g) }
    const origine = parse(debut).getTime()
    const dateDe = (i: number) => new Date(origine + Math.round(i) * 86400000)

    const relancer = (sens: number, impulsion: number) => {
      const maintenant = performance.now()
      const enchaine = e.elan !== 0 && Math.sign(e.elan) === sens && maintenant - e.dernierElan < ENCHAINEMENT_MS
      e.coups = enchaine ? e.coups + 1 : 1
      const v = e.coups === 1 ? Math.min(1.2, Math.max(0.3, impulsion)) : VITESSES[Math.min(e.coups, VITESSES.length - 1)]
      e.elan = sens * v; e.dernierElan = maintenant
    }

    const dessiner = () => {
      ctx.clearRect(0, 0, W, H)
      const base = H - 15, p0 = pente(0)
      const lueur = ctx.createRadialGradient(W / 2, base - 8, 0, W / 2, base - 8, W * 0.15)
      lueur.addColorStop(0, 'rgba(224,169,74,.16)'); lueur.addColorStop(1, 'rgba(224,169,74,0)')
      ctx.fillStyle = lueur; ctx.fillRect(0, 0, W, H)
      ctx.lineCap = 'round'
      for (let i = Math.floor(e.pos - D); i <= Math.ceil(e.pos + D); i++) {
        const d = i - e.pos, x = X(d), p = pente(d), L = Math.pow(p / p0, 0.6), dt = dateDe(i)
        const hors = i < 0 || i > total
        const estMois = dt.getUTCDate() === 1, estSemaine = dt.getUTCDay() === 1
        let h: number, couleur: string, epais: number
        const a = hors ? 0.35 : 1
        if (estMois) { h = 8 + 15 * L; couleur = `rgba(224,169,74,${(0.55 + 0.45 * L) * a})`; epais = 2 }
        else if (estSemaine) { if (p < 1.6) continue; h = 5 + 11 * L; couleur = `rgba(236,231,218,${(0.45 + 0.55 * L) * a})`; epais = 1.5 }
        else { if (p < 3.5) continue; h = 3 + 6 * L; couleur = `rgba(200,205,214,${(0.35 + 0.55 * L) * a})`; epais = 1 }
        ctx.strokeStyle = couleur; ctx.lineWidth = epais
        ctx.beginPath(); ctx.moveTo(x, base); ctx.lineTo(x, base - h); ctx.stroke()
        if (estMois && 30 * p > 30) {
          const janv = dt.getUTCMonth() === 0
          ctx.fillStyle = janv ? `rgba(242,191,94,${(0.65 + 0.35 * L) * a})` : `rgba(236,231,218,${(0.5 + 0.5 * L) * a})`
          ctx.font = `${janv ? 600 : 400} ${9 + 2 * L}px system-ui, sans-serif`; ctx.textAlign = 'center'
          ctx.fillText(janv ? String(dt.getUTCFullYear()) : MOIS[dt.getUTCMonth()], x, base + 11)
        } else if (!estMois && p >= 13 && Math.abs(d) > 0.5 && (p >= 26 || (dt.getUTCDate() !== 2 && dateDe(i + 1).getUTCDate() !== 1))) {
          ctx.fillStyle = `rgba(200,205,214,${L * a})`; ctx.font = '9px system-ui, sans-serif'; ctx.textAlign = 'center'
          ctx.fillText(String(dt.getUTCDate()), x, base + 11)
        }
      }
      // événements du corpus : petites pastilles au-dessus des traits
      for (const m of marquesRef.current) {
        const d = ecartJours(debut, m.date) - e.pos
        if (Math.abs(d) > D) continue
        ctx.fillStyle = m.couleur; ctx.beginPath(); ctx.arc(X(d), base - 26, 2.5 + 1.5 * Math.pow(pente(d) / p0, 0.6), 0, Math.PI * 2); ctx.fill()
      }
      // curseur central
      ctx.strokeStyle = '#f2bf5e'; ctx.lineWidth = 2
      ctx.beginPath(); ctx.moveTo(W / 2, 9); ctx.lineTo(W / 2, base + 4); ctx.stroke()
    }

    const boucle = () => {
      if (!tirRef.current && e.elan !== 0) {
        e.cible = borne(e.cible + e.elan); e.pos = e.cible; e.elan *= FROTTEMENT
        if (e.cible === 0 || e.cible === total) e.elan = 0
        if (Math.abs(e.elan) < 0.06) { e.elan = 0; e.cible = Math.round(e.cible) }
      }
      e.pos += (e.cible - e.pos) * 0.18; if (Math.abs(e.cible - e.pos) < 0.002) e.pos = e.cible
      dessiner()
      const i = Math.round(e.pos), s = iso(dateDe(i))
      if (s !== dernierAffiche) { dernierAffiche = s; setAffiche(s) }
      // la carte suit : au plus toutes les 80 ms pendant un défilement, et toujours à l'arrêt
      const maintenant = performance.now(), auRepos = e.elan === 0 && !tirRef.current && e.pos === e.cible
      if (i !== e.emis && (auRepos || maintenant - e.emisA > 80)) { e.emis = i; e.emisA = maintenant; rappel.current(ajouterJours(debut, i)) }
      const v = Math.abs(e.elan) < 0.3 ? '' : `${e.elan > 0 ? '▶▶' : '◀◀'} ${e.coups <= 2 ? 'jours' : e.coups <= 5 ? 'mois' : 'années'}`
      if (v !== derniereVitesse) { derniereVitesse = v; setVitesse(v) }
      raf = requestAnimationFrame(boucle)
    }

    const bas = (ev: PointerEvent) => { tirRef.current = { x: ev.clientX, depart: e.cible, bouge: false, elanAvant: e.elan, hist: [[ev.clientX, performance.now()]] }; e.elan = 0; regle.setPointerCapture(ev.pointerId) }
    const bouge = (ev: PointerEvent) => { const t = tirRef.current; if (!t) return; const dx = ev.clientX - t.x
      if (Math.abs(dx) > 5) t.bouge = true
      if (t.bouge) { e.cible = borne(t.depart - dx / pente(0)); e.pos = e.cible; t.hist.push([ev.clientX, performance.now()]); if (t.hist.length > 6) t.hist.shift() } }
    const haut = (ev: PointerEvent) => { const t = tirRef.current; if (!t) return; tirRef.current = null
      if (!t.bouge) {
        if (Math.abs(t.elanAvant) > 0.3) { e.cible = Math.round(e.cible); return }
        const r = regle.getBoundingClientRect(); e.cible = borne(Math.round(e.pos + ecartDe(ev.clientX - r.left))); return
      }
      const a = t.hist[0], b = t.hist[t.hist.length - 1], dtm = Math.max(1, b[1] - a[1])
      const v = -(b[0] - a[0]) / dtm / pente(0) * 16
      if (Math.abs(v) < 0.2) { e.cible = Math.round(e.cible); return }
      e.elan = t.elanAvant; relancer(Math.sign(v), Math.abs(v)) }
    const annule = () => { tirRef.current = null; e.cible = Math.round(e.cible) }
    let dernierCoup = 0
    const molette = (ev: WheelEvent) => { ev.preventDefault()
      const delta = Math.abs(ev.deltaY) >= Math.abs(ev.deltaX) ? ev.deltaY : ev.deltaX; if (!delta) return
      const maintenant = performance.now(); if (maintenant - dernierCoup < 140) return
      dernierCoup = maintenant; relancer(Math.sign(delta), BASE_MOLETTE) }
    const clavier = (ev: KeyboardEvent) => {
      if ((ev.target as HTMLElement)?.closest?.('input, textarea, select')) return
      const pas = ev.shiftKey ? 7 : 1
      if (ev.key === 'ArrowRight') { e.elan = 0; e.cible = borne(Math.round(e.cible) + pas) }
      if (ev.key === 'ArrowLeft') { e.elan = 0; e.cible = borne(Math.round(e.cible) - pas) } }

    regle.addEventListener('pointerdown', bas); regle.addEventListener('pointermove', bouge)
    regle.addEventListener('pointerup', haut); regle.addEventListener('pointercancel', annule)
    regle.addEventListener('wheel', molette, { passive: false }); addEventListener('keydown', clavier)
    raf = requestAnimationFrame(boucle)
    return () => {
      cancelAnimationFrame(raf); ro.disconnect(); removeEventListener('keydown', clavier)
      regle.removeEventListener('pointerdown', bas); regle.removeEventListener('pointermove', bouge)
      regle.removeEventListener('pointerup', haut); regle.removeEventListener('pointercancel', annule)
      regle.removeEventListener('wheel', molette)
    }
  }, [debut, total])

  const d = parse(affiche)
  return (
    <div className="regle-temps">
      <button className="regle-date" onClick={() => setOuvert(!ouvert)} aria-haspopup="dialog" aria-expanded={ouvert}>
        <span className="regle-jour">{JOURS_SEM[d.getUTCDay()]}</span>
        <span className="regle-texte">{jourLisible(affiche)}</span>
        {titre && affiche === debut && <span className="regle-titre">{titre}</span>}
        <span className="regle-fleche">▾</span>
      </button>
      <div className="regle-piste" ref={regleRef} aria-label="Règle du temps : glisser pour changer de date">
        <canvas ref={canvasRef} />
      </div>
      {vitesse && <div className="regle-vitesse">{vitesse}</div>}
      {ouvert && <Selecteur debut={debut} fin={fin} actuel={affiche}
        onValider={(s) => { setOuvert(false); onChange(s) }} onFermer={() => setOuvert(false)} />}
    </div>
  )
}

function Selecteur({ debut, fin, actuel, onValider, onFermer }: { debut: string; fin: string; actuel: string; onValider: (d: string) => void; onFermer: () => void }) {
  const [choix, setChoix] = useState<{ a: number | null; m: number | null; j: number | null }>({ a: null, m: null, j: null })
  const [etape, setEtape] = useState<'a' | 'm' | 'j'>('a')
  const zoneRef = useRef<HTMLDivElement>(null)
  const d0 = parse(debut), d1 = parse(fin), dA = parse(actuel)
  const aMin = d0.getUTCFullYear(), aMax = d1.getUTCFullYear()
  const dansPlage = (a: number, m: number, j: number) => { const s = iso(new Date(Date.UTC(a, m, j))); return s >= debut && s <= fin }
  const moisPossible = (a: number, m: number) => iso(new Date(Date.UTC(a, m + 1, 0))) >= debut && iso(new Date(Date.UTC(a, m, 1))) <= fin
  const cible = () => { if (choix.a === null) return null
    const s = iso(new Date(Date.UTC(choix.a, choix.m ?? 0, choix.j ?? 1)))
    return s < debut ? debut : s > fin ? fin : s }

  useEffect(() => { if (etape !== 'a') return
    const z = zoneRef.current, b = z?.querySelector<HTMLElement>('.choisi, .actuel'); if (z && b) z.scrollTop = b.offsetTop - z.offsetTop - 50 }, [etape])
  useEffect(() => { const k = (ev: KeyboardEvent) => { if (ev.key === 'Escape') onFermer() }; addEventListener('keydown', k); return () => removeEventListener('keydown', k) }, [onFermer])

  const decennies: number[] = []
  for (let dec = Math.floor(aMin / 10) * 10; dec <= aMax; dec += 10) decennies.push(dec)
  const s = cible()
  return (
    <div className="regle-selecteur" role="dialog" aria-label="Choisir une date">
      <div className="sel-fil">
        <button className={`${choix.a !== null ? 'rempli' : ''} ${etape === 'a' ? 'actif' : ''}`} onClick={() => setEtape('a')}>{choix.a ?? 'Année'}</button>
        <button className={`${choix.m !== null ? 'rempli' : ''} ${etape === 'm' ? 'actif' : ''}`} disabled={choix.a === null} onClick={() => setEtape('m')}>{choix.m !== null ? MOIS_LONG[choix.m] : 'Mois'}</button>
        <button className={`${choix.j !== null ? 'rempli' : ''} ${etape === 'j' ? 'actif' : ''}`} disabled={choix.m === null} onClick={() => setEtape('j')}>{choix.j ?? 'Jour'}</button>
      </div>
      {etape === 'a' && <>
        <p className="sel-titre">Choisis une année</p>
        <div className="sel-annees" ref={zoneRef}>
          {decennies.map((dec) => (
            <div key={dec}>
              <div className="sel-decennie">Années {dec}</div>
              <div className="sel-grille g5">
                {Array.from({ length: 10 }, (_, k) => dec + k).filter((a) => a >= aMin && a <= aMax).map((a) => (
                  <button key={a} className={`sel-case ${choix.a === a ? 'choisi' : ''} ${dA.getUTCFullYear() === a ? 'actuel' : ''}`}
                    onClick={() => { setChoix({ a, m: null, j: null }); setEtape('m') }}>{a}</button>
                ))}
              </div>
            </div>
          ))}
        </div>
      </>}
      {etape === 'm' && choix.a !== null && <>
        <p className="sel-titre">Un mois de {choix.a} ? (facultatif)</p>
        <div className="sel-grille g4">
          {MOIS.map((nom, m) => (
            <button key={m} className={`sel-case ${choix.m === m ? 'choisi' : ''}`} disabled={!moisPossible(choix.a!, m)}
              onClick={() => { setChoix({ ...choix, m, j: null }); setEtape('j') }}>{nom}</button>
          ))}
        </div>
      </>}
      {etape === 'j' && choix.a !== null && choix.m !== null && <>
        <p className="sel-titre">Un jour de {MOIS_LONG[choix.m]} {choix.a} ? (facultatif)</p>
        <div className="sel-grille g7">
          {['L', 'M', 'M', 'J', 'V', 'S', 'D'].map((l, k) => <div key={k} className="sel-entete">{l}</div>)}
          {Array.from({ length: (new Date(Date.UTC(choix.a, choix.m, 1)).getUTCDay() + 6) % 7 }, (_, k) => <span key={`v${k}`} />)}
          {Array.from({ length: new Date(Date.UTC(choix.a, choix.m + 1, 0)).getUTCDate() }, (_, k) => k + 1).map((j) => (
            <button key={j} className={`sel-case ${choix.j === j ? 'choisi' : ''}`} disabled={!dansPlage(choix.a!, choix.m!, j)}
              onClick={() => setChoix({ ...choix, j })}>{j}</button>
          ))}
        </div>
      </>}
      <div className="sel-pied">
        <button className="sel-annuler" onClick={onFermer}>Annuler</button>
        <button className="sel-ok" disabled={!s} onClick={() => s && onValider(s)}>{s ? `Aller au ${jourLisible(s)}` : 'OK'}</button>
      </div>
      <p className="sel-note">Le mois et le jour sont facultatifs. Données disponibles du {jourLisible(debut)} au {jourLisible(fin)}.</p>
    </div>
  )
}
