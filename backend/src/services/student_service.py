from models.academic.semilleros import Semillero
from models.academic.convocatoria import Convocatoria
from models.evaluation.evaluation import Evaluation
from models.evaluation.content_view import ContentView
from models.evaluation.question import Question
from config.database import SessionLocal

from models.academic.content import Content 

class StudentService:
    
    def __init__(self):
        self.db = SessionLocal()
    
    def get_student_content(self, user_id):
        """Obtener todo el contenido (Estructurado y HTML) para el estudiante desde la BD"""
        try:
            semilleros = self.db.query(Semillero).filter(Semillero.activo == True).all()
            semilleros_data = [{
                'id': s.id,
                'nombre': s.nombre,
                'profesor': s.profesor,
                'proyecto': s.proyecto,
                'año': s.año,
                'descripcion': s.descripcion,
                'contacto': s.contacto,
                'activo': s.activo
            } for s in semilleros]
            
            convocatorias = self.db.query(Convocatoria).filter(Convocatoria.activa == True).all()
            convocatorias_data = [{
                'id': c.id,
                'titulo': c.titulo,
                'tipo': c.tipo,
                'año': c.año,
                'numero': c.numero,
                'archivo_url': c.archivo_url,
                'descripcion': c.descripcion,
                'fecha_limite': c.fecha_limite.strftime('%Y-%m-%d') if c.fecha_limite else None,
                'activa': c.activa
            } for c in convocatorias]
            
            try:
                from models.academic.redinvestigacion import RedInvestigacion
                redes = self.db.query(RedInvestigacion).filter(RedInvestigacion.activa == True).all()
                redes_data = [{
                    'id': r.id,
                    'nombre': r.nombre,
                    'descripcion': r.descripcion,
                    'objetivo': r.objetivo,
                    'instituciones': r.instituciones,
                    'contacto': r.contacto,
                    'activa': r.activa
                } for r in redes]
            except ImportError:
                redes_data = [] 

            contenido_gestionable = self.db.query(Content).filter(Content.is_active == True).all()
            contenido_data = {}
            for c in contenido_gestionable:
                contenido_data[c.slug] = c.to_dict() 

            
            return {
                'semilleros': semilleros_data,
                'convocatorias': convocatorias_data,
                'redes': redes_data,
                'contenido_gestionable': contenido_data, 
                'puede_evaluar': self._puede_realizar_evaluacion(user_id)
            }
        except Exception as e:
            print(f"Error obteniendo contenido estudiante: {e}")
            return None
        finally:
            self.db.close()
            
    def _puede_realizar_evaluacion(self, user_id):
        """Verificar si el usuario puede realizar evaluación"""
        try:
            vistas = self.db.query(ContentView).filter(
                ContentView.usuario_id == user_id,
                ContentView.completado == True
            ).count()
            
            evaluacion_pendiente = self.db.query(Evaluation).filter(
                Evaluation.usuario_id == user_id,
                Evaluation.completada == False
            ).first()
            
            return vistas >= 2 and not evaluacion_pendiente
        except Exception as e:
            print(f"Error verificando evaluación: {e}")
            return False
            
    def registrar_vista_contenido(self, user_id, content_type, content_id):
        """Registrar que el usuario vio contenido"""
        try:
            vista_existente = self.db.query(ContentView).filter(
                ContentView.usuario_id == user_id,
                ContentView.tipo_contenido == content_type,
                ContentView.contenido_id == content_id
            ).first()
            
            if vista_existente:
                if not vista_existente.completado:
                    vista_existente.completado = True
                    self.db.commit()
            else:
                nueva_vista = ContentView(
                    usuario_id=user_id,
                    tipo_contenido=content_type,
                    contenido_id=content_id,
                    completado=True
                )
                self.db.add(nueva_vista)
                self.db.commit()
            
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error registrando vista: {e}")
            return False

    def get_evaluation_questions(self):
        """
        Obtiene las preguntas activas para la evaluación del estudiante, 
        excluyendo la respuesta correcta.
        """
        try:
            questions = self.db.query(Question).filter(Question.is_active == True).all()
            
            questions_data = []
            for q in questions:
                questions_data.append({
                    'id': q.id,
                    'text': q.text,
                    'options': q.options,  
                    'type': q.type,       
                    'puntos': q.puntos     
                })
            
            return questions_data
        except Exception as e:
            print(f"Error obteniendo preguntas de evaluación: {e}")
            return []
            
    def realizar_evaluacion(self, user_id, respuestas):
        """Procesar evaluación del usuario"""
        try:
            preguntas = self.db.query(Question).all()
            puntaje_total = 0
            respuestas_correctas = 0
            
            
            for pregunta_id, respuesta_usuario in respuestas.items():
                pregunta = next((p for p in preguntas if p.id == int(pregunta_id)), None)
                if pregunta and respuesta_usuario == pregunta.respuesta_correcta:
                    puntaje_total += pregunta.puntos
                    respuestas_correctas += 1
            
            total_puntos_posible = sum(p.puntos for p in preguntas)
            porcentaje = (puntaje_total / total_puntos_posible) * 100 if total_puntos_posible > 0 else 0
            
            retroalimentacion = self._generar_retroalimentacion(porcentaje)
          
            evaluacion = Evaluation(
                usuario_id=user_id,
                puntaje=porcentaje,
                respuestas=respuestas, 
                retroalimentacion=retroalimentacion,
                completada=True
            )
            
            self.db.add(evaluacion)
            self.db.commit()
            
            return {
                'puntaje': porcentaje,
                'respuestas_correctas': respuestas_correctas,
                'total_preguntas': len(preguntas),
                'retroalimentacion': retroalimentacion
            }
        except Exception as e:
            self.db.rollback()
            print(f"Error realizando evaluación: {e}")
            return None
    
   
    def _generar_retroalimentacion(self, puntaje):
        """Generar retroalimentación basada en el puntaje"""
        if puntaje >= 90:
            return "¡Excelente! Dominas completamente los conceptos de investigación."
        elif puntaje >= 70:
            return "¡Buen trabajo! Tienes un buen conocimiento sobre investigación."
        elif puntaje >= 50:
            return "Tienes conocimientos básicos. Sigue estudiando los conceptos."
        else:
            return "Necesitas repasar los conceptos de investigación. Revisa el contenido nuevamente."
    
    
    def obtener_resultados_evaluacion(self, user_id):
        """Obtener resultados de evaluación del usuario"""
        try:
            evaluacion = self.db.query(Evaluation).filter(
                Evaluation.usuario_id == user_id
            ).order_by(Evaluation.fecha_evaluacion.desc()).first()
            
            if evaluacion:
                return {
                    'puntaje': evaluacion.puntaje,
                    'retroalimentacion': evaluacion.retroalimentacion,
                    'fecha_evaluacion': evaluacion.fecha_evaluacion.strftime('%Y-%m-%d %H:%M:%S'),
                    'completada': evaluacion.completada
                }
            return None
        except Exception as e:
            print(f"Error obteniendo resultados: {e}")
            return None