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
   
    resultado = AuthController.aceptar_usuario(db, id_usuario_pendiente)
    
    if resultado is None:
        return {"error": "Usuario pendiente no encontrado"}, 404
        
    return {"mensaje": "Usuario aceptado y registrado correctamente"}

@router.delete("/rechazar_usuario/{id_usuario_pendiente}")
async def rechazar_usuario(id_usuario_pendiente: int, db: Session = Depends(get_db)):

    resultado = AuthController.rechazar_usuario(db, id_usuario_pendiente)
    
    if resultado is None:
        return {"error": "Usuario pendiente no encontrado"}, 404
        
    return {"mensaje": "Usuario rechazado y eliminado de la lista de pendientes"}

@router.get("/usuarios_activos")
async def obtener_usuarios_activos(
    db: Session = Depends(get_db)
):
    """
    Ruta para que el administrador obtenga la lista completa de usuarios (activos, rechazados, etc.).
    """
    return AuthController.obtener_todos_los_usuarios(db)


@router.delete("/usuario/{user_id}")
async def eliminar_usuario(
    user_id: int, 
    db: Session = Depends(get_db)
):
    """
    Ruta para que el administrador elimine un usuario por su ID.
    """
    exito = AuthController.eliminar_usuario(db, user_id)
    
    if not exito:
        
        return {"error": f"Usuario con ID {user_id} no encontrado o no pudo ser eliminado"}, 404
        
    return {"mensaje": f"Usuario con ID {user_id} eliminado correctamente"}

@router.get("/usuarios/buscar")
async def buscar_usuario(
    nombre: str, 
    db: Session = Depends(get_db)
):
    """Ruta para buscar usuarios por nombre (para modificar)."""
    return AuthController.buscar_usuario_por_nombre(db, nombre)


@router.put("/usuario/{user_id}")
async def modificar_usuario(
    user_id: int, 
    datos: dict, 
    db: Session = Depends(get_db)
):
    """Ruta para actualizar los datos de un usuario por su ID."""
    
    filas_afectadas = AuthController.modificar_usuario(db, user_id, datos)
    
    if filas_afectadas == 0:
        return {"error": f"Usuario con ID {user_id} no encontrado o no se pudo actualizar"}, 404
        
    return {"mensaje": f"Usuario con ID {user_id} modificado correctamente"}