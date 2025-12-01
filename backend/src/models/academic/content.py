
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from config.database import Base 

class Content(Base):
    """Modelo para el contenido académico gestionable (Contenido de las lecciones)."""
    
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False) 
    content_html = Column(Text, nullable=False) 
    type = Column(String(50), nullable=False) 
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content_html': self.content_html,
            'type': self.type,
            'is_active': self.is_active
        }