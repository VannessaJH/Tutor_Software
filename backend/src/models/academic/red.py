from sqlalchemy import Column, Integer, String, Text
from config.database import Base

class Red(Base):
    __tablename__ = 'redes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    tipo = Column(String(50))  # 'investigacion', 'colaboracion', 'academica'
    enlace = Column(String(500))
    activa = Column(Boolean, default=True)