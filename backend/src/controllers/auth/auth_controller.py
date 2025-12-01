from sqlalchemy.orm import Session
from models.user.usuario import Usuario
from sqlalchemy import func, desc, literal_column
from models.evaluation.Evaluacion_Usuario import EvaluacionUsuario
from sqlalchemy import update
from models.user.usuarios_pendientes import UsuariosPendientes
from passlib.context import CryptContext
from fastapi import HTTPException


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
                print ("Nombre de usuario incorrecto")
                return {"error": "Crendeciales incorrectas"}
            
            if not pwd_context.verify(credenciales["contrasena"], usuario.contrasena):
                print(f"Contraseña para verificar: {credenciales["contrasena"]}, contrasena guardada {usuario.contrasena}, la contraseña es incorrecta")
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
        
    @staticmethod
    def aceptar_usuario(db: Session, id_usuario_pendiente: int):
        usuario_pendiente = db.query(UsuariosPendientes).filter(
            UsuariosPendientes.id == id_usuario_pendiente
        ).first()
        
        if not usuario_pendiente:
            return None 

        nuevo_usuario = Usuario(
            nombre=usuario_pendiente.nombre,
            correo=usuario_pendiente.correo,
            contrasena=usuario_pendiente.contrasena,
            rol=usuario_pendiente.rol
        )
        
        db.add(nuevo_usuario)
        
     
        db.delete(usuario_pendiente)
        
        db.commit()
        return nuevo_usuario
    
    @staticmethod
    def rechazar_usuario(db: Session, id_usuario_pendiente: int):
        usuario_pendiente = db.query(UsuariosPendientes).filter(
            UsuariosPendientes.id == id_usuario_pendiente
        ).first()
        
        if not usuario_pendiente:
            return None 


        db.delete(usuario_pendiente)
        db.commit()
        return True
    
    @staticmethod
    def obtener_todos_los_usuarios(db: Session):
        """Obtiene todos los usuarios de la base de datos (para gestión del Admin)."""
        return db.query(Usuario).all()

    @staticmethod
    def eliminar_usuario(db: Session, user_id: int):
        """Elimina un usuario de la tabla Usuario por su ID."""
        usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
        
        if not usuario:
            return False 
            
        db.delete(usuario)
        db.commit()
        return True 
    
    @staticmethod
    def buscar_usuario_por_nombre(db: Session, nombre_usuario: str):
        """Busca usuarios por nombre para la interfaz de modificación."""
        
        usuarios = db.query(Usuario).filter(
            Usuario.nombre_usuario.ilike(f"%{nombre_usuario}%")
        ).all()
        
        return [
            {"id": u.id, "nombre": u.nombre_usuario, "correo": u.correo, "rol": u.rol}
            for u in usuarios
        ]

    @staticmethod
    def modificar_usuario(db: Session, user_id: int, datos_actualizacion: dict):
        """Actualiza los campos de un usuario específico."""
        
        campos_a_actualizar = {}
        
        if 'nombre' in datos_actualizacion:
            campos_a_actualizar['nombre_usuario'] = datos_actualizacion['nombre']
        if 'correo' in datos_actualizacion:
            campos_a_actualizar['correo'] = datos_actualizacion['correo']
            
        if not campos_a_actualizar:
            return 0 
            
        
        stmt = (
            update(Usuario)
            .where(Usuario.id == user_id)
            .values(**campos_a_actualizar)
        )
        
        resultado = db.execute(stmt)
        db.commit()
        
        return resultado.rowcount 
    
    @staticmethod
    def obtener_reporte_resultados(db: Session):
        """
        Devuelve el puntaje y la fecha del registro de evaluación MÁS RECIENTE para cada usuario.
        """
        try:
        
            subconsulta_ranking = (
                db.query(
                    EvaluacionUsuario.id_usuario,
                    EvaluacionUsuario.id_evaluacion,
                    EvaluacionUsuario.fecha,
                    EvaluacionUsuario.puntaje,
                    func.row_number()
                    .over(
                        partition_by=EvaluacionUsuario.id_usuario,
                        order_by=desc(EvaluacionUsuario.fecha) 
                    )
                    .label('rn') 
                )
                .subquery()
            )

            
            reporte = (
                db.query(
                    Usuario.id.label("id_usuario"),
                    Usuario.nombre_usuario.label("nombre_usuario"), 
                    subconsulta_ranking.c.puntaje.label("puntaje_reciente"), 
                    subconsulta_ranking.c.fecha.label("fecha_evaluacion")    
                )
                .join(subconsulta_ranking, Usuario.id == subconsulta_ranking.c.id_usuario)
                .filter(subconsulta_ranking.c.rn == 1) 
                .order_by(desc(subconsulta_ranking.c.fecha))
                .all()
            )
            
       
            return [
                {
                    "id_usuario": r.id_usuario,
                    "nombre_usuario": r.nombre_usuario,
                    "puntaje": r.puntaje, 
                    "fecha": r.fecha.isoformat() 
                } 
                for r in reporte
            ]

        except Exception as e:
            print(f"Error al generar el reporte de resultados (último registro): {e}")
            raise HTTPException(
                status_code=500, 
                detail="Error interno del servidor al obtener el reporte de resultados."
            )
            
    @staticmethod
    def obtener_historial_evaluaciones(db: Session, id_usuario: int):
        """
        Devuelve el listado completo de todas las evaluaciones de un usuario,
        ordenadas por fecha descendente.
        """
        evaluaciones = (
            db.query(EvaluacionUsuario)
            .filter(EvaluacionUsuario.id_usuario == id_usuario)
            .order_by(desc(EvaluacionUsuario.fecha)) 
            .all()
        )

        if not evaluaciones:
            return [] 

        return [
            {
                "id_evaluacion": e.id_evaluacion,
                "puntaje": e.puntaje,
                "fecha": e.fecha.isoformat(),
         
            } 
            for e in evaluaciones
        ]
        
    