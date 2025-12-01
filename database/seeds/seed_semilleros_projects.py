import os
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean 

current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..')) 
sys.path.append(os.path.join(root_dir, 'backend', 'src'))


try:
    from database import Base, engine, SessionLocal
    from models.academic.semillero import Semillero 
except ImportError as e:
    print(f"ADVERTENCIA: No se pudo importar el modelo real Semillero o conf.database. Usando un mock temporal. Error: {e}")
    
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()
    
    class Semillero(Base): 
        __tablename__ = 'semilleros'
        id = Column(Integer, primary_key=True, index=True)
        nombre = Column(String, nullable=False)
        profesor = Column(String, nullable=False)
        proyecto = Column(Text, nullable=False)
        año = Column(Integer, nullable=False)
        descripcion = Column(Text)
        contacto = Column(String)
        activo = Column(Boolean)

    engine = create_engine('sqlite:///./mock_semillero.db')
    SessionLocal = lambda: Session(bind=engine) # Definir SessionLocal para el mock
    
SEEDS_PROJECTS = [
    {'año': 2025, 'nombre': 'Mecatrónica aplicada a la industria', 'profesor': 'Juan José Bernal Segura', 'proyecto': 'Diseño y construcción de un robot scara con visión artificial para detección y selección de objetos', 'descripcion': 'Proyecto de mecatrónica', 'contacto': 'juan.bernal@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Virtual Aprende (VIRTUS)', 'profesor': 'Eduardo Hernández / Martín Encizo Méndez', 'proyecto': 'Aprendizaje flexible multimedial', 'descripcion': 'Semillero enfocado en el aprendizaje digital.', 'contacto': 'ehernandez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Automatools (atm)', 'profesor': 'Miguel Alfonso Morales Granados', 'proyecto': 'Desarrollo de un prototipo de trazabilidad de instrumentos industriales', 'descripcion': 'Semillero de automatización.', 'contacto': 'm.morales@etitc.edu.co'},
    {'año': 2025, 'nombre': 'CANSAT', 'profesor': 'Jheyson Fabián Villavisan Buitrago', 'proyecto': 'Diseñar y construir un prototipo de nanosatélite tipo CANSAT', 'descripcion': 'Desarrollo de nanosatélites.', 'contacto': 'jvillavisan@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Manufactura aditiva (Impresión 3d)', 'profesor': 'Javier Muños Tovar', 'proyecto': 'Impresión 3D, corte láser, escáner 3D', 'descripcion': 'Semillero de fabricación digital.', 'contacto': 'jmunos@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Cultivando con virtud', 'profesor': 'Brian Alejandro Corredor León', 'proyecto': 'Agricultura urbana inteligente: transformación digital de un cultivo de papa', 'descripcion': 'Innovación en agricultura.', 'contacto': 'bcorredor@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Fabricación digital', 'profesor': 'Myriam Herrera Paloma', 'proyecto': 'Creación de un banco de proyectos de mecanismos con corte láser e impresión 3d', 'descripcion': 'Mecanismos y prototipado.', 'contacto': 'mherrera@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Isqua', 'profesor': 'Nelson Castañeda Arias', 'proyecto': 'Análisis del impacto de estrategias didácticas basadas en programación desconectada en el pensamiento computacional', 'descripcion': 'Educación y computación.', 'contacto': 'ncastañeda@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Hidrógeno', 'profesor': 'Francisco Javier Cano Ravelo', 'proyecto': 'Evaluación del uso de herramientas pedagógicas para el aprendizaje de producción de hidrógeno', 'descripcion': 'Estudios de energías limpias.', 'contacto': 'fcano@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Materia y energía', 'profesor': 'Holman Enrique Cubides Garzón', 'proyecto': 'Diseño y simulación de pruebas de iluminación circadiana con espectro dinámico usando 4 led rgby', 'descripcion': 'Investigación en física y energía.', 'contacto': 'hcubides@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Mujeres y materialidad', 'profesor': 'Isabel Cristina Castellanos Cuellar', 'proyecto': 'Evaluación del ácido poliláctico (PLA) en ingeniería biomédica y sostenibilidad', 'descripcion': 'Materiales y género.', 'contacto': 'icastellanos@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Sapientiam', 'profesor': 'José Alfredo Trejos Motato', 'proyecto': 'Ciberseguridad para todos: capacitación y divulgación para comunidades no técnicas', 'descripcion': 'Semillero de ciberseguridad.', 'contacto': 'jtrejos@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Solid Works', 'profesor': 'Fabián Guillermo Cortes Sierra', 'proyecto': 'Metodología efectiva utilizando solidworks como herramienta de apoyo', 'descripcion': 'Diseño asistido por computador.', 'contacto': 'fcortes@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Vehículos eléctricos (seve)', 'profesor': 'María Ximena Reyes Ortiz', 'proyecto': 'Mejora de un motor Mazda de combustión para banco de pruebas funcional', 'descripcion': 'Movilidad sostenible.', 'contacto': 'mreyes@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Desarrollo tecnológico sostenible (detec)', 'profesor': 'Jorge Enrique Hower', 'proyecto': 'Desarrollo de alternativas de economía circular para la recuperación y procesamiento de plásticos', 'descripcion': 'Economía circular.', 'contacto': 'jhower@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Ecomovilidad', 'profesor': 'Pedro Emilio Prieto Garzón', 'proyecto': 'Construcción y adecuación de un sistema de celdas solares para energizar una bicicleta convencional', 'descripcion': 'Sistemas solares y transporte.', 'contacto': 'pprieto@etitc.edu.co'},
    {'año': 2025, 'nombre': 'ECOS', 'profesor': 'José Francisco Lugo Pinto', 'proyecto': 'Sistema de protección de carga útil, control de vuelo y monitoreo climático CANSAT', 'descripcion': 'Control de vuelo CANSAT.', 'contacto': 'jlugo@etitc.edu.co'},
    {'año': 2025, 'nombre': 'SIAR', 'profesor': 'Alfredo Sánchez Silvera', 'proyecto': 'Diseño de un prototipo de sensor para detección temprana del hongo de la roya en café', 'descripcion': 'Sensores y agricultura.', 'contacto': 'asanchez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Domótica', 'profesor': 'Wladimir Páez Páez', 'proyecto': 'Rs seguridad por reconocimiento facial', 'descripcion': 'Sistemas de seguridad residencial.', 'contacto': 'wpaez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'GIER', 'profesor': 'Germán López', 'proyecto': 'Diseño banco de pruebas para la enseñanza de energía solar en la ETITC', 'descripcion': 'Laboratorios de energía solar.', 'contacto': 'glopez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Inteligencia Artificial (K-IA)', 'profesor': 'Luis Eduardo Baquero Rey', 'proyecto': 'Análisis predictivo de ventas en comercio electrónico mediante web scraping', 'descripcion': 'IA y comercio electrónico.', 'contacto': 'lbaquero@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Inteligencia Artificial (K-IA)', 'profesor': 'Miguel Hernández Bejarano', 'proyecto': 'Análisis de sentimientos usando web scraping', 'descripcion': 'Web scraping y PLN.', 'contacto': 'mhernandez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Nuevas tecnologías saludables', 'profesor': 'Magda Liliana Rincón Meléndez', 'proyecto': 'Nuevas tecnologías para ambientes saludables y productivos', 'descripcion': 'Ambientes saludables.', 'contacto': 'mrincon@etitc.edu.co'},
    {'año': 2025, 'nombre': 'k-immersion', 'profesor': 'Sócrates Rojas Amador', 'proyecto': 'SMARTAXIM', 'descripcion': 'Inmersión tecnológica.', 'contacto': 'srojas@etitc.edu.co'},
    {'año': 2025, 'nombre': 'k-smart', 'profesor': 'Alexander Peña Marín', 'proyecto': 'Detección de figuras geométricas complejas en fotografía aérea con redes neuronales convolucionales', 'descripcion': 'Redes neuronales y fotografía.', 'contacto': 'apena@etitc.edu.co'},
    {'año': 2025, 'nombre': 'k-vant', 'profesor': 'John Alexander Rico Franco', 'proyecto': 'Tendencias tecnológicas de la agricultura 4.0 asociadas a los VANTS', 'descripcion': 'Agricultura 4.0 y drones.', 'contacto': 'jrico@etitc.edu.co'},
    {'año': 2025, 'nombre': 'PRO2', 'profesor': 'Henry Montero', 'proyecto': 'Hidrógeno verde y azul: la apuesta para la transición energética en Colombia', 'descripcion': 'Transición energética.', 'contacto': 'hmontero@etitc.edu.co'},
    {'año': 2025, 'nombre': 'RUAJ-ETITC', 'profesor': 'Milton Rodríguez Chavarro', 'proyecto': 'Matlab: análisis de datos y aplicaciones en ingeniería', 'descripcion': 'Análisis de datos.', 'contacto': 'mrodriguez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'dp4ai', 'profesor': 'Sebastián Yepes', 'proyecto': 'Machine learning y privacidad diferencial: análisis criptográfico para la confidencialidad de datos', 'descripcion': 'ML y privacidad.', 'contacto': 'syepes@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Matter and energy', 'profesor': 'Hollman Yesid Piñeros Herrera', 'proyecto': 'Spartanface security: prototipo de reconocimiento facial para seguridad residencial', 'descripcion': 'Seguridad residencial.', 'contacto': 'hpineros@etitc.edu.co'},
    {'año': 2025, 'nombre': 'k-cybersec', 'profesor': 'Iván Darío Méndez', 'proyecto': 'Adquisición y análisis forense', 'descripcion': 'Análisis forense.', 'contacto': 'imendez@etitc.edu.co'},
    {'año': 2025, 'nombre': 'Escritura creativa', 'profesor': 'Marisol Briñez Ríos', 'proyecto': 'Desarrollo de competencias de comunicación oral y escrita en estudiantes de ingeniería mecánica', 'descripcion': 'Comunicación en ingeniería.', 'contacto': 'mbrinez@etitc.edu.co'},
    # Datos de años anteriores (2024)
    {'año': 2024, 'nombre': 'GIER', 'profesor': 'Germán Arturo López Martínez', 'proyecto': 'Diseño banco de pruebas para la enseñanza de energía solar en la ETITC', 'descripcion': 'Laboratorios de energía solar.', 'contacto': 'glopez@etitc.edu.co'},
    {'año': 2024, 'nombre': 'Vehículos eléctricos (SEVE)', 'profesor': 'María Ximena Reyes Ortiz', 'proyecto': 'Guías prácticas del laboratorio de electromovilidad', 'descripcion': 'Electromovilidad.', 'contacto': 'mreyes@etitc.edu.co'},
    {'año': 2024, 'nombre': 'SIGE', 'profesor': 'Omar López Delgado', 'proyecto': 'Diseño de un sistema híbrido de energía limpia y sostenible para vivienda rural', 'descripcion': 'Sistemas híbridos.', 'contacto': 'olopez@etitc.edu.co'},
    {'año': 2024, 'nombre': 'Inteligencia Artificial (K-IA)', 'profesor': 'Luis Eduardo Baquero Rey', 'proyecto': 'Estudio de técnicas de web scraping para la recolección, procesamiento y análisis de datos con IA', 'descripcion': 'Web scraping con IA.', 'contacto': 'lbaquero@etitc.edu.co'},
    {'año': 2024, 'nombre': 'K-Smart', 'profesor': 'Alexander Peña Marín', 'proyecto': 'Detección de figuras geométricas complejas en fotografía aérea usando redes neuronales convolucionales', 'descripcion': 'Redes neuronales y fotografía.', 'contacto': 'apena@etitc.edu.co'},
    {'año': 2024, 'nombre': 'Ecomovilidad', 'profesor': 'Pedro Emilio Prieto Garzón', 'proyecto': 'Promover la investigación y el desarrollo de tecnologías limpias y eficientes para la movilidad', 'descripcion': 'Movilidad sostenible.', 'contacto': 'pprieto@etitc.edu.co'},
    {'año': 2024, 'nombre': 'Cultivando con Virtud (CV)', 'profesor': 'Brian Alejandro Corredor León', 'proyecto': 'De la adquisición al análisis: un sistema de información para cultivos urbanos de papa', 'descripcion': 'Sistemas de información agrícola.', 'contacto': 'bcorredor@etitc.edu.co'},
    {'año': 2024, 'nombre': 'Robótica Ambiental', 'profesor': 'Sergio Enrique Ramírez Moreno', 'proyecto': 'Diseño y desarrollo de extrusora de PET', 'descripcion': 'Robótica y medio ambiente.', 'contacto': 'sramirez@etitc.edu.co'},
]


def seed_semilleros_data():
    """
    Función para insertar los datos de Semilleros y sus proyectos en la base de datos.
    Solo se insertan datos para los años 2024 y 2025.
    """
    db: Session = SessionLocal() 
    try:
        print("Iniciando la siembra de datos de Semilleros (2024-2025)...")

        for data in SEEDS_PROJECTS:
            existing_semillero = db.query(Semillero).filter(
                Semillero.año == data['año'],
                Semillero.nombre == data['nombre'],
            ).first()
            
            if existing_semillero:
                print(f"Skipping: Semillero '{data['nombre']}' ya existe para el año {data['año']}.")
                continue

            new_semillero = Semillero(
                nombre=data['nombre'],
                profesor=data['profesor'],
                proyecto=data['proyecto'],
                año=data['año'],
                descripcion=data.get('descripcion', 'Sin descripción detallada.'),
                contacto=data.get('contacto', 'contacto@etitc.edu.co'),
                activo=(data['año'] == 2025) 
            )
            db.add(new_semillero)
            print(f"Agregado: {data['nombre']} ({data['año']}) - Activo: {new_semillero.activo}")

        db.commit()
        print("✅ Siembra de datos de Semilleros completada con éxito.")

    except Exception as e:
        db.rollback()
        print(f"❌ Error durante la siembra de datos de Semilleros: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    seed_semilleros_data()