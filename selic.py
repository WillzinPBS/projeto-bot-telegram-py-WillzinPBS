import urllib.request

from bs4 import BeautifulSoup

wiki = 'https://blog.nubank.com.br/taxa-selic'

page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page, 'html5lib')

list_item = soup.find('blockquote', attrs={'class': 'wp-block-quote'})
name = list_item.text.strip()

nameSplited = name.split()

print(nameSplited)