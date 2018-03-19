CREATE DATABASE IF NOT EXISTS `naming_analysis`;

USE `naming_analysis`;

DROP TABLE IF EXISTS `naming_elements`;
CREATE TABLE IF NOT EXISTS `naming_elements`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `datatype_id` varchar(1) NOT NULL DEFAULT '8',
  `naming_element` varchar(20) NOT NULL,
  `naming_position` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
);
