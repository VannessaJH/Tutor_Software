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
    }, 


    obtenerReporteResultados: async () => {
        const url = `${API_BASE_URL}/resultados/reporte`;
        console.log("Llamando a la API para obtener el reporte de resultados:", url);
        
        try {
            const token = localStorage.getItem('token'); 
            
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
        
                    'Authorization': `Bearer ${token}`, 
                },
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `Error al cargar los resultados: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error("Error en obtenerReporteResultados:", error);
            throw error; 
        }
    },

    cerrarSesion: () => {

        localStorage.removeItem('token');
   
        localStorage.removeItem('userRole'); 
       
        return true; 
    },

    obtenerHistorialEvaluaciones: async (idUsuario) => {
    const url = `${API_BASE_URL}/evaluaciones/usuario/${idUsuario}`;
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`, 
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Error al cargar el historial: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error(`Error en obtenerHistorialEvaluaciones para ID ${idUsuario}:`, error);
        throw error;
    }

}

};
// frontend/services/apiService.js

/**
 * Servicio para manejar todas las peticiones a la API del backend
 */
class ApiService {
  // URL base de tu backend
  static baseURL = 'http://localhost:8000';
  
  // ------------ AUTENTICACIÓN ------------
  static async registrar(usuarioData) {
    const response = await fetch(`${this.baseURL}/api/auth/registrar`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(usuarioData)
    });
    if (!response.ok) throw new Error('Error al registrar usuario');
    return await response.json();
  }

  static async login(credenciales) {
    const response = await fetch(`${this.baseURL}/api/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credenciales)
    });
    if (!response.ok) throw new Error('Error al iniciar sesión');
    return await response.json();
  }

  static async obtenerUsuariosPendientes() {
    const response = await fetch(`${this.baseURL}/api/auth/obtener_usuarios_pendientes`);
    if (!response.ok) throw new Error('Error al obtener usuarios pendientes');
    return await response.json();
  }

  static async aceptarUsuario(idUsuarioPendiente) {
    const response = await fetch(`${this.baseURL}/api/auth/aceptar_usuario/${idUsuarioPendiente}`, {
      method: 'POST'
    });
    if (!response.ok) throw new Error('Error al aceptar usuario');
    return await response.json();
  }

  static async rechazarUsuario(idUsuarioPendiente) {
    const response = await fetch(`${this.baseURL}/api/auth/rechazar_usuario/${idUsuarioPendiente}`, {
      method: 'DELETE'
    });
    if (!response.ok) throw new Error('Error al rechazar usuario');
    return await response.json();
  }

  static async obtenerTodosLosUsuarios() {
    const response = await fetch(`${this.baseURL}/api/auth/usuarios_activos`);
    if (!response.ok) throw new Error('Error al obtener usuarios activos');
    return await response.json();
  }

  static async buscarUsuario(nombre) {
    const response = await fetch(`${this.baseURL}/api/auth/usuarios/buscar?nombre=${encodeURIComponent(nombre)}`);
    if (!response.ok) throw new Error('Error al buscar usuario');
    return await response.json();
  }

  static async modificarUsuario(userId, datos) {
    const response = await fetch(`${this.baseURL}/api/auth/usuario/${userId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    });
    if (!response.ok) throw new Error('Error al modificar usuario');
    return await response.json();
  }

  static async eliminarUsuario(userId) {
    const response = await fetch(`${this.baseURL}/api/auth/usuario/${userId}`, {
      method: 'DELETE'
    });
    if (!response.ok) throw new Error('Error al eliminar usuario');
    return await response.json();
  }

  static async obtenerReporteResultados() {
    const response = await fetch(`${this.baseURL}/api/auth/resultados/reporte`);
    if (!response.ok) throw new Error('Error al obtener reporte de resultados');
    return await response.json();
  }

  static async obtenerHistorialEvaluaciones(idUsuario) {
    const response = await fetch(`${this.baseURL}/api/auth/evaluaciones/usuario/${idUsuario}`);
    if (!response.ok) throw new Error('Error al obtener historial de evaluaciones');
    return await response.json();
  }

  // ------------ SEMILLEROS ------------
  static async obtenerSemilleros(year = null) {
    let url = `${this.baseURL}/academic/semilleros/`;
    if (year) {
      url += `?year=${year}`;
    }
    const response = await fetch(url);
    if (!response.ok) throw new Error('Error al obtener semilleros');
    return await response.json();
  }

  static async buscarSemilleroPorNombre(nombre) {
    // Primero obtenemos todos los semilleros
    const semilleros = await this.obtenerSemilleros();
    // Luego filtramos localmente por nombre
    return semilleros.filter(s => 
      s.nombre.toLowerCase().includes(nombre.toLowerCase())
    );
  }

  static async obtenerSemilleroPorId(id) {
    const response = await fetch(`${this.baseURL}/academic/semilleros/${id}`);
    if (!response.ok) throw new Error('Error al obtener semillero');
    return await response.json();
  }

  static async modificarSemillero(id, datos) {
    const response = await fetch(`${this.baseURL}/academic/semilleros/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    });
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Error al modificar semillero');
    }
    return await response.json();
  }

  // ------------ CONVOCATORIAS ------------
  static async obtenerConvocatorias(onlyActive = null) {
    let url = `${this.baseURL}/academic/convocatorias/`;
    if (onlyActive !== null) {
      url += `?active=${onlyActive}`;
    }
    const response = await fetch(url);
    if (!response.ok) throw new Error('Error al obtener convocatorias');
    return await response.json();
  }

  static async buscarConvocatoriaPorNombre(titulo) {
    // Obtenemos todas las convocatorias
    const convocatorias = await this.obtenerConvocatorias();
    // Filtramos localmente por título
    return convocatorias.filter(c => 
      c.titulo.toLowerCase().includes(titulo.toLowerCase())
    );
  }

  static async obtenerConvocatoriaPorId(id) {
    const response = await fetch(`${this.baseURL}/academic/convocatorias/${id}`);
    if (!response.ok) throw new Error('Error al obtener convocatoria');
    return await response.json();
  }

  static async modificarConvocatoria(id, datos) {
    // NOTA: Primero necesitas crear la ruta PUT en el backend
    const response = await fetch(`${this.baseURL}/academic/convocatorias/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    });
    if (!response.ok) throw new Error('Error al modificar convocatoria');
    return await response.json();
  }

  // ------------ REDES ------------
  // IMPORTANTE: Primero necesitas crear el backend para Redes
  // Estas son las rutas que deberías crear en el backend
  
  static async obtenerRedes() {
    // Cambia esta URL según como crees el backend
    const response = await fetch(`${this.baseURL}/academic/redes/`);
    if (!response.ok) throw new Error('Error al obtener redes');
    return await response.json();
  }

  static async buscarRedPorNombre(nombre) {
    const redes = await this.obtenerRedes();
    return redes.filter(r => 
      r.nombre.toLowerCase().includes(nombre.toLowerCase())
    );
  }

  static async modificarRed(id, datos) {
    const response = await fetch(`${this.baseURL}/academic/redes/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    });
    if (!response.ok) throw new Error('Error al modificar red');
    return await response.json();
  }

  // ------------ CONTENIDO (para las páginas) ------------
  static async obtenerContenidoPorSlug(slug) {
    const response = await fetch(`${this.baseURL}/admin/content/${slug}`);
    if (!response.ok) throw new Error('Error al obtener contenido');
    return await response.json();
  }

  static async guardarContenido(data) {
    const response = await fetch(`${this.baseURL}/admin/content/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Error al guardar contenido');
    return await response.json();
  }

  // ------------ UTILIDADES ------------
  static async verificarConexion() {
    try {
      const response = await fetch(`${this.baseURL}/health`);
      return response.ok;
    } catch (error) {
      console.error('Error de conexión con el backend:', error);
      return false;
    }
  }

  static getAuthHeader() {
    // Si usas tokens JWT, aquí los agregas
    const token = localStorage.getItem('token');
    return token ? { 'Authorization': `Bearer ${token}` } : {};
  }

  static cerrarSesion() {
    // Limpia los datos de sesión del localStorage
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    // Redirige al login
    window.location.href = '/login';
  }
}

export default ApiService;

