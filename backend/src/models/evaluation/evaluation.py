from datetime import datetime

class Evaluation:
    def __init__(self, id=None, user_id=None, puntaje=0, respuestas=None, 
                 fecha_evaluacion=None, retroalimentacion=None, completada=False,
                 contenido_visto=True):  
        self.id = id
        self.user_id = user_id
        self.puntaje = puntaje
        self.respuestas = respuestas or {}
        self.fecha_evaluacion = fecha_evaluacion or datetime.now()
        self.retroalimentacion = retroalimentacion
        self.completada = completada
        self.contenido_visto = contenido_visto 

    def puede_realizar_evaluacion(self):
        """Verifica si el usuario puede hacer la evaluación"""
        return self.contenido_visto and not self.completada

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'puntaje': self.puntaje,
            'fecha_evaluacion': self.fecha_evaluacion,
            'retroalimentacion': self.retroalimentacion,
            'completada': self.completada,
            'contenido_visto': self.contenido_visto,
            'puede_evaluar': self.puede_realizar_evaluacion()  
        }