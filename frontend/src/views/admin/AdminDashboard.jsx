import React, { useState, useEffect } from 'react';
import {AuthService } from '../../services/apiService.js';
import "./AdminDashboard.css"; 
"import '../../../../backend/src/models/user/usuarios_pendientes';"

export default function AdminDashboard() {

  const [usuariosPendientes, setUsuariosPendientes] = useState([]);
  const [todosLosUsuarios, setTodosLosUsuarios] = useState([]);
  const [seccionActiva, setSeccionActiva] = useState("inicio");
  const [menuVisible, setMenuVisible] = useState(false);
  const [seccionUsuarioActiva, setSeccionUsuarioActiva] = useState(null);

  const [terminoBusqueda, setTerminoBusqueda] = useState('');
  const [usuarioEncontrado, setUsuarioEncontrado] = useState(null);

  const [terminoBusquedaModificar, setTerminoBusquedaModificar] = useState('');
  const [resultadosBusqueda, setResultadosBusqueda] = useState([]);
  const [usuarioSeleccionado, setUsuarioSeleccionado] = useState(null);
  const [datosModificacion, setDatosModificacion] = useState({
    nombre: '',
    correo: '',
  });



  useEffect(() => {
    console.log(' Sección activa cambiada:', seccionActiva);
    if (seccionActiva === "usuarios") {
      console.log(' Cargando usuarios pendientes...');
      cargarUsuariosPendientes();
    }

    if (seccionUsuarioActiva === 'eliminar') {
        cargarTodosLosUsuarios(); 
    }
  }, [seccionActiva]);

  const cargarUsuariosPendientes = async () => {
    try {


      const data = await AuthService.obtenerUsuariosPendientes();
      console.log(' Usuarios recibidos:', data);
      setUsuariosPendientes(data);
    } catch (error) {
      console.error("Error cargando usuarios:", error);
    }
  };

  const manejarAceptar = async (usuario) => {
  
    
    const datosUsuario = {
        nombre: usuario.nombre,
        correo: usuario.correo, 
        contrasena: "", 
    };
    
    console.log('Datos a enviar:', datosUsuario);
    
    try {
        const resultado = await AuthService.registrar(datosUsuario);
        console.log(' Respuesta del registro:', resultado);
        
     
        cargarUsuariosPendientes();
    } catch (error) {
        console.error(' Error al aceptar usuario:', error);
    }
};

  const manejarRechazar = async (idUsuario) => {
    await AuthService.rechazarUsuario(idUsuario);
    cargarUsuariosPendientes(); 
  };

  const manejarEliminarUsuario = async (idUsuario) => {
   

    try {
        await AuthService.eliminarUsuario(idUsuario);
        alert(`Usuario con ID ${idUsuario} eliminado correctamente.`);
        
        
        setUsuarioEncontrado(null);
        setTerminoBusqueda('');
        cargarTodosLosUsuarios(); 
    } catch (error) {
        alert(`Error al eliminar usuario: ${error.message}`);
    }
  };

  const cargarTodosLosUsuarios = async () => {
    try {
        const data = await AuthService.obtenerTodosLosUsuarios();
        
        setTodosLosUsuarios(data); 
        console.log("Usuarios cargados para la búsqueda:", data);
    } catch (error) {
        console.error("Error cargando todos los usuarios:", error);
    }
};

  
  const buscarUsuarioPorNombre = () => {
    if (!terminoBusqueda.trim()) {
        alert("Por favor, introduce un nombre para buscar.");
        setUsuarioEncontrado(null);
        console.log("Buscando término:", terminoBusqueda.toLowerCase());
        return;
    }
    console.log("Buscando término:", terminoBusqueda.toLowerCase());
    const encontrado = todosLosUsuarios.find(usuario => {
    if (usuario && usuario.nombre_usuario) { 
     
        return usuario.nombre_usuario.toLowerCase().includes(terminoBusqueda.toLowerCase());
    }
    return false;
});
  

    if (encontrado) {
        setUsuarioEncontrado(encontrado);
    } else {
        alert(`No se encontró ningún usuario con el nombre: ${terminoBusqueda}`);
        setUsuarioEncontrado(null);
    }
  };

  const handleMenuClick = (opcion) => {
    setSeccionUsuarioActiva(opcion);
    setSeccionActiva("gestion-usuarios"); 
    setMenuVisible(false); 
  };

  

const manejarBusquedaModificar = async () => {
    if (!terminoBusquedaModificar.trim()) {
      alert("Por favor, introduce un nombre para buscar.");
      setResultadosBusqueda([]);
      return;
    }
    
    try {
      const data = await AuthService.buscarUsuario(terminoBusquedaModificar);
      setResultadosBusqueda(data);
      setUsuarioSeleccionado(null);
    } catch (error) {
      console.error("Error buscando usuarios:", error);
      setResultadosBusqueda([]);
    }
  };

  const seleccionarUsuarioParaModificar = (usuario) => {
    setUsuarioSeleccionado(usuario);
    setDatosModificacion({
      nombre: usuario.nombre,
      correo: usuario.correo,
    });
    setResultadosBusqueda([]); 
  };

  const manejarCambioFormulario = (e) => {
    const { name, value } = e.target;
    setDatosModificacion(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const manejarModificacion = async (e) => {
    e.preventDefault();
    if (!usuarioSeleccionado) return;

    const payload = {
        nombre: datosModificacion.nombre,
        correo: datosModificacion.correo,
    };

    try {
      const resultado = await AuthService.modificarUsuario(usuarioSeleccionado.id, payload);
      alert(resultado.mensaje);
      
      setUsuarioSeleccionado(null);
      setTerminoBusquedaModificar('');
      setDatosModificacion({ nombre: '', correo: '' });


    } catch (error) {
      alert(`Error al modificar usuario: ${error.message}`);
    }
  };

  return (
    <div className="admin-dashboard">
      <header className="header-etitc">
        <h1>Tutor Web de Investigación - Administrador</h1>
        <p>Gestión y supervisión del contenido institucional</p>
      </header>

      <nav className="admin-nav">

        <div className="menu-dropdown">
              <button 
                  onClick={() => setMenuVisible(!menuVisible)}
                  className="btn-menu"
              >
                  ⚙️ Gestión de Usuarios 
              </button>
              {menuVisible && (
                  <div className="dropdown-content">
                      <button onClick={() => handleMenuClick("eliminar")}>🗑️ Eliminar Usuario</button>
                      <button onClick={() => handleMenuClick("modificar")}>✏️ Modificar Usuario</button>
                      <button onClick={() => handleMenuClick("consultar")}>📋 Consultar Resultados</button>
                  </div>
              )}
          </div>


      <button onClick={() => setSeccionActiva("inicio")}>🏠 Inicio</button>
      <button onClick={() => setSeccionActiva("semilleros")}>📚 Semilleros</button>
      <button onClick={() => setSeccionActiva("convocatorias")}>🧩 Convocatorias</button>
      <button onClick={() => setSeccionActiva("usuarios")}>👥 Usuarios</button> 
      <button onClick={() => setSeccionActiva("evaluaciones")}>📝 Evaluaciones</button>
      </nav>

      <main className="admin-content">
        <section>
          <h2>Gestión de Contenido</h2>
          <p>
            Desde este panel, el administrador puede actualizar información de
            semilleros, validar registros de usuarios y agregar nuevas
            convocatorias.
          </p>
        </section>

        {seccionActiva === "usuarios" && (
          <section>
            <h2>Gestión de Usuarios Pendientes</h2>
            <div className="usuarios-pendientes">
              {console.log(' usuariosPendientes:', usuariosPendientes)}
              {console.log(' Tipo:', typeof usuariosPendientes)}
              {usuariosPendientes.map(usuario => (
                <div key={usuario.id} className="usuario-card">
                  <h4>{usuario.nombre}</h4>
                  <p>Email: {usuario.correo}</p>
                  <div className="acciones-usuario">
                    <button 
                      className="btn-aceptar"
                      onClick={() => manejarAceptar(usuario)}
                    >
                        Aceptar
                    </button>
                    <button 
                      className="btn-rechazar"
                      onClick={() => manejarRechazar(usuario.id)}
                    >
                        Rechazar
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        <section>
          <h3>Convocatorias Activas</h3>
          <iframe
            src="https://www.etitc.edu.co/es/page/investigacion&convocatorias"
            title="Convocatorias ETITC"
            width="100%"
            height="600px"
            style={{ borderRadius: "10px", border: "2px solid #1B5E20" }}
          ></iframe>
        </section>

        {seccionActiva === "gestion-usuarios" && seccionUsuarioActiva === "eliminar" && (
            <section>
                <h2>🗑️ Eliminar Usuario por Nombre</h2>
                <p>Busca un usuario por su nombre para confirmar su eliminación.</p>

             
                <div className="search-box">
                    <input
                        type="text"
                        placeholder="Introduce el nombre completo"
                        value={terminoBusqueda}
                        onChange={(e) => setTerminoBusqueda(e.target.value)}
                    />
                    <button onClick={buscarUsuarioPorNombre}>Buscar</button>
                </div>

                {usuarioEncontrado ? (
                    <div className="usuario-confirmacion-card">
                        <h3>Usuario Encontrado:</h3>
                        <p><strong>ID:</strong> {usuarioEncontrado.id}</p>
                        <p><strong>Nombre:</strong> {usuarioEncontrado.nombre_usuario}</p>
                        <p><strong>Email:</strong> {usuarioEncontrado.correo}</p>
                        
                        <div className="confirmacion-accion">
                            <button 
                                className="btn-eliminar-confirmar"
                                onClick={() => manejarEliminarUsuario(usuarioEncontrado.id)}
                            >
                               Eliminar
                            </button>
                            <button 
                                className="btn-cancelar"
                                onClick={() => { setUsuarioEncontrado(null); setTerminoBusqueda(''); }}
                            >
                                Cancelar
                            </button>
                        </div>
                    </div>
                ) : (
                    terminoBusqueda.trim() && <p>Introduce el nombre y haz clic en Buscar.</p>
                )}
            </section>
        )}

        {seccionActiva === "gestion-usuarios" && seccionUsuarioActiva === "modificar" && (
            <section>
                <h2>✏️ Modificar Usuario</h2>
                
                {!usuarioSeleccionado && (
                    <div className="search-box">
                        <input
                            type="text"
                            placeholder="Buscar usuario por nombre..."
                            value={terminoBusquedaModificar}
                            onChange={(e) => setTerminoBusquedaModificar(e.target.value)}
                        />
                        <button onClick={manejarBusquedaModificar}>Buscar</button>
                    </div>
                )}

                {resultadosBusqueda.length > 0 && !usuarioSeleccionado && (
                    <div className="resultados-busqueda">
                        <h3>Resultados encontrados:</h3>
                        {resultadosBusqueda.map(usuario => (
                            <div key={usuario.id} className="usuario-resultado">
                                <span>{usuario.nombre} ({usuario.correo})</span>
                                <button onClick={() => seleccionarUsuarioParaModificar(usuario)}>
                                    Seleccionar
                                </button>
                            </div>
                        ))}
                    </div>
                )}
                
     
                {usuarioSeleccionado && (
                    <div className="formulario-modificacion">
                        <h3>Modificando a: {usuarioSeleccionado.nombre} (ID: {usuarioSeleccionado.id})</h3>
                        <form onSubmit={manejarModificacion}>
                            <div>
                                <label>Nombre de Usuario</label>
                                <input
                                    type="text"
                                    name="nombre"
                                    value={datosModificacion.nombre}
                                    onChange={manejarCambioFormulario}
                                    required
                                />
                            </div>
                            <div>
                                <label>Correo Electrónico</label>
                                <input
                                    type="email"
                                    name="correo"
                                    value={datosModificacion.correo}
                                    onChange={manejarCambioFormulario}
                                    required
                                />
                            </div>
                            <button type="submit" className="btn-guardar">Guardar Cambios</button>
                            <button 
                                type="button" 
                                className="btn-cancelar"
                                onClick={() => setUsuarioSeleccionado(null)}
                            >
                                Cancelar
                            </button>
                        </form>
                    </div>
                )}
            </section>
        )}
      </main>

      <footer className="footer-etitc">
        <p>© 2025 Escuela Tecnológica Instituto Técnico Central - ETITC</p>
      </footer>
    </div>
  );
}
