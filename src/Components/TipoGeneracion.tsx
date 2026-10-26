import { useState } from 'react'

interface TipoGeneracion {
    tipoGen: 'Manual' | 'Aleatoria';
    setTipoGen: (tipo: 'Manual' | 'Aleatoria') => void;
    onGenerar: ()=> void;
    bloqueado: boolean;
}

export const TipoGeneracion = ({tipoGen, setTipoGen, onGenerar, bloqueado}: TipoGeneracion) => {
 
  return (
    <>
        <div className="tipo-generacion" role="group" aria-label="Tipo de generación">
            {(['Manual', 'Aleatoria'] as const).map((tipo) => (
                <button
                key={tipo}
                type="button"
                className={`btn ${tipoGen === tipo ? 'btn-principal' : 'btn-secundario'}`}
                aria-pressed={tipoGen === tipo}
                onClick={() => setTipoGen(tipo)}
                disabled={bloqueado}
                >
                {tipo}
                </button>
            ))}
        </div>

        <button type="button" className="btn btn-secundario" onClick={onGenerar} disabled={bloqueado}>
            Siguiente
        </button>
    </>
  )
}
