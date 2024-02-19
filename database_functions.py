from configurations import *



# Function to insert data into the Brand table
def insert_brand(brand_dict):
    try:
        cursor,connection=get_datbase_connection()
        for brand, url in brand_dict.items():
            query = "INSERT INTO Brand (Brandname, `Brand Url`) VALUES (%s, %s)"
            cursor.execute(query, (brand, url))
            connection.commit()
    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


# Function to insert data into the Models table
def insert_brand_model(brand_model_directory):
    try:
        cursor,connection=get_datbase_connection()
        brands_url = get_brand_url_from_database()
        brand_foreign_key = {key:value for value,key in brands_url }
        for model_name, model_url in brand_model_directory.items():
                idBrand = None
                for brand_name in brand_foreign_key.keys():
                    # Check if the brand name is a prefix of the model name
                    if model_name.lower().startswith(brand_name.lower()):
                        idBrand = brand_foreign_key[brand_name]
                        break
                query = "INSERT INTO Models (`Model Name`, `Model Url`,`idBrand`) VALUES (%s, %s,%s)"
                cursor.execute(query, (model_name, model_url,idBrand))
                connection.commit() 
                
    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Function to insert data into the ModelVariant table
def insert_model_variant(id_model,model_variant_list):
    try:
        cursor,connection=get_datbase_connection()
        for each_variant in model_variant_list:
            for model_variant_name, model_variant_url in each_variant.items():
                    # print(f"For {model_name}",Brand_idBrand)
                    query = "INSERT INTO ModelVariant (`Modelvariantname`, `ModelVarianturl`,`idModels`) VALUES (%s, %s,%s)"
                    # print(f"{model_variant_name},{model_variant_url},{id_model}")
                    cursor.execute(query, (model_variant_name, model_variant_url,id_model))
                    connection.commit() 
                    # print(f"Data inserted successfully for brand: {model_variant_name}")
    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Function to insert data into the PriceInformationDelhi table
def insert_price_information(price_info, idModelvariant,cursor,connection):
    try:
        
        query = "INSERT INTO PriceInformationDelhi(`Ex-showroom price`, RTO, Insurance,Others, Optional, `On-Road Price`,idModelvariant) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (price_info['Ex-Showroom Price'],price_info['RTO'], price_info['Insurance'],price_info['Others'] ,price_info['Optional'], price_info['On-Road Price'], idModelvariant))
        connection.commit()
        print(f"Inserted Data For {price_info['Model']}")
    except Exception as e:
            print(e)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Function to insert data into the Key Specifications table
def insert_key_specifications(key_specification_info,idModelvariant,cursor,connection):
    try:
        table_name = 'Key Specifications'
        cursor.execute("SHOW COLUMNS FROM `" + table_name + "` WHERE Field != 'idFeatures'")
        # Fetch all column names
        columns = [column[0] for column in cursor.fetchall()]
        columns.remove('idModelvariant')

        # Filter feature_info dictionary to only include keys that are columns in the database
        filtered_feature_info = {key: value for key, value in key_specification_info.items() if key in columns}


        # Create a dictionary with null values for all columns
        data_to_insert = {column: None for column in columns}

        # Update data_to_insert with values from feature_info
        data_to_insert.update(filtered_feature_info)

        # Insert data into the database
        columns_str = ', '.join([f"`{col}`" for col in data_to_insert.keys()]) + ', idModelvariant'
        values_str = ', '.join(['%s'] * (len(data_to_insert) + 1))  # +1 for idModelvariant
        insert_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({values_str})"
        data_values = tuple(list(data_to_insert.values()) + [idModelvariant])  # Add model_variant_id to the tuple
        # print("Data Values:\n",data_values)
        cursor.execute(insert_query, data_values)
        connection.commit()
        print(f"Data Inserted for {idModelvariant}")
    except Exception as e:
            print(e)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def insert_into_key_features(key_feature_info, idModelvariant, cursor,connection):
    try:
        cursor,connection=get_datbase_connection()
        table_name = 'Key Features'
        cursor.execute("SHOW COLUMNS FROM `" + table_name + "` WHERE Field != 'idFeatures'")
        # Fetch all column names
        columns = [column[0] for column in cursor.fetchall()]
        columns.remove('idModelvariant')

        # Filter feature_info dictionary to only include keys that are columns in the database
        filtered_feature_info = {key: value for key, value in key_feature_info.items() if key in columns}


        # Create a dictionary with null values for all columns
        data_to_insert = {column: None for column in columns}

        # Update data_to_insert with values from feature_info
        data_to_insert.update(filtered_feature_info)
        
        # Insert data into the database
        columns_str = ', '.join([f"`{col}`" for col in data_to_insert.keys()]) + ', idModelvariant'
        values_str = ', '.join(['%s'] * (len(data_to_insert) + 1))  # +1 for idModelvariant
        insert_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({values_str})"
        data_values = tuple(list(data_to_insert.values()) + [idModelvariant])  # Add model_variant_id to the tuple
        cursor.execute(insert_query, data_values)
        connection.commit()
        print(f"Data inserted {idModelvariant}")
        
    except Exception as e:
            print(e)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def get_brand_url_from_database():
        try:
            cursor,connection=get_datbase_connection()
            # Execute SELECT statement to fetch data from the Brand table
            cursor.execute("SELECT idBrand, Brandname FROM Brand")
            # Fetch all rows from the result set
            brands_url = cursor.fetchall()
            return brands_url
        except Exception as e:
            print(e)
        finally:
            # Closing cursor and connection
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

def get_brand_models_from_database():
    try:
        cursor,connection=get_datbase_connection()
        cursor.execute("SELECT idModels,`Model Name`,`Model Url` FROM models")
        all_brand_models = cursor.fetchall()
        return all_brand_models

    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    
    except Exception as e:
        print(e)
        
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            
def get_model_variant_url_from_database():
    try:
        cursor,connection=get_datbase_connection()
            # Execute SELECT statement to fetch data from the Brand table
        cursor.execute("SELECT idModelvariant,`Modelvariantname`,`ModelVarianturl` FROM modelvariant")
        all_model_varinats = cursor.fetchall()
        # print(all_model_varinats)
        return all_model_varinats

    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    
    except Exception as e:
        print(e)
        
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def get_column_names_from_database(cursor, table_name):
    cursor,connection=get_datbase_connection()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    column_names = [column[0] for column in columns]
    return column_names

def get_varinat_count():
    curor,connection = get_datbase_connection()
    curor.execute("select count(*) from modelvariant;")
    count = curor.fetchone()
    return count