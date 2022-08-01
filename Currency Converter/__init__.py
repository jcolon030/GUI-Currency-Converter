from bs4 import BeautifulSoup
import requests
import json

# Use to get real time currency conversion data -----------
def refresh_data():
    html_link = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")

    soup = BeautifulSoup(html_link.content, 'html.parser')

    return soup

#-----------------------------------------------------------

# Processing data to put in JSON format --------------------

def recheck_prices(soup):

    data_processing = []

    for i in (soup.find_all("td")):
        data_processing.append(i.get_text())

    data_processing = [data_processing[x:x+3] for x in range(0, len(data_processing), 3)]

    processed_data = {}

    for i in data_processing:
        processed_data[i[0]] = [i[1], i[2]]

    json_object = json.dumps(processed_data, indent=2)

    with open("conversions.json", "w+") as output:
        output.write(json_object)

# ----------------------------------------------------------

html_link = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")

soup = BeautifulSoup(html_link.content, 'html.parser')

data_processing = []

for i in (soup.find_all("td")):
    data_processing.append(i.get_text())

data_processing = [data_processing[x:x+3] for x in range(0, len(data_processing), 3)]

processed_data = {}

for i in data_processing:
    processed_data[i[0]] = [i[1], i[2]]

json_object = json.dumps(processed_data, indent=2)

with open("conversions.json", "w+") as output:
    output.write(json_object)
