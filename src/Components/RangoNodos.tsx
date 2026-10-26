import { useState } from 'react';
import { numeroMaximo, numeroMinimo } from '../Constantes';

interface RangoNodosProps {
  valor: string;
  setValor: (nuevoValor: string) => void;
  bloqueado: boolean;
};

export const RangoNodos = ({valor, setValor, bloqueado}:RangoNodosProps) => {

  const [error, setError] = useState('');
 
  const manejarCambio = (e: React.ChangeEvent<HTMLInputElement>) => {
      const texto = e.target.value;
      setValor(texto);

      if (Number(texto)<numeroMinimo || Number(texto)>numeroMaximo) {
        setError('El numero debe estar dentro del Rango');
      }
      else {
        setError('');
        
      }
  };

  const enviarFormulario = (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      if (valor.trim() === '')
      {
        setError('El campo es obligatorio.');
        return;
      }

      console.log('Valor enviado:', valor);
  };


  return (
    <>  
        <h2>Número de nodos</h2>

        <div className="rango-nodos">
            <span className="limite">{numeroMinimo}</span>
            <span className="operador">≤</span>

            <input
                type="number"
                className="input-nodos"
                min={numeroMinimo}
                max={numeroMaximo}
                value={valor}
                onChange={manejarCambio}
                disabled={bloqueado}
            />

            <span className="operador">≤</span>

            <span className="limite">{numeroMaximo}</span>
        </div>
        
        {error && <p className="error">{error}</p>}
        
        
    </>
  )
}
