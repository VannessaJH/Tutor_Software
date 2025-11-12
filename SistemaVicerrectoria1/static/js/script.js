// ====== Mostrar solo una sección a la vez ======
function mostrarSeccion(id) {
    const secciones = document.querySelectorAll("main section");
    secciones.forEach(sec => sec.classList.remove("active"));
    document.getElementById(id).classList.add("active");

    // Cierra el menú lateral (en modo móvil)
    document.getElementById("sidebar").classList.remove("open");

    // Si se selecciona "logout", muestra solo el mensaje
    if (id === "logout") {
        document.querySelector(".logout-box").style.display = "flex";
    } else {
        document.querySelector(".logout-box").style.display = "none";
    }

    // Cierra todos los submenús al cambiar de sección
    document.querySelectorAll(".submenu").forEach(sub => {
        sub.style.display = "none";
    });
}

// ====== Menú desplegable de contenido ======
function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.style.display = submenu.style.display === "block" ? "none" : "block";
}

// ====== Abrir / cerrar el menú lateral (modo móvil) ======
function toggleMenu() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("open");
}

// ====== Cargar solo la sección de inicio al abrir ======
window.onload = function() {
    document.querySelectorAll("main section").forEach(sec => sec.classList.remove("active"));
    document.getElementById("inicio").classList.add("active");
};
