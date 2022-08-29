import requests

# Bibliotecas selenium para importar os valores em tempo real
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import json

from datetime import datetime

horaAtual = datetime.now().strftime('%H:%M')

# importo os valores dos sites
import urllib.request
from bs4 import BeautifulSoup

#Taxa Selic
selic = 'https://blog.nubank.com.br/taxa-selic'

selicPage = urllib.request.urlopen(selic)

selicSoup = BeautifulSoup(selicPage, 'html5lib')

selic_list_item = selicSoup.find('blockquote', attrs={'class': 'wp-block-quote'})
selicName = selic_list_item.text.strip()

selicSplitedName = selicName.split()

# Coin to Fish (CTFT)
ctft = 'https://coinmarketcap.com/pt-br/currencies/coin-to-fish/'

# ctft = 'https://coinmarketcap.com/pt-br/currencies/coin-to-fish/'

# ctftPage = urllib.request.urlopen(ctft)

# ctftSoup = BeautifulSoup(ctftPage, 'html5lib')

# ctft_name = ctftSoup.find('div', attrs={'class': 'priceValue'})
# ctftPrice = ctft_name.text.strip()


#Classe Telegram Bot
class TelegramBot:
    def __init__(self):
        token = '2015407738:AAFWbZ65SqyvKGDhGfLT1zdKCi6C-Q2b6NQ'

        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.ObterMensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.CriarResposta(mensagem, primeira_mensagem)
                    self.Responder(resposta, chat_id)


    def ObterMensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)


    def CriarResposta(self, mensagem, primeira_mensagem):
        mensagem = mensagem['message']['text']

        if primeira_mensagem == True:
            return 'pai?'

        # Bom dia
        if mensagem.lower() == 'bom dia':
            return 'com você aqui é ótimo'

        # Menu de Opções
        if mensagem.lower() == 'menu':
            return f'O que você deseja meu rei? \n\n Taxa selic \n Agendar uma mensagem'

        # Taxa Selic
        if mensagem.lower() in ('selic', 'taxa selic'):
            return f'A taxa selic atualmente está em {selicSplitedName[10]} ao ano. Nada de poupança :)'

        # CoinToFish (CTFT)
        if mensagem.lower() in ('ctft', 'cointofish', 'coin to fish'):
            while True:
                ctftPage = urllib.request.urlopen(ctft)

                ctftSoup = BeautifulSoup(ctftPage, 'html5lib')
                
                ctft_name = ctftSoup.find('div', attrs={'class': 'priceValue'})
                ctftPrice = ctft_name.text.strip()

                options = Options()

                options.add_argument('--headless')#add_argument('--headless')


                driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))

                driver.get(ctft)

                # time.sleep(20)

                return f'CTFT tá {ctftPrice}'

                # driver.close()

        # Agendar uma mensagem
        if mensagem.split()[0] in ('agendar', 'agenda', 'lembrete') and len(mensagem.split().pop()) != 5:
            return 'Por favor, escolha uma hora no formato HH:MM'
        elif mensagem.split()[0] in ('agendar', 'agenda', 'lembrete'):
            horaAgendada = mensagem.split().pop()
            while True:
                horaAtual = datetime.now().strftime('%H:%M')
                if horaAtual == horaAgendada:
                    return f'Lembrete de {horaAtual}'



    # Função de Resposta
    def Responder(self, resposta, chat_id):
        if resposta == None:
            pass
        else:
            link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
            requests.get(link_de_envio)


bot = TelegramBot()

bot.Iniciar()