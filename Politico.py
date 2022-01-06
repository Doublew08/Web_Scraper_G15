import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479")
soup = BeautifulSoup(response.text, 'html.parser')
Achievements = soup.find_all('div', attrs={'class' : 'story-text'})
for Achievement in Achievements:
    for pStory in Achievement.find_all('p' , attrs={'class': 'story-text__paragraph'}):
        if pStory.find('span') is not None:
            span_text = pStory.find('span').text
           # final_span = span_text.replace("the move:", )\
            print(span_text)

#for div in soup.find_all('div', class_='story-text'):
    #for h3s1 in div.find_all('h3',  class_='story-text__heading-medium label') or div.find_all('h3', class_='story-text__heading-medium'):
         #print(h3s1.text)

