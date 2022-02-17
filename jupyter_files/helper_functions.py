# We'll create a fucntion to webscrape all the unique zipcode values
def scrape_data(zipcode):

    import pandas as pd
    import json
    import requests
    from bs4 import BeautifulSoup
    import time
    import re
    import time
    import numpy as np

    time.sleep(2)

    # Setting up the web scraper
    headers = requests.utils.default_headers()
    headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    url = f'https://www.unitedstateszipcodes.org/{zipcode}/'

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    if len(soup.find_all('script')) != 46:
        blank_dict = {'time': np.nan, 'RegionName': zipcode, 
                      'population': np.nan, 'household_income': np.nan, 
                      'population_density': np.nan}
        return blank_dict
    else:
        # We'll firstly retrieve the populations
        pop_text = soup.find_all('script')[11].string.strip().replace('\t', '').replace('\n', '')
        pattern = '(?:\[)(.*)(?=];var.c)'
        population_group = json.loads(re.findall(pattern, pop_text)[0])
        population = population_group['values']
        pop_list = [i['y'] for i in population]
        time = [i['x'] for i in population]

        # We'll then retrieve the area of the zipcode in square miles
        land_area = float(soup.find_all('td', class_='text-right')[4].get_text().replace(',', ''))
        
        # Average income per zipcode
        income_text = soup.find_all('script')[-16].string.strip().replace('\t', '').replace('\n', '')
        income_group = json.loads(re.findall(pattern, income_text)[0])
        income = income_group['values']
        income_list = [round(i['y'], 2) for i in income]
        
        # Then we form a dictionary from the scraped data
        zipcode_dictionary = {'RegionName': zipcode, 'time': time, 
                            'population': pop_list, 'land_area': land_area, 
                            'household_income': income_list}

        # We'll now convert the 
        df = pd.DataFrame(zipcode_dictionary)
        
        # Set the time column to datetime and set it as an index
        df['time'] = pd.to_datetime(df['time'], format='%Y')
        df.set_index('time', inplace = True)

        # The scraped data is yearly so we'll need to resample it to make it monthly
        df = df.resample('M').mean()

        # Fill the na values with interpolation
        df = df.interpolate(method = 'polynomial', order = 2)

        # Feature engineer a population density column
        df['population_density'] = df['population'] / df['land_area']
        df.drop('land_area', axis = 1, inplace = True)

        # Turn our values into integers
        df['population'] = df['population'].apply(lambda x: int(x))
        df['RegionName'] = df['RegionName'].apply(lambda x: int(x))
        df['household_income'] = df['household_income'].apply(lambda x: int(x))

        # Finally turn the dataframe into a dictionary
        df = df.reset_index()
        completed_dict = df.to_dict()

        return completed_dict