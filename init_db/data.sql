-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: car_workshop
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `date_of_registration` date DEFAULT NULL,
  `is_regular` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('0e6547d6-3714-44ac-8547-94f20f440fc0','Anja','Stosic','astosic@gmail.com','+381632904329','2022-10-28',0),('1402c87b-9f5e-4b08-8be3-7fc636bd7d9e','Ivana','Todorovic','itodorovic@yahoo.com','+3816534284','2019-01-11',0),('70c505c3-5e87-47fe-8d94-c0153d128892','Stefan','Stankovic','sstankovic@gmail.com','+381632894298','2021-04-15',1),('dc0b7838-0e9e-4694-bc4a-8bc65037aabc','Marko','Jelic','mjelic@gmail.com','+38165943024','2023-02-22',0),('e295e582-95ef-4401-835d-f86ac986d156','Matija','Tadic','mtadic@gmail.com','+38163873173','2021-06-30',1),('f7d53689-96c9-45e3-9933-2d60607a7492','Uros','Seferovic','useferovic@gmail.com','+381674328742','2023-01-20',0);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `surname` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES ('2f5ff621-ca84-4bf7-b41f-8b49ca6942c6','Marija','Lovcevic','mlovcevic@gmail.com','6d8294e0048d1cd529fbb3a0bd4ea7a63eaf1eeb1d87f3a6582514235c469f4f','+381374831437','clerk',0),('335234ff-16f4-4549-ae08-872ccca87850','Luka','Stanojevic','lstanojevic@gmail.com','b60ccaae1d71e9dc00cd30d3b8f7084d5ef36a93ea742cb1eb203fd7e2eab9bd','+3817438743','clerk',0),('40426bc8-48d2-4b43-b300-f697355350fb','Vuk','Petrovic','vpetrovic@gmail.com',NULL,'+381657314713','mechanic',0),('44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','Nenad','Babic','nbabic@gmail.com',NULL,'+38168318631','mechanic',0),('4869dd5a-1c98-4e63-ab15-5d3b986fd7c8','Milos','Stanicic','mstanicic@gmail.com','253a46afd9d38f6bf114b2dfdf51b8d2c819e57911033b32d7938cc986ab975a','+38169045093','manager',1),('ea147890-d2bf-48d1-bf73-d6e5b8280fdf','Petar','Nedeljkovic','pnedeljkovic@gmail.com',NULL,'+38162632617231','mechanic',0);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_types`
--

DROP TABLE IF EXISTS `service_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_types` (
  `name` varchar(50) NOT NULL,
  `cost` float DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_types`
--

