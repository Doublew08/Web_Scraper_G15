from bs4 import BeautifulSoup
import requests
from requests.models import Response
html_response = requests.get('https://en.wikipedia.org/wiki/Donald_Trump')
html_text = requests.get('https://en.wikipedia.org/wiki/Donald_Trump').text
prettified_code = BeautifulSoup(html_text,'lxml')
#printing the full webpage 
#print(html_text)
#Printing the response code , Status code let us know if the request was success , failure or smth in between and a well functioning url will respond with 200 
#print(html_response)
# printing with prettify method to visualise code 
#print(prettified_code.prettify())


