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
    models_directory = get_brand_models_from_database()
    with Progress() as progress:
        task_scraping = progress.add_task("[cyan]Scraping Model Variants...", total=len(models_directory))
        task_inserting = progress.add_task("[cyan]Inserting Model Variants...", total=len(models_directory))
        
        for idModel, model_name, model_url in models_directory:
            # Scraping model variant URLs
            model_variant_directory = scrap_model_variant_url(model_url)
            insert_model_variant(idModel, model_variant_directory)
            
            # Update the progress bar for scraping and inserting tasks
            progress.update(task_scraping, advance=1)
            progress.update(task_inserting, advance=1)

    print("[green]Scraping and Inserting Completed.")

def scrape_and_create_variant_information_table():
    variant_directory = get_model_variant_url_from_database()
    cursor,connection=get_datbase_connection()
    with Progress() as progress:
        task_scraping = progress.add_task("[cyan]Scraping Variant Information...", total=len(variant_directory))

        for idModelvariant, Modelvariantname, ModelVarianturl in variant_directory:
            try:
                # Parse the HTML content using BeautifulSoup
                soup = get_soup(ModelVarianturl)
            
                # Scraping price information
                price_info = scrap_on_road_price_delhi(ModelVarianturl, soup)
                insert_price_information(price_info, idModelvariant,cursor,connection)

                # Scraping key specifications
                key_specification_info = scrap_key_specifications(ModelVarianturl,soup)
                insert_key_specifications(key_specification_info, idModelvariant,cursor,connection)

                # Scraping key features
                key_feature_info = scrap_key_features(ModelVarianturl,soup)
                insert_into_key_features(key_feature_info, idModelvariant,cursor,connection)
            
            except Exception as e:
                print(f"Error processing {Modelvariantname}: {str(e)}")
                continue

    print("[green]Scraping Variant Information Completed.")



if __name__ == "__main__":
    cursor,connection=get_datbase_connection()
    console = Console()
    # Check if the brand and model table exists
    with console.status("[bold green]Checking Brand & Model Table exist in the database") as status:
        spinner = SpinnerColumn()
        console.print(spinner, end="")
        varint_count = get_varinat_count()[0] # Replace this with the actual function call
        time.sleep(2)
        status.update("[bold green]Task complete!")
    
    if varint_count < 4530:
        print("Brand and Model Table does not exist.")
        create_brand_model_table()
        create_variant_table()
    else:
        print("[bold yellow]Brand and Model Table does exist.")
        time.sleep(5)
        print("[bold green]Creating Model Variant Table...")
        time.sleep(5)
        # pass
        scrape_and_create_variant_information_table()
        print("[bold green]All Tasks Completed")
