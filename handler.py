import requests
from lxml import html
import telegram_bot

headers = {
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


def check_azerty(link):
    result = []
    result.append('Azerty.nl')

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/h1')[0].text_content()
    result.append(name)

    stock = tree.xpath('//*[@id="detail"]/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/text()')

    if stock[0].split()[0] != '0':
        result.append("OP VOORRAAD")
        telegram_bot.sendMsg(link)
    else:
        result.append("UITVERKOCHT")

    return result


def check_alternate(link):
    result = []
    result.append('Alternate.nl')

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('//*[@id="product-top"]/div[1]/div[2]/div/h1/span[2]')[0].text_content()
    result.append(name)

    stock = tree.xpath('//*[@id="add-to-cart-form"]/div[1]/div/span/b')[0].text_content()

    if 'Niet' not in stock:
        result.append("OP VOORRAAD")
        telegram_bot.sendMsg(link)
    else:
        result.append("UITVERKOCHT")

    return result


def check_mediamarkt(link):
    result = []
    result.append('MediaMarkt.nl')

    page = requests.get(link)
    tree = html.fromstring(page.text)

    name = tree.xpath('/html/head/meta[17]/@content')[0]
    result.append(name)

    stock = tree.xpath('//*[@id="product-details"]/div[3]/div[1]')[0].text_content()

    if 'uitverkocht' not in stock:
        result.append("OP VOORRAAD")
        telegram_bot.sendMsg(link)
    else:
        result.append("UITVERKOCHT")

    return result


def check_sicomputers(link):
    result = []
    result.append('SiComputers.nl')

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('/html/body/div[4]/main/div/div/div[2]/div[3]/div[1]/div/div/div[1]/div[1]/div[1]/h1/span')[
        0].text_content()
    result.append(name)

    stock = tree.xpath(
        '/html/body/div[4]/main/div/div/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/text()')

    if len(stock) == 0:
        result.append("OP VOORRAAD")
        telegram_bot.sendMsg(link)
    else:
        result.append("UITVERKOCHT")

    return result


def check_proshop(link):
    result = []
    result.append('ProShop.nl')

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('/html/body/div[5]/div/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/h1')[0].text_content()
    result.append(name)

    try:
        tree.xpath('/html/body/div[5]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[5]/div/div[2]')[0] \
            .text_content()
        result.append("OP VOORRAAD")
        telegram_bot.sendMsg(link)
    except:
        result.append("UITVERKOCHT")

    return result
