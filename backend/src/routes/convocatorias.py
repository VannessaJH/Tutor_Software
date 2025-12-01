from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional


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