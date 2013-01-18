#!/usr/bin/env python
import nltk

def count(text):
    fd = nltk.FreqDist()
    for sent in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sent):
            fd.inc(word)
    return fd

def remove(dist, *args):
    newDist = dist
    for dist in args:
        for word in dist:
            newDist[word] = 0
    return newDist

if __name__ == '__main__':
    c= count('''hi there how are you today this word this there are fifteen dogs
    for w in c:
    for w in c:
    doing doggy things this is worded twice dog dogs dog''')
    text1 = count('this is a sample text which is from a different day')
    text2 = count('this text is from the days in the past and has no relevance')
    common = count('a the this is are today hello why where')
    print remove(c, common, text1, text2)
