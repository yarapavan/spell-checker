import newspaper # pip3 install newspaper3k
from nltk import word_tokenize # curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
import enchant #pip3 install pyenchant
import re

url = 'http://www.grammarcheck.net/improve-your-writing-in-7-easy-steps/'
my_article = newspaper.Article(url,language='en') # Extract Article Content
my_article.download()
my_article.parse()  
d = enchant.Dict("en_US") # Spell-Check tokenized words 
print(list(set([word.encode('ascii', 'ignore') for word in word_tokenize(my_article.text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] )))
