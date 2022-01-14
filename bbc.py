import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
 
    else :
        print("Neutral")

url='https://www.bbc.com/news/topics/cp7r8vgl2lgt/donald-trump#main-content'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines=[]
headlines = soup.find('body').find_all('h3')
for x in headlines:
    print(x.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
descs=[]
descs = soup.find('body').find_all('p')
for y in descs:
    print(y.text.strip())

import pandas as pd
dict= {'The Headlines:':[x.text.strip()],
'The Description:':[y.text.strip()]}
df=pd.DataFrame(dict)
print(df)
df.to_csv('output.csv',header=True)
print("The whole paragraph is overall:")
sentiment_scores(y.text.strip())