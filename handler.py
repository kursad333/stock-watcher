import requests
from lxml import html


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
    pass


def check_amazonNL(link):
    pass


def check_amazonDE(link):
    pass


def check_mediamarkt(link):
    pass


def check_sicomputers(link):
    pass


def check_informatique(link):
    pass


def check_proshop(link):
    pass