LOCK TABLES `service_types` WRITE;
/*!40000 ALTER TABLE `service_types` DISABLE KEYS */;
INSERT INTO `service_types` VALUES ('mali servis',2500),('nadogradnja',1500),('popravka',1000),('tehnicki pregled',3000),('veliki servis',5000);
/*!40000 ALTER TABLE `service_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle_services`
--

DROP TABLE IF EXISTS `vehicle_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_services` (
  `id` varchar(50) NOT NULL,
  `date_of_service` date DEFAULT NULL,
  `vehicle_id` varchar(50) DEFAULT NULL,
  `employee_id` varchar(50) DEFAULT NULL,
  `service_type_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vehicle_id` (`vehicle_id`),
  KEY `employee_id` (`employee_id`),
  KEY `service_type_name` (`service_type_name`),
  CONSTRAINT `vehicle_services_ibfk_1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`id`),
  CONSTRAINT `vehicle_services_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `vehicle_services_ibfk_3` FOREIGN KEY (`service_type_name`) REFERENCES `service_types` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle_services`
--

LOCK TABLES `vehicle_services` WRITE;
/*!40000 ALTER TABLE `vehicle_services` DISABLE KEYS */;
INSERT INTO `vehicle_services` VALUES ('03e6196e-491e-4df8-91f3-5c6d324087e0','2018-01-21','60d88e51-462e-4f8e-a8a9-87863ff98d31','ea147890-d2bf-48d1-bf73-d6e5b8280fdf','popravka'),('1672c288-a287-4d44-bcb9-8cdf1aa9aed9','2020-05-11','531d7d7b-90c0-463f-be5e-1a79a372187f','44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','nadogradnja'),('224397cc-b23c-41b3-bb01-a1f13cac69c2','2023-01-10','7bbbaeb6-7430-4d1e-af3a-abfc1b4c1e89','40426bc8-48d2-4b43-b300-f697355350fb','tehnicki pregled'),('49fa9fa5-6303-4901-b2e6-5b8609ec4ed3','2022-11-22','9b81b866-ff31-4c71-aa09-a93f60e2467a','44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','veliki servis'),('501c41cb-926f-4958-9047-fe57a90103bb','2022-11-22','6da4601b-2d37-412f-af27-28d8bee7b014','44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','mali servis'),('706e7f2c-99ad-4021-a463-d1daccb5a1bf','2022-07-19','4e0e18b6-7347-4739-afcf-fc83b32e553f','44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','veliki servis'),('730f3ec9-fd60-467b-a7cd-fbe84f6983d9','2021-10-13','f6bda753-b206-4ce3-9b39-856c022a76f2','44aa51eb-4207-43f5-86c9-a79f3f1a7ab8','popravka'),('b96c5353-bd5f-4469-ad44-96ec214942ad','2022-11-22','624e2f19-32bd-43cd-88f0-1414a06a960a','ea147890-d2bf-48d1-bf73-d6e5b8280fdf','tehnicki pregled'),('bed96ee3-1c53-4198-9c21-c697f7e915f5','2023-02-22','47e1b418-05eb-4359-a22c-5a000099dde3','40426bc8-48d2-4b43-b300-f697355350fb','mali servis');
/*!40000 ALTER TABLE `vehicle_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicles` (
  `id` varchar(50) NOT NULL,
  `license_plate` varchar(50) DEFAULT NULL,
  `manufacturer` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `manufacture_year` varchar(4) DEFAULT NULL,
  `customer_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `license_plate` (`license_plate`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `vehicles_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES ('47e1b418-05eb-4359-a22c-5a000099dde3','12-XC-19','Mercedes Benz','E320','2015','0e6547d6-3714-44ac-8547-94f20f440fc0'),('4e0e18b6-7347-4739-afcf-fc83b32e553f','NS-320-AB','Volkswagen','Golf 6','2013','dc0b7838-0e9e-4694-bc4a-8bc65037aabc'),('531d7d7b-90c0-463f-be5e-1a79a372187f','BG-998-BC','Mazda','6','2017','70c505c3-5e87-47fe-8d94-c0153d128892'),('60d88e51-462e-4f8e-a8a9-87863ff98d31','BG-408-OR','Volkswagen','Golf 5','2011','f7d53689-96c9-45e3-9933-2d60607a7492'),('624e2f19-32bd-43cd-88f0-1414a06a960a','BG-589-AD','BMW','M3','2006','f7d53689-96c9-45e3-9933-2d60607a7492'),('6da4601b-2d37-412f-af27-28d8bee7b014','BG-457-RE','Audi','A8','2016','f7d53689-96c9-45e3-9933-2d60607a7492'),('7bbbaeb6-7430-4d1e-af3a-abfc1b4c1e89','TO-123-AM','Tesla','Model S','2018','e295e582-95ef-4401-835d-f86ac986d156'),('9b81b866-ff31-4c71-aa09-a93f60e2467a','BG-115-MP','Volkswagen','Passat','2009','70c505c3-5e87-47fe-8d94-c0153d128892'),('f6bda753-b206-4ce3-9b39-856c022a76f2','NI-145-OR','BMW','520D','2017','1402c87b-9f5e-4b08-8be3-7fc636bd7d9e');
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 15:45:14
