-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-11-2025 a las 23:03:15
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tutor_software`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre_usuario` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `rol` enum('Administrador','Usuario') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre_usuario`, `correo`, `contrasena`, `rol`) VALUES
(0, 'profesor_test', 'plqs@gmail.com', '$2b$12$DnQst48964gcWj8PVjSideJq7bXGjX57adTDwhnpdWfwDEwgLXGHy', NULL),
(0, 'Admin', 'admin@sistema.edu.co', '$2b$12$dtbtO59rTe6kkSVDrvUcauVD..F1P4sMylZjgIzXEVzrlx4e5xvny', 'Administrador'),
(0, 'Majo Solís', 'msol@gmail.com', '$2b$12$mvlxTbfaNPdwmFwPyntdbO5Ww1VOzMxHZ6moame3IlA3YEgpRmoPu', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_pendientes`
--

CREATE TABLE `usuarios_pendientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `estado` enum('Aceptado','Pendiente','Rechazado') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios_pendientes`
--

INSERT INTO `usuarios_pendientes` (`id`, `nombre`, `correo`, `contrasena`, `estado`) VALUES
(1, 'Majo Solís', 'msol@gmail.com', '$2b$12$Ynovmj33iyA20C25CG.WYuLobpgKeTeBz./QJl5CjMxHsS.M10xwi', 'Pendiente');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios_pendientes`
--
ALTER TABLE `usuarios_pendientes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios_pendientes`
--
ALTER TABLE `usuarios_pendientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
