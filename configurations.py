from requests import get,request
from bs4 import BeautifulSoup
from time import time, sleep
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

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

base_url = "https://www.cardekho.com"

base_path = os.getcwd()

all_brands = ['maruti-suzuki-cars','Maruti Suzuki','Maruti', 'Tata', 'Kia', 'Toyota', 'Hyundai', 'Mahindra', 'Honda', 'MG', 
              'Skoda', 'Jeep', 'Renault', 'Nissan', 'Volkswagen', 'Citroen', 'Aston Martin', 
              'Audi', 'Bajaj', 'Bentley', 'BMW', 'BYD', 'Ferrari', 'Force', 'Isuzu', 'Jaguar', 
              'Lamborghini', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mclaren', 'Mercedes-Benz', 
              'Mini', 'PMV', 'Porsche', 'Pravaig', 'Rolls-Royce', 'Strom Motors', 'Volvo']

# all_brands = ['maruti-suzuki-cars', 'Tata']


def get_datbase_connection():
    # Connect to MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pravin@1995",
            database="car_dekho"  # Assuming your database name is car_dekho
        )

        cursor = connection.cursor()
        return cursor,connection

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        # exit(1)
