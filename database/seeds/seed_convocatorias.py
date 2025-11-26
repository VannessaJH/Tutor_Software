import os
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean 


current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..')) 
sys.path.append(os.path.join(root_dir, 'backend', 'src'))


try:
    from database import Base, engine, SessionLocal
    from models.academic.convocatoria import Convocatoria 
except ImportError as e:
    print(f"ADVERTENCIA: No se pudo importar el modelo real Convocatoria o conf.database. Usando un mock temporal. Error: {e}")
    
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    
    class Convocatoria(Base): 
        __tablename__ = 'convocatorias'
        id = Column(Integer, primary_key=True, index=True)
        titulo = Column(String, nullable=False)
        categoria_bloque = Column(String, nullable=False)
        categoria_tipo = Column(String, nullable=False)   
        año = Column(Integer)
        periodo_numero = Column(String) 
        url = Column(String, nullable=False)
        is_active = Column(Boolean, default=True) 

    engine = create_engine('sqlite:///./mock_convocatoria.db')
    SessionLocal = lambda: Session(bind=engine)

SEEDS_CONVOCATORIAS = [
    # 1. INSTITUCIONALES
    {'titulo': 'Plan de Trabajo 2024 - Vicerrectoría de Investigación', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Planificación', 'año': 2024, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/pt24.pdf', 'is_active': True},
    {'titulo': 'Lineamientos Generales (Grupos, Semilleros, Ética, P.I., etc.)', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Lineamiento', 'año': 2024, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/lineamientos24.pdf', 'is_active': True},
    {'titulo': 'Procedimiento para el Aval de Proyectos de Investigación', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Procedimiento', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/procedimientoaval.pdf', 'is_active': True},
    {'titulo': 'Reglamento de Semilleros de Investigación', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Normatividad', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/reglamentosemilleros.pdf', 'is_active': True},
    {'titulo': 'Formato Acta de Conformación de Semillero', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Formato', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/formatoactasemillero.pdf', 'is_active': True},
    {'titulo': 'Manual de Propiedad Intelectual', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Manual', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/manualpi.pdf', 'is_active': True},
    {'titulo': 'Resolución 510 de 2022 (Actualiza Grupos)', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Normatividad', 'año': 2022, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/res510.pdf', 'is_active': True},
    {'titulo': 'Resolución 354 de 2021 (Reglamento de Grupos)', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Normatividad', 'año': 2021, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/res354.pdf', 'is_active': True},
    {'titulo': 'Noticia: Vicerrectoría se fortalece con nueva funcionaria', 'categoria_bloque': 'INSTITUCIONALES', 'categoria_tipo': 'Noticia', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/es/noticia/vicerrectoria-se-fortalece-con-nueva-funcionaria-70', 'is_active': False},

    # 2. CONVOCATORIAS INTERNAS
    {'titulo': 'Convocatoria Interna Proyectos de Investigación N° 01-2025', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Convocatoria Interna', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriainterna25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Interna Proyectos de Investigación N° 02-2024', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Convocatoria Interna', 'año': 2024, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/convocatoriainterna224.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Interna Proyectos de Investigación N° 01-2024', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Convocatoria Interna', 'año': 2024, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriainterna124.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Interna Proyectos de Investigación N° 01-2023', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Convocatoria Interna', 'año': 2023, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriainterna23.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Interna Proyectos de Investigación N° 01-2022', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Convocatoria Interna', 'año': 2022, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriainterna22.pdf', 'is_active': False},
    {'titulo': 'Evento: Resultados Convocatoria Interna de Investigación', 'categoria_bloque': 'CONVOCATORIAS_INTERNAS', 'categoria_tipo': 'Evento', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/es/evento/71', 'is_active': False},

    # 3. ESTÍMULOS
    {'titulo': 'Convocatoria para Apoyo a Publicaciones N° 01-2025', 'categoria_bloque': 'ESTIMULOS', 'categoria_tipo': 'Apoyo Económico', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/apoyopublicaciones25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria para Eventos (Docentes, Semilleros) N° 01-2025', 'categoria_bloque': 'ESTIMULOS', 'categoria_tipo': 'Apoyo a Eventos', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/apoyoeventos25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria para Apoyo a Publicaciones N° 01-2024', 'categoria_bloque': 'ESTIMULOS', 'categoria_tipo': 'Apoyo Económico', 'año': 2024, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/apoyopublicaciones24.pdf', 'is_active': False},
    {'titulo': 'Convocatoria para Eventos (Docentes, Semilleros) N° 01-2024', 'categoria_bloque': 'ESTIMULOS', 'categoria_tipo': 'Apoyo a Eventos', 'año': 2024, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/apoyoeventos24.pdf', 'is_active': False},
    {'titulo': 'Resolución 207 de 2023 (Estímulos a la IIDT)', 'categoria_bloque': 'ESTIMULOS', 'categoria_tipo': 'Normatividad', 'año': 2023, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/res2072023.pdf', 'is_active': True},

    # 4. CONVOCATORIAS EXTERNAS
    {'titulo': 'Convocatoria 923-2023 - Reconocimiento de Investigadores Minciencias', 'categoria_bloque': 'CONVOCATORIAS_EXTERNAS', 'categoria_tipo': 'Minciencias', 'año': 2023, 'periodo_numero': '923', 'url': 'https://www.etitc.edu.co/archives/minciencias23.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Pasantías Minciencias (02-2023)', 'categoria_bloque': 'CONVOCATORIAS_EXTERNAS', 'categoria_tipo': 'Minciencias', 'año': 2023, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/pasantiasminciencias223.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Pasantías Minciencias (01-2023)', 'categoria_bloque': 'CONVOCATORIAS_EXTERNAS', 'categoria_tipo': 'Minciencias', 'año': 2023, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/pasantiasminciencias123.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Pasantías Minciencias (01-2022)', 'categoria_bloque': 'CONVOCATORIAS_EXTERNAS', 'categoria_tipo': 'Minciencias', 'año': 2022, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/pasantiasminciencias22.pdf', 'is_active': False},
    
    # 5. INVESTIGACIÓN ESTUDIANTIL
    {'titulo': 'Publicación de Facebook: Inscripción Semilleros II-2023', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Red Social', 'año': 2023, 'periodo_numero': 'II', 'url': '.../pfbid0iuuVN43Duwz9vYDDkzocNq2erx7wYsXUc2fQrCTEfyKQXpgNnPmQK2YrsLuVugNWl', 'is_active': False},
    {'titulo': 'Publicación de Facebook: Inscripción Semilleros I-2023', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Red Social', 'año': 2023, 'periodo_numero': 'I', 'url': '.../pfbid0J6WwS8GjqioC3aBaGfGLUFqnJetZ7uCs8kfDvACRp3RE7JnrcXnwdaKmBxq1Givyl', 'is_active': False},
    {'titulo': 'II Encuentro Interinstitucional de Semilleros', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Evento', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/es/evento/72', 'is_active': False},
    {'titulo': 'II Convocatoria Banco de Elegibles (Auxiliar, Asistente, Joven Investigador)', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Banco de Elegibles', 'año': 2022, 'periodo_numero': 'II', 'url': 'https://www.etitc.edu.co/archives/convocatoriabeinv22.pdf', 'is_active': False},
    {'titulo': 'Convocatoria de I, I y T Estudiantil N° 01-2022', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Convocatoria Estudiantil', 'año': 2022, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriainnovaciontec22.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Financiación y Materiales Semilleros 2022-1', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Apoyo Económico', 'año': 2022, 'periodo_numero': 'I', 'url': 'https://www.etitc.edu.co/archives/convocatoriamateriales22.pdf', 'is_active': False},
    {'titulo': 'Noticia: Convocatoria Semilleros de Investigación 2022-1', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Noticia', 'año': 2022, 'periodo_numero': 'I', 'url': 'https://www.etitc.edu.co/es/noticia/convocatoria-semilleros-de-investigacion-2022-1-62', 'is_active': False},
    {'titulo': 'Convocatoria Banco de Elegibles para Jóvenes Investigadores 2020', 'categoria_bloque': 'INVESTIGACION_ESTUDIANTIL', 'categoria_tipo': 'Banco de Elegibles', 'año': 2020, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/convocatoriabeinv20.pdf', 'is_active': False},

    # 6. PUBLICACIONES Y EVALUACIÓN
    {'titulo': 'Convocatoria presentación de textos - Boletines VIET N° 02-2025', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Boletín VIET', 'año': 2025, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/convocatoriaboletines225.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Revista Letras ConCiencia Tecnológica 2025', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Revista', 'año': 2025, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/convocatoriarlct25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Cuadernos ETITC N° 01-2025', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Cuadernos ETITC', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriacuadernos125.pdf', 'is_active': True},
    {'titulo': 'Convocatoria presentación de textos - Boletines VIET N° 01-2025', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Boletín VIET', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriaboletines25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Banco Pares Evaluadores N° 02-2025', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Banco Pares', 'año': 2025, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/convocatoriaparesevaluadores25.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Banco Pares Evaluadores N° 01-2024', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Banco Pares', 'año': 2024, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriaparesevaluadores24.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Cuadernos ETITC N° 01-2024', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Cuadernos ETITC', 'año': 2024, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/convocatoriacuadernos124.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Revista Letras ConCiencia Tecnológica 2024', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Revista', 'año': 2024, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/convocatoriarlct24.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Financiar Publicación Revistas Indexadas WOS/SCOPUS N° 02-2022', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Financiación Indexada', 'año': 2022, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/pubiliacionrevistasindexadas222.pdf', 'is_active': False},
    {'titulo': 'Sello Red Editorial de la Red de Docentes Transdisciplinar de México', 'categoria_bloque': 'PUBLICACIONES_EVALUACION', 'categoria_tipo': 'Sello Editorial', 'año': 2025, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/sellorededitorial25.pdf', 'is_active': True},

    # 7. INNOVACIÓN TECNOLÓGICA
    {'titulo': 'Convocatoria Registro Productos DT e Innovación N° 01-2025', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Registro DT', 'año': 2025, 'periodo_numero': '01', 'url': 'https://www.etitc.edu.co/archives/desarrollotecnologico125.pdf', 'is_active': True},
    {'titulo': 'Convocatoria Registro Productos DT e Innovación N° 04-2024', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Registro DT', 'año': 2024, 'periodo_numero': '04', 'url': 'https://www.etitc.edu.co/archives/desarrollotecnologico224.pdf', 'is_active': False},
    {'titulo': 'Bootcamp Blockchain', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Capacitación', 'año': 2024, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/bootcamp24.pdf', 'is_active': False},
    {'titulo': 'Plan de Capacitación en Emprendimiento (2023)', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Capacitación', 'año': 2023, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/emprendimientoc23.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Emprendimiento Tecnológico en Fase de Pre-incubación N° 03-2023', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Emprendimiento', 'año': 2023, 'periodo_numero': '03', 'url': 'https://www.etitc.edu.co/archives/emprendimiento323.pdf', 'is_active': False},
    {'titulo': 'Convocatoria Acompañamiento Propiedad Intelectual N° 02-2022', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Propiedad Intelectual', 'año': 2022, 'periodo_numero': '02', 'url': 'https://www.etitc.edu.co/archives/terminosreferenciaebt222.pdf', 'is_active': False},
    {'titulo': 'Noticia: Nuevo Logro de la ETITC (Convocatoria Fomento Protección Patente)', 'categoria_bloque': 'INNOVACION_TECNOLOGICA', 'categoria_tipo': 'Noticia', 'año': None, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/es/noticia/nuevo-logro-de-la-etitc-26', 'is_active': True},

    # 8. PONENCIAS NACIONALES E INTERNACIONALES
    {'titulo': 'Consolidado de Ponencias Nacionales e Internacionales', 'categoria_bloque': 'PONENCIAS', 'categoria_tipo': 'Consolidado PDF', 'año': 2023, 'periodo_numero': '2022-2023', 'url': 'https://www.etitc.edu.co/archives/ponenciasnalint122.pdf', 'is_active': True},
    
    # 9. EVALUACIÓN Y SEGUIMIENTO
    {'titulo': 'Resolución oficial de seguimiento (Res. 466 de 2021)', 'categoria_bloque': 'EVALUACION_SEGUIMIENTO', 'categoria_tipo': 'Normatividad', 'año': 2021, 'periodo_numero': None, 'url': 'https://www.etitc.edu.co/archives/res4662021.pdf', 'is_active': True},
]


def seed_convocatorias_data():
    """
    Función para insertar los datos de Convocatorias y Documentos Fundamentales 
    en la base de datos, agrupados por 9 categorías temáticas.
    """
    db: Session = SessionLocal() 
    try:
        print("Iniciando la siembra de datos de Convocatorias y Documentos...")

        for data in SEEDS_CONVOCATORIAS:
            existing_convocatoria = db.query(Convocatoria).filter(
                Convocatoria.titulo == data['titulo'],
                Convocatoria.categoria_bloque == data['categoria_bloque'],
            ).first()
            
            if existing_convocatoria:
                print(f"Skipping: Convocatoria '{data['titulo']}' ya existe en el bloque '{data['categoria_bloque']}'.")
                continue

            new_convocatoria = Convocatoria(
                titulo=data['titulo'],
                categoria_bloque=data['categoria_bloque'],
                categoria_tipo=data['categoria_tipo'],
                año=data['año'],
                periodo_numero=data['periodo_numero'],
                url=data['url'],
                is_active=data['is_active']
            )
            db.add(new_convocatoria)
            print(f"Agregado: {data['titulo']} | Bloque: {data['categoria_bloque']} | Activo: {new_convocatoria.is_active}")

        db.commit()
        print("✅ Siembra de datos de Convocatorias completada con éxito.")

    except Exception as e:
        db.rollback()
        print(f"❌ Error durante la siembra de datos de Convocatorias: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    seed_convocatorias_data()   