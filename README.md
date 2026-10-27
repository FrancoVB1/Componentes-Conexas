# Componentes Conexas

Aplicación web para trabajar con grafos dirigidos, calcular la matriz de caminos mediante el algoritmo de Warshall e identificar componentes fuertemente conexas.

El proyecto utiliza **React + TypeScript** para la interfaz gráfica y **Python + FastAPI** para el procesamiento de las matrices.

## Tecnologías utilizadas

**Frontend**
- React
- TypeScript
- Vite
- CSS

**Backend**
- Python
- FastAPI
- Uvicorn
- NumPy
- Matplotlib

## Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (incluye npm)
- [Python](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/) (recomendado)

## Instalación

### 1. Clonar el repositorio

Abrir una terminal (CMD, PowerShell o la terminal de Visual Studio Code) y ejecutar:

```bash
git clone https://github.com/FrancoVB1/Componentes-Conexas.git
```

Ingresar a la carpeta del proyecto:

```bash
cd Componentes-Conexas
```

Abrir esta carpeta en Visual Studio Code.

### 2. Instalar las dependencias del frontend

Desde la carpeta principal del proyecto, ejecutar:

```bash
npm install
```

Este comando instala las dependencias de React, TypeScript y Vite registradas en `package.json`.

### 3. Instalar las dependencias del backend

Desde la misma carpeta principal del proyecto, ejecutar:

```bash
python -m pip install -r backend/requirements.txt
```

Este comando instala las librerías indicadas en `requirements.txt`:

- FastAPI
- Uvicorn
- NumPy
- Matplotlib

## Ejecución del proyecto

Para ejecutar la aplicación es necesario iniciar **dos servidores en terminales separadas**: uno para React y otro para Python.

Ambos comandos deben ejecutarse desde la carpeta principal del proyecto (`Componentes-Conexas`).

### Terminal 1: Iniciar React (frontend)

Abrir la carpeta del proyecto en Visual Studio Code y abrir una terminal desde **Terminal → New Terminal**.

Ejecutar:

```bash
npm run dev
```

Vite mostrará una dirección similar a:

```text
http://localhost:5173/
```

Abrir esa dirección en el navegador para utilizar la aplicación.

### Terminal 2: Iniciar FastAPI (backend)

Sin cerrar la primera terminal, abrir una segunda terminal en Visual Studio Code.

Desde la misma carpeta principal del proyecto, ejecutar:

```bash
python -m uvicorn backend.main:app --reload
```

El servidor Python estará disponible en:

```text
http://127.0.0.1:8000
```

Para probar los endpoints de FastAPI, abrir:

```text
http://127.0.0.1:8000/docs
```

**Importante:** mantener ambas terminales abiertas mientras se utiliza la aplicación.

También es posible ejecutar los comandos desde CMD o PowerShell, siempre que la terminal esté ubicada en la carpeta principal del proyecto.

## Funcionalidades implementadas

- Selección de la cantidad de nodos, entre 4 y 12.
- Construcción manual de una matriz de adyacencia.
- Modificación interactiva de las conexiones del grafo.
- Envío de la matriz desde React a Python mediante HTTP POST.
- Cálculo de la matriz de caminos utilizando el algoritmo de Warshall.
- Almacenamiento de las matrices intermedias correspondientes a cada nodo considerado.
- Visualización de la evolución del algoritmo.
- Navegación entre las matrices mediante los botones Anterior y Siguiente.

## Organización del proyecto

```text
Componentes-Conexas/
├── backend/
│   ├── main.py
│   ├── algoritmos.py
│   ├── codigo_tf_MC.py
│   └── requirements.txt
├── src/
│   └── Components/
├── public/
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

### Descripción de los archivos principales

- `backend/main.py`: configuración de FastAPI y definición de los endpoints HTTP.
- `backend/algoritmos.py`: funciones de procesamiento del grafo, incluyendo Warshall.
- `backend/codigo_tf_MC.py`: implementación original del programa en Python.
- `backend/requirements.txt`: dependencias necesarias para ejecutar el backend.
- `src/`: código de la interfaz desarrollada con React y TypeScript.
- `package.json`: dependencias y comandos del frontend.
- `.gitignore`: archivos y carpetas que Git debe ignorar.

## Estado del proyecto

El proyecto se encuentra en desarrollo.

Actualmente se ha implementado la construcción manual de matrices de adyacencia, su comunicación con FastAPI y el cálculo de la matriz de caminos mediante Warshall, incluyendo la visualización de sus pasos intermedios.

Las siguientes funcionalidades están previstas para futuras etapas:

- Generación aleatoria de grafos desde la interfaz web.
- Ordenamiento de filas y columnas de la matriz de caminos.
- Identificación de componentes fuertemente conexas.
- Representación gráfica de los grafos y sus conexiones.