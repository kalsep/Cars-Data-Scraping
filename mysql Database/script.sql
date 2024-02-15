-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema car_dekho
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `car_dekho` ;

-- -----------------------------------------------------
-- Schema car_dekho
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `car_dekho` DEFAULT CHARACTER SET utf8 ;
USE `car_dekho` ;

-- -----------------------------------------------------
-- Table `car_dekho`.`Brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`Brand` (
  `idBrand` INT NOT NULL AUTO_INCREMENT,
  `Brandname` VARCHAR(45) NOT NULL,
  `Brand Url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idBrand`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Brandname_UNIQUE` ON `car_dekho`.`Brand` (`Brandname` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `car_dekho`.`Models`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`Models` (
  `idModels` INT NOT NULL AUTO_INCREMENT,
  `Model Name` VARCHAR(45) NOT NULL,
  `Model Url` VARCHAR(100) NOT NULL,
  `idBrand` INT NOT NULL,
  PRIMARY KEY (`idModels`),
  CONSTRAINT `fk_Models_Brand`
    FOREIGN KEY (`idBrand`)
    REFERENCES `car_dekho`.`Brand` (`idBrand`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`ModelVariant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`ModelVariant` (
  `idModelvariant` INT NOT NULL AUTO_INCREMENT,
  `Modelvariantname` TEXT NOT NULL,
  `ModelVarianturl` TEXT NOT NULL,
  `idModels` INT NOT NULL,
  PRIMARY KEY (`idModelvariant`),
  CONSTRAINT `fk_Modelvariant_Models1`
    FOREIGN KEY (`idModels`)
    REFERENCES `car_dekho`.`Models` (`idModels`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`PriceInformationDelhi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`PriceInformationDelhi` (
  `idPriceInformation` INT NOT NULL AUTO_INCREMENT,
  `Ex-showroom price` INT NULL,
  `RTO` INT NULL,
  `Insurance` INT NULL,
  `Others` INT NULL,
  `Optional` INT NULL,
  `On-Road Price` INT NOT NULL,
  `idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idPriceInformation`),
  CONSTRAINT `fk_PriceInformation_Modelvariant1`
    FOREIGN KEY (`idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`Key Specifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`Key Specifications` (
  `idSpecification` INT NOT NULL AUTO_INCREMENT,
  `Fuel Type` VARCHAR(100) NULL,
  `Transmission Type` VARCHAR(100) NULL,
  `City Mileage` VARCHAR(100) NULL,
  `Engine Displacement` VARCHAR(100) NULL,
  `Max Power` VARCHAR(100) NULL,
  `Seating Capacity` VARCHAR(100) NULL,
  `Boot Space` VARCHAR(100) NULL,
  `Body Type` VARCHAR(100) NULL,
  `Fuel Tank Capacity` VARCHAR(100) NULL,
  `No. of Cylinders` VARCHAR(100) NULL,
  `ARAI Mileage` VARCHAR(100) NULL,
  `idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idSpecification`),
  CONSTRAINT `fk_features_Modelvariant1`
    FOREIGN KEY (`idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`key Features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`key Features` (
  `idFeatures` INT NOT NULL AUTO_INCREMENT,
  `Multi-function Steering Wheel` VARCHAR(100) NULL,
  `Power Adjustable Exterior Rear View Mirror` VARCHAR(100) NULL,
  `Touch Screen` VARCHAR(100) NULL,
  `Automatic Climate Control` VARCHAR(100) NULL,
  `Engine Start Stop Button` VARCHAR(100) NULL,
  `Anti Lock Braking System` VARCHAR(100) NULL,
  `Alloy Wheels` VARCHAR(100) NULL,
  `Power Windows Rear` VARCHAR(100) NULL,
  `Power Windows Front` VARCHAR(100) NULL,
  `Wheel Covers` VARCHAR(100) NULL,
  `Passenger Airbag` VARCHAR(100) NULL,
  `Power Steering` VARCHAR(100) NULL,
  `Air Conditioner` VARCHAR(100) NULL,
  `idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idFeatures`),
  CONSTRAINT `fk_key Features_ModelVariant1`
    FOREIGN KEY (`idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
