import { useState } from 'react';
import './MatrizAdyacencia.css'

interface MatrizAdyacenciaProps {
  numeroNodos: number;
}

interface PasoWarshall{
    nodo:string;
    matriz:number[][];

}

export const MatrizAdyacencia = ({numeroNodos}: MatrizAdyacenciaProps) => {
    /*===============================================================
        ESTADOS
    ===============================================================*/

    //Crear matriz con cantidad de filas de numeroNodos
    const [matriz, setMatriz] = useState<number[][]>(
        Array.from({ length: numeroNodos }, () =>
            Array(numeroNodos).fill(0)//Por cada fila se crean columnas, dependiendo del parametro Array(numeroNodos). Todas con valor 0
        )
    );

    const [pasos, setPasos] = useState<PasoWarshall[]>([]);
    const [pasoActual, setPasoActual] = useState(0);



    /*===============================================================
        FUNCIONES
    ===============================================================*/

    //Funcion para las letras de las FILAS y COLUMNAS
    const letras = Array.from(
        { length: numeroNodos },
        (_, i) => String.fromCharCode(65 + i)  
    );   

    //Recorre Matriz y busca la celda donde se desea cambiar de valor
    const cambiarValor = (fila: number, columna: number) => {
        setMatriz((matrizActual) =>
            matrizActual.map((valores, i) =>
                valores.map((valor, j) =>
                    i === fila && j === columna ? (valor === 0 ? 1 : 0) : valor
                )       
            )
        );
    };

    const enviarMatriz = async () => {
        try {
            const respuesta = await fetch('http://localhost:8000/matriz', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({ matriz })
            });

            if (!respuesta.ok) {
                throw new Error('Error al enviar la matriz');
            }

            const datos = await respuesta.json();

            const todosLosPasos: PasoWarshall[] = [//En todosLosPasos no guardamos la matriz de caminos que nos envia datos
                {
                    nodo:"Inicial",
                    matriz: datos.matriz_inicial
                },
                ...datos.historial
            ];

            setPasos(todosLosPasos);
            setPasoActual(0);
            console.log("Todos los pasos de Warshall:", todosLosPasos);

            

        } catch (error) {
            console.error('Error de conexión:', error);
        }
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
                    {letras.map((fila, i) => (
                        <tr key={fila}>
                        <th>{fila}</th>

                        {letras.map((columna, j) => (
                            <td key={columna}>
                                <button
                                    type="button"
                                    className="celda-matriz"
                                    onClick={() => cambiarValor(i, j)}
                                    aria-label={`Conexión de ${fila} a ${columna}`}
                                    aria-pressed={matriz[i][j] === 1}
                                >
                                    {matriz[i][j]}
                                </button>
                            </td>
                        ))}
                        </tr>
                    ))}
                    </tbody>

                </table>

            <div className="contenedor-calcular">
                <button type="button" className="btn btn-principal" onClick={enviarMatriz}>
                    Calcular
                </button>
            </div>

            {pasos.length > 0 && (
            <div>
                    <h2>Matriz de caminos</h2>

                    <h3>
                        {pasoActual ===0 ? "Matriz de adyacencia con 1 en la diagonal" : `Paso ${pasoActual} considerando el nodo ${pasos[pasoActual].nodo}`} 
                    </h3>

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
                            {pasos[pasoActual].matriz.map((fila, i) => (
                                <tr key={i}>

                                    <th>{letras[i]}</th>

                                    {fila.map((valor, j) => (
                                        <td key={j}>
                                            <button
                                                type='button'
                                                className='celda-matriz'
                                                aria-pressed={valor === 1}
                                                >
                                                {valor}
                                            </button>
                                        </td>
                                    ))}

                                </tr>
                            ))}
                    </tbody>
                </table>

                <div className="navegacion-pasos">
                    <button
                        type="button"
                        className="btn btn-principal"
                        onClick={() => setPasoActual(pasoActual - 1)}
                        disabled={pasoActual === 0}
                    >
                        Anterior
                    </button>

                    <button
                        type="button"
                        className="btn btn-principal"
                        onClick={() => setPasoActual(pasoActual + 1)}
                        disabled={pasoActual === pasos.length - 1}
                    >
                        Siguiente
                    </button>
                </div>

            </div>
            )}


        </div>
  )}
