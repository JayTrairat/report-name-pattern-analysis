CREATE TABLE IF NOT EXISTS `naming_elements_tagged_type_8`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `datatype_id` varchar(1) NOT NULL DEFAULT "8",
    `naming_element` varchar(100) NOT NULL,
    `naming_position` varchar(8) NOT NULL,
    PRIMARY KEY (`id`)
);
