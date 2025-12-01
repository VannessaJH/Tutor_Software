from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importar el router de autenticación (ya existente)
from routes.auth_routes import router as auth_router 
#  Importar el nuevo router del estudiante (desde routes/routes/student_routes.py)
from routes.student_routes import student_bp as student_router 
import uvicorn

# Importar la nueva ruta de semilleros
from routes.semilleros import router as semilleros_router 

print("INICIANDO SCRIPT MAIN.PY")

app = FastAPI(title="Tutor_Software")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://127.0.0.1:3001"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Conexión de Rutas ---

# 1. Rutas de Autenticación
try:
    # Esta importación ya estaba, la incluimos por completitud
    app.include_router(auth_router)
    print(" Rutas de Autenticación importadas correctamente")
except Exception as e:
    print(f"Error al incluir rutas de Autenticación: {e}")

# 2. Rutas del Estudiante (¡NUEVAS!)
try:
    # Conecta el APIRouter definido en student_routes.py
    app.include_router(student_router)
    print(" Rutas de Estudiante importadas y conectadas correctamente")
except Exception as e:
    print(f"Error al incluir rutas de Estudiante: {e}")

# 3. Rutas Académicas: Semilleros (¡NUEVAS!)
try:
    # Conecta el APIRouter definido en routes/academic/semilleros.py
    app.include_router(semilleros_router)
    print(" Rutas de Semilleros importadas y conectadas correctamente")
except Exception as e:
    print(f"Error al incluir rutas de Semilleros: {e}")


@app.get("/")
def root():
    return {"message": " Servidor funcionando"}

print(" ANTES de uvicorn.run")

if __name__ == "__main__":
    print(" EJECUTANDO uvicorn.run()")
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8001, 
        reload=True,
        log_level="info"
    )
    print(" Esta línea no debería verse")