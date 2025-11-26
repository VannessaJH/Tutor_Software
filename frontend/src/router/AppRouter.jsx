// frontend/src/router/AppRouter.jsx

import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import ContenidoView from '../views/student/ContenidoView';
import EvaluationView from '../views/student/EvaluationView';

const ProtectedRoute = ({ children }) => {
    // ⚠️ IMPLEMENTAR LÓGICA DE AUTENTICACIÓN REAL AQUÍ
    // const { isAuthenticated, userRole } = useAuthStore();
    const isAuthenticated = true; // Simulación: estás logueado
    const userRole = 'student'; // Simulación: eres estudiante

    if (!isAuthenticated) {
        // Redirigir al login si no está autenticado
        return <Navigate to="/login" replace />; 
    }

    if (userRole !== 'student') {
        // Redirigir a una página de error o al dashboard si el rol no coincide
        return <Navigate to="/unauthorized" replace />;
    }

    // Si está autenticado y es estudiante, renderiza el contenido
    return children;
};


const AppRouter = () => {
    return (
        // 1. Usar BrowserRouter como wrapper principal
        <BrowserRouter>
            {/* 2. Definir los grupos de rutas */}
            <Routes>

                {/* RUTAS PÚBLICAS (Login/Registro) */}
                {/* <Route path="/login" element={<LoginView />} /> */}
                <Route path="/" element={<Navigate to="/student/content" />} /> 
                
                {/* ------------------------------------------- */}
                {/* RUTAS DEL ESTUDIANTE (Protegidas) */}
                {/* ------------------------------------------- */}
                <Route 
                    path="/student" 
                    element={
                        // Envolviendo todo en el Layout si usas uno
                        // <ProtectedRoute><MainLayout /></ProtectedRoute> 
                        <ProtectedRoute><div>{/* Simulación de Layout */}</div></ProtectedRoute>
                    }
                >
                    {/* Ruta para ver el contenido HTML migrado */}
                    <Route 
                        path="content" 
                        element={<ContenidoView />} 
                    />
                    
                    {/* Ruta para realizar la evaluación */}
                    <Route 
                        path="evaluation" 
                        element={<EvaluationView />} 
                    />
                </Route>

                {/* ------------------------------------------- */}
                {/* MANEJO DE ERRORES */}
                {/* ------------------------------------------- */}
                {/* <Route path="*" element={<NotFound />} /> */}
                
            </Routes>
        </BrowserRouter>
    );
};

export default AppRouter;