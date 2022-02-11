import requests
from lxml import html
import telegram_bot

telegram_connection = telegram_bot.check_creds()


def validate_response(url):
    result, req = [], ''

    try:
        req = requests.get(url)
        if '200' in str(req):
            result.append(True)
            result.append(req)
        else:
            result.append(False)
            result.append('Website onbereikbaar, probeer het later opnieuw.')
    except:
        result.append(False)
        result.append('Geen actieve internetverbinding gevonden, probeer het later opnieuw.')

    return result


def check_azerty(link):
    result = ['Azerty.nl']
    response = validate_response(link)

    if response[0]:
        try:
            tree = html.fromstring(response[1].content)

            name = tree.xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/h1')[0].text_content()
            result.append(name)

            # Fixed element for stock information
            stock = tree.xpath('//*[@id="detail"]/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/text()')
            stockExt = tree.xpath(
                '/html/body/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div[2]')

            if stock[0].split()[0] != '0' or 'niet' not in stockExt[0].text_content():
                result.append("OP VOORRAAD")
                if telegram_connection: telegram_bot.sendMsg(link)
            else:
                result.append("UITVERKOCHT")

            result.insert(0, True)
        except:
            result.append('Kan geen voorraad vinden. Controleer het product of raadpleeg de beheerder.')
            result.insert(0, False)
    else:
        result.insert(0, False)
        result.append(response[1])

    return result


def check_alternate(link):
    result = ['Alternate.nl']
    response = validate_response(link)

    if response[0]:
        try:
            tree = html.fromstring(response[1].content)
            name = tree.xpath('//*[@id="product-top"]/div[1]/div[2]/div/h1/span[2]')[0].text_content()
            result.append(name)

            # Fixed location for stock information
            stock = tree.xpath('//*[@id="add-to-cart-form"]/div[1]/div/span/b')[0].text_content()

            if 'Niet' not in stock:
                result.append("OP VOORRAAD")
                if telegram_connection: telegram_bot.sendMsg(link)
            else:
                result.append("UITVERKOCHT")

            result.insert(0, True)
        except:
            result.append('Kan geen voorraad vinden. Controleer het product of raadpleeg de beheerder.')
            result.insert(0, False)
    else:
        result.insert(0, False)
        result.append(response[1])

    return result


def check_mediamarkt(link):
    result = ['MediaMarkt.nl']
    response = validate_response(link)

    if response[0]:
        try:
            tree = html.fromstring(response[1].text)

            name = tree.xpath('/html/head/meta[17]/@content')[0]
            result.append(name)

            # Mediamarkt stock information differs per page
            stock = tree.xpath('//*[@id="product-details"]/div[3]/div[1]')[0].text_content()

            if 'uitverkocht' not in stock:
                result.append("OP VOORRAAD")
                if telegram_connection: telegram_bot.sendMsg(link)
            else:
                result.append("UITVERKOCHT")

            result.insert(0, True)

        except:
            result.append('Kan geen voorraad vinden. Controleer het product of raadpleeg de beheerder.')
            result.insert(0, False)

    else:
        result.insert(0, False)
        result.append(response[1])

    return result


def check_sicomputers(link):
    result = ['SiComputers.nl']
    response = validate_response(link)

    if response[0]:
        try:
            tree = html.fromstring(response[1].content)

            name = \
                tree.xpath('/html/body/div[4]/main/div/div/div[2]/div[3]/div[1]/div/div/div[1]/div[1]/div[1]/h1/span')[
                    0].text_content()
            result.append(name)

            # Proshop uses fixed location if product is in stock
            stock = tree.xpath(
                '/html/body/div[4]/main/div/div/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/text()')

            if len(stock) == 0:
                result.append("OP VOORRAAD")
                if telegram_connection: telegram_bot.sendMsg(link)
            else:
                result.append("UITVERKOCHT")

            result.insert(0, True)
        except:
            result.append('Kan geen voorraad vinden. Controleer het product of raadpleeg de beheerder.')
            result.insert(0, False)
    else:
        result.insert(0, False)
        result.append(response[1])

    return result


def check_proshop(link):
    result = ['ProShop.nl']
    response = validate_response(link)

    if response[0]:
        try:
            tree = html.fromstring(response[1].content)

            name = tree.xpath('/html/body/div[5]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/h1')[0].text_content()
            result.append(name)

            # Proshop uses fixed location if product is in stock
            try:
                tree.xpath('/html/body/div[5]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[5]/div/div[2]')[0] \
                    .text_content()
                result.append("OP VOORRAAD")
                if telegram_connection: telegram_bot.sendMsg(link)
            except:
                result.append("UITVERKOCHT")

            result.insert(0, True)

        except:
            result.append('Kan geen voorraad vinden. Controleer het product of raadpleeg de beheerder.')
            result.insert(0, False)

    else:
        result.insert(0, False)
        result.append(response[1])

    return result
