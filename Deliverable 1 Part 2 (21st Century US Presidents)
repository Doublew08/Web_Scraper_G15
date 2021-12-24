from bs4 import BeautifulSoup
import requests
#Joe Biden
page = requests.get("https://en.wikipedia.org/wiki/Joe_Biden")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#GW Bush 
page = requests.get("https://en.wikipedia.org/wiki/George_W._Bush")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Barack Obama
page = requests.get("https://en.wikipedia.org/wiki/Barack_Obama")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Donald Trump 
page = requests.get("https://en.wikipedia.org/wiki/Donald_Trump")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
  
#conversion to .csv
import pandas as pd
nme = ["George W. Bush", "Barack Obama", "Donald Trump", "Joe Biden"] 
prec = ["Bill Clinton", "George W. Bush", "Barack Obama", "Donald Trump"] 
succ = ["Barack Obama", "Donald Trump", "Joe Biden", "N.A"] 
prty=["Republican","Democrat","Republican","Democrat"]
dict = {'Name of President ': nme, 'Preceded By': prec, 'Succeeded By': succ, 'Political Party':prty}        
df = pd.DataFrame(dict) 
df.to_csv('21stCenturyUSPresidents.csv') 
