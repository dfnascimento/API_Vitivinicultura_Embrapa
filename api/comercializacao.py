import os
from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from utils import ano_invalido
from services.scrapping import scrap_comercializacao
from services.leitura_arquivos import get_comercializacao_csv
from auth.autenticacao import auth

comercializacao = Blueprint('comercializacao', __name__ )

base_path = os.path.dirname(__file__) 
parent_path = os.path.abspath(os.path.join(base_path, os.pardir))
file_path = os.path.join(parent_path, 'docs', 'comercializacao.yml')

@comercializacao.route('/', methods=['GET'])
@swag_from(file_path)
@auth.login_required
def get_comercializacao():
    """
    Endpoint para retornar dados de comercialização do ano fornecido.
    
    Parametros:

        - ano (int): ano do qual deseja retornar os dados de comercialização.
    Retorno:
    
        - Objeto Um objeto JSON com as colunas ['Produto','Tipo','Quantidade[L.]', 'Ano']) e os dados de produção do ano especificado.
        
    """

    ano = request.args.get('ano')
   
    valida_ano = ano_invalido(ano)

    if valida_ano != None :
        return jsonify(valida_ano), 400

    df = scrap_comercializacao(ano)

    if not df.empty:
        df = df.to_json(orient='records', force_ascii=False, indent=4)
        return df, 200
    
    else:
        df = get_comercializacao_csv(ano)
        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df,200
