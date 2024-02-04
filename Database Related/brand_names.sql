-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cardekho
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cardekho
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cardekho` DEFAULT CHARACTER SET utf8 ;
USE `cardekho` ;
--------------------------------------------------------
DROP TABLE IF EXISTS brand_names;
-- -----------------------------------------------------
-- Table `cardekho`.`brand_names`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardekho`.`brand_names` (
  `brand_id` INT AUTO_INCREMENT NOT NULL,
  `brand_name` VARCHAR(45) NOT NULL unique,
  `brand_url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`brand_id`),
  UNIQUE INDEX `brand_id_UNIQUE` USING BTREE (`brand_id`) VISIBLE,
  UNIQUE INDEX `brand_name_UNIQUE` (`brand_name` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
