from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

def scrap_producao(ano):

    url = URL + "?ano=" + str(ano) + "&opcao=opt_02"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        itens = soup.find_all('td', class_=['tb_item','tb_subitem'])

        df_itens = pd.DataFrame([], columns=['Produto','Tipo','Quantidade[L.]', 'Ano'])
        
        print(len(itens))

        tipo = ''

        for i in range(0, len(itens), 2):
            produto = itens[i].text.strip()
            quantidade = itens[i+1].text.strip()

            if (produto.upper()):
                tipo = produto

            df_itens.loc[df_itens] = [produto, tipo, quantidade, ano]

        print(df_itens)
    except Exception as e:
        print("Erro" + str(e))


scrap_producao(2021)