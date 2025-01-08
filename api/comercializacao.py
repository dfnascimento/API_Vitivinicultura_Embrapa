from flask import Blueprint, request
from utils import ano_invalido
from core.scrapping import scrap_comercializacao

comercializacao = Blueprint('comercializacao', __name__ )

@comercializacao.route('/', methods=['GET'])
def get_comercializacao():

    ano = request.args.get('ano')
   
    valida_ano = ano_invalido(ano)

    if valida_ano != None :
        return valida_ano

    df = scrap_comercializacao(ano)

    if not df.empty:
        df = df.to_json(orient='records', force_ascii=False, indent=4)
        return df
    
    else:
        return "Erro"
