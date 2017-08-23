from bs4 import BeautifulSoup
import urllib
import sys

band = ""
if len(sys.argv)==2:
    band = sys.argv[1]
    print ("Szukam danych dla zespolu: ", band)
elif len(sys.argv)>2:
    print "Podano za duzo danych"
    exit
else:
    band = "Metallica"

url = "https://pl.wikipedia.org/wiki/" + band
print url
source = urllib.urlopen(url).read()
soup = BeautifulSoup(source, 'html.parser')
heading = soup.find(id='Dyskografia')
heading2 = heading.find_next('h3')
titles = heading2.find_next('ul')
discs = titles.find_all('li')
for disc in discs:
    print disc.get_text()
