import requests
from bs4 import BeautifulSoup , SoupStrainer
import pandas as pd
import httplib2


Categories = []
Data = []
listsopresidents = []
response = requests.get(listopresidents)
document = BeautifulSoup(response.text, 'html.parser')
for soup in soup.find_all("li" , a = "href")
for list in listsopresidents:
     
"""  
def get_page (link):
    response = requests.get(link)
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
    politician_bfullname = politician_card.find('div' , class_='nickname').text
    #print(f'politician birth fullname: {politician_bfullname}')
    politician_pob = politician_card.findAll('td', class_='infobox-data')[3].a.text
    #print(f'politician place of birth: {politician_pob}')
    politician_party = politician_card.findAll('td', class_='infobox-data')[4].a.text
    #print(f'politician party: {politician_party}')
Headers = ['politician name','politician date of birth','politician birth fullname','politician place of birth','politician party']
"""
Categories.extend([politician_name, politician_dob, politician_bfullname,politician_pob,politician_party])

Data.append(Categories)
df =pd.DataFrame(Data, columns = Headers)
df.to_csv('output.csv')