s// frontend/src/services/studentService.js

const API_BASE_URL = '/api/student'; 


export const fetchStudentContent = async (token) => {
    const response = await fetch(`${API_BASE_URL}/content`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        }
    });

    if (!response.ok) {
        throw new Error('Error al cargar el contenido del estudiante.');
    }

    return response.json();
};


export const registerContentView = async (token, contentSlug, contentId) => {
    const response = await fetch(`${API_BASE_URL}/content/view`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            content_slug: contentSlug,
            content_id: contentId
        })
    });

    if (!response.ok) {
        // Devuelve el mensaje de error del backend si existe
        const errorData = await response.json(); 
        throw new Error(errorData.error || 'Error al registrar la vista.');
    }

    return response.json();
};


export const fetchEvaluationQuestions = async (token) => {
    const response = await fetch(`${API_BASE_URL}/evaluation/questions`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        }
    });

    if (!response.ok) {
        throw new Error('Error al cargar las preguntas de evaluación.');
    }

    const data = await response.json();
    return data.questions;
};


export const submitEvaluationAnswers = async (token, respuestas) => {
    const response = await fetch(`${API_BASE_URL}/evaluation/submit`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ respuestas })
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || 'Error al enviar la evaluación.');
    }

    return data;
};