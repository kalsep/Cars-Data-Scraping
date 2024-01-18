from configurations import *

#get the soup data
def get_soup(url='https://www.cardekho.com'):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup

def get_company_url(url):
    soup = get_soup(url)
    main_section = soup.find('main', class_='gsc_container newcarsLanding')
    brand_section = main_section.find_all('div', class_='contentHold gsc_row')
    sec = brand_section[0].find('ul', class_='listing gsc_row clearfix')

    # Find all list items within the 'ul' tag
    list_items = sec.find_all('li')
    brand_directctory = {}
    # Extract information from each list item
    for item in list_items:
        # Extract the brand name
        brand_name = item.find('span').text

        # Extract the image source URL
        href = item.find('a')['href']
        brand_directctory[brand_name] = base_url+href
        
    return brand_directctory

#get All Models list from page of company
def get_company_model_url(title):
    # Extracting company name and models
    each_model = title.split(" ")
    company_name = each_model[0]
    models = each_model[1:]
    path = f"{company_name}/{'-'.join(models)}"
    return urljoin(base_url, path)
 
def get_models_url(url): #https://www.cardekho.com/maruti-suzuki-cars
    try:
        soup = get_soup(url)
        pre_model = soup.find('div', class_="gsc_col-md-8 gsc_col-lg-9 gsc_col-sm-12 gsc_col-xs-12 BrandDesc")
        model_list = pre_model.find('ul', class_="modelList")
        all_models = model_list.find_all('li')
        
        
        result_dict = {}
        for i in all_models:
            target_tag  = i.find('div', class_='gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder posS')
            # print(list1)
            title = target_tag.find('h3').find('a').text
            
            link_href = target_tag.find('h3').find('a')['href']
            full_url = urljoin(base_url, link_href)
            
            #Storing in the result dictionary
            result_dict[title] = full_url
        # print("CHecking Results: ",result_dict)
        return result_dict
    except Exception as e:
        return None


def get_modelvariant_link(model_page_url):
    soup = get_soup(model_page_url)
    pre_model = soup.find('main', class_="gsc_container")
    table = pre_model.find('table',class_='allvariant contentHold')
    # Extract information from the table
    try:
        # Initialize a list to store extracted data
        extracted_data = []

        # Extract information from the table
        if table:
            # Extract data from each row
            for row in table.find_all('tr')[1:]:  # Skip the first row (headers)
                # Extracting specific information from each row
                columns = row.find_all(['td', 'th'])
                title = columns[0].find('a', {'class': 'pricecolor'}).text.strip()

                # Extracting href
                href = columns[0].find('a', {'class': 'pricecolor'})['href']
                link = urljoin(base_url,href)

                # Creating a dictionary for each row
                row_data = {title:link}
                extracted_data.append(row_data)
        else:
            raise ValueError("Table not found.")

        # Return the extracted data
        return extracted_data

    except Exception as e:
        # print(f"Error: {e}")
        return None

#this function return price breakup for delhi city by default
def get_on_road_price_delhi(variant_page_url):
    try:
        # Parse the HTML content using BeautifulSoup
        soup = get_soup(variant_page_url)

        # Find the section with on-road price details
        on_road_price_section = soup.find('section', {'id': 'OnRoadPrice'})

        # Initialize a dictionary to store extracted information
        on_road_price_info = {}

        # Extract the price details if the section is found
        if on_road_price_section:
            # Extract the price heading
            price_heading = on_road_price_section.find('h2').text.strip()
            on_road_price_info['Model'] = price_heading.replace("Price",'').replace('price','').strip()

            # Extract details from the table
            table = on_road_price_section.find('table')
            if table:
                for row in table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()

                        # Ignore the specified span element for 'Insurance'
                        if key.split(" ")[0] == 'Insurance':
                            span = columns[0].find('span', class_='infodetail')
                            if span:
                                key = key.replace(span.text.strip(), '').strip()
                        elif key.split(" ")[0] == 'On-Road':
                            key = key.replace(key, " ".join(key.split(' ')[0:2])).strip()
                        value = columns[1].text.strip()
                        on_road_price_info[key] = value

            return (on_road_price_info)

    except Exception as e:
        # print(f"Error: {e}")
        return None

#Get each variant info
def get_each_car_info(variant_url):
    soup = get_soup(variant_url)
    pre_model = soup.find('main', class_="gsc_container")
    content = pre_model.find('section',class_='specsAllLists')
    try:
        # Find the sections with key specifications and key features
        specs_section = content.find('div', class_='featuresIocnsSec gsco_content first')
        features_section = content.find('div',class_="toggleAccordion specsFeaturesBlock")

        # Extract key specifications
        specs = {}
        if specs_section:
            spec_table = specs_section.find('table', {'class': 'keyfeature'})
            if spec_table:
                for row in spec_table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()
                        value = columns[1].text.strip()
                        specs[key] = value

        # Extract key features
        features = {}
        if features_section:
            feature_table = features_section.find('table', {'class': 'keyfeature'})
            if feature_table:
                for row in feature_table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()
                        value = True if 'icon-check' in columns[1].prettify() else False
                        features[key] = value

        return {'Key Specifications': specs, 'Key Features': features}

    except Exception as e:
        # print(f"Error: {e}")
        return None