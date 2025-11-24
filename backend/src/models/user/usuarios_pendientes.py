from sqlalchemy import Column, Integer, String, Enum
from config.database import Base

class UsuariosPendientes(Base):
    __tablename__ = 'usuarios_pendientes'
    
    id = Column(Integer(), primary_key = True)
    nombre = Column(String(100), nullable = False)
    correo = Column(String(100), nullable = False)
    contrasena = Column(String(255), nullable=False)
    estado = Column(Enum('Aceptado', 'Pendiente', 'Rechazado' ), default = 'Pendiente')
