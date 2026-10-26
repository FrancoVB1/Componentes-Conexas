import { useState } from 'react'
import './App.css'
import { RangoNodos } from './Components/RangoNodos'
import { TipoGeneracion } from './Components/TipoGeneracion'
import { numeroMaximo, numeroMinimo } from './Constantes';
import { MatrizAdyacencia } from './Components/MatrizAdyacencia';

function App() {
  const [numeroNodos, setNumeroNodos] = useState('4');
  const [tipoGen, setTipoGen] = useState<'Manual' | 'Aleatoria'>('Manual');

  const [nodosGenerados, setNodosGenerados] = useState<number | null>(null);




  const generarGrafo = () => {
      const cantidad = Number(numeroNodos);

      if ( numeroNodos.trim() === '' || !Number.isInteger(cantidad) ||cantidad < numeroMinimo || cantidad > numeroMaximo ) 
      {
          setNodosGenerados(null);
          return;
      }

      setNodosGenerados(cantidad);
  };

  return (
    <>
      <div className="form-nodos">
        <RangoNodos valor={numeroNodos} setValor={setNumeroNodos} bloqueado={nodosGenerados !== null}/>
        <TipoGeneracion tipoGen={tipoGen} setTipoGen={setTipoGen} onGenerar={generarGrafo} bloqueado={nodosGenerados !== null}/>
      </div>

      {nodosGenerados !== null && tipoGen=='Manual' && (
        <MatrizAdyacencia numeroNodos={nodosGenerados}/>
      )}
    </>
  )
}

export default App
