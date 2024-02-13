from configurations import *

# Function to insert data into the Brand table
def insert_brand(brand_dict):
    try:
        cursor,connection=get_datbase_connection()
        for brand, url in brand_dict.items():
            query = "INSERT INTO Brand (Brandname, `Brand Url`) VALUES (%s, %s)"
            cursor.execute(query, (brand, url))
            connection.commit()
            # print(f"Data inserted successfully for brand: {brand}")
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
        brands_url = get_brand_url()
        brand_foreign_key = {key:value for value,key in brands_url }
        # print(brand_foreign_key)
        for model_name, model_url in brand_model_directory.items():
                Brand_idBrand = None
                for brand_name in brand_foreign_key.keys():
                    # Check if the brand name is a prefix of the model name
                    if model_name.lower().startswith(brand_name.lower()):
                        Brand_idBrand = brand_foreign_key[brand_name]
                        break
                # print(f"For {model_name}",Brand_idBrand)
                query = "INSERT INTO Models (`Model Name`, `Model Url`,`Brand_idBrand`) VALUES (%s, %s,%s)"
                # print(f"{model_name},{model_url},{Brand_idBrand}")
                cursor.execute(query, (model_name, model_url,Brand_idBrand))
                connection.commit() 
                # print(f"Data inserted successfully for brand: {model_name}")
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
        for each_varint in model_variant_list:
            for model_variant_name, model_variant_url in each_varint.items():
                    # print(f"For {model_name}",Brand_idBrand)
                    query = "INSERT INTO ModelVariant (`Modelvariantname`, `ModelVarianturl`,`Models_idModels`) VALUES (%s, %s,%s)"
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
def insert_price_information(price_info, modelvariant_id):
    try:
        cursor,connection=get_datbase_connection()
        query = "INSERT INTO PriceInformationDelhi(`Ex-showroom price`, RTO, Insurance,Others, Optional, `On-Road Price`, Modelvariant_idModelvariant) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (price_info['Ex-Showroom Price'],price_info['RTO'], price_info['Insurance'],price_info['Others'] ,price_info['Optional'], price_info['On-Road Price'], modelvariant_id))
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
def insert_key_specifications(key_specification_info,idModelvariant):
    try:
        cursor,connection=get_datbase_connection()
        table_name = 'Key Specifications'
        cursor.execute("SHOW COLUMNS FROM `" + table_name + "` WHERE Field != 'idFeatures'")
        # Fetch all column names
        columns = [column[0] for column in cursor.fetchall()]
        columns.remove('Modelvariant_idModelvariant')
        # print("Columns Names: \n",columns)

        # Filter feature_info dictionary to only include keys that are columns in the database
        filtered_feature_info = {key: value for key, value in key_specification_info.items() if key in columns}


        # Create a dictionary with null values for all columns
        data_to_insert = {column: None for column in columns}

        # Update data_to_insert with values from feature_info
        data_to_insert.update(filtered_feature_info)
        # print("Data To Insert:\n",data_to_insert)

        # Insert data into the database
        columns_str = ', '.join([f"`{col}`" for col in data_to_insert.keys()]) + ', ModelVariant_idModelvariant'
        values_str = ', '.join(['%s'] * (len(data_to_insert) + 1))  # +1 for ModelVariant_idModelvariant
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


def insert_into_key_features(key_feature_info, model_variant_id):
    try:
        cursor,connection=get_datbase_connection()
        table_name = 'Key Features'
        cursor.execute("SHOW COLUMNS FROM `" + table_name + "` WHERE Field != 'idFeatures'")
        # Fetch all column names
        columns = [column[0] for column in cursor.fetchall()]
        columns.remove('ModelVariant_idModelvariant')
        print("Columns Names: \n",columns)

        # Filter feature_info dictionary to only include keys that are columns in the database
        filtered_feature_info = {key: value for key, value in key_feature_info.items() if key in columns}


        # Create a dictionary with null values for all columns
        data_to_insert = {column: None for column in columns}

        # Update data_to_insert with values from feature_info
        data_to_insert.update(filtered_feature_info)
        print("Data To Insert:\n",data_to_insert)

        # Insert data into the database
        columns_str = ', '.join([f"`{col}`" for col in data_to_insert.keys()]) + ', ModelVariant_idModelvariant'
        values_str = ', '.join(['%s'] * (len(data_to_insert) + 1))  # +1 for ModelVariant_idModelvariant
        insert_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({values_str})"
        data_values = tuple(list(data_to_insert.values()) + [model_variant_id])  # Add model_variant_id to the tuple
        # print("Data Values:\n",data_values)
        cursor.execute(insert_query, data_values)
        connection.commit()
    except Exception as e:
            print(e)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def get_brand_url():
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

def get_brand_models_url():
    try:
        cursor,connection=get_datbase_connection()
            # Execute SELECT statement to fetch data from the Brand table
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
            
def get_model_variant_url():
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


def get_column_names(cursor, table_name):
    cursor,connection=get_datbase_connection()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    column_names = [column[0] for column in columns]
    return column_names