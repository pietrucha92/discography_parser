from bs4 import BeautifulSoup
import urllib

source = urllib.urlopen('https://pl.wikipedia.org/wiki/Metallica').read()
soup = BeautifulSoup(source, 'html.parser')
heading = soup.find(id='Dyskografia')
heading2 = heading.find_next('h3')
titles = heading2.find_next('ul')
discs = titles.find_all('a')
for disc in discs:
    print disc.string
