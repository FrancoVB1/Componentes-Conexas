from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .algoritmos import calcular_matriz_caminos, encontrar_componentes, ordenar_matriz
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class MatrizEntrada(BaseModel):
    matriz: list[list[int]]

class ComponentesEntrada(BaseModel):
    matriz: list[list[int]]
    orden: list[int]


#Metodos:
@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando correctamente"}

@app.post("/matriz")
def recibir_matriz(datos: MatrizEntrada):
    matriz = datos.matriz

    matriz_inicial, pasos, matriz_caminos = calcular_matriz_caminos(matriz)

    matriz_ordenada, orden = ordenar_matriz(matriz_caminos)
    return {
        "matriz_inicial": matriz_inicial,
        "historial": pasos,
        "matriz_caminos": matriz_caminos,
        "matriz_ordenada": matriz_ordenada,
        "orden": orden
    }

@app.post("/componentes")
def recibir_componentes(datos: ComponentesEntrada):
    matriz_caminos = datos.matriz
    orden = datos.orden

    componentes = encontrar_componentes(matriz_caminos, orden)

    return {
        "componentes": componentes
    }