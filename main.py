from configurations import *
from functions import get_models_and_urls,get_company_url

all_brands = ['maruti-suzuki-cars', 'Tata', 'Kia', 'Toyota', 'Hyundai', 'Mahindra', 'Honda', 'MG', 
              'Skoda', 'Jeep', 'Renault', 'Nissan', 'Volkswagen', 'Citroen', 'Aston Martin', 
              'Audi', 'Bajaj', 'Bentley', 'BMW', 'BYD', 'Ferrari', 'Force', 'Isuzu', 'Jaguar', 
              'Lamborghini', 'Land Rover', 'Lexus', 'Lotus', 'Maserati', 'Mclaren', 'Mercedes-Benz', 
              'Mini', 'PMV', 'Porsche', 'Pravaig', 'Rolls-Royce', 'Strom Motors', 'Volvo']

for brand in all_brands:
    companyurl = base_url + ("cars/" + brand if brand != "maruti-suzuki-cars" else brand)
    print(companyurl)
    try:
        response = requests.get(companyurl, headers=agent)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            urls_dict = get_models_and_urls(companyurl)
            brand_url = get_company_url(brand)
            try:
                urls_json = json.dumps(urls_dict)
                filename = os.path.join(base_path,'outputFiles\Linksofcompany',brand+'.txt')
                with open(filename,'w+') as f:
                    f.write(f"Brand URL: {brand_url}\n")
                    f.write(f"Models URLs:\n{urls_json}\n")
                    print("file Written sucesfully")
            except Exception as e:
                print("fileNotCreated",e)
        else:
            print(f"Request failed with status code {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        