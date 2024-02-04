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
  `idBrand` INT NOT NULL,
  `Brandname` VARCHAR(45) NOT NULL,
  `Brand Url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idBrand`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Brandname_UNIQUE` ON `car_dekho`.`Brand` (`Brandname` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `car_dekho`.`Models`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`Models` (
  `idModels` INT AUTO_INCREMENT NOT NULL,
  `Model Name` VARCHAR(100) NOT NULL,
  `Model Url` VARCHAR(45) NOT NULL,
  `Brand_idBrand` INT NOT NULL,
  PRIMARY KEY (`idModels`),
  CONSTRAINT `fk_Models_Brand`
    FOREIGN KEY (`Brand_idBrand`)
    REFERENCES `car_dekho`.`Brand` (`idBrand`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`ModelVariant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`ModelVariant` (
  `idModelvariant` INT AUTO_INCREMENT NOT NULL,
  `Modelvariantname` VARCHAR(45) NOT NULL,
  `Models_idModels` INT NOT NULL,
  PRIMARY KEY (`idModelvariant`),
  CONSTRAINT `fk_Modelvariant_Models1`
    FOREIGN KEY (`Models_idModels`)
    REFERENCES `car_dekho`.`Models` (`idModels`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`PriceInformationDelhi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`PriceInformationDelhi` (
  `idPriceInformation` INT AUTO_INCREMENT NOT NULL,
  `Type of model` VARCHAR(45) NULL,
  `Ex-showroom price` INT NULL,
  `Insurance` INT NULL,
  `RTO` INT NULL,
  `Optional` VARCHAR(45) NULL,
  `On-Road Price` INT NOT NULL,
  `Modelvariant_idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idPriceInformation`),
  CONSTRAINT `fk_PriceInformation_Modelvariant1`
    FOREIGN KEY (`Modelvariant_idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`Key Specifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`Key Specifications` (
  `idfeatures` INT AUTO_INCREMENT NOT NULL,
  `Fuel Type` VARCHAR(45) NULL,
  `Transmission Type` VARCHAR(45) NULL,
  `City Mileage` VARCHAR(45) NULL,
  `Engine Displacement (cc)` VARCHAR(45) NULL,
  `Max Power (bhp@rpm)` VARCHAR(45) NULL,
  `Seating Capacity` VARCHAR(45) NULL,
  `Boot Space (Litres)` VARCHAR(45) NULL,
  `Body Type` VARCHAR(45) NULL,
  `Fuel Tank Capacity (Litres)` VARCHAR(45) NULL,
  `No. of Cylinders` VARCHAR(45) NULL,
  `ARAI Mileage` VARCHAR(45) NULL,
  `Modelvariant_idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idfeatures`),
  CONSTRAINT `fk_features_Modelvariant1`
    FOREIGN KEY (`Modelvariant_idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dekho`.`key Features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dekho`.`key Features` (
  `idFeatures` INT AUTO_INCREMENT NOT NULL,
  `Multi-function Steering Wheel` VARCHAR(45) NULL,
  `Power Adjustable Exterior Rear View Mirror` VARCHAR(45) NULL,
  `Touch Screen` VARCHAR(45) NULL,
  `Automatic Climate Control` VARCHAR(45) NULL,
  `Engine Start Stop Button` VARCHAR(45) NULL,
  `Anti Lock Braking System` VARCHAR(45) NULL,
  `Alloy Wheels` VARCHAR(45) NULL,
  `Power Windows Rear` VARCHAR(45) NULL,
  `Power Windows Front` VARCHAR(45) NULL,
  `Wheel Covers` VARCHAR(45) NULL,
  `Passenger Airbag` VARCHAR(45) NULL,
  `Power Steering` VARCHAR(45) NULL,
  `Air Conditioner` VARCHAR(45) NULL,
  `ModelVariant_idModelvariant` INT NOT NULL,
  PRIMARY KEY (`idFeatures`),
  CONSTRAINT `fk_key Features_ModelVariant1`
    FOREIGN KEY (`ModelVariant_idModelvariant`)
    REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
