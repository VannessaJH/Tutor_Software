from sqlalchemy.orm import Session
from models.user.usuario import Usuario
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
                rol=datos_usuario["rol"]
            )
            
    
            db.add(nuevo_usuario)
            db.commit()
            db.refresh(nuevo_usuario)
            
            return {
                "mensaje": "Usuario registrado correctamente",
                "id_usuario": nuevo_usuario.id,
                "rol": nuevo_usuario.rol
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
                "rol":usuario.rol,
                "correo": usuario.correo
            }
        except Exception as e:
            return {"error":f"Error en login: {str(e)}"}