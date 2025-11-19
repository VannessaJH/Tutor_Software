from sqlalchemy.orm import Session
from models.user.usuario import Usuario
from models.user.usuarios_pendientes import UsuariosPendientes
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthController:
    
    @staticmethod
    def registrar_usuario(db: Session, datos_usuario: dict):
        try:
           
            usuario_existente = db.query(Usuario).filter(
                Usuario.correo == datos_usuario["correo"]
            ).first()
            
            if usuario_existente:
                return {"error": "El correo ya está registrado"}
            
            contrasena_encriptada = pwd_context.hash(datos_usuario["contrasena"])
          
      
            nuevo_usuario = Usuario(
                nombre_usuario=datos_usuario["nombre"],
                correo=datos_usuario["correo"],
                contrasena=contrasena_encriptada,  
            )
            
    
            db.add(nuevo_usuario)
            db.commit()
            db.refresh(nuevo_usuario)
            
            return {
                "mensaje": "Usuario registrado correctamente",
                "id_usuario": nuevo_usuario.id,
            }
            
        except Exception as e:
            db.rollback()
            return {"error": f"Error al registrar usuario: {str(e)}"}
        
    @staticmethod
    def usuario_pendiente(db: Session, datos_usuario: dict):
        try:
           
            usuario_existente = db.query(UsuariosPendientes).filter(
                UsuariosPendientes.correo == datos_usuario["correo"]
            ).first()
            
            if usuario_existente:
                return {"error": "El correo ya está registrado"}
            
            contrasena_encriptada = pwd_context.hash(datos_usuario["contrasena"])
          
      
            usuario_pendiente = UsuariosPendientes(
                nombre=datos_usuario["nombre"],
                correo=datos_usuario["correo"],
                contrasena=contrasena_encriptada, 
                estado = 'Pendiente' 
            )
            
    
            db.add(usuario_pendiente)
            db.commit()
            db.refresh(usuario_pendiente)
            
            return {
                "mensaje": "El usuario ha sido puesto en espera",
                "id_usuario": usuario_pendiente.id,
                "rol": usuario_pendiente.rol
            }
            
        except Exception as e:
            db.rollback()
            return {"error": f"Error al registrar usuario: {str(e)}"}
            
        
    @staticmethod
    def login_usuario(db: Session, credenciales: dict):
        try:
            usuario = db.query(Usuario).filter(
                Usuario.nombre_usuario == credenciales["usuario"]
            ).first()
            
            if not usuario:
                return {"error": "Crendeciales incorrectas"}
            
            if not pwd_context.verify(credenciales["contrasena"], usuario.contrasena):
                return {"error": "Credenciales incorrectas"}
            
            return {
                "mensaje": "Login exitoso", 
                "id_usuario": usuario.id,
                "nombre_usuario": usuario.nombre_usuario, 
                "correo": usuario.correo,
                "rol": usuario.rol
                
            }
        except Exception as e:
            return {"error":f"Error en login: {str(e)}"}
        
    @staticmethod
    def obtener_usuarios_pendientes(db:Session):
        try:
            usuarios_pendientes = db.query(UsuariosPendientes).all()
            return usuarios_pendientes
        except Exception as e:
            print(f"Error obteniendo usuarios pendientes: {e}")
            return []
        
    