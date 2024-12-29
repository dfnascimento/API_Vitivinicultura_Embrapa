from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging

URL_PRODUCAO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
URL_PROCESSAMENTO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
URL_COMERCIALIZACAO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
URL_IMPORTACAO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'

# Criar um logger
logger = logging.getLogger('Log API')
logger.setLevel(logging.INFO)

# Criar um handler para escrever em um arquivo
file_handler = logging.FileHandler('meu_log.log')
file_handler.setLevel(logging.ERROR)

# Criar um handler para escrever no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Criar um formatter e adicioná-lo aos handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionar os handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def scrap_producao(ano):

    url = URL_PRODUCAO + "&ano=" + str(ano)

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

def scrap_processamento(sub_opcao, ano):

    dict_opcao = { 1 : "subopt_01", 2 : "subopt_02", 3 : "subopt_03", 4 : "subopt_04"}
    dict_rotulo = { 1 : "Viníferas", 2 : "Americanas e hibridas", 3 : "Uvas de mesa", 4 : "Sem Classificação"}

    url = URL_PROCESSAMENTO + "&subopcao=" + dict_opcao[sub_opcao] + "&ano=" + str(ano)

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

            lista.append([dict_rotulo[sub_opcao], cultivar, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Opção','Produto','Tipo','Quantidade[L.]', 'Ano'])

        return df_itens

    except Exception as e:
        print("Erro" + str(e))

    return None


def scrap_comercializacao(ano):

    url = URL_COMERCIALIZACAO + "&ano=" + str(ano)

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

    return None



def scrap_importacao(sub_opcao, ano):

    dict_opcao = { 1 : "subopt_01", 2 : "subopt_02", 3 : "subopt_03", 4 : "subopt_04", 5 : '"subopt_04"'}
    dict_rotulo = { 1 : "Vinhos de mesa", 2 : "Espumantes", 3 : "Uvas frescas", 4 : "Uvas passas", 5 : "Suco de uva"}

    url = URL_IMPORTACAO + "&subopcao=" + dict_opcao[sub_opcao] + "&ano=" + str(ano)

    logger.info("URL: " + url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        itens = soup.find('table').find_all('tr')

        result = []

        for item in itens:
            result += item.find_all('td')

        lista = []

        print(result)
        for i in range(0, len(result), 3):
            paises = result[i].text.strip()
            quantidade = result[i+1].text.strip()
            valor = result[i+2].text.strip()


            lista.append([dict_rotulo[sub_opcao], paises, quantidade, valor, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto', 'Países','Quantidade[kg]', 'Valor(US$)', 'Ano'])

        return df_itens

    except Exception as e:
        print("Erro" + str(e))

    return pd.DataFrame()

