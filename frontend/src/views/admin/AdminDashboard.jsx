import React, { useState, useEffect } from 'react';
import { AuthService } from '../../services/apiService.js';
import "./AdminDashboard.css";
"import '../../../../backend/src/models/user/usuarios_pendientes';"
import ApiService from '../../services/apiService.js';

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

  const [reporteResultados, setReporteResultados] = useState([]);
  const [historialEvaluaciones, setHistorialEvaluaciones] = useState([]);
  const [loadingHistorial, setLoadingHistorial] = useState(false);

  const [terminoBusquedaReporte, setTerminoBusquedaReporte] = useState('');
  const [reporteFiltrado, setReporteFiltrado] = useState([]);

  // -------- SEMILLEROS --------
  const [listaSemilleros, setListaSemilleros] = useState([]);
  const [busquedaSemillero, setBusquedaSemillero] = useState("");
  const [resultadosBusquedaSemilleros, setResultadosBusquedaSemilleros] = useState([]);
  const [semilleroSeleccionado, setSemilleroSeleccionado] = useState(null);
  const [mostrarFormularioSemillero, setMostrarFormularioSemillero] = useState(false);
  const [formSemillero, setFormSemillero] = useState({
    nombre: '',
    profesor: '',
    proyecto: '',
    año: '',
    descripcion: '',
    contacto: '',
    activo: true
  });

  // -------- CONVOCATORIAS --------
  const [listaConvocatorias, setListaConvocatorias] = useState([]);
  const [busquedaConvocatoria, setBusquedaConvocatoria] = useState("");
  const [resultadosBusquedaConvocatorias, setResultadosBusquedaConvocatorias] = useState([]);
  const [convocatoriaSeleccionada, setConvocatoriaSeleccionada] = useState(null);
  const [mostrarFormularioConvocatoria, setMostrarFormularioConvocatoria] = useState(false);
  const [formConvocatoria, setFormConvocatoria] = useState({
    titulo: '',
    tipo: '',
    año: '',
    numero: '',
    archivo_url: '',
    descripcion: '',
    fecha_limite: '',
    activa: true
  });

  // -------- REDES --------
  const [listaRedes, setListaRedes] = useState([]);
  const [busquedaRed, setBusquedaRed] = useState("");
  const [resultadosBusquedaRedes, setResultadosBusquedaRedes] = useState([]);
  const [redSeleccionada, setRedSeleccionada] = useState(null);
  const [mostrarFormularioRed, setMostrarFormularioRed] = useState(false);
  const [formRed, setFormRed] = useState({
    nombre: '',
    descripcion: '',
    tipo: '',
    enlace: '',
    activa: true
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

    if (seccionUsuarioActiva === 'consultar') {
      cargarReporteResultados();
    }
  }, [seccionActiva, seccionUsuarioActiva]);

  useEffect(() => {


    if (!reporteResultados || reporteResultados.length === 0 || !terminoBusquedaReporte.trim()) {
      setReporteFiltrado(reporteResultados);
      return;
    }

    const termino = terminoBusquedaReporte.toLowerCase();


    const resultados = reporteResultados.filter(usuario => {

      const nombreCoincide = usuario.nombre_usuario && usuario.nombre_usuario.toLowerCase().includes(termino);
      const idCoincide = String(usuario.id_usuario).includes(termino);
      return nombreCoincide || idCoincide;
    });

    setReporteFiltrado(resultados);

  }, [reporteResultados, terminoBusquedaReporte]);

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

  const cargarReporteResultados = async () => {
    try {
      const data = await AuthService.obtenerReporteResultados();
      setReporteResultados(data);
      console.log("Reporte de resultados cargado:", data);
    } catch (error) {
      console.error("Error cargando el reporte de resultados:", error);
    }
  };

  const manejarCerrarSesion = () => {

    AuthService.cerrarSesion();

    window.location.href = '/login';
  };

  // Cargar lista de semilleros (llamar API si existe)
 const buscarSemilleros = async () => {
  try {
    const semilleros = await ApiService.obtenerSemilleros();
    console.log('Semilleros obtenidos:', semilleros);
    setListaSemilleros(semilleros);
  } catch (error) {
    console.error('Error:', error.message);
  }
};

