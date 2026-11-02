import { useState } from 'react'
import './ComponentesConexas.css';

interface ComponentesConexasProps {
  matrizCaminos: number[][],
  orden: number[]

}

export const ComponentesConexas = ({matrizCaminos, orden}:ComponentesConexasProps) => {
  const [componentes, setComponentes] = useState<number[][]>([]);
  const [cargando, setCargando] = useState<boolean>(false);
  const [error, setError] = useState('');


  const identificarComponentes = async () => {
    setCargando(true);
    setError('');

    try {
      const respuesta = await fetch('http://localhost:8000/componentes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                matriz: matrizCaminos,
                orden: orden
            })
      });

      if (!respuesta.ok) {
        throw new Error('Error al identificar componentes conexas');
      }

      const datos = await respuesta.json();
      setComponentes(datos.componentes);
        
    } catch (error) {
        console.error('Error:', error);
        setError('No se pudieron identificar las componentes');
    } finally {
      setCargando(false);
    }

  };
  return (
    <section className="componentes-conexas">
        <button
            className="btn btn-principal"
            onClick={identificarComponentes}
            disabled={cargando}
        >
            {cargando ? 'Calculando...' : 'Identificar componentes'}
        </button>

        {error && <p className="error">{error}</p>}

        {componentes.length > 0 && (
            <div className="resultado-componentes">
                <h2>Componentes fuertemente conexas:</h2>
                <p>Total de componentes: {componentes.length}</p>

                {componentes.map((componente, i) => (
                        <p key={i}>
                            <strong>Componente {i + 1}:</strong>{' '}
                            {'{ '}
                            {componente
                                .map((indice) => String.fromCharCode(65 + indice))
                                .join(', ')}
                            {' }'}
                        </p>
                ))}



            </div>
        )}
    </section>
  )
}
