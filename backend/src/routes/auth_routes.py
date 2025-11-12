from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.auth.auth_controller import AuthController


router = APIRouter(prefix="/api/auth", tags=["Autenticación"])

@router.post("/registrar")
async def registrar_usuario(
    datos_usuario: dict,
    db: Session = Depends(get_db)
):  
    print(f"ENDPOINT: Datos recibidos: {datos_usuario}")
    return AuthController.registrar_usuario(db, datos_usuario)
        
    

@router.post("/login")
async def login(
    credenciales: dict,
    db: Session = Depends(get_db)
):
    return AuthController.login_usuario(db, credenciales)