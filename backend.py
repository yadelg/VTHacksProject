import requests
from bs4 import BeautifulSoup

url = "https://data.bls.gov/timeseries/APUS23B72610?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"


def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    odd_rows = soup.find_all('tr', class_="odd")
    even_rows = soup.find_all('tr', class_="even")  

    odd_data = [[td.text for td in row.find_all('td')] for row in odd_rows]
    even_data = [[td.text for td in row.find_all('td')] for row in even_rows]

    combined_data = []

    for odd, even in zip(odd_data, even_data):
        combined_data.append(odd)
        combined_data.append(even)

    if len(odd_data) > len(even_data): 
        combined_data.extend(odd_data[len(even_data):])

    elif len(even_data) > len(odd_data):
        combined_data.extend(even_data[len(odd_data):])

    for row in combined_data:
        print(row)

fetch(url)
