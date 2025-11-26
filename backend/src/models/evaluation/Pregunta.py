from sqlalchemy import Column, Integer, String, JSON
from config.database import Base

class Pregunta(Base):
    __tablename__ = 'preguntas'
    
    id_pregunta = Column(Integer, primary_key=True, autoincrement=True)
    enunciado = Column(String(), nullable=False)
    opciones = Column(JSON)
    respuesta_correcta = Column(String(1))