import os
from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from utils import ano_invalido
from services.scrapping import scrap_producao
from services.leitura_arquivos import get_producao_csv
from autenticacao import auth


producao = Blueprint('producao', __name__ )

base_path = os.path.dirname(__file__) 
parent_path = os.path.abspath(os.path.join(base_path, os.pardir))
file_path = os.path.join(parent_path, 'docs', 'producao.yml')

@producao.route('/', methods=['GET'])
@swag_from(file_path)
@auth.login_required
def get_producao():
    """
    Endpoint para buscar dados de produção por ano.
    
     Parâmetros:
        - ano (int): O ano desejado para buscar os dados de produção.
     
     Retorno:
        - JSON: Um objeto JSON com as colunas ['Produto','Tipo','Quantidade[L.]', 'Ano'] e os dados de produção do ano especificado.
     
     """

    ano = request.args.get('ano')
   
    valida_ano = ano_invalido(ano)  

    if valida_ano != None :
        return jsonify({"error": valida_ano}), 400

    df = scrap_producao(ano)

    if not df.empty:
        df = df.to_json(orient='records', force_ascii=False, indent=4)
        return df, 201
    
    else:
        
        df = get_producao_csv(ano)
        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df


