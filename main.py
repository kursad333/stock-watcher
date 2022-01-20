import requests
from lxml import html
import re

# DEBUG CODE
def write_debug(content):
    with open('debug.txt', 'w') as log:
        log.write(content)
# DEBUG CODE

# Deze functie is verantwoordelijk voor het ophalen van alle product URLs
def read_products():
    watchlist = []
    with open('products.txt', 'r') as products:
        for product in products:
            product = product.strip('\n') #verwijdert alle spaties
            watchlist.append(product)
    return watchlist

# Deze functie maakt onderscheid tussen de domeinnamen
def domain_sorter(watchlist):
    domain = re.findall('https?://([A-Za-z_0-9.-]+).*', watchlist[1])
    print(domain)

