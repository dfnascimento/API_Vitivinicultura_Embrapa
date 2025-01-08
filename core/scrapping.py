from bs4 import BeautifulSoup
import requests
import pandas as pd
from config import *
from utils import *


def scrap_producao(ano):

    url = get_url(PRODUCAO, None, ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])

        lista = []

        for i in range(0, len(itens), 2):
            produto = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()
            print(itens[i]['class'][0])

            if (itens[i]['class'][0] == "tb_item"):
                tipo = produto



            lista.append([produto, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto','Tipo','Quantidade[L.]', 'Ano'])

        return df_itens
    
    except Exception as e:
    
        print("Erro" + str(e))

    return pd.DataFrame()

def scrap_processamento(subopcao, ano):

    url = get_url(PROCESSAMENTO, subopcao, ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])

        lista = []


        for i in range(0, len(itens), 2):
            cultivar = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()
            
            if (itens[i]['class'][0] == "tb_item"):
                tipo = cultivar

            lista.append([subopcao[0], cultivar, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Opção','Produto','Tipo','Quantidade[L.]', 'Ano'])

        return df_itens

    except Exception as e:
        print("Erro" + str(e))

    return pd.DataFrame()


def scrap_comercializacao(ano):

    url = get_url(COMERCIALIZACAO, None, ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])
        lista = []

        for i in range(0, len(itens), 2):
            produto = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()

            if (itens[i]['class'][0] == "tb_item"):
                tipo = produto

            lista.append([produto, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto','Tipo','Quantidade[L.]', 'Ano'])

        return df_itens
    
    except Exception as e:
        print("Erro" + str(e))

    return pd.DataFrame()



def scrap_importacao(subopcao, ano):

    url = get_url(IMPORTACAO, subopcao, ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_=['tb_base tb_dados'])
        itens = table.find_all('td')

        lista = []

        for i in range(0, len(itens), 3):
            paises = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()
            valor = itens[i+2].text.strip()


            lista.append([subopcao[0], paises, quantidade, valor, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto', 'Países','Quantidade[kg]', 'Valor(US$)', 'Ano'])

        df_itens = df_itens.iloc[:-1]

        return df_itens

    except Exception as e:
        print("Erro" + str(e))

    return pd.DataFrame()



def scrap_exportacao(subopcao, ano):

    url = get_url(EXPORTACAO, subopcao, ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_=['tb_base tb_dados'])
        itens = table.find_all('td')

        lista = []

        for i in range(0, len(itens), 3):
            paises = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()
            valor = itens[i+2].text.strip()


            lista.append([subopcao[0], paises, quantidade, valor, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto', 'Países','Quantidade[kg]', 'Valor(US$)', 'Ano'])

        df_itens = df_itens.iloc[:-1]
        
        return df_itens

    except Exception as e:
        print("Erro" + str(e))

    return pd.DataFrame()
