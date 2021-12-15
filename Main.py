from bs4 import BeautifulSoup
with open('First.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    labels_tags = soup.find_all('label')
    for label in labels_tags:
        print(label.text)
    