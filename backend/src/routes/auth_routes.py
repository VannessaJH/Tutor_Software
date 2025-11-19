from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.auth.auth_controller import AuthController
from models.user.usuario import Usuario
from models.user.usuarios_pendientes import UsuariosPendientes


router = APIRouter(prefix="/api/auth", tags=["Autenticación"])

@router.post("/registrar")
async def registrar_usuario(
    datos_usuario: dict,
    db: Session = Depends(get_db)
):  
    print(f"ENDPOINT: Datos recibidos: {datos_usuario}")
    return AuthController.registrar_usuario(db, datos_usuario)



@router.post("/usuario_pendiente")
async def usuario_pendiente(
    datos_usuario: dict,
    db: Session = Depends(get_db)
):
    print(f"ENDPOINT: Datos recibidos: {datos_usuario}")
    return AuthController.usuario_pendiente(db, datos_usuario)

@router.get("/obtener_usuarios_pendientes")
async def obtener_usuarios_pendientes(
    db: Session = Depends(get_db)
):
    print("ENDPOINT: obteniendo usuarios pendientes")
    return AuthController.obtener_usuarios_pendientes(db)
        
    

@router.post("/login")
async def login(
    credenciales: dict,
    db: Session = Depends(get_db)
):
    return AuthController.login_usuario(db, credenciales)

@router.post("/aceptar_usuario/{id_usuario_pendiente}")
async def aceptar_usuario(id_usuario_pendiente: int, db: Session = Depends(get_db)):

    usuario_pendiente = db.query(UsuariosPendientes).filter(
        UsuariosPendientes.id == id_usuario_pendiente
    ).first()
    
    if not usuario_pendiente:
        return {"error": "Usuario pendiente no encontrado"}
    

    nuevo_usuario = Usuario(
        nombre=usuario_pendiente.nombre,
        correo=usuario_pendiente.correo,
        contrasena=usuario_pendiente.contrasena,
        rol=usuario_pendiente.rol
    )
    
    db.add(nuevo_usuario)
    
    db.delete(usuario_pendiente)
    
    db.commit()
    return {"mensaje": "Usuario aceptado correctamente"}