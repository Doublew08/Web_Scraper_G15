import requests
import re
from bs4 import BeautifulSoup
response = requests.get("https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479")
soup = BeautifulSoup(response.text, 'html.parser')
Achievements = soup.find_all('div', attrs={'class' : 'story-text'})
Moves = soup.find_all('div', attrs={'class' : 'story-text'}) 
#move
paragraphs = []
for Achievement in Achievements:
    for pStory in Achievement.find_all('p' , attrs={'class': 'story-text__paragraph'}):
        if pStory.find('span') is not None:
            span_text = pStory.find('span').text
            noMOve_span = span_text.replace("The move:","")
            noImpact_span = noMOve_span.replace("The impact:","")
            noUpshot_span = noImpact_span.replace("The upshot:","")
#this is the title of the thing done by trump
            #print(noUpshot_span)
for div in soup.find_all('div', class_='story-text'):
    #print(div)
    for p in div.find_all('p', attrs={'class': 'story-text__paragraph'}):
      #  if p.find('The move') is not None:
          #pimpact = p.split("The impact:")
          
          
              
              paragraphs.append(str(p.text))
              
              #print(type(x))
              print(paragraphs)
              #paragraphs = [ x for x in paragraphs if not paragraphs.startswitch("The move")]
              #filter(lambda x:x[0]!='The move:',paragraphs.split())
              for x in paragraphs :
                  if "The move:" not in x:
                      paragraphs.remove(x)  

#impact                     
paragraphs2 = []
for Achievement in Achievements:
    for pStory in Achievement.find_all('p' , attrs={'class': 'story-text__paragraph'}):
        if pStory.find('span') is not None:
            span_text = pStory.find('span').text
            noMOve_span = span_text.replace("The move:","")
            noImpact_span = noMOve_span.replace("The impact:","")
            noUpshot_span = noImpact_span.replace("The upshot:","")
#this is the title of the thing done by trump
            #print(noUpshot_span)
for div in soup.find_all('div', class_='story-text'):
    #print(div)
    for p in div.find_all('p', attrs={'class': 'story-text__paragraph'}):
      #  if p.find('The move') is not None:
          #pimpact = p.split("The impact:")
          
          
              
              paragraphs2.append(str(p.text))
              
              #print(type(x))
              print(paragraphs2)
              #paragraphs = [ x for x in paragraphs if not paragraphs.startswitch("The move")]
              #filter(lambda x:x[0]!='The move:',paragraphs.split())
              for x in paragraphs2 :
                  if "The impact:" not in x:
                      paragraphs2.remove(x)  

#upshot                     
paragraphs3 = []
for Achievement in Achievements:
    for pStory in Achievement.find_all('p' , attrs={'class': 'story-text__paragraph'}):
        if pStory.find('span') is not None:
            span_text = pStory.find('span').text
            noMOve_span = span_text.replace("The move:","")
            noImpact_span = noMOve_span.replace("The impact:","")
            noUpshot_span = noImpact_span.replace("The upshot:","")
#this is the title of the thing done by trump
            #print(noUpshot_span)
for div in soup.find_all('div', class_='story-text'):
    #print(div)
    for p in div.find_all('p', attrs={'class': 'story-text__paragraph'}):
      #  if p.find('The move') is not None:
          #pimpact = p.split("The impact:")
          
          
              
              paragraphs3.append(str(p.text))
              
              #print(type(x))
              print(paragraphs3)
              #paragraphs = [ x for x in paragraphs if not paragraphs.startswitch("The move")]
              #filter(lambda x:x[0]!='The move:',paragraphs.split())
              for x in paragraphs3 :
                  if "The upshot:" not in x:
                      paragraphs3.remove(x)  

#prints the move only                  
#print[paragraphs]
          #print(pimpact.text)
                

#for p in soup.find_all('p' , style = font-family:'Jubilat', serif; font-weight:700; font-size:20px;:
    #print(p)
 #conversion to csv 
import pandas as pd
name_dict = {
            'The Move': [paragraphs],
            'The Impact':[paragraphs2],
            'The Upshot':[paragraphs3]
                      }
df = pd.DataFrame(name_dict)
print (df)
df.to_csv('output.csv',header=True)

