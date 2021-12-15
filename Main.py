from bs4 import BeautifulSoup
with open('First.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h1')
    print(tags)
    