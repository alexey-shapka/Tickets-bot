-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июл 26 2019 г., 22:09
-- Версия сервера: 5.6.38
-- Версия PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `tickets_db`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Concerts`
--

CREATE TABLE `Concerts` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Place` text NOT NULL,
  `Date` datetime NOT NULL,
  `Price` int(11) NOT NULL,
  `Seat_1` text NOT NULL,
  `Seat_2` text NOT NULL,
  `Seat_3` text NOT NULL,
  `Seat_4` text NOT NULL,
  `Seat_5` text NOT NULL,
  `Seat_6` text NOT NULL,
  `Seat_7` text NOT NULL,
  `Seat_8` text NOT NULL,
  `Seat_9` text NOT NULL,
  `Seat_10` text NOT NULL,
  `Seat_11` text NOT NULL,
  `Seat_12` text NOT NULL,
  `Seat_13` text NOT NULL,
  `Seat_14` text NOT NULL,
  `Seat_15` text NOT NULL,
  `Seat_16` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Concerts`
--

INSERT INTO `Concerts` (`ID`, `Name`, `Place`, `Date`, `Price`, `Seat_1`, `Seat_2`, `Seat_3`, `Seat_4`, `Seat_5`, `Seat_6`, `Seat_7`, `Seat_8`, `Seat_9`, `Seat_10`, `Seat_11`, `Seat_12`, `Seat_13`, `Seat_14`, `Seat_15`, `Seat_16`) VALUES
(1, 'FOALS', 'Арт-завод Платформа\nКиев, ул. Беломорская, 1', '2019-08-27 19:00:00', 1190, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 'БУМБОКС. ТАЄМНИЙ КОД', 'Дворец Спорта\nКиев, Спортивная площадь, 1', '2019-11-09 19:00:00', 399, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(3, 'ЛЯПИС 98', 'Зелёный театр\nОдесса, парк им. Т.Г. Шевченко', '2019-07-23 20:00:00', 300, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Структура таблицы `Festivals`
--

CREATE TABLE `Festivals` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Place` text NOT NULL,
  `Date` datetime NOT NULL,
  `Price` int(11) NOT NULL,
  `Seat_1` text NOT NULL,
  `Seat_2` text NOT NULL,
  `Seat_3` text NOT NULL,
  `Seat_4` text NOT NULL,
  `Seat_5` text NOT NULL,
  `Seat_6` text NOT NULL,
  `Seat_7` text NOT NULL,
  `Seat_8` text NOT NULL,
  `Seat_9` text NOT NULL,
  `Seat_10` text NOT NULL,
  `Seat_11` text NOT NULL,
  `Seat_12` text NOT NULL,
  `Seat_13` text NOT NULL,
  `Seat_14` text NOT NULL,
  `Seat_15` text NOT NULL,
  `Seat_16` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Festivals`
--

INSERT INTO `Festivals` (`ID`, `Name`, `Place`, `Date`, `Price`, `Seat_1`, `Seat_2`, `Seat_3`, `Seat_4`, `Seat_5`, `Seat_6`, `Seat_7`, `Seat_8`, `Seat_9`, `Seat_10`, `Seat_11`, `Seat_12`, `Seat_13`, `Seat_14`, `Seat_15`, `Seat_16`) VALUES
(1, 'DISCO 80', 'Стадион \"Черноморец\"\nОдесса, г.Одесса', '2019-07-27 19:00:00', 200, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 'ФАЙНЕ МІСТО 2019', 'Тернопольский Ипподром\nТернополь, Ипподром', '2019-07-25 08:00:00', 250, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(3, 'БЕЛЫЕ НОЧИ', 'Арт-завод Платформа\nКиев, ул. Беломорская, 1', '2019-08-16 20:00:00', 350, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Структура таблицы `Theater`
--

CREATE TABLE `Theater` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Place` text NOT NULL,
  `Date` datetime NOT NULL,
  `Price` int(11) NOT NULL,
  `Seat_1` text NOT NULL,
  `Seat_2` text NOT NULL,
  `Seat_3` text NOT NULL,
  `Seat_4` text NOT NULL,
  `Seat_5` text NOT NULL,
  `Seat_6` text NOT NULL,
  `Seat_7` text NOT NULL,
  `Seat_8` text NOT NULL,
  `Seat_9` text NOT NULL,
  `Seat_10` text NOT NULL,
  `Seat_11` text NOT NULL,
  `Seat_12` text NOT NULL,
  `Seat_13` text NOT NULL,
  `Seat_14` text NOT NULL,
  `Seat_15` text NOT NULL,
  `Seat_16` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Theater`
--

INSERT INTO `Theater` (`ID`, `Name`, `Place`, `Date`, `Price`, `Seat_1`, `Seat_2`, `Seat_3`, `Seat_4`, `Seat_5`, `Seat_6`, `Seat_7`, `Seat_8`, `Seat_9`, `Seat_10`, `Seat_11`, `Seat_12`, `Seat_13`, `Seat_14`, `Seat_15`, `Seat_16`) VALUES
(1, 'БЕЛАЯ АКАЦИЯ', 'Театр музкомедии\nОдесса, ул. Пантелеймоновская, 3', '2019-07-27 18:30:00', 40, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 'ДЕТСКИЙ БАЛЕТ СПЯЩАЯ КРАСАВИЦА', 'Одесский Национальный Академический театр Оперы и Балета\nОдесса, пров. Чайковського, 1', '2019-07-27 11:00:00', 40, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(3, 'ДМИТРИЙ РОМАНОВ', 'Зелёный театр\nОдесса, парк им. Т.Г. Шевченко', '2019-07-24 20:00:00', 300, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Структура таблицы `Users`
--

CREATE TABLE `Users` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Surname` text NOT NULL,
  `Tickets` text NOT NULL,
  `Status_bot` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Concerts`
--
ALTER TABLE `Concerts`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `Festivals`
--
ALTER TABLE `Festivals`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `Theater`
--
ALTER TABLE `Theater`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Concerts`
--
ALTER TABLE `Concerts`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Festivals`
--
ALTER TABLE `Festivals`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Theater`
--
ALTER TABLE `Theater`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
