#nltk==3.8.1
#urllib3==1.26.9
#beautifulsoup4==4.11.1
#html5lib==1.1
#matplotlib==3.5.3

'''This project is a simple web scraper that takes a website link as input and returns the top 30 most common words in it,
excluding stopwords. It uses the nltk, urllib, BeautifulSoup, html5lib and matplotlib libraries to perform the tasks of
tokenization, web request, html parsing, frequency distribution and visualization.'''



import nltk
import urllib.request
from bs4 import BeautifulSoup
import html5lib
import matplotlib.pyplot as plt
#nltk.download('stopwords')

from nltk.corpus import stopwords

#Get information from websites:\
Website_URL = input("Enter any website link: ")
response = urllib.request.urlopen(Website_URL)
html = response.read()  # Read complete data from website.
#print(html)
soup = BeautifulSoup( html, 'html5lib' )
text = soup.get_text( strip = True )
#print(text)

StopWords = stopwords.words('english')
#print(StopWords)     --> List of stopwords of len = 179
#print("Length = ",len(StopWords))

#Removing stopwords from the text.
tokens = [ t for t in text.split() ]
clean_tokens = tokens[:]
#print(tokens)

for token in tokens:
    if token in StopWords:
        clean_tokens.remove(token)
#print(clean_tokens)

#Calculating the frequency distribution of the remaining words.
freq = nltk.FreqDist( clean_tokens)  # most used common words = tags in a dictionary

print(freq)
for key,val in freq.items():
    print( str(key) ,":",str(val))
    
# Graph plot the frequency distribution of the top 30 words.
freq.plot( 30, cumulative = False )
