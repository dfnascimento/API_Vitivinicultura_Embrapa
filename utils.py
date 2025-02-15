import logging
from config import *

def get_url(opcao, subopcao, ano):
    """
    Retorna a URL com os parametros de opcao, subopcao e ano
    
     Args:
        opcao (tupla): Opção do tipo de dados (PRODUCAO, COMERCIALIZACAO, PROCESSAMENTO, IMPORTACAO, EXPORTACAO)
        subopcao (tupla): Subopção do tipo de dados (VINIFERAS, AMERICANAS_E_HIBRIDAS, ...)
        ano (str): Ano dos dados a serem extraídos"""

    url = ''

    if (opcao in (PRODUCAO, COMERCIALIZACAO)):
        url = URL + "?ano=" + str(ano) + '&opcao=' + opcao[1]

    elif (opcao in (PROCESSAMENTO, IMPORTACAO, EXPORTACAO)):
        url = URL + "?ano=" + str(ano) + '&opcao=' + opcao[1] + '&subopcao=' + subopcao[1]

    return url



def ano_invalido(ano):
    """
    Verifica se o ano informado é válido
    
     Args:
        ano (str): Ano dos dados a serem extraídos
     Returns:
        str: Mensagem de erro caso o ano seja inválido ou None caso seja válido"""

    if not ano:
        return "Ano deve ser informado"
    
    try:
        ano_int = int(ano)
    except ValueError as e:
        return "Ano inválido. Informe apenas numeros entre 1970 e 2023"
    
    if ano_int > 2023 or ano_int < 1970:
        return "Ano inválido. Informe apenas numeros entre 1970 e 2023"
    
    return None

def subopcao_invalida(opcao, subopcao):
    """
    Verifica se a subopção informada é válida
    
     Args:
        opcao (tupla): Opção do tipo de dados (PRODUCAO, COMERCIALIZACAO, PROCESSAMENTO, IMPORTACAO, EXPORTACAO)
        subopcao (str): Subopcao recebida como string
     Returns:
        str: Mensagem de erro caso a subopção seja inválida ou None caso seja válida"""
    
    try:
        subopcao = subopcao.strip().lower()
    except Exception as e:
        return "Subopção deve ser informada"

    if opcao == PROCESSAMENTO:
        if subopcao.lower() not in (VINIFERAS[0].lower(), AMERICANAS_E_HIBRIDAS[0].lower(), UVAS_DE_MESA[0].lower(), SEM_CLASSIFICACAO[0].lower()):

            return "Subopção inválida. Informe uma subopção dentre as a seguir: " + \
                VINIFERAS[0] + ", " + \
                    AMERICANAS_E_HIBRIDAS[0] + ", " + \
                        UVAS_DE_MESA[0] + " ou " + SEM_CLASSIFICACAO[0]

    elif opcao == IMPORTACAO:
        if subopcao.lower() not in (VINHOS_DE_MESA_IMP[0].lower(), ESPUMANTES_IMP[0].lower(), UVAS_FRESCAS_IMP[0].lower(), UVAS_PASSAS_IMP[0].lower(), SUCO_DE_UVA_IMP[0].lower()):

            return "Subopção inválida. Informe uma subopção dentre as a seguir:" + \
                VINHOS_DE_MESA_IMP[0] + ", " + \
                    ESPUMANTES_IMP[0] + ", " + \
                        UVAS_FRESCAS_IMP[0] + ", " + \
                            UVAS_PASSAS_IMP[0] + " ou " + SUCO_DE_UVA_IMP[0]

    elif opcao == EXPORTACAO:
        if subopcao.lower() not in (VINHOS_DE_MESA_EXP[0].lower(), ESPUMANTES_EXP[0].lower(), UVAS_FRESCAS_EXP[0].lower(), SUCO_DE_UVA_EXP[0].lower()):

            return "Subopção inválida. Informe uma subopção dentre as a seguir: " + \
                VINHOS_DE_MESA_EXP[0] + ", " + \
                    ESPUMANTES_EXP[0] + ", " + \
                        UVAS_FRESCAS_EXP[0] + " ou " + SUCO_DE_UVA_EXP[0]        

    return None

def retorna_subopcao(opcao, subopcao):
    """
    Retorna a constante correspondente a subopcao informada
    
     Args:
        opcao (tupla): Opção do tipo de dados (PRODUCAO, COMERCIALIZACAO, PROCESSAMENTO, IMPORTACAO, EXPORTACAO)
        subopcao (str): Subopcao recebida como string
     Returns:
        tupla: Subopção correspondente ou None caso não seja encontrada"""

    subopcao = subopcao.strip().lower()

    if opcao == PROCESSAMENTO:

        lista = [VINIFERAS, AMERICANAS_E_HIBRIDAS, UVAS_DE_MESA, SEM_CLASSIFICACAO]

        for item in lista:
            if (item[0].lower() == subopcao):
                return item 

    elif opcao == IMPORTACAO:
        
        lista = [VINHOS_DE_MESA_IMP, ESPUMANTES_IMP, UVAS_FRESCAS_IMP, UVAS_PASSAS_IMP, SUCO_DE_UVA_IMP]

        for item in lista:
            if (item[0].lower() == subopcao):
                return item 

    elif opcao == EXPORTACAO:

        lista = [VINHOS_DE_MESA_EXP, ESPUMANTES_EXP, UVAS_FRESCAS_EXP, SUCO_DE_UVA_EXP]

        for item in lista:
            if (item[0].lower() == subopcao):
                return item 
    return None
