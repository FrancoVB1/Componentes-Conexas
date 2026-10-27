from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.algoritmos import calcular_matriz_caminos
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class MatrizEntrada(BaseModel):
    matriz: list[list[int]]

#Metodos:
@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando correctamente"}

@app.post("/matriz")
def recibir_matriz(datos: MatrizEntrada):
    matriz = datos.matriz

    matriz_inicial, pasos, matriz_caminos = calcular_matriz_caminos(matriz)

    return {
        "matriz_inicial": matriz_inicial,
        "historial": pasos,
        "matriz_caminos": matriz_caminos
    }