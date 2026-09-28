import { useEffect, useState } from 'react'
import { ajouterJours, dateLongue, ecartJours } from '../engine/temporal'

export interface Marque { date: string; titre: string; couleur: string }

interface Props {
  date: string
  debut: string
  fin: string
  marques: Marque[]
  onChange: (d: string) => void
  titre?: string
}

/** Curseur temporel jour par jour. */
export default function Timeline({ date, debut, fin, marques, onChange, titre }: Props) {
  const total = ecartJours(debut, fin)
  const index = ecartJours(debut, date)
  const [lecture, setLecture] = useState(false)

  useEffect(() => {
    if (!lecture) return
    const t = setInterval(() => {
      const suivant = ajouterJours(date, 1)
      if (suivant > fin) setLecture(false)
      else onChange(suivant)
    }, 700)
    return () => clearInterval(t)
  }, [lecture, date, fin, onChange])

  const aller = (n: number) => {
    const d = ajouterJours(date, n)
    if (d >= debut && d <= fin) onChange(d)
  }

  return (
    <div className="timeline">
      <div className="timeline-tete">
        <button onClick={() => aller(-1)} disabled={date <= debut} aria-label="Jour précédent">◀</button>
        <button className="lecture" onClick={() => setLecture(!lecture)}>{lecture ? '❚❚ Pause' : '▶ Lecture'}</button>
        <button onClick={() => aller(1)} disabled={date >= fin} aria-label="Jour suivant">▶</button>
        <div className="date-affichee">{titre && <span className="titre-snapshot">{titre}</span>}{dateLongue(date)}</div>
      </div>
      <div className="piste">
        <input type="range" min={0} max={total} value={index}
          onChange={(e) => onChange(ajouterJours(debut, Number(e.target.value)))} aria-label="Date affichée" />
        <div className="marques">
          {marques.map((m) => (
            <button key={m.date + m.titre} className="marque" title={`${m.date} — ${m.titre}`}
              style={{ left: `${(ecartJours(debut, m.date) / total) * 100}%`, background: m.couleur }}
              onClick={() => onChange(m.date)} />
          ))}
        </div>
        <div className="bornes"><span>{dateLongue(debut)}</span><span>{dateLongue(fin)}</span></div>
      </div>
    </div>
  )
}
