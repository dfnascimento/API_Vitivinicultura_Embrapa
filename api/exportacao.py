from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from utils import *
from core.scrapping import scrap_exportacao
from core.leitura_arquivos import get_exportacao_csv
from autenticacao import auth


exportacao = Blueprint('exportacao', __name__ )

@exportacao.route('/', methods=['GET'])
#@swag_from('../docs/exportacao.yml')
@auth.login_required
def get_exportacao():
    """

    Endpoint para buscar dados de exportação

    Parametros:
    
        - ano (int): Ano de referencia
        - subopcao (str): Subopcao de exportacao
    
    Returns:
        
        - JSON: Um objeto JSON com as colunas ['Produto', 'Países','Quantidade[kg]', 'Valor(US$)', 'Ano'] e os dados de processamento do ano especificado.
    
    """

    ano = request.args.get('ano')
    subopcao = request.args.get('subopcao')
     
    valida_ano = ano_invalido(ano)
    if valida_ano != None :
        return jsonify(valida_ano), 400
    
    valida_sub_opcao= subopcao_invalida(EXPORTACAO, subopcao)

    if valida_sub_opcao != None:
        return jsonify(valida_sub_opcao), 400
    
    const_subopcao = retorna_subopcao(EXPORTACAO, subopcao)

    df = scrap_exportacao(const_subopcao, ano)


    if not df.empty:

        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
    
    else:
    
        df = get_exportacao_csv(const_subopcao, ano)
        df = df.to_json(orient='records', force_ascii=False, indent=4)

        return df, 200
