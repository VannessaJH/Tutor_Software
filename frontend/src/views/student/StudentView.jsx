import React, { useState } from 'react';
import ContentPage from './ContentPage';
import Evaluation from './Evaluation';

const StudentView = () => {
    const [currentView, setCurrentView] = useState('content');
    const [contentViewed, setContentViewed] = useState(false);

    const handleContentViewed = () => {
        setContentViewed(true);
        setCurrentView('evaluation');
    };

    return (
        <div>
            {currentView === 'content' && (
                <ContentPage onViewed={handleContentViewed} />
            )}
            {currentView === 'evaluation' && contentViewed && (
                <Evaluation />
            )}
        </div>
    );
};

export default StudentView;