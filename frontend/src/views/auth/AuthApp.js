import React, { useState } from 'react';
import Login from './Login.js';
import Register from './Register.js';
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
        return <div>Bienvenido {user.nombre}</div>;
    }

    return currentView === 'login' 
        ? <Login onLoginSuccess={handleLoginSuccess}  
            onSwitchView={() => setCurrentView('register')} />
        : <Register onRegister={() => setCurrentView('login')} 
            onGoToLogin={() => setCurrentView('login')}  />;
}

