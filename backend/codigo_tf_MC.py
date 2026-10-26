# ==============================================
# PRIMERA ENTREGA - AVANCE FUNCIONAL
# COMPONENTES CONEXAS
# ==============================================

# LIBRERÍAS UTILIZADAS
# ------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import random


# 1. VALIDACIÓN DE LA CANTIDAD DE NODOS
# ------------------------------------------------------------
while True:
    try:
        x = int(input("Ingresa la cantidad de nodos (4<=x<=12)\n"))
        if 4 <= x <= 12:
            break
        else:
            print("Tener en cuenta el rango (4<=x<=12)\n")
    except ValueError:
        print("Ingresar números (4<=x<=12)\n")


# 2. ELECCIÓN DEL TIPO DE GENERACIÓN
# ------------------------------------------------------------
while True:
    try:
        print("Selecciona el tipo de generación del grafo.\n")
        print("1. Generación manual.\n")
        print("2. Generación aleatoria.\n")
        w = int(input("Opción: "))
        if w == 1 or w == 2:
            break
        else:
            print("Tener en cuenta el número de las opciones.\n")
    except ValueError:
        print("Ingresar números correspondientes a las opciones.\n")


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def nombre_nodo(i):
    return chr(65 + i)


def mostrar_matriz(matriz, titulo="MATRIZ", orden=None):
    """
    Muestra la matriz.
    Si 'orden' se proporciona, las etiquetas de filas y columnas
    se muestran en el mismo orden en que fueron reordenadas.
    """
    n = len(matriz)

    if orden is None:
        orden = list(range(n))

    etiquetas = [nombre_nodo(i) for i in orden]

    print("\n" + titulo)
    print("    " + " ".join(f"{etiqueta:>2}" for etiqueta in etiquetas))

    for i in range(n):
        fila = " ".join(f"{matriz[i][j]:>2}" for j in range(n))
        print(f"{etiquetas[i]:>2}  {fila}")


# 3. GENERACIÓN DEL GRAFO
# ------------------------------------------------------------

def generar_manual(n):

    matriz = np.zeros((n, n), dtype=int)

    print("\n--- GENERACIÓN MANUAL ---")
    print("El grafo es dirigido.")
    print("Ingresa 1 si existe la conexión indicada y 0 si no existe.\n")

    for i in range(n):

        for j in range(n):

            if i != j:

                while True:

                    try:

                        valor = int(
                            input(
                                f"¿Existe conexión "
                                f"{nombre_nodo(i)} -> {nombre_nodo(j)}? (1/0): "
                            )
                        )

                        if valor in (0, 1):

                            matriz[i][j] = valor

                            break

                        else:

                            print("Solo se permite ingresar 1 o 0.")

                    except ValueError:

                        print("Ingresar solamente 1 o 0.")

    return matriz


def generar_aleatorio(n):

    matriz = np.zeros((n, n), dtype=int)

    probabilidad = 0.40

    for i in range(n):

        for j in range(n):

            if i != j:

                if random.random() < probabilidad:

                    matriz[i][j] = 1

    return matriz


# 4. MATRIZ DE CAMINOS
# ------------------------------------------------------------

def calcular_matriz_caminos(matriz):

    n = len(matriz)

    # Copiamos la matriz de adyacencia
    caminos = matriz.copy()

    # Paso 1: Agregar 1 en la diagonal para indicar que cada nodo es alcanzable desde sí mismo.

    for i in range(n):
        caminos[i][i] = 1

    mostrar_matriz(
        caminos,
        "MATRIZ DE ADYACENCIA CON 1 EN LA DIAGONAL"
    )

    input("\nPresiona ENTER para iniciar el cálculo de la matriz de caminos...")

    # Cálculo de la matriz de caminos
    # mediante el procedimiento de Warshall:
    # si i llega a k y k llega a j, entonces i llega a j.
    for k in range(n):

        for i in range(n):

            for j in range(n):

                if caminos[i][j] == 0:

                    if caminos[i][k] == 1 and caminos[k][j] == 1:

                        caminos[i][j] = 1

        print("\n----------------------------------------")
        print(f"Paso {k + 1}: considerando el nodo {nombre_nodo(k)}")
        print("----------------------------------------")

        mostrar_matriz(caminos, "MATRIZ DE CAMINOS")

        input("\nPresiona ENTER para continuar...")

    return caminos


# 5. ORDENAMIENTO DE FILAS Y COLUMNAS
# ------------------------------------------------------------

def ordenar_matriz(caminos):

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

    print("\n========================================")
    print("ORDENAMIENTO DE FILAS")
    print("========================================")

    for posicion, i in enumerate(orden, start=1):

        print(
            f"{posicion}. Nodo {nombre_nodo(i)} "
            f"-> {cantidades[i]} unos"
        )

    # Reordenar filas y columnas con el mismo orden
    matriz_ordenada = caminos[np.ix_(orden, orden)]

    print("\n========================================")
    print("MATRIZ REORDENADA")
    print("========================================")

    mostrar_matriz(
        matriz_ordenada,
        "MATRIZ DE CAMINOS REORDENADA",
        orden
    )

    input("\nPresiona ENTER para identificar las componentes...")

    return matriz_ordenada, orden


