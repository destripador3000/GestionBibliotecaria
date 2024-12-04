-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-11-2024 a las 00:03:12
-- Versión del servidor: 10.4.32-MariaDB-log
-- Versión de PHP: 8.2.12



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_bibliotecario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id` int(7) NOT NULL,
  `nombre` varchar(40) NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gestion_prestamo`
--

CREATE TABLE `gestion_prestamo` (
  `id_estudiante` NOT NULL,
  `id_prestamo`  NOT NULL
);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `id`  NOT NULL,
  `nombre`  NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `multa`
--

CREATE TABLE `multa` (
  `id`  NOT NULL,
  `tipo`  NOT NULL,
  `id_prestamo`  NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `id` NOT NULL,
  `id_libro`  NOT NULL
) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `gestion_prestamo`
--
ALTER TABLE `gestion_prestamo`
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_prestamo` (`id_prestamo`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `multa`
--
ALTER TABLE `multa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_prestamo` (`id_prestamo`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_libro` (`id_libro`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `gestion_prestamo`
--
ALTER TABLE `gestion_prestamo`
  ADD CONSTRAINT `gestion_prestamo_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id`),
  ADD CONSTRAINT `gestion_prestamo_ibfk_2` FOREIGN KEY (`id_prestamo`) REFERENCES `prestamo` (`id`);

--
-- Filtros para la tabla `multa`
--
ALTER TABLE `multa`
  ADD CONSTRAINT `multa_ibfk_1` FOREIGN KEY (`id_prestamo`) REFERENCES `prestamo` (`id`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `prestamo_ibfk_2` FOREIGN KEY (`id_libro`) REFERENCES `libro` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
