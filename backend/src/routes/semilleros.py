from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional


from models.academic.semilleros import Semillero
from controllers.academic.semilleros_controller import get_all_semilleros, get_semillero_by_id

from schemas.semillero_schema import SemilleroUpdate

from config.database import get_db 

router = APIRouter(
    prefix="/academic/semilleros",
    tags=["Semilleros"],
)

@router.get("/", response_model=List[Semillero])
def read_semilleros(
    db: Session = Depends(get_db),
    year: Optional[int] = Query(None, description="Año para filtrar los semilleros (ej: 2025)"),
):
    """
    Obtiene una lista de todos los semilleros de investigación.
    
    Permite filtrar los resultados por un año específico.
    """
    semilleros = get_all_semilleros(db, year=year)
    return semilleros

@router.get("/{semillero_id}", response_model=Semillero)
def read_semillero(
    semillero_id: int, 
    db: Session = Depends(get_db)
):
    """
    Obtiene los detalles de un semillero de investigación por su ID.
    """
    semillero = get_semillero_by_id(db, semillero_id=semillero_id)
    if semillero is None:
        raise HTTPException(status_code=404, detail="Semillero no encontrado")
    return semillero

@router.put("/{semillero_id}")
def update_semillero_route(
    semillero_id: int,
    semillero_data: SemilleroUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza los datos de un semillero existente.
    Solo actualiza los campos enviados (parcial).
    """

    actualizado = update_semillero(
        db,
        semillero_id,
        semillero_data.dict(exclude_unset=True)
    )

    if actualizado is None:
        raise HTTPException(status_code=404, detail="Semillero no encontrado")

    return {
        "message": "Semillero actualizado correctamente",
        "semillero": actualizado
    }

