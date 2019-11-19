# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:06:45 2019

@author: Noel Chang
"""

import bs4 as bs
import urllib.request
import os
import filetype

noCharTag = []
tag = []
DocId = []
urlDownload = []
urldict = {}
index = 0

sauce = urllib.request.urlopen('https://cogcc.state.co.us/weblink/results.aspx?id=12335822').read()
soup = bs.BeautifulSoup(sauce,'lxml')

for url in soup.find_all('a'):
    if url.get('href').startswith('DownloadDocumentPDF'):
        fullUrl = 'https://cogcc.state.co.us/weblink/'+url.get('href')
        urlDownload.append(fullUrl)
        s = ''.join(x for x in url.get('href') if x.isdigit())
        DocId.append(s)
        
for span in soup.find_all('td'):
    if span.text.isupper():
        tag.append(span.text)

for elem in tag:
        newElem = elem.replace('/',' ')
        noCharTag.append(newElem)
            
#print(noCharTag)
#
#print(DocId)
#
urldict = dict(zip(DocId,noCharTag))
print(urldict)
print(urlDownload)

for x in urlDownload:
    #print(x)
    urllib.request.urlretrieve(x, urldict[DocId[index]])
    index += 1

folder = 'C:/Users/Noel Chang/Videos/Study/Andrew NG Machine Learning/Webscraping'

for file in os.listdir(folder):
    kind = filetype.guess_extension(file)
    print(kind)
    if kind is None or kind == 'py':
        continue
    infilename = os.path.join(folder,file)
    newname = infilename + '.'+kind
    output = os.rename(infilename, newname)
    