const modificarSemillero = async (id, nuevosDatos) => {
  try {
    const resultado = await ApiService.modificarSemillero(id, nuevosDatos);
    console.log('Semillero modificado:', resultado);
    alert('¡Semillero actualizado correctamente!');
  } catch (error) {
    console.error('Error al modificar:', error.message);
    alert('Error: ' + error.message);
  }
};

  const buscarElemento = async (busqueda) => {
  if (!busqueda.trim()) {
    alert('Por favor, escribe algo para buscar');
    return;
  }

  try {
    let resultados = [];
    
    switch (moduloActivo) {
      case 'semilleros':
        resultados = await ApiService.buscarSemilleroPorNombre(busqueda);
        break;
      case 'convocatorias':
        resultados = await ApiService.buscarConvocatoriaPorNombre(busqueda);
        break;
      case 'redes':
        // Implementa búsqueda para redes
        break;
    }

    setResultadosBusqueda(resultados);
    setElementoSeleccionado(null);
    setMostrarFormulario(false);
    
  } catch (error) {
    console.error('Error buscando:', error);
    alert('Error al buscar: ' + error.message);
  }
};

const seleccionarElemento = (elemento) => {
  setElementoSeleccionado(elemento);
  setFormData({
    nombre: elemento.nombre || elemento.titulo,
    descripcion: elemento.descripcion,
    // ... otros campos
  });
  setMostrarFormulario(true);
};

