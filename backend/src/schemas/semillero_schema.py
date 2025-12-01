from pydantic import BaseModel, Field
from typing import Optional

class SemilleroBase(BaseModel):
    """
    Define los campos básicos que se usan en la creación y/o actualización.
    """
    nombre: str = Field(..., max_length=200, description="Nombre del Semillero (e.g., 'Mecatrónica aplicada a la industria')")
    profesor: str = Field(..., max_length=100, description="Nombre del docente a cargo del Semillero")
    proyecto: str = Field(..., description="Título o descripción concisa del proyecto principal del año")
    año: int = Field(..., description="Año de ejecución del proyecto")
    descripcion: Optional[str] = Field(None, description="Descripción detallada del Semillero y su enfoque general")
    contacto: Optional[str] = Field(None, max_length=100, description="Correo electrónico o teléfono de contacto")
    activo: Optional[bool] = Field(True, description="Indica si el Semillero está activo.")


class SemilleroCreate(SemilleroBase):
    """
    Modelo usado para crear una nueva instancia de Semillero.
    Hereda de SemilleroBase y no requiere el campo 'id'.
    """
    pass


class SemilleroResponse(SemilleroBase):
    """
    Modelo usado para formatear y validar la respuesta que se envía al cliente.
    Incluye el 'id' generado por la base de datos.
    """
    id: int = Field(..., description="Identificador único del Semillero.")
    
    class Config:
  
        orm_mode = True 
  