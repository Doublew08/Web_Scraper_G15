import requests
from bs4 import BeautifulSoup
#bbc
url='https://www.bbc.com/news/world-us-canada-59703761'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h1')
for x in headlines:
    print(x.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
descs = soup.find('body').find_all('p')
for y in descs:
    print(y.text.strip())
print("============NEXT ARTICLE=========")
  
#Daily Mail
url1='https://www.dailymail.co.uk/news/article-10340497/Trump-asks-Supreme-Court-block-release-White-House-records-Jan-6-committee.html'
response = requests.get(url1)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('body').find_all('h2')
for a in title:
    print(a.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find('body').find_all('p')
for b in content:
    print(b.text.strip())
print("============NEXT ARTICLE=========")


#The Independent
url2=('https://www.independent.co.uk/news/world/americas/us-politics/trump-mike-rounds-election-south-dakota-b1990190.html')
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')
title1 = soup.find('body').find_all('h1')
for c in title1:
    print(c.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content1 = soup.find('body').find_all('p')
for d in content1:
    print(d.text.strip())
print("============NEXT ARTICLE=========")

#HuffPost
url3=('https://www.huffingtonpost.co.uk/entry/donald-trump-capitol-riot-january-6-coup_uk_61d6a7c4e4b0d637ae9e08bc')
response = requests.get(url3)
soup = BeautifulSoup(response.text, 'html.parser')
title2 = soup.find('body').find_all('h1')
for e in title2:
    print(e.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content2 = soup.find('body').find_all('p')
for f in content2:
    print(f.text.strip())
print("============NEXT ARTICLE=========")
#The Sun 
url4=('https://www.thesun.co.uk/news/13699364/where-donald-trump-today/')
response = requests.get(url4)
soup = BeautifulSoup(response.text, 'html.parser')
title3 = soup.find('body').find_all('h1')
for g in title3:
    print(g.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content3 = soup.find('body').find_all('p')
for h in content3:
    print(h.text.strip())
print("============NEXT ARTICLE=========")

#Daily Express
url5=('https://www.express.co.uk/news/world/1546931/joe-biden-news-popularity-polls-chaotic-trump-divided-america-midterm-elections')
response = requests.get(url5)
soup = BeautifulSoup(response.text, 'html.parser')
title4 = soup.find('body').find_all('h1')
for i in title4:
    print(i.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content3 = soup.find('body').find_all('p')
for j in content3:
    print(j.text.strip())
print("============END=========")
