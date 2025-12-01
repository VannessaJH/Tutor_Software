from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

# Importar el modelo, controlador y la función para obtener la sesión DB
from models.academic.convocatoria import Convocatoria
from controllers.academic.convocatorias_controller import get_all_convocatorias, get_convocatoria_by_id
from config.database import get_db 

router = APIRouter(
    prefix="/academic/convocatorias",
    tags=["Convocatorias"],
)

@router.get("/", response_model=List[Convocatoria])
def read_convocatorias(
    db: Session = Depends(get_db),
    active: Optional[bool] = Query(None, description="Filtrar por convocatorias activas (True) o todas (None)."),
):
    """
    Obtiene una lista de todas las convocatorias académicas (becas, eventos, etc.).
    
    Permite filtrar los resultados para ver solo las convocatorias activas.
    """
    convocatorias = get_all_convocatorias(db, only_active=active)
  
    return convocatorias

@router.get("/{convocatoria_id}", response_model=Convocatoria)
def read_convocatoria(
    convocatoria_id: int, 
    db: Session = Depends(get_db)
):
    """
    Obtiene los detalles de una convocatoria por su ID.
    """
    convocatoria = get_convocatoria_by_id(db, convocatoria_id=convocatoria_id)
    if convocatoria is None:
        raise HTTPException(status_code=404, detail="Convocatoria no encontrada")
    return convocatoria

# backend/routes/convocatorias.py (añade estas rutas)
@router.put("/{convocatoria_id}")
def update_convocatoria(
    convocatoria_id: int,
    convocatoria_data: dict,  # Necesitas crear el schema
    db: Session = Depends(get_db)
):
    convocatoria = db.query(Convocatoria).filter(Convocatoria.id == convocatoria_id).first()
    
    if not convocatoria:
        raise HTTPException(status_code=404, detail="Convocatoria no encontrada")
    
    # Actualizar campos
    for key, value in convocatoria_data.items():
        setattr(convocatoria, key, value)
    
    db.commit()
    db.refresh(convocatoria)
    
    return {"message": "Convocatoria actualizada", "data": convocatoria}