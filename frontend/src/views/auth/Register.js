import React, { useState } from 'react';
import { AuthService } from '../../services/apiService.js';
import './AuthCommon.css';
import './Register.css';    // Estilos específicos

const Register = ({ onRegisterSuccess, onGoToLogin }) => {
    const [formData, setFormData] = useState({
        nombre: '',
        correo: '',
        contrasena: '',

    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(' 1. Formulario registro enviado');
        console.log(' 2. Datos registro:', formData);
        setLoading(true);
        setError('');
        setSuccess('');


        if (formData.contrasena.length < 6) {
            setError('La contraseña debe tener al menos 6 caracteres');
            setLoading(false);
            return;
        }

        try {
            console.log('3. Llamando AuthService.usuario_pendiente...');
            const resultado = await AuthService.usuario_pendiente({
                nombre: formData.nombre,
                correo: formData.correo,
                contrasena: formData.contrasena,
            });
            console.log(' 4. Respuesta backend registro:', resultado);
            
            if (resultado.error) {
                setError(resultado.error);
            } else {
                setSuccess('SU solicitud ha sido enviada al administrador...');
           
                console.log(' 5. Uusario en espera');
                setTimeout(() => {
                    onGoToLogin();
                }, 2000);
            }
        } catch (error) {
            console.log(' 6. Error catch:', error);
            setError('Error de conexión con el servidor');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="formulario">
        <h1>Registro</h1>

        <form onSubmit={handleSubmit}>
            <div className="input-group">
                <input 
                    type="text" 
                    name="nombre" 
                    value={formData.nombre}
                    onChange={handleChange}
                    required 
                />
                <label>Nombre Completo</label>
                <span></span>
            </div>

            <div className="input-group">
                <input 
                    type="email" 
                    name="correo" 
                    value={formData.correo}
                    onChange={handleChange}
                    required 
                 />
                 <label>Correo Electrónico</label>
                <span></span>
            </div>

            <div className="input-group">
                <input 
                    type="password" 
                    name="contrasena" 
                    value={formData.contrasena}
                    onChange={handleChange}
                    required 
                />
                <label>Contraseña</label>
                <span></span>
            </div>

            <input type="submit" value="Registrarme" />

            <div className="registrarse">
                ¿Ya tienes cuenta? <a href="index.html">Inicia sesión</a>
            </div>
        </form>
    </div>
    );
};

export default Register;