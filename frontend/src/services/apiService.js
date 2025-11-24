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

    async aceptarUsuario(idUsuarioPendiente) {
    
    const response = await fetch(`${API_BASE_URL}/aceptar_usuario/${idUsuarioPendiente}`, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        }
    });
    
    return await response.json();
},

async rechazarUsuario(idUsuarioPendiente) {
  
    const response = await fetch(`${API_BASE_URL}/rechazar_usuario/${idUsuarioPendiente}`, {
        method: 'DELETE', 
        headers: {
            'Content-Type': 'application/json',
        }
    });

    if (!response.ok) {
      
        throw new Error('Fallo al rechazar usuario');
    }

    return await response.json();
},

async obtenerTodosLosUsuarios() {
        const response = await fetch(`${API_BASE_URL}/usuarios_activos`);
        if (!response.ok) {
            throw new Error('Fallo al obtener todos los usuarios.');
        }
        return await response.json();
    },

    async eliminarUsuario(idUsuario) {
        const response = await fetch(`${API_BASE_URL}/usuario/${idUsuario}`, {
            method: 'DELETE', 
        });
        
        if (!response.ok) {
         
            const error = await response.json();
            throw new Error(error.error || 'Fallo al eliminar el usuario.');
        }

        return await response.json();
    },

    async buscarUsuario(nombre) {
       
        const response = await fetch(`${API_BASE_URL}/usuarios/buscar?nombre=${encodeURIComponent(nombre)}`);
        if (!response.ok) {
            throw new Error('Fallo al buscar usuarios.');
        }
        return await response.json();
    },

    async modificarUsuario(idUsuario, datos) {
        const response = await fetch(`${API_BASE_URL}/usuario/${idUsuario}`, {
            method: 'PUT', 
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(datos),
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Fallo al modificar el usuario.');
        }

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

