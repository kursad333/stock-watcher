import re
import handler
import datetime
import time


# WET & DRY

# Deze functie is verantwoordelijk voor het ophalen van alle product URLs uit products.txt
def read_products():
    watchlist = []
    with open('products.txt', 'r') as products:
        for product in products:
            product = product.strip('\n')  # verwijdert alle spaties

            # filtert lege regels eruit
            if len(product) > 0:
                watchlist.append(product)
            else:
                pass

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
    if domain == 'www.mediamarkt.nl':
        return handler.check_mediamarkt(url)
    if domain == 'www.sicomputers.nl':
        return handler.check_sicomputers(url)
    if domain == 'www.proshop.nl':
        return handler.check_proshop(url)


# Deze functie is verantwoordelijk voor de update-interval in te stellen door de gebruiker
def set_interval():
    valid = False
    update_interval = 0

    while not valid:
        try:
            update_interval = float(input("Voer update-interval in minuten")) * 60
            valid = True
        except:
            print("Invoer onjuist, probeer het opnieuw.")

    return update_interval


if __name__ == '__main__':

    # Haal alle URLs uit product.txt
    watchlist = read_products()

    # Set interval van gebruiker
    update_interval = set_interval()
    count = 0

    while True:
        for item in watchlist:
            result = domain_sorter(item)
            curr_time = datetime.datetime.now().strftime('%d-%b [%X]')

            # Alle opgehaalde data wordt hierin weergegeven
            print(f'{curr_time} - {result[0]} {result[2]} - {result[1]}  ')

            count = count + 1

            if len(watchlist) == count:
                time.sleep(update_interval)
                count = 0
