from requests import get,request
from bs4 import BeautifulSoup
from time import time, sleep
import random
import re
import os
import requests
from urllib.parse import urljoin, urlencode
import json

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

base_url = "https://www.cardekho.com/"

base_path = os.getcwd()
