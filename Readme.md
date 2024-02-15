---

# Car Variant Information Scraper

## Overview

The Car Variant Information Scraper is a Python project designed to scrape car variant information from the CarDekho website. It consists of multiple Python files that work together to achieve the desired functionality. The project includes modules for scraping functions, database interactions, and configurations.

## Project Structure

The project includes the following files:

- `main.py`: This is the main Python script that orchestrates the scraping process by calling functions from other modules.
- `configurations.py`: This file contains configuration variables used throughout the project, such as URLs and database connection settings.
- `scraping_functions.py`: This module defines functions responsible for scraping data from web pages.
- `database_functions.py`: This module contains functions for interacting with the MySQL database, including inserting scraped data.
- `main_rich.py`: use this for rich termial interaction.

## Functionality

The project provides the following functionality:

### 1. Scraping Functions (`scraping_functions.py`)

- Functions to scrape brand directories, model URLs, variant URLs, on-road price details, key specifications, and key features from the CarDekho website.

### 2. Database Functions (`database_functions.py`)

- Functions to establish a database connection, insert data into the database tables (Brand, Models, ModelVariant, PriceInformationDelhi, Key Specifications, and Key Features), and retrieve data from the database for foreigh key.

### 3. Main Script (`main.py`,`main_rich.py`)

- The main script orchestrates the scraping process by calling functions from other modules in the appropriate sequence.

## Usage

To use this project, follow these steps:

1. Install the required dependencies listed in `requirements.txt` by running:
   ```
   pip install -r requirements.txt
   ```
2. Create database running `script.sql`

3. Configure the MySQL database connection settings in `configurations.py`.

4. Run the `main.py` or `main_rich.py` script:
   ```
   python main.py
   ```

## Dependencies

The project depends on the following Python libraries:

- requests
- BeautifulSoup
- mysql-connector-python
- pandas
- rich

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests to enhance its functionality or address any issues.

## License

This project is licensed under the [MIT License](LICENSE).

---