-- Adminer 4.8.1 MySQL 8.0.29 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE AromaMocha;

USE AromaMocha;

DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Products` (`ID`, `Name`, `Price`, `Stock`) VALUES
(1,	'Hawaii Kona Coffee',	4,	500),
(2,	'Indian Coffee',	3.5,	1000),
(3,	'Aroma Italica',	5,	2000),
(4,	'Coffee Latte',	3,	1000),
(5,	'Aroma Americano',	5,	3000),
(6,	'Aroma Vanilla',	3,	1000),
(7,	'Vanilla Mochito',	5,	2000),
(8,	'Chai Latte',	3,	2000),
(9,	'Caramel Pudding',	4,	20),
(10,	'Caramel Choco Chips',	3,	300);

DROP TABLE IF EXISTS `Couriers`;
CREATE TABLE `Couriers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Couriers` (`ID`, `Name`, `Phone`) VALUES
(1,	'Deliveroo',	'0975868646'),
(3,	'Just Eat',	'0745985210'),
(4,	'Uber',	'098765432'),
(5,	'Swiggy',	'0986456336'),
(6,	'Zomato Delivery',	'876576757');

DROP TABLE IF EXISTS `Order_Status`;
CREATE TABLE `Order_Status` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Order_Status` (`ID`, `Name`) VALUES
(1,	'ORDER RECEIVED'),
(2,	'PREPARING'),
(3,	'OUT FOR DELIVERY'),
(4,	'DELIVERED');

DROP TABLE IF EXISTS `Orders`;
CREATE TABLE `Orders` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Order_Name` varchar(250) NOT NULL,
  `Customer_Name` varchar(255) NOT NULL,
  `Customer_Address` varchar(250) NOT NULL,
  `Customer_Phone` varchar(200) NOT NULL,
  `Courier_ID` int NOT NULL,
  `Order_Status` int NOT NULL,
  `Items` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Courier_ID` (`Courier_ID`),
  KEY `Order_Status` (`Order_Status`),
  KEY `Items` (`Items`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Courier_ID`) REFERENCES `Couriers` (`ID`),
  CONSTRAINT `Orders_ibfk_10` FOREIGN KEY (`Courier_ID`) REFERENCES `Couriers` (`ID`),
  CONSTRAINT `Orders_ibfk_11` FOREIGN KEY (`Order_Status`) REFERENCES `Order_Status` (`ID`),
  CONSTRAINT `Orders_ibfk_12` FOREIGN KEY (`Items`) REFERENCES `Products` (`ID`),
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`Order_Status`) REFERENCES `Order_Status` (`ID`),
  CONSTRAINT `Orders_ibfk_3` FOREIGN KEY (`Courier_ID`) REFERENCES `Couriers` (`ID`),
  CONSTRAINT `Orders_ibfk_4` FOREIGN KEY (`Order_Status`) REFERENCES `Order_Status` (`ID`),
  CONSTRAINT `Orders_ibfk_5` FOREIGN KEY (`Courier_ID`) REFERENCES `Couriers` (`ID`),
  CONSTRAINT `Orders_ibfk_6` FOREIGN KEY (`Order_Status`) REFERENCES `Order_Status` (`ID`),
  CONSTRAINT `Orders_ibfk_7` FOREIGN KEY (`Courier_ID`) REFERENCES `Couriers` (`ID`),
  CONSTRAINT `Orders_ibfk_8` FOREIGN KEY (`Order_Status`) REFERENCES `Order_Status` (`ID`),
  CONSTRAINT `Orders_ibfk_9` FOREIGN KEY (`Items`) REFERENCES `Products` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Orders` (`ID`, `Order_Name`, `Customer_Name`, `Customer_Address`, `Customer_Phone`, `Courier_ID`, `Order_Status`, `Items`) VALUES
(1,	'JD124',	'Jack Dorsey',	'5 Lilham London',	'6799600',	4,	3,	3),
(5,	'KN832',	'Kenny',	'88 Middle Town NW13BG',	'796857645',	1,	2,	3),
(6,	'KN832',	'Kenny',	'88 Middle Town NW13BG',	'796857645',	1,	2,	5),
(7,	'KN832',	'Kenny',	'88 Middle Town NW13BG',	'796857645',	1,	3,	5),
(8,	'NJ324',	'Nick J',	'78 Middlesex Town',	'0745982630',	6,	3,	7),
(10,	'KM982',	'Keith Marcus',	'54 Selson Road ',	'0654321098',	4,	3,	7),
(11,	'KM982',	'Keith Marcus',	'54 Selson Road ',	'0654321098',	4,	3,	6),
(12,	'NK876',	'Nikisha K',	'87 KK Road',	'0986875453',	4,	2,	3),
(14,	'JK235',	'John K',	'3 Kennedy Road',	'0973448244',	6,	4,	4);


