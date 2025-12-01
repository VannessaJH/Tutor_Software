from flask import Blueprint, jsonify, request
from services.student_service import StudentService

from controllers.academic.student_controller import (
    get_student_content_controller, 
    register_content_view_controller,
    get_evaluation_questions_controller,
    submit_evaluation_controller
)

student_bp = Blueprint('student', __name__, url_prefix='/api/student') 

@student_bp.route('/content', methods=['GET'])
def get_student_content_route():
    """
    Ruta para obtener todo el contenido (Estructurado + HTML) y el estado de 'puede_evaluar'.
    Llama a la función del controlador que ya maneja la lógica.
    """
  
    response, status = get_student_content_controller(request)
    return jsonify(response), status

@student_bp.route('/content/view', methods=['POST'])
def register_content_view_route():
    """
    Ruta para registrar que el estudiante vio un ítem de contenido.
    """
    response, status = register_content_view_controller(request)
    return jsonify(response), status


@student_bp.route('/evaluation/questions', methods=['GET'])
def get_evaluation_questions_route():
    """
    Obtiene las preguntas disponibles para la evaluación.
    """
    response, status = get_evaluation_questions_controller(request)
    return jsonify(response), status

@student_bp.route('/evaluation/submit', methods=['POST'])
def submit_evaluation_route():
    """
    Envía las respuestas del estudiante, procesa la calificación y devuelve el resultado.
    """
    response, status = submit_evaluation_controller(request)
    return jsonify(response), status

