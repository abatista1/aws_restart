-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: university
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `ID` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Mark` int NOT NULL,
  `Grade` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (111111,'    John Smith    ',55,'P'),(111222,'David Alen Jones',89,'HD'),(119736,'Jim Lee',80,'D'),(124500,'Emilia Adams',56,'P'),(124578,'Carl Ridle',55,'P'),(124584,'Patrick Chan',50,'P'),(151515,'Paula Costa',77,'D'),(156457,'Allen field',54,'P'),(172534,'Lucy Lu',59,'P'),(174188,'Jessica Jones',67,'C'),(206893,'Sally Lin',65,'C'),(223488,'Chris Sven',91,'HD'),(333743,'Carol Knox',74,'C'),(348496,'Liza Ming',65,'C'),(420015,'Rico Gomez',70,'C'),(440055,'Paulo Rossi',45,'Z'),(444555,'Andreas Brehme',40,'Z'),(448094,'John Smith',50,'P'),(457848,'Dominic Xavier',49,'Z'),(558096,'Anna Cruz',80,'D'),(558866,'Carmen Shultz',99,'HD'),(563344,'Luke Cage',81,'D'),(645158,'Darius Beam',44,'Z'),(700560,'Serena Mateo',60,'P'),(702350,'Samia Ruben',85,'HD'),(705399,'Jin Jinhai',77,'D'),(745566,'Elena Miles',92,'HD'),(785275,'Jason Lim',66,'C'),(805370,'Alana Lopez',30,'Z'),(878451,'Daisy Bloom',66,'C'),(995932,'Adam Batler',88,'HD');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-01 12:38:47
