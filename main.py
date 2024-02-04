from configurations import *
from scraping_functions import *
from database_functions import *


start_url = "https://www.cardekho.com/newcars"
# brand_url_directctory = get_company_url(start_url)
# # insert_brand_from_dict(brand_url_directctory)
# # # print(brand_url_directctory)

# for brand, brand_url in brand_url_directctory.items():
# # for brand, brand_url in islice(brand_url_directctory.items(),16):
#     brand_model_directory = scrap_model_urls(brand_url)
    insert_brand_model(brand_model_directory)

# get_brand_models_url()
print(get_brand_models_url())