from configurations import *
from functions import *
import json

all_brands = ['maruti-suzuki-cars', 'Tata', 'Kia', 'Toyota', 'Hyundai', 'Mahindra', 'Honda', 'MG', 
              'Skoda', 'Jeep', 'Renault', 'Nissan', 'Volkswagen', 'Citroen', 'Aston Martin', 
              'Audi', 'Bajaj', 'Bentley', 'BMW', 'BYD', 'Ferrari', 'Force', 'Isuzu', 'Jaguar', 
              'Lamborghini', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mclaren', 'Mercedes-Benz', 
              'Mini', 'PMV', 'Porsche', 'Pravaig', 'Rolls-Royce', 'Strom Motors', 'Volvo']

for brand in all_brands:
    companyurl = base_url + ("cars/" + brand if brand != "maruti-suzuki-cars" else brand)
    # print(companyurl)
    try:
        all_details = {}
        response = requests.get(companyurl, headers=agent)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            urls_dict = get_models_url(companyurl)
            for model,model_url in urls_dict.items():
                model_info = get_modelvariant_link(model_url)
                all_details.update(model_info)
        else:
            print(f"Request failed with status code {response.status_code}")
        
        # Write dictionaries to JSON file
        try:
            with open('trashfile.txt', 'a') as file:
                json.dump(all_details, file, indent=4)

            print(f"Data written to {'trashfile.txt'}")
        except Exception as e:
            print(f"Error writing to {'trashfile.txt'}: {e}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")