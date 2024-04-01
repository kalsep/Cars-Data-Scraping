from configurations import *

#get the soup data
def get_soup(url='https://www.cardekho.com'):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    page = requests.get(url, headers=agent)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


#This function scrapes brand directory
def scrap_brand_directory(url):
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


 #Scrapes models name and url
def scrap_model_urls(url): #https://www.cardekho.com/maruti-suzuki-cars
    try:
        # print(f"inside get models for {url}")
        brand_model_directory = {}
        soup = get_soup(url)
        main = soup.find('div',id='main')
        gsc_container = main.find('main',class_='gsc_container Brandpage')
        model_list = gsc_container.find('ul',class_='modelList')
        ul_list = model_list.findAll("li")
        # print(len(ul_list))
        for index, eachmodel in enumerate(ul_list):
            # Extract name and URL
            try:
                model_name = eachmodel.find('h3').find('a').text.strip()
                model_url = eachmodel.find('h3').find('a')['href']
                brand_model_directory[model_name] = urljoin(base_url,model_url)
            except Exception as e:
                print(e)
        return brand_model_directory
    except Exception as e:
        return None


def scrap_model_variant_url(model_page_url):
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
def scrap_on_road_price_delhi(variant_page_url, soup)-> dict:
    try:
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
                        elif key.startswith("Others"):
                            key="Others"
                        elif key.startswith('Optional'):
                            key='Optional'
                        
                        value = columns[1].text.strip()

                        # Replace 'Rs.', ',', and '#' with an empty string
                        value = value.replace('Rs.', '').replace(',', '').replace('#', '')
                        if value.isnumeric():
                            value = int(value)
                        on_road_price_info[key] = value
        return on_road_price_info
    except Exception as e:
        # print(f"Error: {e}")
        return None


def process_on_road_price(price_info):
    processed_price_info = {}
    for key,value in price_info.items():
        # print(key,":",value,end="\n")

        if key.startswith("Others"):
            input_string = str(key)
            # Define regular expression pattern to extract keys and corresponding charges
            charge_pattern_other = r'([a-zA-Z\s]+):Rs\.(\d+(?:,\d{3})*)(?=\D|$)'
            charge_items = re.findall(charge_pattern_other, input_string)

            # Create a dictionary from the matches
            charge_dict_ot = {charge[0].strip(): int(charge[1].replace(',', '')) for charge in charge_items}

            # print(f"For Others:",charge_dict)
            processed_price_info.update(charge_dict_ot)
       
        elif key.startswith('Optional'):
            input_string = str(key)
            # Define regular expression pattern to extract keys and corresponding charges
            charge_pattern_optional = r'(\w+\s*\w*)\s*:\s*Rs\.(\d{1,3},?\d{3})'
            charge_items = re.findall(charge_pattern_optional, input_string)

            # Create the first dictionary
            # op_charge_dict = {key: value for key, value in charge_items}

            # Create a dictionary from the matches
            charge_dict_op = {charge[0].strip(): int(charge[1].replace(',', '')) for charge in charge_items}

            processed_price_info.update(charge_dict_op)

        else:
            # print(f"For NOT:",key)
            processed_price_info[key]=value
    print("processed_price_info:",processed_price_info)
    return processed_price_info

def scrap_key_specifications(url, soup)->dict:
    pre_model = soup.find('main', class_="gsc_container")
    content = pre_model.find('section',class_='specsAllLists')
    try:
        # Find the sections with key specifications and key features
        specs_section = content.find('div', class_='featuresIocnsSec gsco_content first')
        features_section = content.find('div',class_="toggleAccordion specsFeaturesBlock")

        # Extract key specifications
        variant_key_specifications = {}
        if specs_section:
            spec_table = specs_section.find('table', {'class': 'keyfeature'})
            if spec_table:
                for row in spec_table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()
                        value = columns[1].text.strip()
                        variant_key_specifications[key] = value
        return variant_key_specifications
    except Exception as e:
        print(e)

    

#Get each variant info
def scrap_key_features(variant_url, soup)->dict:
    
    #Extract Content
    pre_model = soup.find('main', class_="gsc_container")
    content = pre_model.find('section',class_='specsAllLists')
    try:
        # Find the sections with key specifications and key features
        features_section = content.find_all('div',class_="toggleAccordion specsFeaturesBlock")

        # Extract key features
        varint_key_features = {}
        if features_section[1]:
            feature_table = features_section[1].find('table', {'class': 'keyfeature'})
            if feature_table:
                for row in feature_table.find_all('tr'):
                    columns = row.find_all('td')
                    if len(columns) == 2:
                        key = columns[0].text.strip()
                        value = True if 'icon-check' in columns[1].prettify() else False
                        varint_key_features[key] = value
        return varint_key_features

    except Exception as e:
        # print(f"Error: {e}")
        return None