-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2024 a las 07:17:44
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12




/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE libro (
  `ID`  INTEGER PRIMARY KEY AUTOINCREMENT,
  `Codigo` NOT NULL,
  `Autor` DEFAULT NULL,
  `Nombre`  NOT NULL
); 

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE prestamo (
  `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
  `Fecha` date NOT NULL,
  `libro`  NOT NULL,
  `estudiante`  NOT NULL
); 

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE usuario (
  `ID`   INTEGER PRIMARY KEY AUTOINCREMENT,
  `Codigo`  NOT NULL,
  `Password`  NOT NULL,
  `Rol`  NOT NULL
);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `libro`
--


--
-- Indices de la tabla `prestamo`


--
-- Indices de la tabla `usuario`
--

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `libro`
--


--
-- AUTO_INCREMENT de la tabla `prestamo`
--


--
-- AUTO_INCREMENT de la tabla `usuario`


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
