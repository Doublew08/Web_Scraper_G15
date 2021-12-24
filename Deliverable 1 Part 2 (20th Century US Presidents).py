from bs4 import BeautifulSoup
import requests
#George H. W. Bush
page = requests.get("https://en.wikipedia.org/wiki/George_H._W._Bush")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Jimmy Carter
page = requests.get("https://en.wikipedia.org/wiki/Jimmy_Carter")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Bill Clinton
page = requests.get("https://en.wikipedia.org/wiki/Bill_Clinton")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Calvin Coolidge
page = requests.get("https://en.wikipedia.org/wiki/Calvin_Coolidge")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Dwight D. Eisenhower
page = requests.get("https://en.wikipedia.org/wiki/Dwight_D._Eisenhower")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Gerald Ford
page = requests.get("https://en.wikipedia.org/wiki/Gerald_Ford")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Warren G. Harding
page = requests.get("https://en.wikipedia.org/wiki/Warren_G._Harding")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Herbert Hoover
page = requests.get("https://en.wikipedia.org/wiki/Herbert_Hoover")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Lyndon B. Johnson
page = requests.get("https://en.wikipedia.org/wiki/Lyndon_B._Johnson")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#John F. Kennedy
page = requests.get("https://en.wikipedia.org/wiki/John_F._Kennedy")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#William McKinley
page = requests.get("https://en.wikipedia.org/wiki/William_McKinley")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Richard Nixon
page = requests.get("https://en.wikipedia.org/wiki/Richard_Nixon")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Ronald Reagan
page = requests.get("https://en.wikipedia.org/wiki/Ronald_Reagan")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Franklin D. Roosevelt
page = requests.get("https://en.wikipedia.org/wiki/Franklin_D._Roosevelt")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Theodore Roosevelt
page = requests.get("https://en.wikipedia.org/wiki/Theodore_Roosevelt")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#William Howard Taft
page = requests.get("https://en.wikipedia.org/wiki/William_Howard_Taft")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Harry S. Truman
page = requests.get("https://en.wikipedia.org/wiki/Harry_S._Truman")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Woodrow Wilson
page = requests.get("https://en.wikipedia.org/wiki/Woodrow_Wilson")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#conversion to .csv
import pandas as pd
nme = ["George H. W. Bush", "Jimmy Carter", "Bill Clinton", "Calvin Coolidge","Dwight D. Eisenhower","Gerald Ford","Warren G. Harding","Herbert Hoover","Lyndon B. Johnson","John F. Kennedy","William McKinley","Richard Nixon","Ronald Reagan","Franklin D. Roosevelt","Theodore Roosevelt","William Howard Taft","Harry S. Truman","Woodrow Wilson"] 
prec = ["Bill Clinton", "George W. Bush", "Barack Obama", "Donald Trump"] 
succ = ["Barack Obama", "Donald Trump", "Joe Biden", "N.A"] 
prty=["Republican","Democrat","Republican","Democrat"]
dict = {'Name of President ': nme, 'Preceded By': prec, 'Succeeded By': succ, 'Political Party':prty}        
df = pd.DataFrame(dict) 
df.to_csv('21stCenturyUSPresidents.csv') 
