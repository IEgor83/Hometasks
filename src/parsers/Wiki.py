"""parsing using bs4"""

import os
import uuid
import re
import requests
from bs4 import BeautifulSoup as BS
from src.maps.hash_map import HashMap


"""parsing wiki"""


def write_map_in_file(url: str):
    """write map in file"""
    hash_map = HashMap()
    req = requests.get(url)
    soup = BS(req.content, 'html.parser')
    with open('urls.txt', 'a', encoding="utf-8") as file:
        file.write(req.url + '\n')
    words = list(map(lambda s: s.lower().strip(), filter(lambda s: s.isalpha(), soup.text.split())))
    for element in words:
        try:
            hash_map[element] += 1
        except KeyError:
            hash_map[element] = 1
    wiki_title = soup.find(id="firstHeading").string.replace(' ', '') + '.txt'
    hash_map.write(wiki_title)


WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
write_map_in_file(WIKI_RANDOM)