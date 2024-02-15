from rich.console import Console
from configurations import *
from scraping_functions import *
from database_functions import *

def create_car_dekho_databse():
    start_url = "https://www.cardekho.com/newcars"
    print("Started Scrapping Brand Directory")
    brand_url_directctory = scrap_brand_directory(start_url)
    print("Brand Data Scrapped...")
    insert_brand(brand_url_directctory)
    print("Database Created For brand Directory")
    # print(brand_url_directctory)

    print("Working on Creating Databse of car Models Database")
    for brand, brand_url in brand_url_directctory.items():
    # for brand, brand_url in islice(brand_url_directctory.items(),16):
        print("Started Scraping Data")
        brand_model_directory = scrap_model_urls(brand_url)
        print("Data Scrape Complited..\nStarted Database Creation")
        insert_brand_model(brand_model_directory)
    print("Database Creationh completed")


    models_directory = get_brand_models_from_database()
    print("Starting Varinat scraper wizard")
    for idModel,model_name,model_url in models_directory:
       
        model_variant_directory = scrap_model_variant_url(model_url)
        insert_model_variant(idModel, model_variant_directory)

    print("WIzard Completed Database Creation\n")

    print("Major Updated Coming On th way..")

    varinat_directory = get_model_variant_url_from_database()
    # varinat_directory_temp = varinat_directory[:1]
    print("Creating Key Feature,Price,key Specifications Table\n")
    for idModelvariant,Modelvariantname,ModelVarianturl in varinat_directory:
        print(f"For Model {Modelvariantname}")
        price_info = scrap_on_road_price_delhi(ModelVarianturl)
        # print("**"*10,"Price Info","**"*10)
        # print(price_info)
        insert_price_information(price_info,idModelvariant)

        key_specification_info = scrap_key_specifications(ModelVarianturl)
        print("**"*10,"Key Specifications","**"*10)
        print(key_specification_info)
        print("---"*30)
        insert_key_specifications(key_specification_info,idModelvariant)

        key_feature_info = scrap_key_features(ModelVarianturl)
        print("*"*10,"Key Fetures","**"*10)
        print(key_feature_info)
        print("----"*40)
        insert_into_key_features(key_feature_info,idModelvariant)
    
    print("*****"*20)
    print("*****"*5,"Completed All Tasks","*****"*5)
    print("*****"*20)
        
if __name__=="__main__":
    print("*" * 50)
    print("Welcome to Car Dekho Database Creation!")
    print("*" * 50)
    create_car_dekho_databse()