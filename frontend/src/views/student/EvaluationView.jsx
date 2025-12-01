
import React, { useState, useEffect } from 'react';
import { fetchEvaluationQuestions, submitEvaluationAnswers } from '../../services/studentService';
// Asume que tienes un hook o store para obtener el token del usuario
// import { useAuthStore } from '../../stores/authStore'; 

const EvaluationView = () => {
    const [questions, setQuestions] = useState([]);
    const [answers, setAnswers] = useState({}); // { preguntaId: respuestaSeleccionada }
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    //  Obtener el token real aquí
    const token = "TOKEN_DE_EJEMPLO"; 

    useEffect(() => {
        const loadQuestions = async () => {
            if (!token) {
                setError("No autenticado. Por favor, inicie sesión.");
                setLoading(false);
                return;
            }
            try {
                const data = await fetchEvaluationQuestions(token);
                setQuestions(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        loadQuestions();
    }, [token]);

    const handleAnswerChange = (questionId, selectedAnswerValue) => {
        setAnswers(prev => ({
            ...prev,
            // Aseguramos que la ID y el valor sean strings, como espera Python
            [String(questionId)]: String(selectedAnswerValue) 
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        
        if (Object.keys(answers).length !== questions.length) {
            alert("Por favor, responde todas las preguntas antes de enviar.");
            return;
        }

        setLoading(true);

        try {
            const finalResult = await submitEvaluationAnswers(token, answers);
            setResult(finalResult);
        } catch (err) {
            setError(err.message || 'Error desconocido al enviar la evaluación.');
        } finally {
            setLoading(false);
        }
    };

    if (loading) return <div className="text-center mt-5">Cargando Evaluación...</div>;
    if (error) return <div className="alert alert-danger mt-5">Error: {error}</div>;


    if (result) {
        const isApproved = result.puntaje >= 70; 
        return (
            <div className="container mt-5">
                <h2 className="text-primary">✨ Resultados de la Evaluación</h2>
                <div className={`alert ${isApproved ? 'alert-success' : 'alert-danger'}`}>
                    <h4>Puntaje Obtenido: {result.puntaje.toFixed(2)}%</h4>
                    <p>Respuestas Correctas: {result.respuestas_correctas} / {result.total_preguntas}</p>
                    <hr/>
                    <p><strong>Retroalimentación:</strong> {result.retroalimentacion}</p>
                </div>
                <button className="btn btn-secondary mt-3" onClick={() => window.history.back()}>
                    Volver al Contenido
                </button>
            </div>
        );
    }

    return (
        <div className="container mt-4">
            <h1 className="text-secondary">Evaluación de Inducción</h1>
            <p className="lead">Selecciona la respuesta correcta para cada pregunta. Debes responder las {questions.length} preguntas.</p>

            <form onSubmit={handleSubmit}>
                {questions.map((q, index) => (
                    <div key={q.id} className="card mb-4 shadow-sm">
                        <div className="card-body">
                            <h5 className="card-title">{index + 1}. {q.text}</h5>
                            
                            {/* Renderizar Opciones (asume que q.options es un array [ {value: 'A', text: 'Opción A'}, ... ]) */}
                            <div className="mt-3">
                                {q.options && q.options.map((option, idx) => (
                                    <div className="form-check" key={idx}>
                                        <input 
                                            className="form-check-input" 
                                            type="radio" 
                                            name={`question-${q.id}`} 
                                            id={`q${q.id}-opt${idx}`} 
                                            // Usamos option.value como el valor a enviar
                                            value={option.value} 
                                            onChange={() => handleAnswerChange(q.id, option.value)}
                                            checked={answers[q.id] === String(option.value)}
                                            required
                                        />
                                        <label className="form-check-label" htmlFor={`q${q.id}-opt${idx}`}>
                                            {option.text}
                                        </label>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                ))}

                <button type="submit" className="btn btn-primary btn-lg w-100 mt-4" disabled={loading}>
                    {loading ? 'Enviando...' : 'Enviar Evaluación y Obtener Resultados'}
                </button>
            </form>
        </div>
    );
};

export default EvaluationView;