from bs4 import BeautifulSoup
with open('/media/double/DC5A48EB5A48C3CC/Projects/2/Project/Web_Scraper_G15/First.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())