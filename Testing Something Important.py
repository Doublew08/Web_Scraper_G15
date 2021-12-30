import requests
from bs4 import BeautifulSoup
Links = []
response = requests.get("https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States")
soup = BeautifulSoup(response.text,'html.parser')
for div in soup.find_all('div' , class_='mw-category-group'):
 for ultag in div.find_all('ul'):
     for litag in ultag.find_all('li'):
         for atag in litag.find_all('a' , href = True):
             print(f'{atag.text} :https://en.wikipedia.org/'+atag['href'])