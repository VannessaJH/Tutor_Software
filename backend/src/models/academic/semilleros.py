from sqlalchemy import Column, Integer, String, Text, Boolean
from config.database import Base 

class Semillero(Base):
    """
    Representa un Semillero de Investigación y el Proyecto principal asociado a un año específico.
    """
    __tablename__ = 'semilleros'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False, index=True, comment="Nombre del Semillero (e.g., 'Mecatrónica aplicada a la industria')")
    profesor = Column(String(100), nullable=False, comment="Nombre del docente a cargo del Semillero")
    proyecto = Column(Text, nullable=False, comment="Título o descripción concisa del proyecto principal del año")
    año = Column(Integer, nullable=False, index=True, comment="Año de ejecución del proyecto")
    descripcion = Column(Text, comment="Descripción detallada del Semillero y su enfoque general")
    contacto = Column(String(100), comment="Correo electrónico o teléfono de contacto del profesor/semillero")
    activo = Column(Boolean, default=True, comment="Indica si el Semillero está activo en el año actual.")
    
    def __repr__(self):
        return f"<Semillero(id={self.id}, nombre='{self.nombre}', año={self.año}, profesor='{self.profesor}')>"