from requests import get, request
from bs4 import BeautifulSoup
import time
# from time import time, sleep
import random
import re
import os
import requests
from urllib.parse import urljoin, urlencode
import json
import pandas as pd
from datetime import datetime
from itertools import islice
import mysql.connector
from rich.console import Console
from rich.progress import Progress
from rich import print
from rich.progress import SpinnerColumn

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a user agent for web scraping
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# Define base URL and starting URL for web scraping
base_url = "https://www.cardekho.com"
start_url = "https://www.cardekho.com/newcars"

# Get the current working directory path
base_path = os.getcwd()

# List of all car brands to be scraped
all_brands = ['maruti-suzuki-cars', 'Maruti Suzuki', 'Maruti', 'Tata', 'Kia', 'Toyota', 'Hyundai', 'Mahindra', 'Honda', 'MG',
              'Skoda', 'Jeep', 'Renault', 'Nissan', 'Volkswagen', 'Citroen', 'Aston Martin',
              'Audi', 'Bajaj', 'Bentley', 'BMW', 'BYD', 'Ferrari', 'Force', 'Isuzu', 'Jaguar',
              'Lamborghini', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mclaren', 'Mercedes-Benz',
              'Mini', 'PMV', 'Porsche', 'Pravaig', 'Rolls-Royce', 'Strom Motors', 'Volvo']

# function for mysql database
def get_datbase_connection():
    # Connect to MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pravin@1995",
            database="car_dekho" 
        )

        cursor = connection.cursor()
        return cursor,connection

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        exit(1)
        
# function for sqlite database       
# def get_database_connection():
#     try:
#         connection = sqlite3.connect('car_dekho.db')
#         cursor = connection.cursor()
#         return cursor, connection
#     except sqlite3.Error as error:
#         print("Error while connecting to SQLite:", error)