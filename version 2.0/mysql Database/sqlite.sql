-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql

PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;
BEGIN TRANSACTION;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
DROP SCHEMA IF EXISTS `car_dekho` ;
CREATE SCHEMA IF NOT EXISTS `car_dekho` DEFAULT  ;

CREATE TABLE IF NOT EXISTS `car_dekho`.`Brand` (
`idBrand` INT NOT NULL ,
`Brandname` TEXT NOT NULL,
`Brand Url` TEXT NOT NULL,
PRIMARY KEY (`idBrand`))
ENGINE = InnoDB;
CREATE UNIQUE INDEX `Brandname_UNIQUE` ON `car_dekho`.`Brand` (`Brandname` ASC) VISIBLE;

CREATE TABLE IF NOT EXISTS `car_dekho`.`Models` (
`idModels` INT NOT NULL ,
`Model Name` TEXT NOT NULL,
`Model Url` TEXT NOT NULL,
`idBrand` INT NOT NULL,
PRIMARY KEY (`idModels`),
CONSTRAINT `fk_Models_Brand`
FOREIGN KEY (`idBrand`)
REFERENCES `car_dekho`.`Brand` (`idBrand`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `car_dekho`.`ModelVariant` (
`idModelvariant` INT NOT NULL ,
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

CREATE TABLE IF NOT EXISTS `car_dekho`.`PriceInformationDelhi` (
`idPriceInformation` INT NOT NULL ,
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

CREATE TABLE IF NOT EXISTS `car_dekho`.`Key Specifications` (
`idSpecification` INT NOT NULL ,
`Fuel Type` TEXT NULL,
`Transmission Type` TEXT NULL,
`City Mileage` TEXT NULL,
`Engine Displacement` TEXT NULL,
`Max Power` TEXT NULL,
`Seating Capacity` TEXT NULL,
`Boot Space` TEXT NULL,
`Body Type` TEXT NULL,
`Fuel Tank Capacity` TEXT NULL,
`No. of Cylinders` TEXT NULL,
`ARAI Mileage` TEXT NULL,
`idModelvariant` INT NOT NULL,
PRIMARY KEY (`idSpecification`),
CONSTRAINT `fk_features_Modelvariant1`
FOREIGN KEY (`idModelvariant`)
REFERENCES `car_dekho`.`ModelVariant` (`idModelvariant`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `car_dekho`.`key Features` (
`idFeatures` INT NOT NULL ,
`Multi-function Steering Wheel` TEXT NULL,
`Power Adjustable Exterior Rear View Mirror` TEXT NULL,
`Touch Screen` TEXT NULL,
`Automatic Climate Control` TEXT NULL,
`Engine Start Stop Button` TEXT NULL,
`Anti Lock Braking System` TEXT NULL,
`Alloy Wheels` TEXT NULL,
`Power Windows Rear` TEXT NULL,
`Power Windows Front` TEXT NULL,
`Wheel Covers` TEXT NULL,
`Passenger Airbag` TEXT NULL,
`Power Steering` TEXT NULL,
`Air Conditioner` TEXT NULL,
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





COMMIT;
PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
