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
DROP TABLE IF EXISTS brand_models;
-- -----------------------------------------------------
-- Table `cardekho`.`brand_models`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardekho`.`brand_models` (
  `brand_models_id` INT AUTO_INCREMENT NOT NULL,
  `brand_model_name` VARCHAR(45) NULL,
  `model_url` VARCHAR(45) NULL,
  `brand_id` INT NOT NULL,
  PRIMARY KEY (`brand_models_id`),
  UNIQUE INDEX `brand_models_id_UNIQUE` (`brand_models_id` ASC) VISIBLE,
  INDEX `fk_brand_models_brand_names_idx` (`brand_id` ASC) VISIBLE,
  CONSTRAINT `fk_brand_models_brand_names`
    FOREIGN KEY (`brand_id`)
    REFERENCES `cardekho`.`brand_names` (`brand_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
