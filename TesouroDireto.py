import urllib.request

from bs4 import BeautifulSoup

wiki = 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'

page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page, 'html5lib')

list_item = soup.find('table', attrs={'class': 'td-invest-table td-invest-table--rows td-invest-table--rows--resgatar td-tela-1'}).findAll('tr')[1]

# name = list_item.text.strip()

# print(name)
# name = list_item.soup.find('h3', attrs={'class': 'td-investment-values__card__title'})

# print(name)