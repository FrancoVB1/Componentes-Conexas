import { useState } from 'react';
import './MatrizAdyacencia.css'

interface MatrizAdyacenciaProps {
  numeroNodos: number;
}

export const MatrizAdyacencia = ({numeroNodos}: MatrizAdyacenciaProps) => {

    //Funcion para las letras de las FILAS y COLUMNAS
    const letras = Array.from(
        { length: numeroNodos },
        (_, i) => String.fromCharCode(65 + i)  
    );

    //Crear matriz con cantidad de filas de numeroNodos
    const [matriz, setMatriz] = useState<number[][]>(
        Array.from({ length: numeroNodos }, () =>
            Array(numeroNodos).fill(0)//Por cada fila se crean columnas, dependiendo del parametro Array(numeroNodos). Todas con valor 0
        )
    );

    const cambiarValor = (fila: number, columna: number) => {
        setMatriz((matrizActual) =>
            matrizActual.map((valores, i) =>
                valores.map((valor, j) =>
                    i === fila && j === columna ? (valor === 0 ? 1 : 0) : valor
                )       
            )
        );
    };

  return (
        <div className="matriz-adyacencia">
            <h2>Matriz de adyacencia</h2>

                <table>
                    <thead>
                        <tr>
                            <th></th>

                            {letras.map((letra) => (
                            <th key={letra}>{letra}</th>
                            ))}
                        </tr>
                    </thead>

                    <tbody>
                    {letras.map((fila) => (
                        <tr key={fila}>
                        <th>{fila}</th>

                        {letras.map((columna) => (
                            <td key={columna}>0</td>
                        ))}
                        </tr>
                    ))}
                    </tbody>

                </table>
        </div>
  )
}
