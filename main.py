import re
import domains

# Deze functie is verantwoordelijk voor het ophalen van alle product URLs uit products.txt
def read_products():
    watchlist = []
    with open('products.txt', 'r') as products:
        for product in products:
            product = product.strip('\n') #verwijdert alle spaties
            watchlist.append(product)
    return watchlist

# Deze functie maakt onderscheid tussen de domeinnamen
def domain_sorter(url):
    domain_raw = re.findall('https?://([A-Za-z_0-9.-]+).*', url)
    domain = domain_raw[0]
