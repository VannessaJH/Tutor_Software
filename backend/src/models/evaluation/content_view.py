from datetime import datetime

class ContentView:
    def __init__(self, id=None, user_id=None, content_type=None, content_id=None,
                 fecha_visto=None, tiempo_visualizacion=0, completado=False):
        self.id = id
        self.user_id = user_id
        self.content_type = content_type  
        self.content_id = content_id
        self.fecha_visto = fecha_visto or datetime.now()
        self.tiempo_visualizacion = tiempo_visualizacion
        self.completado = completado  

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content_type': self.content_type,
            'content_id': self.content_id,
            'fecha_visto': self.fecha_visto,
            'completado': self.completado
        }