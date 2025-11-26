from sqlalchemy import Column, Integer, String, Text, JSON
from config.database import Base

class Question(Base):
    __tablename__ = 'preguntas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(Text, nullable=False)
    tipo = Column(String(50), default='opcion_multiple')
    opciones = Column(JSON) 
    respuesta_correcta = Column(String(200))
    puntos = Column(Integer, default=1)
    categoria = Column(String(100))  