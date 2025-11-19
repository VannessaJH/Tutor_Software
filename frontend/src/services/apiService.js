const API_BASE_URL = 'http://localhost:8001/api/auth';

export const AuthService = {
    async login(credenciales) {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credenciales)
        });
        return await response.json();
    },

    async registrar(usuarioData) {
        const response = await fetch(`${API_BASE_URL}/registrar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(usuarioData)
        });
        return await response.json();
    },

    async usuario_pendiente(usuarioData){
        const response = await fetch(`${API_BASE_URL}/usuario_pendiente`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  
            },
            body:JSON.stringify(usuarioData)
        });
        return await response.json();

    },

    async obtenerUsuariosPendientes() {
        const response = await fetch(`${API_BASE_URL}/obtener_usuarios_pendientes`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        return await response.json();
    },

    async aceptarUsuarioPendiente(idUsuarioPendiente) {
        const response = await fetch(`${API_BASE_URL}/aceptar_usuario/${idUsuarioPendiente}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        return await response.json();
    },

    async rechazarUsuario(idUsuario) {
        const response = await fetch(`${API_BASE_URL}/admin/rechazar_usuario/${idUsuario}`, {
            method: 'POST'
        });
        return await response.json();
    },



    async obtenerUsuarioActual() {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_BASE_URL}/usuario/actual`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        return await response.json();
    }
};