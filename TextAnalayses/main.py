'''
pip install nltk 
pip install textblob
pip intall newspaper3k
'''

from newspaper import Article  # type: ignore
import nltk # type: ignore
from textblob import TextBlob # type: ignore
nltk.download('punkt')

'''
Url
'''
url = 'https://en.wikipedia.org/wiki/World_War_II'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)

"""
with open('text.txt','r') as f:
    text = f.read()
"""


blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)