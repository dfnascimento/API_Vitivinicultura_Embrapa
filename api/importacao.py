import os
from flask import Blueprint, jsonify,  request
from flasgger.utils import swag_from
from utils import *
from services.scrapping import scrap_importacao
from services.leitura_arquivos import get_importacao_csv
from autenticacao import auth

importacao = Blueprint('importacao', __name__ )

base_path = os.path.dirname(__file__)  
parent_path = os.path.abspath(os.path.join(base_path, os.pardir))
file_path = os.path.join(parent_path, 'docs', 'importacao.yml')


@importacao.route('/', methods=['GET'])
@swag_from(file_path)
@auth.login_required
def get_importacao():
    """

    Endpoint para obtenção dos dados de importação

    Parâmetros:
        - ano: (int) Ano para o qual deseja buscar os dados.
        - subopcao: (str) Subopção para a qual deseja buscar os dados.
    
    Retorno:
        - JSON: Um objeto JSON com as colunas ['Produto', 'Países','Quantidade[kg]', 'Valor(US$)', 'Ano'] e os dados de processamento do ano especificado.

    """

    ano = request.args.get('ano')
    subopcao = request.args.get('subopcao')

    ano = request.args.get('ano')
    subopcao = request.args.get('subopcao')
     
    valida_ano = ano_invalido(ano)
    if valida_ano != None :
        return jsonify(valida_ano), 400
    
    valida_sub_opcao= subopcao_invalida(IMPORTACAO, subopcao)

    if valida_sub_opcao != None:
        return jsonify(valida_sub_opcao), 400
    
    const_subopcao = retorna_subopcao(IMPORTACAO, subopcao)

    df = scrap_importacao(const_subopcao, ano)


    if not df.empty:

        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
    
    else:
    
        df = get_importacao_csv(const_subopcao, ano)
        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
