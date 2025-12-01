import React from 'react';
import ReactDOM from 'react-dom/client';
// RUTA CORREGIDA: Asume que App.jsx está en el mismo nivel que index.jsx (dentro de la carpeta src)
import App from './App.jsx'; 
// Importa tu CSS si tienes uno, por ejemplo:
// import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);