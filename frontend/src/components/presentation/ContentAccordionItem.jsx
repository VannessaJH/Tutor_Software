
import React from 'react';

const ContentAccordionItem = ({ title, bodyHtml, targetId, isCompleted, onMarkViewed }) => {
    
    const renderHtml = () => {
        return { __html: bodyHtml };
    };

    return (
        <div className="accordion-item">
            <h2 className="accordion-header" id={`heading-${targetId}`}>
                <button 
                    className="accordion-button collapsed" 
                    type="button" 
                    data-bs-toggle="collapse" 
                    data-bs-target={`#collapse-${targetId}`} 
                    aria-expanded="false" 
                    aria-controls={`collapse-${targetId}`}
                >
                    <span className="me-2">{isCompleted ? '✅' : '📖'}</span>
                    {title}
                </button>
            </h2>
            <div 
                id={`collapse-${targetId}`} 
                className="accordion-collapse collapse" 
                aria-labelledby={`heading-${targetId}`} 
                data-bs-parent="#mainContentAccordion"
            >
                <div className="accordion-body">
                    {}
                    <div className="mb-3" dangerouslySetInnerHTML={renderHtml()} />
                    
                    {!isCompleted && (
                        <button 
                            className="btn btn-sm btn-info mt-3"
                            onClick={() => onMarkViewed(targetId)}
                            disabled={isCompleted}
                        >
                            Marcar como Visto
                        </button>
                    )}
                    {isCompleted && (
                        <div className="alert alert-success mt-3 p-2">¡Contenido completado!</div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ContentAccordionItem;