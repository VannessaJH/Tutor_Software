from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_router
import uvicorn

print("INICIANDO SCRIPT MAIN.PY")

app = FastAPI(title="Tutor_Software")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://127.0.0.1:3001"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    from routes.auth_routes import router as auth_router
    print(" Auth routes importadas correctamente")
except Exception as e:
    print(f"Error importando auth routes: {e}")


app.include_router(auth_router)


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