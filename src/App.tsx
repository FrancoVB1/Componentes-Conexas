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




  const generarMatriz = () => {
      const cantidad = Number(numeroNodos);

      if ( numeroNodos.trim() === '' || !Number.isInteger(cantidad) ||cantidad < numeroMinimo || cantidad > numeroMaximo ) 
      {
          setNodosGenerados(null);
          return;
      }

      setNodosGenerados(cantidad);
  };

  const limpiar = () => {
    setNumeroNodos('4');
    setTipoGen('Manual');
    setNodosGenerados(null);
};

  return (
    <>
      <div className="form-nodos">
        <RangoNodos valor={numeroNodos} setValor={setNumeroNodos} bloqueado={nodosGenerados !== null}/>
        <TipoGeneracion tipoGen={tipoGen} setTipoGen={setTipoGen} onGenerar={generarMatriz} onLimpiar={limpiar} bloqueado={nodosGenerados !== null}/>
      </div>

      {nodosGenerados !== null && (
        <MatrizAdyacencia numeroNodos={nodosGenerados} tipoGen={tipoGen}/>
      )}
    </>
  )
}

export default App
