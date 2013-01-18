#!/usr/bin/python

from llgc import Search
from xml.etree import ElementTree

s = Search()

# GET DATE TO SEARCH FOR

y = "1886"
m = "11"
d = "20"

query = "IssueDate:[{year}-{month}-{day}T00:00:00Z%20TO%20{year}-{month}-{day}T23:59:59Z]".format(year=y, month=m, day=d)

xmlString = s.search(q = query, fl = "ArticleText", rows=10)


tree = ElementTree.ElementTree(ElementTree.fromstring(xmlString))

articles = []

for el in tree.iterfind('.//str[@name="ArticleText"]'):
	articles.append(el.text)

tree = ElementTree.parse("wordlist.xml")
commonWords = []

for el in tree.iterfind(".//lst[@name='topTerms']/int"):
	commonWords.append(el.get("name"))

print commonWords

# parse XML for articleIDs

# FOR EACH ARTICLE ID



# GET WORD COUNT OF COMMON WORDS

# FILTER LIST BASED ON 10,000 most common words

# FIND OCCURENCES LEFT COMMON TO ALL ARTICLES

####

# RANK THEM

# SEARCH FOR ARTICLE CONTAINING THESE TERMS

# RETURN IMAGE OF IT


