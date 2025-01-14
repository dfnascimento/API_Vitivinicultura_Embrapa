import pandas as pd
from config import *

def get_producao_csv(ano):
    """
    Lê o arquivo CSV da produção do ano fornecido e retorna um DataFrame com os dados

    Args:
        ano (int): ano para produção
     Returns:
        Dataframe: Dataframe com os dados do arquivo csv 

    """

    path_file = 'files/' + PRODUCAO[2]

    df = pd.read_csv(path_file, sep =';', usecols=['produto', 'control', str(ano)])

    df= df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df = df[['produto', 'control', str(ano)]]
    df.columns = ['Produto','Tipo','Quantidade[L.]']

    df['Ano'] = str(ano)

    df['Tipo'] = df['Tipo'].apply(altera_tipo)
    df['Tipo'] = df['Tipo'].fillna(df['Produto'])

    return df

def altera_tipo(tipo):
    """
    Altera o tipo do produto de acordo com um dicionário
    """
    try:
        if len(tipo) < 3:
            return None
    except Exception as e:
        return None
    
    dict_tipos = {'vm_' : 'VINHO DE MESA', 
                'vv_' : 'VINHO FINO DE MESA (VINIFERA)',
                'su_' : 'SUCO DE UVAS',
                'de_' : 'DERIVADOS',
                'ti_' : 'TINTAS',
                'br_' : 'BRANCAS E ROSADAS',
                've_' : 'VINHO ESPECIAL',
                'es_' : 'ESPUMANTES',
                'ou_' : 'OUTROS PRODUTOS COMERCIALIZADOS'
                }
    

    return dict_tipos.get(tipo[0:3])



def get_processamento_csv(subopcao, ano):
    """
    Lê o arquivo CSV do processamento do ano fornecido e retorna um DataFrame com os dados
    
     Args:
        subopcao (list): lista com opção e código do arquivo
        ano (int): ano para processamento
     Returns:
     
     Dataframe: Dataframe com os dados do arquivo csv  
    """

    path_file = 'files/' + subopcao[2]

    try:
        df = pd.read_csv(path_file, sep =';', usecols=['control','cultivar', str(ano)])
    except Exception as e:
        df = pd.read_csv(path_file, sep ='\t', usecols=['control','cultivar', str(ano)])

    df= df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df = df[['cultivar', 'control', str(ano)]]
    df.columns = ['Produto','Tipo','Quantidade[L.]']

    df.insert(0,'Opção', subopcao[0])
    df['Ano'] = str(ano)

    df['Tipo'] = df['Tipo'].apply(altera_tipo)
    df['Tipo'] = df['Tipo'].fillna(df['Produto'])

    return df

def get_comercializacao_csv(ano):
    """
    Lê o arquivo CSV da comercialização do ano fornecido e retorna um DataFrame com os dados
    
     Args:
        ano (int): ano para comercialização
     Returns:
        Dataframe: Dataframe com os dados do arquivo csv
    
    """
    path_file = 'files/' + COMERCIALIZACAO[2]

    df = pd.read_csv(path_file, sep =';', usecols=['control', 'Produto', str(ano)])

    df= df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df = df[['Produto', 'control', str(ano)]]
    df.columns = ['Produto','Tipo','Quantidade[L.]']

    df['Ano'] = str(ano)

    df['Tipo'] = df['Tipo'].apply(altera_tipo)
    df['Tipo'] = df['Tipo'].fillna(df['Produto'])

    return df


def get_importacao_csv(subopcao, ano):
    """
    Lê o arquivo CSV da importação do ano fornecido e retorna um DataFrame com os dados
    
     Args:
        subopcao (list): lista com opção e código do arquivo
        ano (int): ano para importação
     Returns:
        Dataframe: Dataframe com os dados do arquivo csv
    
    """
    path_file = 'files/' + subopcao[2]

    path_file = 'files/' + subopcao[2]

    try:
        df = pd.read_csv(path_file, sep =';', usecols=['País', str(ano), str(ano) + '.1'])
    except Exception as e:
        df = pd.read_csv(path_file, sep ='\t', usecols=['País',  str(ano), str(ano) + '.1'])

    df= df.map(lambda x: x.strip() if isinstance(x, str) else x)


    df = df[['País', str(ano), str(ano) + '.1']]
    df.columns = ['Países','Quantidade[kg]', 'Valor(US$)']

    df.insert(0,'Produto', subopcao[0])
    df['Ano'] = str(ano)


    return df

def get_exportacao_csv(subopcao, ano):
    """
    Lê o arquivo CSV da exportação do ano fornecido e retorna um DataFrame com os dados
    
     Args:
        subopcao (list): lista com opção e código do arquivo
        ano (int): ano para exportação
     Returns:
        Dataframe: Dataframe com os dados do arquivo csv"""

    path_file = 'files/' + subopcao[2]

    try:
        df = pd.read_csv(path_file, sep =';', usecols=['País', str(ano), str(ano) + '.1'])
    except Exception as e:
        df = pd.read_csv(path_file, sep ='\t', usecols=['País',  str(ano), str(ano) + '.1'])

    df= df.map(lambda x: x.strip() if isinstance(x, str) else x)


    df = df[['País', str(ano), str(ano) + '.1']]
    df.columns = ['Países','Quantidade[kg]', 'Valor(US$)']

    df.insert(0,'Produto', subopcao[0])
    df['Ano'] = str(ano)


    return df
