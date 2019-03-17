#Use python to TOKENIZE 

from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords
 
response = urllib.request.urlopen('http://php.net/')
html = response.read()
#for the second variable of BeautifulSoup,
#is represent the type of function used
#for html5lib is most popular to be taken
#to scrap the webpage of HTML5 structure
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
#split out all the words by one to one
tokens = text.split()
clean_tokens = list()
#choose the ENGLISH version of stopwords
sr = stopwords.words('english')
for token in tokens:
    if not token in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))

#use mathlab to plot a graph
freq.plot(20, cumulative=False)
