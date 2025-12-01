import React, { useState, useEffect } from 'react';
import Login from './Login.js';
import Register from './Register.js';
import  AdminDashboard from '../admin/AdminDashboard.jsx';
import ContentView from '../student/ContenidoView.jsx';

import './AuthCommon.css';
import './Login.css';
import './Register.css';


export default function AuthApp() {
    const [currentView, setCurrentView] = useState('login');
    const [user, setUser] = useState(null);

    const handleLoginSuccess = (userData) => {
        console.log('Usuario logueado:', userData);
        console.log(' Datos recibidos del backend:', userData);
        setUser(userData);

        localStorage.setItem('user', JSON.stringify(userData));
    };


    if (user) {
        if (user.rol === 'Administrador') {
            return <AdminDashboard />;
        } else {
            return <ContentView user={user} />;
        }
    }

    return currentView === 'login' 
        ? <Login onLoginSuccess={handleLoginSuccess}  
            onSwitchView={() => setCurrentView('register')} />
        : <Register onRegister={() => setCurrentView('login')} 
            onGoToLogin={() => setCurrentView('login')}  />;
}

