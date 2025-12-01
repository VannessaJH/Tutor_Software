from sqlalchemy.orm import Session
from typing import List, Optional

from models.academic.convocatoria import Convocatoria 

def get_all_convocatorias(db: Session, only_active: Optional[bool] = None) -> List[Convocatoria]:
    """
    Recupera todas las convocatorias de la base de datos, con opción de filtrar por estado activo.
    
    :param db: Sesión de la base de datos.
    :param only_active: Si es True, solo devuelve convocatorias activas.
    :return: Lista de objetos Convocatoria.
    """
    query = db.query(Convocatoria)
    
    if only_active is True:
        query = query.filter(Convocatoria.activa == True)
    
 
    return query.order_by(Convocatoria.fecha_fin.asc()).all()

def get_convocatoria_by_id(db: Session, convocatoria_id: int) -> Optional[Convocatoria]:
    """
    Recupera una convocatoria específica por su ID.
    
    :param db: Sesión de la base de datos.
    :param convocatoria_id: ID de la convocatoria a buscar.
    :return: Objeto Convocatoria o None.
    """
    return db.query(Convocatoria).filter(Convocatoria.id == convocatoria_id).first()