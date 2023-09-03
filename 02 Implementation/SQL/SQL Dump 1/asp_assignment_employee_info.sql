-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: asp_assignment
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `employee_info`
--

DROP TABLE IF EXISTS `employee_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_info` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `FullName` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Postcode` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Telephone` varchar(45) DEFAULT NULL,
  `DateOfBirth` date NOT NULL,
  `StartDate` date NOT NULL,
  `AdminID` varchar(45) DEFAULT NULL,
  `Level` int NOT NULL,
  `Password` varchar(45) NOT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_info`
--

LOCK TABLES `employee_info` WRITE;
/*!40000 ALTER TABLE `employee_info` DISABLE KEYS */;
INSERT INTO `employee_info` VALUES (1,'Administrator','NA','NA','NA',NULL,'2023-08-10','2010-08-23','1',3,'Administrator'),(2,'Alex Wall','NA','NA','NA',NULL,'2002-05-13','2023-10-08','2',2,'Testing'),(3,'James Holt','unknown','unknown','NA',NULL,'2002-07-10','2023-08-11','1',1,'Password'),(5,'Alex Wall','30a Springfield Drive','MK43 8LE','awall02@hotmail.co.uk','07757218761','2002-05-13','2023-08-11','2',2,'Password'),(6,'sdkjihf','sdf','sdf','sdf@kjashd.com','sdf','6069-05-12','2455-03-12','1',1,'Password'),(7,'testing','testing','testing','test@testing.com','3214','3424-02-20','2324-04-23','1',1,'Password'),(8,'Daniel Wall','30a Springfield Drive','MK43 8LE','dwall04@hotmail.co.uk','07961932291','2344-04-23','3432-02-24','1',1,'Password'),(9,'Jake Doherty','NA','NA','NA@NA.com','012345678910','2023-08-15','2023-08-16','1',1,'Password');
/*!40000 ALTER TABLE `employee_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-20 18:03:05