# 6. IDENTIFICACIÓN DE COMPONENTES
# ------------------------------------------------------------

def encontrar_componentes(caminos, orden):

    n = len(caminos)

    visitados = [False] * n

    componentes = []

    print("\n========================================")
    print("IDENTIFICACIÓN DE COMPONENTES")
    print("========================================")

    # Se recorren los nodos respetando el orden obtenido
    # en el paso anterior.
    for nodo in orden:

        if not visitados[nodo]:

            componente = []

            for j in orden:

                # Dos nodos pertenecen a la misma componente
                # cuando existe camino de nodo -> j
                # y también de j -> nodo.
                if (
                    caminos[nodo][j] == 1
                    and caminos[j][nodo] == 1
                ):

                    componente.append(j)

                    visitados[j] = True

            componentes.append(componente)

    print("\nBloques diagonales encontrados:")

    for numero, componente in enumerate(componentes, start=1):

        nombres = [
            nombre_nodo(nodo)
            for nodo in componente
        ]

        print(f"\nBloque {numero}:")
        print(
            "{ "
            + ", ".join(nombres)
            + " }"
        )

    return componentes


# 7. REPRESENTACIÓN GRÁFICA
# ------------------------------------------------------------

def mostrar_grafo(matriz):

    n = len(matriz)

    angulos = np.linspace(
        0,
        2 * np.pi,
        n,
        endpoint=False
    )

    posiciones = {}

    for i in range(n):

        posiciones[i] = (
            np.cos(angulos[i]),
            np.sin(angulos[i])
        )

    plt.figure(figsize=(8, 8))

    # --------------------------------------------------------
    # Dibujar las conexiones dirigidas
    # --------------------------------------------------------

    for i in range(n):

        for j in range(n):

            if i != j and matriz[i][j] == 1:

                x1, y1 = posiciones[i]
                x2, y2 = posiciones[j]

                # Si existe conexión en ambos sentidos,
                # utilizamos una pequeña curvatura.
                if matriz[j][i] == 1:

                    curvatura = 0.15 if i < j else -0.15

                    plt.annotate(
                        "",
                        xy=(x2, y2),
                        xytext=(x1, y1),
                        arrowprops=dict(
                            arrowstyle="->",
                            connectionstyle=f"arc3,rad={curvatura}",
                            linewidth=1.5,
                            shrinkA=18,
                            shrinkB=18
                        )
                    )

                else:

                    plt.annotate(
                        "",
                        xy=(x2, y2),
                        xytext=(x1, y1),
                        arrowprops=dict(
                            arrowstyle="->",
                            linewidth=1.5,
                            shrinkA=18,
                            shrinkB=18
                        )
                    )

    # --------------------------------------------------------
    # Dibujar nodos
    # --------------------------------------------------------

    for i in range(n):

        x_pos, y_pos = posiciones[i]

        plt.scatter(
            x_pos,
            y_pos,
            s=900,
            edgecolors="black",
            zorder=2
        )

        plt.text(
            x_pos,
            y_pos,
            nombre_nodo(i),
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold",
            zorder=3
        )

    plt.xlim(-1.35, 1.35)
    plt.ylim(-1.35, 1.35)

    plt.title("Representación del grafo dirigido")

    plt.axis("off")

    plt.tight_layout()

    plt.show()


# 8. CONSTRUCCIÓN DEL GRAFO
# ------------------------------------------------------------

if w == 1:

    matriz = generar_manual(x)

else:

    matriz = generar_aleatorio(x)


print("\nGrafo construido correctamente.")

mostrar_matriz(
    matriz,
    "MATRIZ DE ADYACENCIA"
)


input(
    "\nPresiona ENTER para calcular las componentes conexas..."
)


# 9. MATRIZ DE CAMINOS
# ------------------------------------------------------------

matriz_caminos = calcular_matriz_caminos(matriz)


# 10. ORDENAR FILAS Y COLUMNAS
# ------------------------------------------------------------

matriz_ordenada, orden = ordenar_matriz(
    matriz_caminos
)


# 11. IDENTIFICAR COMPONENTES
# ------------------------------------------------------------

componentes = encontrar_componentes(
    matriz_caminos,
    orden
)


# 12. RESULTADO FINAL
# ------------------------------------------------------------

print("\n\n========================================")
print("          RESULTADO FINAL")
print("========================================")

print(
    f"Número total de componentes conexas: "
    f"{len(componentes)}"
)

for i, componente in enumerate(componentes, start=1):

    nombres = [
        nombre_nodo(nodo)
        for nodo in componente
    ]

    print(
        f"Componente {i}: "
        "{ "
        + ", ".join(nombres)
        + " }"
    )


# 13. REPRESENTACIÓN GRÁFICA FINAL
# ------------------------------------------------------------

mostrar_grafo(matriz)

print("\nPrograma finalizado.")
