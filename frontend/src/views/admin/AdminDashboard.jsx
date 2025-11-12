import React from "react";
import "./AdminDashboard.css"; // para estilos personalizados si quieres

export default function AdminDashboard() {
  return (
    <div className="admin-dashboard">
      <header className="header-etitc">
        <h1>Tutor Web de Investigación - Administrador</h1>
        <p>Gestión y supervisión del contenido institucional</p>
      </header>

      <nav className="admin-nav">
        <button>🏠 Inicio</button>
        <button>📚 Semilleros</button>
        <button>🧩 Convocatorias</button>
        <button>👥 Usuarios</button>
        <button>📝 Evaluaciones</button>
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
