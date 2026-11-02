#=======================================================
#FUNCIONES PARA EL PROCESAMIENTO DEL GRAFO
#=======================================================
import numpy as np

def nombre_nodo(i):
    return chr(65 + i)

def calcular_matriz_caminos(matriz):
    n = len(matriz)

    # Copiamos la matriz de adyacencia
    caminos = [fila.copy() for fila in matriz]

    # Agregamos 1 en la diagonal
    for i in range(n):
        caminos[i][i] = 1

    # Guardamos la matriz inicial
    matriz_inicial = [fila.copy() for fila in caminos]

    pasos = []

    # Algoritmo de Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if caminos[i][j] == 0:
                    if caminos[i][k] == 1 and caminos[k][j] == 1:
                        caminos[i][j] = 1

        pasos.append({
            "nodo": nombre_nodo(k),
            "matriz": [fila.copy() for fila in caminos]
        })

    return matriz_inicial, pasos, caminos


def ordenar_matriz(caminos):
    caminos = np.array(caminos)

    n = len(caminos)

    # Cantidad de unos de cada fila
    cantidades = np.sum(caminos, axis=1)

    # Primera posición donde aparece un 1
    primera_posicion = []

    for i in range(n):
        posiciones = np.where(caminos[i] == 1)[0]

        if len(posiciones) > 0:
            primera_posicion.append(posiciones[0])
        else:
            primera_posicion.append(n)

    # Orden:
    # 1. Mayor cantidad de unos
    # 2. El 1 más cercano a la primera columna
    orden = sorted(
        range(n),
        key=lambda i: (-cantidades[i], primera_posicion[i])
    )

    # Reordenar filas y columnas con el mismo orden
    matriz_ordenada = caminos[np.ix_(orden, orden)]

    return matriz_ordenada.tolist(), orden


def encontrar_componentes(caminos, orden):
    n = len(caminos)
    visitados = set()
    componentes = []

    for nodo in orden:
        if nodo in visitados:
            continue

        componente = []

        for j in orden:
            if (
                j not in visitados
                and caminos[nodo][j] == 1
                and caminos[j][nodo] == 1
            ):
                componente.append(j)

        visitados.update(componente)
        componentes.append(componente)

    return componentes