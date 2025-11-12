
import React, { useState } from 'react';
import { AuthService } from '../../services/apiService.js';
import './AuthCommon.css';
import './Login.css';       // Estilos específicos

const Login = ({ onLoginSuccess, onSwitchView }) => {
    const [formData, setFormData] = useState({
        usuario: '',
        contraseña: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(' 1. Formulario enviado');
        console.log(' 2. Datos:', formData);
        setLoading(true);
        setError('');

        try {
            console.log(' 3. Llamando AuthService...');
            const resultado = await AuthService.login(formData);
            console.log(' 4. Respuesta backend:', resultado);
            
            if (resultado.error) {
                console.log(' 5. Error del backend:', resultado.error);
                setError(resultado.error);
            } else {
                console.log(' 6. Login exitoso');
                console.log('Login exitoso:', resultado);
                onLoginSuccess(resultado);
            }
        } catch (error) {
             console.log(' 7. Error catch:', error);
            setError('Error de conexión con el servidor');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="formulario">
        <h1>Inicio de sesión</h1>

        <form onSubmit={handleSubmit}> 
            <div className="input-group">
                <input type="text" name="usuario" value={formData.usuario} onChange={handleChange}  required/>
                <label>Nombre de Usuario</label>
                <span></span>
            </div>

            <div className="input-group">
                <input type="password" name="contrasena" value={formData.contrasena} onChange={handleChange} required />
                <label>Contraseña</label>
                <span></span>
            </div>

            <input type="submit" value="Iniciar sesión" />

            <div className="registrarse">
                ¿No tienes cuenta? <a href="#" onClick={(e) => { e.preventDefault(); onSwitchView(); }}>Regístrate aquí</a>
            </div>
        </form>
    </div>
    );
};

export default Login;