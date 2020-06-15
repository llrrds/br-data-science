# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd


# inicializar o whatsapp

wp = WhatsApp()

input('pressione enter apos escanear o qr code')

df = pd.read_excel("exemplo_excel.xlsx")

df.head()

df['Contato']

type(df['Contato']) #ver o tipo de objeto

list(df['Contato']) #transforma o objeto em lista

nomes_palavras_chaves = list(df['Contato'])

lista_mensagens = list(df['Mensagem'])


for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, lista_mensagens):
    wp.search_contact(nome_pesquisar)
    sleep(3)
    wp.send_message(mensagem)
    sleep(4)

#esperar 10 segundos e fechar
sleep(10)
wp.driver.close()

