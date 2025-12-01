import React, { useState } from 'react';
import { AuthService } from '../../services/apiService.js';
import './AuthCommon.css';
import './Login.css';

/* * Componente de Login. 
 * Recibe onLoginSuccess y onSwitchView (para ir al registro) como props.
*/
const Login = ({ onLoginSuccess, onSwitchView }) => {
    const [formData, setFormData] = useState({
        // Usamos 'correo' en lugar de 'usuario'
        correo: '', 
        contrasena: ''
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
        setLoading(true);
        setError('');

        try {
            // Llama al servicio de autenticación con el objeto formData
            const resultado = await AuthService.login(formData);

            if (resultado.error) {
                setError(resultado.error);
            } else {
                onLoginSuccess(resultado);
            }
        } catch (error) {
            // Manejo de error de conexión
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
                    {/* El input usa 'correo' como nombre para coincidir con el estado y pide un email */}
                    <input type="email" name="correo" value={formData.correo} onChange={handleChange} required />
                    <label>Correo Electrónico</label> {/* Etiqueta actualizada */}
                    <span></span>
                </div>

                <div className="input-group">
                    <input type="password" name="contrasena" value={formData.contrasena} onChange={handleChange} required />
                    <label>Contraseña</label>
                    <span></span>
                </div>

                <input type="submit" value={loading ? "Ingresando..." : "Iniciar sesión"} disabled={loading} />

                {error && <p className="error-message">{error}</p>}

                <div className="registrarse">
                    {/* ENLACE FUNCIONAL: Llama a onSwitchView para ir a Registro */}
                    ¿No tienes cuenta? <a href="#" onClick={(e) => { e.preventDefault(); onSwitchView(); }}>Regístrate aquí</a>
                </div>
            </form>
        </div>
    );
};

export default Login;