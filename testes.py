import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

# Coin to Fish (CTFT)
# while True:

while True:

    ctft = 'https://coinmarketcap.com/pt-br/currencies/coin-to-fish/'

    ctftPage = urllib.request.urlopen(ctft)

    ctftSoup = BeautifulSoup(ctftPage, 'html5lib')
    
    ctft_name = ctftSoup.find('div', attrs={'class': 'priceValue'})
    ctftPrice = ctft_name.text.strip()

    options = Options()

    # options.add_argument('--headless')#add_argument('--headless')


    driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))

    driver.get(ctft)

    # print(ctftPrice)

    # time.sleep(20)