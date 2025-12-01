from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.database import Base 
from datetime import datetime, timedelta

class UserSession(Base):
    """
    Modelo para gestionar la sesión activa y la revocación de tokens JWT.
    """
    __tablename__ = 'user_sessions'

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False) 
    
    access_token = Column(String(512), unique=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    expires_at = Column(DateTime, nullable=False)

    is_revoked = Column(Boolean, default=False)
    
    usuario = relationship("Usuario", back_populates="user_sessions")

    def __repr__(self):
        return f"<UserSession(id={self.id}, user_id={self.user_id}, expires_at={self.expires_at})>"

    def is_active(self):
        """Verifica si la sesión aún es válida."""
        return not self.is_revoked and self.expires_at > datetime.utcnow()