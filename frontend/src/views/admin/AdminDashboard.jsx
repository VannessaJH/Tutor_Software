import React, { useState, useEffect } from 'react';
import {AuthService } from '../../services/apiService.js';
import "./AdminDashboard.css"; 
"import '../../../../backend/src/models/user/usuarios_pendientes';"

export default function AdminDashboard() {

  const [usuariosPendientes, setUsuariosPendientes] = useState([]);
  const [seccionActiva, setSeccionActiva] = useState("inicio");

  useEffect(() => {
    console.log(' Sección activa cambiada:', seccionActiva);
    if (seccionActiva === "usuarios") {
      console.log(' Cargando usuarios pendientes...');
      cargarUsuariosPendientes();
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
        contrasena: "password123", // contraseña temporal
        rol: usuario.rol
    };
    
    console.log('🔍 Datos a enviar:', datosUsuario);
    
    try {
        const resultado = await AuthService.registrar(datosUsuario);
        console.log('🔍 Respuesta del registro:', resultado);
        
        // Recargar lista
        cargarUsuariosPendientes();
    } catch (error) {
        console.error('🔍 Error al aceptar usuario:', error);
    }
};

  const manejarRechazar = async (idUsuario) => {
    await AuthService.rechazarUsuario(idUsuario);
    cargarUsuariosPendientes(); 
  };



  return (
    <div className="admin-dashboard">
      <header className="header-etitc">
        <h1>Tutor Web de Investigación - Administrador</h1>
        <p>Gestión y supervisión del contenido institucional</p>
      </header>

      <nav className="admin-nav">
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
      </main>

      <footer className="footer-etitc">
        <p>© 2025 Escuela Tecnológica Instituto Técnico Central - ETITC</p>
      </footer>
    </div>
  );
}
