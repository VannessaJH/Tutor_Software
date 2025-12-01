
import React, { useState, useEffect } from 'react';
import ContentAccordionItem from '../../components/presentation/ContentAccordionItem'; 


const MIGRATED_CONTENT_SIMULATION = {
    'que-son-semilleros': {
        title: '1. ¿Qué son y cómo funcionan los Semilleros?',
        content_html: `<p>Los <b>Semilleros de Investigación</b> de la ETITC son la base de los grupos de investigación...</p><ul><li>Buscan la formación integral.</li><li>Requieren tutoría de un docente activo.</li></ul>`,
        slug: 'que-son-semilleros'
    },
    'requisitos-convocatoria': {
        title: '2. Requisitos Básicos para la Convocatoria X',
        content_html: `<p>Para aplicar, el estudiante debe:</p><ol><li>Tener promedio superior a 3.5.</li><li>Estar matriculado en el semestre actual.</li><li>Presentar propuesta avalada.</li></ol>`,
        slug: 'requisitos-convocatoria'
    }
};

const ContenidoView = () => {
    const [contentMap, setContentMap] = useState({});
    const [loading, setLoading] = useState(true);
    const [canEvaluate, setCanEvaluate] = useState(false);
    const [viewedStatus, setViewedStatus] = useState({}); 

    useEffect(() => {
        setTimeout(() => {
            setContentMap(MIGRATED_CONTENT_SIMULATION);
            setCanEvaluate(false); 
            setViewedStatus({'que-son-semilleros': true}); 
            setLoading(false);
        }, 800);
    }, []);

    const handleMarkViewed = async (slug) => {
        
        const newViewedStatus = {...viewedStatus, [slug]: true};
        setViewedStatus(newViewedStatus);
        
        if (Object.keys(newViewedStatus).length === Object.keys(contentMap).length) {
            setCanEvaluate(true);
        }
    };

    if (loading) {
        return <div className="text-center mt-5">Cargando Módulo...</div>;
    }

    const contentArray = Object.values(contentMap);

    return (
        <div className="container mt-4">
            <h1 className="text-success mb-4">📚 Módulo de Inducción a la Investigación</h1>
            
            <div className="alert alert-secondary mb-4 p-3 d-flex justify-content-between align-items-center">
                <span>Estado de Evaluación: {canEvaluate ? '✅ Habilitada' : '🚫 Faltan secciones por completar'}</span>
                <button 
                    className="btn btn-primary"
                    disabled={!canEvaluate}
                    onClick={() => alert("Navegar a la vista de Evaluación (frontend/src/views/student/EvaluationView.jsx)")}
                >
                    Iniciar Evaluación
                </button>
            </div>

            <div className="accordion" id="mainContentAccordion">
                {contentArray.map((item) => (
                    <ContentAccordionItem 
                        key={item.slug} 
                        targetId={item.slug} 
                        title={item.title} 
                        bodyHtml={item.content_html}
                        isCompleted={viewedStatus[item.slug] || false}
                        onMarkViewed={handleMarkViewed}
                    />
                ))}
            </div>
            
        </div>
    );
};

export default ContenidoView;