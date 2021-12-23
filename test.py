import requests
from bs4 import BeautifulSoup
import pandas as pd

Categories = []
Data = []
response = requests.get("https://en.wikipedia.org/wiki/Donald_Trump")
#print(f'Response status: {response.status_code}')
#print(f'HTML page: {response.text}')
document = BeautifulSoup(response.text, 'html.parser')
#print(f'title: {document.title.text}')
#print(f'pretty html: {document.prettify()}')
politician_card = document.find('table', class_='infobox vcard')
politician_name = politician_card.find('div', class_='fn').text
#print(f'politician name: {politician_name}')
politician_dob = politician_card.find('span', class_='bday').text
#print(f'politician date of birth: {politician_dob}')

Headers = ['politician name','politician date of birth']

Categories.extend([politician_name, politician_dob ])

Data.append(Categories)
df =pd.DataFrame(Data, columns = Headers)
df.to_csv('output.csv')