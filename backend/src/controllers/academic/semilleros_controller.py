from sqlalchemy.orm import Session
from typing import List, Optional
from models.academic.semillero import Semillero

def get_all_semilleros(db: Session, year: Optional[int] = None) -> List[Semillero]:
    """
    Recupera todos los semilleros de investigación de la base de datos.
    Opcionalmente filtra por año.
    
    :param db: Sesión de la base de datos.
    :param year: Año opcional para filtrar los resultados.
    :return: Lista de objetos Semillero.
    """
    query = db.query(Semillero)
    
    if year is not None:
        query = query.filter(Semillero.año == year)
    
    # Ordenar por año descendente y luego por nombre alfabéticamente
    return query.order_by(Semillero.año.desc(), Semillero.nombre.asc()).all()

def get_semillero_by_id(db: Session, semillero_id: int) -> Optional[Semillero]:
    """
    Recupera un semillero específico por su ID.
    
    :param db: Sesión de la base de datos.
    :param semillero_id: ID del semillero a buscar.
    :return: Objeto Semillero o None.
    """
    return db.query(Semillero).filter(Semillero.id == semillero_id).first()