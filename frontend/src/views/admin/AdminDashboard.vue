<template>
  <div class="admin-dashboard">
    <header class="header">
      <h1>Panel de Administración – Tutor Web ETITC</h1>
      <p>Bienvenido, administrador. Aquí puedes gestionar el contenido y validar usuarios.</p>
    </header>

    <nav class="menu">
      <button @click="seccion='usuarios'">👥 Gestión de Usuarios</button>
      <button @click="seccion='contenido'">📰 Actualizar Contenido</button>
      <button @click="seccion='reportes'">📊 Reportes</button>
      <button @click="seccion='convocatorias'">📢 Convocatorias</button>
    </nav>

    <section class="contenido">
      <div v-if="seccion==='usuarios'">
        <h2>Gestión de Usuarios</h2>
        <p>Valida el registro de nuevos usuarios o elimina cuentas inactivas.</p>
        <table class="tabla">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Rol</th>
              <th>Estado</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in usuarios" :key="index">
              <td>{{ user.id }}</td>
              <td>{{ user.nombre }}</td>
              <td>{{ user.rol }}</td>
              <td>{{ user.estado }}</td>
              <td>
                <button class="btn-verde" @click="aprobarUsuario(user)">Aprobar</button>
                <button class="btn-rojo" @click="eliminarUsuario(user)">Eliminar</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else-if="seccion==='contenido'">
        <h2>Actualización de Contenido</h2>
        <p>Aquí puedes editar la información institucional, semilleros y noticias.</p>
        <textarea v-model="contenido" rows="6" placeholder="Escribe el nuevo contenido..."></textarea>
        <button class="btn-verde" @click="guardarContenido">💾 Guardar Cambios</button>
      </div>

      <div v-else-if="seccion==='reportes'">
        <h2>Reportes Generales</h2>
        <p>Visualiza la actividad de los estudiantes y docentes registrados.</p>
        <ul>
          <li>Total usuarios activos: {{ reportes.usuariosActivos }}</li>
          <li>Total proyectos registrados: {{ reportes.proyectos }}</li>
          <li>Convocatorias vigentes: {{ reportes.convocatorias }}</li>
        </ul>
      </div>

      <div v-else-if="seccion==='convocatorias'">
        <h2>Convocatorias ETITC</h2>
        <iframe
          src="https://www.etitc.edu.co/es/page/investigacion&convocatorias"
          width="100%"
          height="500"
          frameborder="0"
        ></iframe>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "AdminDashboard",
  data() {
    return {
      seccion: 'usuarios',
      usuarios: [
        { id: 1, nombre: "Laura Gómez", rol: "Estudiante", estado: "Pendiente" },
        { id: 2, nombre: "Carlos Ruiz", rol: "Docente", estado: "Activo" },
      ],
      contenido: "",
      reportes: {
        usuariosActivos: 58,
        proyectos: 12,
        convocatorias: 3,
      },
    };
  },
  methods: {
    aprobarUsuario(user) {
      alert(`Usuario ${user.nombre} aprobado ✅`);
    },
    eliminarUsuario(user) {
      alert(`Usuario ${user.nombre} eliminado ❌`);
    },
    guardarContenido() {
      alert("Contenido actualizado correctamente 💾");
    },
  },
};
</script>

<style scoped>
.admin-dashboard {
  padding: 20px;
  font-family: "Poppins", sans-serif;
  background-color: #f5fff7;
  color: #003b1c;
}

.header {
  background-color: #008037;
  color: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}

.menu {
  margin: 20px 0;
  display: flex;
  gap: 10px;
  justify-content: center;
}

.menu button {
  background-color: #00a859;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}
.menu button:hover {
  background-color: #007b46;
}

.tabla {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  margin-top: 15px;
  border-radius: 8px;
  overflow: hidden;
}
.tabla th {
  background-color: #008037;
  color: white;
  padding: 10px;
}
.tabla td {
  padding: 10px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

textarea {
  width: 100%;
  border-radius: 8px;
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}

.btn-verde {
  background-color: #00a859;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 6px;
  cursor: pointer;
  margin-right: 5px;
}
.btn-verde:hover {
  background-color: #007b46;
}

.btn-rojo {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 6px;
  cursor: pointer;
}
.btn-rojo:hover {
  background-color: #c0392b;
}
</style>
