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
                print(f"Data inserted successfully for brand: {model_name}")
    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Function to insert data into the ModelVariant table
def insert_model_variant(moddel_varaint_directory):
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
                print(f"Data inserted successfully for brand: {model_name}")
    except mysql.connector.Error as error:
        print("Error inserting data into Brand table:", error)
    finally:
        # Closing cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    query = "INSERT INTO ModelVariant (Modelvariantname, Models_idModels) VALUES (%s, %s)"
    cursor.execute(query, (modelvariantname, model_id))
    connection.commit()

# # Function to insert data into the PriceInformationDelhi table
# def insert_price_information(type_of_model, ex_showroom_price, insurance, rto, optional, on_road_price, modelvariant_id,cursor=connection.cursor()):
#     query = "INSERT INTO PriceInformationDelhi (Type_of_model, `Ex-showroom price`, Insurance, RTO, Optional, `On-Road Price`, Modelvariant_idModelvariant) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(query, (type_of_model, ex_showroom_price, insurance, rto, optional, on_road_price, modelvariant_id))
#     connection.commit()

# # Function to insert data into the Key Specifications table
# def insert_key_specifications(fuel_type, transmission_type, city_mileage, engine_displacement, max_power, seating_capacity, boot_space, body_type, fuel_tank_capacity, no_of_cylinders, arai_mileage, modelvariant_id,cursor=connection.cursor()):
#     query = "INSERT INTO `Key Specifications` (`Fuel Type`, `Transmission Type`, `City Mileage`, `Engine Displacement (cc)`, `Max Power (bhp@rpm)`, `Seating Capacity`, `Boot Space (Litres)`, `Body Type`, `Fuel Tank Capacity (Litres)`, `No. of Cylinders`, `ARAI Mileage`, Modelvariant_idModelvariant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(query, (fuel_type, transmission_type, city_mileage, engine_displacement, max_power, seating_capacity, boot_space, body_type, fuel_tank_capacity, no_of_cylinders, arai_mileage, modelvariant_id))
#     connection.commit()

# # Function to insert data into the key Features table
# def insert_key_features(multi_function_steering_wheel, power_adjustable_exterior_rear_view_mirror, touch_screen, automatic_climate_control, engine_start_stop_button, anti_lock_braking_system, alloy_wheels, power_windows_rear, power_windows_front, wheel_covers, passenger_airbag, power_steering, air_conditioner, modelvariant_id,cursor=connection.cursor()):
#     query = "INSERT INTO `key Features` (`Multi-function Steering Wheel`, `Power Adjustable Exterior Rear View Mirror`, `Touch Screen`, `Automatic Climate Control`, `Engine Start Stop Button`, `Anti Lock Braking System`, `Alloy Wheels`, `Power Windows Rear`, `Power Windows Front`, `Wheel Covers`, `Passenger Airbag`, `Power Steering`, `Air Conditioner`, ModelVariant_idModelvariant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(query, (multi_function_steering_wheel, power_adjustable_exterior_rear_view_mirror, touch_screen, automatic_climate_control, engine_start_stop_button, anti_lock_braking_system, alloy_wheels, power_windows_rear, power_windows_front, wheel_covers, passenger_airbag, power_steering, air_conditioner, modelvariant_id))
#     connection.commit()

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

