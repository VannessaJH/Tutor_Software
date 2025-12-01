# backend/src/controllers/student_controller.py

from services.student_service import StudentService
# from utils.auth import get_user_id # Reemplaza por tu método real de autenticación/token

student_service = StudentService()

# ----------------------------------------------------------------------
# 1. RUTA: OBTENER CONTENIDO (Contenido HTML y Estructurado)
# ----------------------------------------------------------------------
def get_student_content_controller(request):
    """
    GET /api/student/content
    Obtiene semilleros, convocatorias y el contenido HTML gestionable.
    """
    # 💡 NOTA: En un entorno real, el user_id se obtendría del token JWT
    # user_id = get_user_id(request)
    user_id = 1 # ID de usuario simulado 
    
    result = student_service.get_student_content(user_id)
    
    if result:
        return result, 200 # Retorna el diccionario con todo el contenido
    else:
        return {"error": "Error al cargar el contenido del estudiante."}, 500

# ----------------------------------------------------------------------
# 2. RUTA: REGISTRAR VISTA DE CONTENIDO
# ----------------------------------------------------------------------
def register_content_view_controller(request):
    """
    POST /api/student/content/view
    Registra que el estudiante ha visto una sección de contenido gestionable.
    """
    # user_id = get_user_id(request)
    user_id = 1 # ID de usuario simulado 
    
    try:
        data = request.json
        # Estos campos son clave para el modelo ContentView
        content_slug = data.get('content_slug') 
        content_id = data.get('content_id')
        
        if not content_slug or not content_id:
            return {"error": "Faltan campos (content_slug o content_id) en el body."}, 400

    except:
        return {"error": "JSON de entrada no válido."}, 400

    # Usamos el 'slug' como 'tipo_contenido' para fines de demostración, 
    # pero tu modelo ContentView usa 'tipo_contenido' y 'contenido_id'.
    # Aquí asumimos que content_slug es el tipo y content_id es el id.
    success = student_service.registrar_vista_contenido(
        user_id=user_id,
        content_type=content_slug,
        content_id=content_id
    )

    if success:
        return {"message": f"Vista de contenido '{content_slug}' registrada exitosamente."}, 200
    else:
        return {"error": "No se pudo registrar la vista."}, 500


# ----------------------------------------------------------------------
# 3. RUTA: OBTENER PREGUNTAS DE EVALUACIÓN
# ----------------------------------------------------------------------
def get_evaluation_questions_controller(request):
    """
    GET /api/student/evaluation/questions
    Obtiene las preguntas activas para que el frontend las muestre.
    """
    # No se requiere user_id aquí, solo se necesitan las preguntas activas.
    
    questions = student_service.get_evaluation_questions()
    
    if questions:
        return {"questions": questions}, 200
    else:
        # Puede ser 200 si no hay preguntas, o 404 si es un requisito
        return {"message": "No hay preguntas de evaluación disponibles."}, 200 

# ----------------------------------------------------------------------
# 4. RUTA: ENVIAR EVALUACIÓN
# ----------------------------------------------------------------------
def submit_evaluation_controller(request):
    """
    POST /api/student/evaluation/submit
    Recibe las respuestas del estudiante y devuelve el resultado.
    """
    # user_id = get_user_id(request)
    user_id = 1 # ID de usuario simulado 
    
    try:
        data = request.json
        # 'respuestas' debe ser un diccionario {pregunta_id: respuesta_seleccionada}
        respuestas = data.get('respuestas') 
        if not respuestas:
            return {"error": "El campo 'respuestas' es requerido."}, 400
            
    except:
        return {"error": "JSON de entrada no válido."}, 400

    result = student_service.realizar_evaluacion(user_id, respuestas)

    if result:
        return result, 200
    else:
        return {"error": "No se pudo procesar la evaluación."}, 500