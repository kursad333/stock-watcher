import re
import handler
import datetime
import time


# Deze functie is verantwoordelijk voor het ophalen van alle product URLs uit products.txt
def read_products():
    watchlist = []
    with open('products.txt', 'r') as products:
        for product in products:
            product = product.strip('\n')  # verwijdert alle spaties
            watchlist.append(product)
    return watchlist


# Deze functie maakt onderscheid tussen de domeinnamen
def domain_sorter(url):
    domain_raw = re.findall('https?://([A-Za-z_0-9.-]+).*', url)
    domain = domain_raw[0]

    # Semi switch-case
    if domain == 'azerty.nl':
        return handler.check_azerty(url)
    if domain == 'www.alternate.nl':
        return handler.check_alternate(url)


def set_interval():
    valid = False
    update_interval = 0

    while not valid:
        try:
            update_interval = float(input("Voer update-interval in minuten"))
            valid = True
        except:
            print("Invoer onjuist, probeer het opnieuw.")

    return update_interval


if __name__ == '__main__':
    watchlist = read_products()

    update_interval = set_interval()
    count = 0

    while True:
        for item in watchlist:
            print(domain_sorter(item))

            count = count + 1
            if len(watchlist) == count:
                time.sleep(update_interval)
                count = 0
