#!/usr/bin/python2.7
from bs4 import BeautifulSoup
import urllib
import sys

band = ""
lan= "en"
discography = "Discography"
if len(sys.argv)==2:
    band = sys.argv[1]
    print ("Szukam danych dla zespolu: ", band)
elif len(sys.argv)==3:
    lan = sys.argv[1]
    band = sys.argv[2]
elif len(sys.argv)>3:
    print "Podano za duzo danych"
    exit
else:
    band = "Metallica"
if lan == "pl":
    discography="Dyskografia"
   
url = "https://"+lan+".wikipedia.org/wiki/" + band
print url, discography
source = urllib.urlopen(url).read()
soup = BeautifulSoup(source, 'html.parser')
heading = soup.find(id=discography)
titles = heading.find_next('ul')
discs = titles.find_all('li')
for disc in discs:
    print disc.get_text()
