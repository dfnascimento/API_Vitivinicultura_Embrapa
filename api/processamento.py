from flask import Blueprint, jsonify,  request
from flasgger.utils import swag_from
from utils import *
from core.scrapping import scrap_processamento
from core.leitura_arquivos import get_processamento_csv
from autenticacao import auth

processamento = Blueprint('processamento', __name__ )

@processamento.route('/', methods=['GET'])
#@swag_from('../docs/processamento.yml')
@auth.login_required
def get_processamento():
    """
    Endpoint para buscar dados de processamento por ano e subopção.
    
        Parâmetros:
            - ano: (int) Ano para o qual deseja buscar os dados.
            - subopcao: (str) Subopção para a qual deseja buscar os dados.
        
        Retorno:
            - JSON: Um objeto JSON com as colunas ['Opção','Produto','Tipo','Quantidade[L.]', 'Ano'] e os dados de processamento do ano especificado.
     
    """

    ano = request.args.get('ano')
    subopcao = request.args.get('subopcao')
     
    valida_ano = ano_invalido(ano)
    if valida_ano != None :
        return jsonify(valida_ano), 400
    
    valida_sub_opcao= subopcao_invalida(PROCESSAMENTO, subopcao)

    if valida_sub_opcao != None:
        return jsonify(valida_sub_opcao), 400
    
    const_subopcao = retorna_subopcao(PROCESSAMENTO, subopcao)

    df = scrap_processamento(const_subopcao, ano)


    if not df.empty:

        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
    
    else:
    
        df = get_processamento_csv(const_subopcao, ano)
        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
