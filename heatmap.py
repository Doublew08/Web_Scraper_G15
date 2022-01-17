import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

BBC = 0
DAILY_MAIL = 1
INDEPENDENT = 2
HUFFINGTONPOST = 3
SUN = 4
DAILY_EXPRESS = 5

TRUMP = 0
BIDEN = 1

def scrape_article(url, source, politician) -> float:
    favorability = 0
    response = requests.get(url)  
    sid_obj = SentimentIntensityAnalyzer()
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h1')
    for x in headlines:
        print(x.text.strip())
    paragraphs = soup.find('body').find_all('p')
    for paragraph in paragraphs:
        sentiment_dict = sid_obj.polarity_scores(paragraph.text.strip())
        favorability += (sentiment_dict['pos'] * 1000)
    return favorability / len(paragraphs)

    #print(full_article)
    #print("----------------------------------------------------------------------------------------------------------")



if __name__ == "__main__":

    ARTICLE_INFO = [{ 'politician': TRUMP, 'source': BBC, 'url': 'https://www.bbc.com/news/world-us-canada-59703761'},
                    { 'politician': TRUMP, 'source': DAILY_MAIL, 'url': 'https://www.dailymail.co.uk/news/article-10340497/Trump-asks-Supreme-Court-block-release-White-House-records-Jan-6-committee.html'},
                    { 'politician': TRUMP, 'source': INDEPENDENT, 'url': 'https://www.independent.co.uk/news/world/americas/us-politics/trump-mike-rounds-election-south-dakota-b1990190.html'},
                    { 'politician': TRUMP, 'source': HUFFINGTONPOST, 'url': 'https://www.huffingtonpost.co.uk/entry/donald-trump-capitol-riot-january-6-coup_uk_61d6a7c4e4b0d637ae9e08bc'},
                    { 'politician': TRUMP, 'source': SUN, 'url': 'https://www.thesun.co.uk/news/13699364/where-donald-trump-today/'},
                    { 'politician': TRUMP, 'source': DAILY_EXPRESS, 'url': 'https://www.express.co.uk/news/world/1546931/joe-biden-news-popularity-polls-chaotic-trump-divided-america-midterm-elections'},
                    { 'politician': BIDEN, 'source': BBC, 'url': 'https://www.bbc.com/news/world-us-canada-59787060'},
                    { 'politician': BIDEN, 'source': DAILY_MAIL, 'url': 'https://www.dailymail.co.uk/news/article-10393911/Joe-Biden-calls-Kamala-President-Harris-slip-tongue-speech.html'},
                    { 'politician': BIDEN, 'source': INDEPENDENT, 'url': 'https://www.independent.co.uk/news/world/americas/us-politics/biden-speech-georgia-filibuster-voting-b1991144.html'},
                    { 'politician': BIDEN, 'source': HUFFINGTONPOST, 'url': 'https://www.huffpost.com/entry/biden-state-of-the-union-2022_n_61d87cfee4b0bcd2195ee408'},
                    { 'politician': BIDEN, 'source': SUN, 'url': 'https://www.thesun.co.uk/news/17256159/joe-biden-putin-douglas-murray/'},
                    { 'politician': BIDEN, 'source': DAILY_EXPRESS, 'url': 'https://www.express.co.uk/news/world/1548925/Joe-biden-news-inflation-us-highest-level-forty-years-president'},
    ]

    data_list = []
    article_favoribility = []
    prev_politician = None
    for a_info in ARTICLE_INFO:
        favorability = scrape_article(a_info['url'], a_info['source'], a_info['politician'])
        print(f"favorability for {a_info['politician']} from {a_info['source']} : {favorability}")
        if a_info['politician'] == prev_politician or prev_politician == None:
            article_favoribility.append(favorability)
        else:
            data_list.append(article_favoribility)
            article_favoribility = []
            article_favoribility.append(favorability)
        prev_politician = a_info['politician']
    data_list.append(article_favoribility)


column_labels = ["BBC", "DAILY MAIL", "INDEPENDANT", "HUFFINGTON POST", "THE SUN", "DAILY_EXPRESS"]
row_labels = ["Donald Trump", "Joe Biden"]
fig, axis = plt.subplots()
heatmap_data = np.array(data_list)
#heatmap = axis.pcolor(heatmap_data)
axis.set_yticks(np.arange(heatmap_data.shape[0]), minor=False)
axis.set_xticks(np.arange(heatmap_data.shape[1]), minor=False)
axis.set_yticklabels(row_labels, minor=False)
axis.set_xticklabels(column_labels, minor=False)

plt.imshow(heatmap_data , cmap = 'autumn' , interpolation = 'nearest')
plt.title("Positivity of Articles for Donald Trump and Joe Biden" )
plt.colorbar()
plt.show()

