from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import sys

url = "https://es.wikipedia.org/wiki/Historia_de_M%C3%A9xico"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

with open ('collect.txt', 'w') as f:
    print (soup.get_text(), file=f)
