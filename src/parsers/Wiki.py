"""parsing using bs4"""
import requests
from bs4 import BeautifulSoup as BS
from src.hash_map import HashMap

WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
r = requests.get(WIKI_RANDOM)
soup = BS(r.content, 'html.parser')
hash_map = HashMap(50)
all_a = soup.find_all('a')
for element in all_a:
    element_text = element.text
    if 'https://ru.wikipedia.org/w/index.php?title=' not in element_text:
        print(element_text)
        if hash_map[element_text] is None:
            hash_map[element_text] = 0
        hash_map[element_text] += 1
print(hash_map)