import requests
from lxml import html

req = requests.get('https://www.mediamarkt.nl/nl/product/_pro-mounts-urbmob-lt2-1688018.html')
content = req.text
tree = html.fromstring(content)

divs = tree.xpath('//*[@id="product-details"]/div[3]/div[1]')[0].text_content()

if 'uitverkocht' not in divs:
    print("voorraad")
else:
    print("uitverkocht")
