from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class MatrizEntrada(BaseModel):
    matriz: list[list[int]]

@app.get("/")
def inicio():
    return {"message": "Hello World"}

@app.post("/matriz")
def recibir_matriz(datos: MatrizEntrada):
    matriz = datos.matriz

    print("Matriz recibida:", matriz)

    return {
        "mensaje": "Matriz recibida correctamente",
        "matriz": matriz
    }