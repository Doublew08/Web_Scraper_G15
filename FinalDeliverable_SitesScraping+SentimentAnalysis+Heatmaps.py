import requests
from bs4 import BeautifulSoup
#Donald Trump
# bbc
url = 'https://www.bbc.com/news/world-us-canada-59703761'
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

# Daily Mail
url1 = 'https://www.dailymail.co.uk/news/article-10340497/Trump-asks-Supreme-Court-block-release-White-House-records-Jan-6-committee.html'
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

# The Independent
url2 = (
    'https://www.independent.co.uk/news/world/americas/us-politics/trump-mike-rounds-election-south-dakota-b1990190.html')
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

# HuffPost
url3 = ('https://www.huffingtonpost.co.uk/entry/donald-trump-capitol-riot-january-6-coup_uk_61d6a7c4e4b0d637ae9e08bc')
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
# The Sun
url4 = ('https://www.thesun.co.uk/news/13699364/where-donald-trump-today/')
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

# Daily Express
url5 = (
    'https://www.express.co.uk/news/world/1546931/joe-biden-news-popularity-polls-chaotic-trump-divided-america-midterm-elections')
response = requests.get(url5)
soup = BeautifulSoup(response.text, 'html.parser')
title4 = soup.find('body').find_all('h1')
for i in title4:
    print(i.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content4 = soup.find('body').find_all('p')
for j in content4:
    print(j.text.strip())
print("============END=========")
print("Articles done for Donald Trump")

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(article):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(article)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("article was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("article was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("article was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("article Overall Rated As", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")


if __name__ == "__main__":
    print("\n1st Article (BBC) DT :")
    article = y.text

    # function calling
    sentiment_scores(article)

    print("\n2nd Article (Daily Mail) DT:")
    article = b.text
    sentiment_scores(article)

    print("\n3rd Article (The Independent) DT :")
    article = d.text
    sentiment_scores(article)

    print("\n4th Article (Huffington Post) DT :")
    article = f.text
    sentiment_scores(article)

    print("\n5th Article (The Sun) DT :")
    article = h.text
    sentiment_scores(article)

    print("\n6th Article (Daily Express) DT :")
    article = j.text
    sentiment_scores(article)
print("Sentiment analysis done for Donald Trump")

# ============Joe Biden===============
# bbc
wrl = 'https://www.bbc.com/news/world-us-canada-59787060'
response = requests.get(wrl)

soup = BeautifulSoup(response.text, 'html.parser')
headlines1 = soup.find('body').find_all('h1')
for x1 in headlines1:
    print(x1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
descs1 = soup.find('body').find_all('p')
for y1 in descs1:
    print(y1.text.strip())
print("y1 after loop ", y1)
print("============NEXT ARTICLE=========")

# Daily Mail
wrl1 = 'https://www.dailymail.co.uk/news/article-10393911/Joe-Biden-calls-Kamala-President-Harris-slip-tongue-speech.html'
response = requests.get(wrl1)
soup = BeautifulSoup(response.text, 'html.parser')
title1 = soup.find('body').find_all('h2')
for a1 in title1:
    print(a1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content11 = soup.find('body').find_all('p')
for b1 in content11:
    print(b1.text.strip())
print("============NEXT ARTICLE=========")

# The Independent
url12 = (
    'https://www.independent.co.uk/news/world/americas/us-politics/biden-speech-georgia-filibuster-voting-b1991144.html')
response = requests.get(url12)
soup = BeautifulSoup(response.text, 'html.parser')
title11 = soup.find('body').find_all('h1')
for c1 in title11:
    print(c1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content111 = soup.find('body').find_all('p')
for d1 in content111:
    print(d1.text.strip())
print("============NEXT ARTICLE=========")

# HuffPost
url13 = ('https://www.huffpost.com/entry/biden-state-of-the-union-2022_n_61d87cfee4b0bcd2195ee408')
response = requests.get(url13)
soup = BeautifulSoup(response.text, 'html.parser')
title12 = soup.find('body').find_all('h1')
for e1 in title12:
    print(e1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content12 = soup.find('body').find_all('p')
for f1 in content12:
    print(f1.text.strip())
print("============NEXT ARTICLE=========")
# The Sun
url14 = ('https://www.thesun.co.uk/news/17256159/joe-biden-putin-douglas-murray/')
response = requests.get(url14)
soup = BeautifulSoup(response.text, 'html.parser')
title13 = soup.find('body').find_all('h1')
for g1 in title13:
    print(g1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content13 = soup.find('body').find_all('p')
for h1 in content13:
    print(h1.text.strip())
print("============NEXT ARTICLE=========")

# Daily Express
url15 = ('https://www.express.co.uk/news/world/1548925/Joe-biden-news-inflation-us-highest-level-forty-years-president')
response = requests.get(url15)
soup = BeautifulSoup(response.text, 'html.parser')
title14 = soup.find('body').find_all('h1')
for i1 in title14:
    print(i1.text.strip())
soup = BeautifulSoup(response.text, 'html.parser')
content14 = soup.find('body').find_all('p')
for j1 in content14:
    print(j1.text.strip())
print("============END=========")
print("End of articles on Joe Biden")


def sentiment_scores(article2):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict2 = sid_obj.polarity_scores(article2)

    print("Overall sentiment dictionary is : ", sentiment_dict2)
    print("article was rated as ", sentiment_dict2['neg'] * 100, "% Negative")
    print("article was rated as ", sentiment_dict2['neu'] * 100, "% Neutral")
    print("article was rated as ", sentiment_dict2['pos'] * 100, "% Positive")

    print("article Overall Rated As", end=" ")
    if sentiment_dict2['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict2['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")



if __name__ == "__main__":
    print("\n1st Article (BBC) :")
    article2 = y1.text

    # function calling
    sentiment_scores(article2)

    print("\n2nd Article (Daily Mail) JB:")
    article2 = b1.text
    sentiment_scores(article2)

    print("\n3rd Article (The Independent) JB:")
    article2 = d1.text
    sentiment_scores(article2)

    print("\n4th Article (Huffington Post) JB:")
    article2 = f1.text
    sentiment_scores(article2)

    print("\n5th Article (The Sun) JB:")
    article2 = h1.text
    sentiment_scores(article2)

    print("\n6th Article (Daily Express) JB :")
    article2 = j1.text
    sentiment_scores(article2)
print("SENTIMENT ANALYSIS DONE FOR JOE BIDEN")