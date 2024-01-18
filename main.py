from configurations import *
from functions import *
# Creating an empty DataFrame
final_data = pd.DataFrame(columns=['brand', 'model', 'variant','variant_link'])

for index,brand in enumerate(all_brands):
    data = pd.DataFrame(columns=['brand','model','variant'])
    brand_url = get_company_model_url(brand)
    all_models = get_models_url(brand_url)
    if all_models!= None:
        for model, model_link in all_models.items():
            all_variants = get_modelvariant_link(model_link)
            for varinat in all_variants:
                for variant_name, variant_link in varinat.items():
                    data = data._append({'brand': brand, 'model': model, 'variant': variant_name,'variant_link':variant_link}, ignore_index=True)
    final_data = pd.concat([final_data, data], ignore_index=True)
final_data.to_csv('all_models_data.csv')