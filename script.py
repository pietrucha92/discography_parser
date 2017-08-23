from bs4 import BeautifulSoup
import urllib

source = urllib.urlopen('https://pl.wikipedia.org/wiki/Metallica').read()
soup = BeautifulSoup(source, 'html.parser')
heading = soup.find(id='Albumy_studyjne')
discs = heading.find_next('ul')
for disc in discs:
    print disc
