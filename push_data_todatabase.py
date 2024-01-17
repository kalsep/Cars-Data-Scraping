
from functions import *
from database_conn import *
def push_brand_data():
    # Connect to MySQL
    try:
        connection,cursor = get_database_connection()
        brand_directory = get_company_url('https://www.cardekho.com/newcars')
        print(brand_directory)

        # Insert data into the 'brand_data' table
        insert_query = "INSERT INTO brand_names (brand_name, brand_url) VALUES (%s, %s)"
        for brand_name, brand_link in brand_directory.items():
            cursor.execute(insert_query, (brand_name, brand_link))
            print(f"inserted {brand_name,brand_link}")
        # Commit changes
        connection.commit()
        print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

def push_brand_models():
    try:
        connection, cursor = get_database_connection()

        # Fetch brand names and IDs from 'brand_names' table
        cursor.execute('SELECT brand_id, brand_name FROM brand_names')
        brand_id_mapping = {brand_name: brand_id for brand_id, brand_name in cursor.fetchall()}

        # Assuming 'get_company_url' returns a dictionary with brand names and URLs
        brand_directory = get_company_url('https://www.cardekho.com/newcars')

        for brand, brand_link in brand_directory.items():
            # Check if the brand is in the database
            if brand in brand_id_mapping:
                brand_id = brand_id_mapping[brand]

                # Assuming 'get_models_url' returns a dictionary with models and URLs
                model_data = get_models_url(brand_link)
                # print(model_data)

                # Insert model data into the 'model_data' table
                insert_model_query = "INSERT INTO brand_models (brand_model_name, brand_id) VALUES (%s, %s)"

                for model_name, model_link in model_data.items():
                    cursor.execute(insert_model_query, (model_name, brand_id))

        # Commit changes
        connection.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(e)

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")\
                          
def push_brand_variant():
    try:
        # push_brand_variant()
        all_data = get_trash(all_brands)
        connection, cursor = get_database_connection()
        cursor.execute('select brand_models_id,brand_model_name from brand_models;')
        model_list = cursor.fetchall()
        for model in model_list:
            print(model, end='\n')
            
            
        
        
    except Exception as e:
        print(e)
# push_brand_variant()
get_trash(all_brands)