from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    contrasena = Column(String(255), nullable=False)
    rol = Column(Enum('Administrador', 'Usuario'), default = 'Usuario')
    
    user_sessions = relationship("UserSession", back_populates="usuario")