const guardarCambios = async () => {
  if (!elementoSeleccionado) return;

  try {
    switch (moduloActivo) {
      case 'semilleros':
        await ApiService.modificarSemillero(elementoSeleccionado.id, formData);
        break;
      case 'convocatorias':
        await ApiService.modificarConvocatoria(elementoSeleccionado.id, formData);
        break;
      case 'redes':
        await ApiService.modificarRed(elementoSeleccionado.id, formData);
        break;
    }

    alert('Cambios guardados exitosamente!');
    // Limpiar estados
    setElementoSeleccionado(null);
    setMostrarFormulario(false);
    setResultadosBusqueda([]);
    
  } catch (error) {
    console.error('Error guardando cambios:', error);
    alert('Error al guardar: ' + error.message);
  }
};

  // ------------ Cargar convocatorias ------------
  const cargarConvocatorias = async () => {
    try {
      const data = await AuthService.obtenerConvocatorias();
      setListaConvocatorias(data);
    } catch (error) {
      console.error("Error cargando convocatorias:", error);
    }
  };

  // ------------ Buscar convocatoria ------------
  const buscarConvocatoria = () => {
    if (!busquedaConvocatoria.trim()) {
      alert("Escribe un nombre para buscar.");
      return;
    }

    const encontrada = listaConvocatorias.find(c =>
      c.nombre.toLowerCase().includes(busquedaConvocatoria.toLowerCase())
    );

    if (!encontrada) {
      alert("No se encontró ninguna convocatoria.");
      setConvocatoriaSeleccionada(null);
      return;
    }

    setConvocatoriaSeleccionada(encontrada);
    setFormConvocatoria({
      nombre: encontrada.nombre,
      descripcion: encontrada.descripcion
    });
  };

  // ------------ Guardar cambios ------------
  const guardarCambiosConvocatoria = async () => {
    if (!formConvocatoria.nombre || !formConvocatoria.descripcion) {
      alert("Completa todos los campos");
      return;
    }

    try {
      await AuthService.modificarConvocatoria(
        convocatoriaSeleccionada.id,
        formConvocatoria
      );

      alert("Convocatoria actualizada");
      cargarConvocatorias();
      setConvocatoriaSeleccionada(null);

    } catch (error) {
      console.error("Error al actualizar:", error);
    }
  };


  // ------------ Cargar redes ------------
  const cargarRedes = async () => {
    try {
      const data = await ApiService.obtenerRedes();
      setListaRedes(data);
    } catch (error) {
      console.error("Error cargando redes:", error);
    }
  };

  const buscarRed = async () => {
    if (!busquedaRed.trim()) {
      alert("Escribe un nombre para buscar.");
      return;
    }

    try {
      const resultados = await ApiService.buscarRedPorNombre(busquedaRed);
      setResultadosBusquedaRedes(resultados);
      setRedSeleccionada(null);
      setMostrarFormularioRed(false);
    } catch (error) {
      console.error("Error buscando red:", error);
      alert("Error al buscar red");
    }
  };

  const seleccionarRed = (red) => {
    setRedSeleccionada(red);
    setFormRed({
      nombre: red.nombre || '',
      descripcion: red.descripcion || '',
      tipo: red.tipo || '',
      enlace: red.enlace || '',
      activa: red.activa || true
    });
    setMostrarFormularioRed(true);
  };

  const guardarCambiosRed = async () => {
    if (!redSeleccionada) return;

    try {
      await ApiService.modificarRed(redSeleccionada.id, formRed);
      alert("Red actualizada correctamente");
      cargarRedes();
      setRedSeleccionada(null);
      setMostrarFormularioRed(false);
      setResultadosBusquedaRedes([]);
    } catch (error) {
      console.error("Error al actualizar red:", error);
      alert("Error al actualizar red: " + error.message);
    }
  };





  const cargarHistorialEvaluaciones = async (idUsuario) => {
    setLoadingHistorial(true);
    setUsuarioSeleccionado(idUsuario);

    try {
      const data = await AuthService.obtenerHistorialEvaluaciones(idUsuario);
      setHistorialEvaluaciones(data);
    } catch (error) {
      console.error("No se pudo cargar el historial:", error);
      setHistorialEvaluaciones([]);
    } finally {
      setLoadingHistorial(false);
    }
  };


  const volverAlReporte = () => {
    setUsuarioSeleccionado(null);
    setHistorialEvaluaciones([]);
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


        <button
          onClick={manejarCerrarSesion}

          style={{ backgroundColor: '#B71C1C', color: 'white' }}
        >
          🚪 Cerrar Sesión
        </button>
        <button onClick={() => setSeccionActiva("semilleros")}>📚 Semilleros</button>
        <button onClick={() => setSeccionActiva("convocatorias")}>🧩 Convocatorias</button>
        <button onClick={() => setSeccionActiva("usuarios")}>👥 Usuarios Pendientes</button>
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

        {seccionActiva === "gestion-usuarios" && seccionUsuarioActiva === "consultar" && (
          <section>
            {usuarioSeleccionado === null ? (
              <>
                <h2>Reporte de Resultados de Evaluación</h2>
                <p>Lista de usuarios y sus resultados más recientes.</p>

                <div className="search-box reporte-search">
                  <input
                    type="text"
                    placeholder="Buscar por nombre o ID..."
                    value={terminoBusquedaReporte}
                    onChange={(e) => setTerminoBusquedaReporte(e.target.value)}
                  />

                </div>


                <div className="reporte-lista">
                  <table>

                    <tbody>

                      {reporteResultados.map(r => (
                        <tr
                          key={r.id_usuario}

                          onClick={() => cargarHistorialEvaluaciones(r.id_usuario)}
                          style={{ cursor: 'pointer' }}
                        >
                          <td>{r.id_usuario}</td>
                          <td>{r.nombre_usuario}</td>
                          <td>{r.puntaje}</td>
                          <td>{new Date(r.fecha).toLocaleDateString()}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </>
            ) : (

              <div className="historial-detalle">
                <button onClick={volverAlReporte}>← Volver al Reporte General</button>
                <h3>Historial de Evaluaciones de Usuario ID: {usuarioSeleccionado}</h3>

                {loadingHistorial ? (
                  <p>Cargando historial...</p>
                ) : historialEvaluaciones.length > 0 ? (
                  <table>
                    <thead>
                      <tr>
                        <th>ID Evaluación</th>
                        <th>Fecha</th>
                        <th>Puntaje</th>
                      </tr>
                    </thead>
                    <tbody>
                      {historialEvaluaciones.map(h => (
                        <tr key={h.id_evaluacion}>
                          <td>{h.id_evaluacion}</td>
                          <td>{new Date(h.fecha).toLocaleString()}</td>
                          <td>{h.puntaje}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                ) : (
                  <p>Este usuario no tiene evaluaciones registradas.</p>
                )}
              </div>
            )}
          </section>
        )}

         {/* SECCIÓN DE SEMILLEROS */}
        {seccionActiva === 'semilleros' && (
          <section>
            <h2>📚 Gestión de Semilleros</h2>
            
            <div className="search-box mb-3">
              <input
                type="text"
                placeholder="Buscar semillero por nombre..."
                value={busquedaSemillero}
                onChange={(e) => setBusquedaSemillero(e.target.value)}
              />
              <button onClick={buscarSemillero}>🔍 Buscar</button>
            </div>

            {resultadosBusquedaSemilleros.length > 0 && !mostrarFormularioSemillero && (
              <div className="resultados-lista">
                <h4>Resultados encontrados:</h4>
                {resultadosBusquedaSemilleros.map((semillero) => (
                  <div key={semillero.id} className="item-resultado">
                    <span>{semillero.nombre} - {semillero.profesor} ({semillero.año})</span>
                    <button onClick={() => seleccionarSemillero(semillero)}>
                      ✏️ Modificar
                    </button>
                  </div>
                ))}
              </div>
            )}

            {mostrarFormularioSemillero && semilleroSeleccionado && (
              <div className="formulario-modificacion">
                <h4>Modificando: {semilleroSeleccionado.nombre}</h4>
                
                <div className="form-group">
                  <label>Nombre:</label>
                  <input
                    type="text"
                    value={formSemillero.nombre}
                    onChange={(e) => setFormSemillero({...formSemillero, nombre: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Profesor:</label>
                  <input
                    type="text"
                    value={formSemillero.profesor}
                    onChange={(e) => setFormSemillero({...formSemillero, profesor: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Proyecto:</label>
                  <input
                    type="text"
                    value={formSemillero.proyecto}
                    onChange={(e) => setFormSemillero({...formSemillero, proyecto: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Año:</label>
                  <input
                    type="number"
                    value={formSemillero.año}
                    onChange={(e) => setFormSemillero({...formSemillero, año: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Descripción:</label>
                  <textarea
                    value={formSemillero.descripcion}
                    onChange={(e) => setFormSemillero({...formSemillero, descripcion: e.target.value})}
                    rows="3"
                  />
                </div>

                <div className="acciones-formulario">
                  <button onClick={guardarCambiosSemillero} className="btn-guardar">
                    💾 Guardar Cambios
                  </button>
                  <button 
                    onClick={() => {
                      setMostrarFormularioSemillero(false);
                      setSemilleroSeleccionado(null);
                    }} 
                    className="btn-cancelar"
                  >
                    ❌ Cancelar
                  </button>
                </div>
              </div>
            )}
          </section>
        )}

        {/* SECCIÓN DE CONVOCATORIAS */}
        {seccionActiva === 'convocatorias' && (
          <section>
            <h2>🧩 Gestión de Convocatorias</h2>
            
            <div className="search-box mb-3">
              <input
                type="text"
                placeholder="Buscar convocatoria por título..."
                value={busquedaConvocatoria}
                onChange={(e) => setBusquedaConvocatoria(e.target.value)}
              />
              <button onClick={buscarConvocatoria}>🔍 Buscar</button>
            </div>

            {resultadosBusquedaConvocatorias.length > 0 && !mostrarFormularioConvocatoria && (
              <div className="resultados-lista">
                <h4>Resultados encontrados:</h4>
                {resultadosBusquedaConvocatorias.map((convocatoria) => (
                  <div key={convocatoria.id} className="item-resultado">
                    <span>{convocatoria.titulo} - {convocatoria.tipo} ({convocatoria.año})</span>
                    <button onClick={() => seleccionarConvocatoria(convocatoria)}>
                      ✏️ Modificar
                    </button>
                  </div>
                ))}
              </div>
            )}

            {mostrarFormularioConvocatoria && convocatoriaSeleccionada && (
              <div className="formulario-modificacion">
                <h4>Modificando: {convocatoriaSeleccionada.titulo}</h4>
                
                <div className="form-group">
                  <label>Título:</label>
                  <input
                    type="text"
                    value={formConvocatoria.titulo}
                    onChange={(e) => setFormConvocatoria({...formConvocatoria, titulo: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Tipo:</label>
                  <input
                    type="text"
                    value={formConvocatoria.tipo}
                    onChange={(e) => setFormConvocatoria({...formConvocatoria, tipo: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Año:</label>
                  <input
                    type="number"
                    value={formConvocatoria.año}
                    onChange={(e) => setFormConvocatoria({...formConvocatoria, año: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Descripción:</label>
                  <textarea
                    value={formConvocatoria.descripcion}
                    onChange={(e) => setFormConvocatoria({...formConvocatoria, descripcion: e.target.value})}
                    rows="3"
                  />
                </div>

                <div className="acciones-formulario">
                  <button onClick={guardarCambiosConvocatoria} className="btn-guardar">
                    💾 Guardar Cambios
                  </button>
                  <button 
                    onClick={() => {
                      setMostrarFormularioConvocatoria(false);
                      setConvocatoriaSeleccionada(null);
                    }} 
                    className="btn-cancelar"
                  >
                    ❌ Cancelar
                  </button>
                </div>
              </div>
            )}
          </section>
        )}

        {/* SECCIÓN DE REDES */}
        {seccionActiva === 'redes' && (
          <section>
            <h2>🔗 Gestión de Redes</h2>
            
            <div className="search-box mb-3">
              <input
                type="text"
                placeholder="Buscar red por nombre..."
                value={busquedaRed}
                onChange={(e) => setBusquedaRed(e.target.value)}
              />
              <button onClick={buscarRed}>🔍 Buscar</button>
            </div>

            {resultadosBusquedaRedes.length > 0 && !mostrarFormularioRed && (
              <div className="resultados-lista">
                <h4>Resultados encontrados:</h4>
                {resultadosBusquedaRedes.map((red) => (
                  <div key={red.id} className="item-resultado">
                    <span>{red.nombre} - {red.tipo}</span>
                    <button onClick={() => seleccionarRed(red)}>
                      ✏️ Modificar
                    </button>
                  </div>
                ))}
              </div>
            )}

            {mostrarFormularioRed && redSeleccionada && (
              <div className="formulario-modificacion">
                <h4>Modificando: {redSeleccionada.nombre}</h4>
                
                <div className="form-group">
                  <label>Nombre:</label>
                  <input
                    type="text"
                    value={formRed.nombre}
                    onChange={(e) => setFormRed({...formRed, nombre: e.target.value})}
                  />
                </div>

                <div className="form-group">
                  <label>Descripción:</label>
                  <textarea
                    value={formRed.descripcion}
                    onChange={(e) => setFormRed({...formRed, descripcion: e.target.value})}
                    rows="3"
                  />
                </div>

                <div className="form-group">
                  <label>Enlace:</label>
                  <input
                    type="text"
                    value={formRed.enlace}
                    onChange={(e) => setFormRed({...formRed, enlace: e.target.value})}
                  />
                </div>

                <div className="acciones-formulario">
                  <button onClick={guardarCambiosRed} className="btn-guardar">
                    💾 Guardar Cambios
                  </button>
                  <button 
                    onClick={() => {
                      setMostrarFormularioRed(false);
                      setRedSeleccionada(null);
                    }} 
                    className="btn-cancelar"
                  >
                    ❌ Cancelar
                  </button>
                </div>
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
