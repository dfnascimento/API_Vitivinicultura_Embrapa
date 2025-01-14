from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from utils import ano_invalido
from core.scrapping import scrap_comercializacao
from core.leitura_arquivos import get_comercializacao_csv
from autenticacao import auth

comercializacao = Blueprint('comercializacao', __name__ )

@comercializacao.route('/', methods=['GET'])
@swag_from('../docs/comercializacao.yml')
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
