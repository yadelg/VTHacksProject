import requests
from bs4 import BeautifulSoup
import csv

# URLs for different cities
NewEngland = "https://data.bls.gov/timeseries/APU011072610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Boston = "https://data.bls.gov/timeseries/APUS11A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
NewYork = "https://data.bls.gov/timeseries/APUS12A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Philadelphia = "https://data.bls.gov/timeseries/APUS12B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Chicago  = "https://data.bls.gov/timeseries/APUS23A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Detroit = "https://data.bls.gov/timeseries/APUS23B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Minneapolis = "https://data.bls.gov/timeseries/APUS24A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
StLouis = "https://data.bls.gov/timeseries/APUS24B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Atlanta = "https://data.bls.gov/timeseries/APUS35C72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Baltimore = "https://data.bls.gov/timeseries/APUS35E72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Miami = "https://data.bls.gov/timeseries/APUS35B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Tampa = "https://data.bls.gov/timeseries/APUS35D72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
WashingtonDC = "https://data.bls.gov/timeseries/APUS35A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Dallas = "https://data.bls.gov/timeseries/APUS37A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Houston = "https://data.bls.gov/timeseries/APUS37B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Denver = "https://data.bls.gov/timeseries/APUS48B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Phoenix = "https://data.bls.gov/timeseries/APUS48A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
LosAngeles = "https://data.bls.gov/timeseries/APUS49A72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Riverside = "https://data.bls.gov/timeseries/APUS49C72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
SanDiego = "https://data.bls.gov/timeseries/APUS49E72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
SanFrancisco = "https://data.bls.gov/timeseries/APUS49B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
Seattle = "https://data.bls.gov/timeseries/APUS49D72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
UrbanAlaska = "https://data.bls.gov/timeseries/APUS49G72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
UrbanHawaii = "https://data.bls.gov/timeseries/APUS49F72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"

cities = [
    NewEngland,
    Boston,
    NewYork,
    Philadelphia,
    Chicago,
    Detroit,
    Minneapolis,
    StLouis,
    Atlanta,
    Baltimore,
    Miami,
    Tampa,
    WashingtonDC,
    Dallas,
    Houston,
    Denver,
    Phoenix,
    LosAngeles,
    Riverside,
    SanDiego,
    SanFrancisco,
    Seattle,
    UrbanAlaska,
    UrbanHawaii
]

city_urls = {
    "New England": NewEngland,
    "Boston": Boston,
    "New York": NewYork,
    "Philadelphia": Philadelphia,
    "Chicago": Chicago,
    "Detroit": Detroit,
    "Minneapolis": Minneapolis,
    "St. Louis": StLouis,
    "Atlanta": Atlanta,
    "Baltimore": Baltimore,
    "Miami": Miami,
    "Tampa": Tampa,
    "Washington D.C.": WashingtonDC,
    "Dallas": Dallas,
    "Houston": Houston,
    "Denver": Denver,
    "Phoenix": Phoenix,
    "Los Angeles": LosAngeles,
    "Riverside": Riverside,
    "San Diego": SanDiego,
    "San Francisco": SanFrancisco,
    "Seattle": Seattle,
    "Urban Alaska": UrbanAlaska,
    "Urban Hawaii": UrbanHawaii
}

def process_rows(rows):
    processed_data = []
    last_known_value = None

    for row in rows:
        cells = row.find_all('td')
        row_data = []

        for cell in cells:
            cell_text = cell.text.strip()

            if cell_text in ['\xa0', '']:  
                row_data.append(last_known_value)
            else:
                last_known_value = cell_text
                row_data.append(last_known_value)

        processed_data.append(row_data)

    return processed_data

def fetchInSite(url, city_name, num_rows=6):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    odd_rows = soup.find_all('tr', class_='odd')
    even_rows = soup.find_all('tr', class_='even')  

    odd_data = process_rows(odd_rows)
    even_data = process_rows(even_rows)

    combined_data = []
    for odd, even in zip(odd_data, even_data):
        combined_data.append(odd)
        combined_data.append(even)

    if len(odd_data) > len(even_data):
        combined_data.extend(odd_data[len(even_data):])

    elif len(even_data) > len(odd_data):
        combined_data.extend(even_data[len(odd_data):])

    #limit to the last `num_rows` rows (really just the last 6)
    limited_data = combined_data[-num_rows:]

    #make the list of lists into a single list and prepend city name
    singleList = [city_name] + [item for sublist in limited_data for item in sublist]

    return singleList

#collect data for all cities
all_city_data = {}

for city_name, url in city_urls.items():
    print(f"Processing data for: {city_name}")
    city_data = fetchInSite(url, city_name)
    all_city_data[city_name] = city_data

num_rows = 73
counter = ['count'] + list(range(1, num_rows + 1))

#writing all data to a single CSV file
with open('all_cities_data_count_price.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #create the header row with "Count" and city names as headers for their price columns

    writer = csv.writer(csvfile)

    #create the row of counting numbers 1-73
    for row_idx in range(num_rows):
        row = [counter[row_idx]]  

    
        for city_name in city_urls.keys():
            city_data = all_city_data[city_name]
            #add the city's price for the current row index (or empty if not enough data)
            price = city_data[row_idx] 
            row.append(price)

        writer.writerow(row)

print("Data saved to all_cities_data_count_price.csv")