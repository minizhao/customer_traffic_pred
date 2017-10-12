/*
SQLyog  v12.2.6 (64 bit)
MySQL - 5.7.19 : Database - zdb_udc
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`zdb_udc` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `zdb_udc`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` varchar(20) COLLATE utf8_bin NOT NULL,
  `name` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `user` */

insert  into `user`(`id`,`name`) values 
('1','Michael');

/*Table structure for table `zt_traffic_prediction` */

DROP TABLE IF EXISTS `zt_traffic_prediction`;

CREATE TABLE `zt_traffic_prediction` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `storeId` bigint(20) DEFAULT NULL,
  `day` date DEFAULT NULL,
  `predictions` varchar(2000) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `zt_traffic_prediction` */

insert  into `zt_traffic_prediction`(`id`,`storeId`,`day`,`predictions`) values 
(1,1,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(2,1,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(3,1,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(4,1,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(5,1,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(6,1,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(7,2,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(8,2,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(9,2,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(10,2,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(11,2,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(12,2,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(13,3,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(14,3,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(15,3,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(16,3,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(17,3,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(18,3,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(19,4,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(20,4,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(21,4,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(22,4,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(23,4,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(24,4,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(25,5,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(26,5,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(27,5,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(28,5,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(29,5,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(30,5,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(31,6,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(32,6,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(33,6,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(34,6,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(35,6,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(36,6,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(37,7,'2017-08-04','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(38,7,'2017-08-05','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(39,7,'2017-08-06','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(40,7,'2017-08-07','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(41,7,'2017-08-08','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]'),
(42,7,'2017-08-09','[[1284,345],[2335,565],[5768,888],[3455,666],[2354,657],[23443,6556],[2355,434],[34545,5454],[4545,555],[33454,657],[67676,766],[4354,55],[23455,66],[34556,324],[7676,777],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;