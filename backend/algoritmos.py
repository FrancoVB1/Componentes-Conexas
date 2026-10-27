#=======================================================
#FUNCIONES PARA EL PROCESAMIENTO DEL GRAFO
#=======================================================


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