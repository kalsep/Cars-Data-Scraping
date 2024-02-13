from rich.console import Console
from configurations import *
from scraping_functions import *
from database_functions import *

def create_car_dekho_database():
    console = Console()
    
    with console.status("[bold green]Scraping brand directory..."):
        brand_url_directory = scrap_brand_directory("https://www.cardekho.com/newcars")

    with console.status("[bold green]Inserting brand data into the database..."):
        insert_brand(brand_url_directory)

    with console.status("[bold green]Scraping model URLs..."):
        brand_model_directory = {}
        for brand, url in brand_url_directory.items():
            brand_model_directory.update(scrap_model_urls(url))

    with console.status("[bold green]Inserting model data into the database..."):
        insert_brand_model(brand_model_directory)

    with console.status("[bold green]Scraping model variant URLs..."):
        for brand, model_url in brand_model_directory.items():
            model_variant_directory = scrap_model_variant_url(model_url)
            for model_name, model_url in model_variant_directory.items():
                model_id = get_model_id(model_name)
                insert_model_variant(model_id, model_variant_directory[model_name])

    with console.status("[bold green]Scraping price, key specifications, and key features..."):
        for model_id, model_name, model_url in get_brand_models_url():
            variant_info = scrap_model_variant_url(model_url)
            for variant_name, variant_url in variant_info.items():
                console.print(f"Processing {variant_name} of {model_name}...", style="bold cyan")
                price_info = scrap_on_road_price_delhi(variant_url)
                insert_price_information(price_info, model_id)

                key_specifications_info = scrap_key_specifications(variant_url)
                insert_key_specifications(key_specifications_info, model_id)

                key_features_info = scrap_key_features(variant_url)
                insert_into_key_features(key_features_info, model_id)

    console.print("[bold green]Database creation completed!")

if __name__ == "__main__":
    create_car_dekho_database()
