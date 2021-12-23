from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://wuzzuf.net/search/jobs/?a=navbl&filters%5Broles%5D%5B0%5D=IT%2FSoftware%20Development&q=Unity').text
print(html_text)