from sqlalchemy import Column, Integer, String, DATETIME, Float
from config.database import Base

class Evaluacion(Base):
    __tablename__ = 'evaluaciones_usuarios'
    
    id_evaluacion = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer(), nullable=False)
    fecha = Column(DATETIME)
    puntaje = Column(Float)
