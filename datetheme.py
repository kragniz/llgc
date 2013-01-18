#!/usr/bin/python

from llgc import Search
from xml.etree import ElementTree
from frequencies import count, remove
import string
import nltk

s = Search()

# GET DATE TO SEARCH FOR

y = "1886"
m = "11"
d = "20"

query = "IssueDate:[{year}-{month}-{day}T00:00:00Z%20TO%20{year}-{month}-{day}T23:59:59Z]".format(year=y, month=m, day=d)

xmlString = s.search(q = query, fl = "ArticleText", rows=40)


tree = ElementTree.parse("wordlist.xml")
commonWords = []

for el in tree.iterfind(".//lst[@name='topTerms']/int"):
	commonWords.append(el.get("name").lower())
	

tree = ElementTree.ElementTree(ElementTree.fromstring(xmlString))

articles = []

for el in tree.iterfind('.//str[@name="ArticleText"]'):
	artWords = []
	origText = el.text.lower()
	newText = []
	for word in origText.split():
		aWord = word.encode('ascii', 'ignore')
		newText.append(''.join([char for char in aWord if char.isalpha()]))
	for word in [x for x in newText if x not in commonWords]:
		if len(word) > 4:	
			artWords.append(word)
	artText = ' '.join(artWords)
	
	articles.append(artText)

arts = {}
dayDist = nltk.FreqDist()
for i, art in enumerate(articles):
	arts[i] = count(art)
	for item in arts[i].keys():
		for y in range(0, arts[i][item]):
			dayDist.inc(item)

print list(dayDist)[:200]
        

            
        


# GET WORD COUNT OF COMMON WORDS

# FILTER LIST BASED ON 10,000 most common words

# FIND OCCURENCES LEFT COMMON TO ALL ARTICLES

####

# RANK THEM

# SEARCH FOR ARTICLE CONTAINING THESE TERMS

# RETURN IMAGE OF IT


