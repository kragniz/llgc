#!/usr/bin/env python
import urllib2, base64
import xml.etree.ElementTree as ET

class Search(object):
    def __init__(self, username='hac1', password='sodcaysEnd'):
        self.username = username
        self.password = password

    def search(self, *args, **kwargs):
        query = '&'.join([str(keys) + '=' + str(items) for keys, items in kwargs.items()])
        url = 'http://hacathon.llgc.org.uk/solr/select/?%s' % query

        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (self.username,
                                                      self.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)
        return result.read()

    def _parseResponse(self, xmlData):
        tree = ET.fromstring(xmlData)
        root = tree.getroot()

if __name__ == '__main__':
    s = Search()
    print s._parseResponse(s.search(q = 'ArticleTitle:Test', rows = 10))
