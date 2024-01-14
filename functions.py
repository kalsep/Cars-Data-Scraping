from configurations import *

#get the soup data
def get_soup(url='https://www.cardekho.com/cars/Tata'):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup

#get All Models list forom page of company
def get_company_url(title):
    # Extracting company name and models
    each_model = title.split(" ")
    company_name = each_model[0]
    models = each_model[1:]
    path = f"{company_name}/{'-'.join(models)}"
    return urljoin(base_url, path)

def get_models_and_urls(url):
    soup = get_soup(url)
    pre_model = soup.find('div', class_="gsc_col-md-8 gsc_col-lg-9 gsc_col-sm-12 gsc_col-xs-12 BrandDesc")
    model_list = pre_model.find('ul', class_="modelList")
    all_models = model_list.find_all('li')
    
    result_dict = {}
    
    for i in all_models:
        try:
            target_tag  = i.find('div', class_='gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS')
            # print(list1)
            title = target_tag.find('h3').find('a').text
            
            link_href = target_tag.find('h3').find('a')['href']
            full_url = urljoin(base_url, link_href)
            #Storing in the result dictionary
            result_dict[title] = {'full_url': full_url}
            
        except Exception as e:
            print(e)
    
    return result_dict
