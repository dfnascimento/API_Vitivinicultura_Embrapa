from flask import Blueprint, request
from utils import *
from core.scrapping import scrap_processamento

processamento = Blueprint('processamento', __name__ )

@processamento.route('/', methods=['GET'])
def get_processamento():

    ano = request.args.get('ano')
    subopcao = request.args.get('subopcao')
     
    valida_ano = ano_invalido(ano)
    if valida_ano != None :
        return valida_ano
    
    valida_sub_opcao= subopcao_invalida(PROCESSAMENTO, subopcao)

    if valida_sub_opcao != None:
        return valida_sub_opcao
    
    const_subopcao = retorna_subopcao(PROCESSAMENTO, subopcao)

    df = scrap_processamento(const_subopcao, ano)


    if not df.empty:

        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df
    
    else:
    
        return "Erro"
