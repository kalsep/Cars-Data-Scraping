from configurations import *
from functions import *



for brand in all_brands:
    companyurl = base_url + ("/cars/" + brand if brand != "maruti-suzuki-cars" else brand)
    # print(companyurl)
    try:
        response = requests.get(companyurl, headers=agent)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful!")
            urls_dict = get_models_url(companyurl)
            for model,model_url in urls_dict.items():
                model_info = get_modelvariant_link(model_url)
                # onroad_price_info = get_on_road_price_delhi(model_info[0]['link'])
                print(get_each_car_info(model_info[0]['link']))
                print("Model Varaint Links\n",model_info)
                # print("Onroad_price_info\n",onroad_price_info)
        else:
            print(f"Request failed with status code {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        