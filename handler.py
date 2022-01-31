import requests
from lxml import html

headers = {
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


def writedebug(content):
    with open('debug.html', 'w') as log:
        log.write(content)


def check_azerty(link):
    result = []

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/h1')[0].text_content()
    result.append(name)

    stock = tree.xpath('//*[@id="detail"]/div/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/text()')

    if stock[0].split()[0] != '0':
        result.append(True)
    else:
        result.append(False)

    return result


def check_alternate(link):
    result = []

    page = requests.get(link)
    tree = html.fromstring(page.content)

    name = tree.xpath('//*[@id="product-top"]/div[1]/div[2]/div/h1/span[2]')[0].text_content()
    result.append(name)

    stock = tree.xpath('//*[@id="add-to-cart-form"]/div[1]/div/span/b')[0].text_content()

    if 'Niet' not in stock:
        result.append(True)
    else:
        result.append(False)

    return result


def check_amazonNL(link):
    pass


def check_amazonDE(link):
    pass


def check_mediamarkt(link):
    result = []

    page = requests.get(link)
    tree = html.fromstring(page.text)

    name = tree.xpath('/html/head/meta[17]/@content')[0]
    result.append(name)

    stock = tree.xpath('//*[@id="product-details"]/div[3]/div[1]/div[3]/ul/li[3]/span')[0].text_content()

    if 'uitverkocht' not in stock:
        result.append(True)
    else:
        result.append(False)

    return result


def check_sicomputers(link):
    pass


def check_proshop(link):
    pass
