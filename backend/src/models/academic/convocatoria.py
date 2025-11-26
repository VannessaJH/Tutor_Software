from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from config.database import Base 

class Convocatoria(Base):
    """
    Representa una Convocatoria Interna o Externa (Investigación, Innovación, Estímulo) 
    con detalles extendidos y fechas.
    """
    __tablename__ = 'convocatorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False, comment="Título completo de la convocatoria")
    tipo = Column(String(50), nullable=False, comment="Tipo de convocatoria: 'interna', 'externa', 'estimulo', etc.") 
    año = Column(Integer, nullable=False, index=True, comment="Año de la convocatoria (e.g., 2025)")
    numero = Column(String(50), nullable=False, index=True, comment="Número de referencia interna (e.g., '18-2025')")
    archivo_url = Column(String(500), comment="URL al documento de la convocatoria (PDF o enlace)")
    descripcion = Column(Text, comment="Descripción detallada de los objetivos y alcances de la convocatoria")
    fecha_limite = Column(Date, comment="Fecha límite para la presentación de propuestas")
    activa = Column(Boolean, default=True, comment="Indica si la convocatoria está actualmente abierta o en curso.")

    def __repr__(self):
        return f"<Convocatoria(id={self.id}, titulo='{self.titulo}', año={self.año}, activa={self.activa})>"