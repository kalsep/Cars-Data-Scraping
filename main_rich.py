from configurations import *
from scraping_functions import *
from database_functions import *

def create_brand_model_table():
    brand_url_directory = scrap_brand_directory(start_url)
    insert_brand(brand_url_directory)
    with Progress() as progress:
        task = progress.add_task("[cyan]Scraping Brand Models...", total=len(brand_url_directory))
        for brand, brand_url in brand_url_directory.items():
            brand_model_directory = scrap_model_urls(brand_url)
            insert_brand_model(brand_model_directory)
            progress.update(task, advance=1)

def create_variant_table():
    models_directory = get_brand_models_url_from_database()
    with Progress() as progress:
        task = progress.add_task("[cyan]Scraping Model Variants...", total=len(models_directory))
        for idModel, model_name, model_url in models_directory:
            model_variant_directory = scrap_model_variant_url(model_url)
            insert_model_variant(idModel, model_variant_directory)
            progress.update(task, advance=1)

def scrape_variant_information():
    variant_directory = get_model_variant_url_from_database()
    with Progress() as progress:
        task = progress.add_task("[cyan]Scraping Variant Information...", total=len(variant_directory))
        for idModelvariant, Modelvariantname, ModelVarianturl in variant_directory:
            price_info = scrap_on_road_price_delhi(ModelVarianturl)
            insert_price_information(price_info, idModelvariant)

            key_specification_info = scrap_key_specifications(ModelVarianturl)
            insert_key_specifications(key_specification_info, idModelvariant)

            key_feature_info = scrap_key_features(ModelVarianturl)
            insert_into_key_features(key_feature_info, idModelvariant)
            progress.update(task, advance=1)

if __name__ == "__main__":
    create_brand_model_table()
    create_variant_table()
    scrape_variant_information()
