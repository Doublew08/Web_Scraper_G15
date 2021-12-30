from bs4.element import Doctype
import requests
from bs4 import BeautifulSoup
#here put the list
response = requests.get("https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States")
soup = BeautifulSoup(response.text,'html.parser')
for div in soup.find_all('div' , class_='mw-category-group'):
 for ultag in div.find_all('ul'):
     for litag in ultag.find_all('li'):
         for atag in litag.find_all('a' , href = True):
             print(f'{atag.text} :https://en.wikipedia.org/'+atag['href'])
             responser = requests.get('https://en.wikipedia.org/'+atag['href'])
             document = BeautifulSoup(responser, 'html.parser')
             politician_card = document.find('table', class_='infobox vcard')
             politician_name = politician_card.find('div', class_='fn').text
             politician_dob = politician_card.find('span', class_='bday').text
             politician_bfullname = politician_card.find('div' , class_='nickname').text
             politician_pob = politician_card.findAll('td', class_='infobox-data')[3].a.text
             politician_party = politician_card.findAll('td', class_='infobox-data')[4].a.text
             print(f'politician name: {politician_name}')
             print(f'politician date of birth: {politician_dob}')
             print(f'politician birth fullname: {politician_bfullname}')
             print(f'politician place of birth: {politician_pob}')
             print(f'politician party: {politician_party}')





