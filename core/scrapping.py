from bs4 import BeautifulSoup
import requests
import pandas as pd

URL_PRODUCAO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
URL_PROCESSAMENTO = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'

def scrap_producao(ano):

    url = URL_PRODUCAO + "&ano=" + str(ano)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])

        lista = []
        print(str(itens))

        for i in range(0, len(itens), 2):
            produto = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()

            if (itens[i]['class'][0] == "tb_item"):
                tipo = produto

            lista.append([produto, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Produto','Tipo','Quantidade[L.]', 'Ano'])
        print(df_itens)
    except Exception as e:
        print("Erro" + str(e))


def scrap_processamento(sub_opcao, ano):

    dict_opcao = { 1 : "subopt_01", 2 : "subopt_02", 3 : "subopt_03", 4 : "subopt_04"}
    dict_rotulo = { 1 : "Viníferas", 2 : "Americanas e hibridas", 3 : "Uvas de mesa", 4 : "Sem Classificação"}

    url = URL_PROCESSAMENTO + "&subopcao=" + dict_opcao[sub_opcao] + "&ano=" + str(ano)

    print(url)


    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])

        print(itens)

        lista = []


        for i in range(0, len(itens), 2):
            cultivar = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()
            
            if (itens[i]['class'][0] == "tb_item"):
                tipo = cultivar

            lista.append([dict_rotulo[sub_opcao], cultivar, tipo, quantidade, ano])

        df_itens = pd.DataFrame(lista, columns=['Opção','Produto','Tipo','Quantidade[L.]', 'Ano'])
        print(df_itens)
    except Exception as e:
        print("Erro" + str(e))

scrap_producao(2023)