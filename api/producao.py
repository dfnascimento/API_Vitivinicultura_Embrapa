
from flask import Blueprint, request
from utils import ano_invalido
from core.scrapping import scrap_producao

producao = Blueprint('producao', __name__ )

@producao.route('/', methods=['GET'])
def get_producao():

    ano = request.args.get('ano')
   
    valida_ano = ano_invalido(ano)

    if valida_ano != None :
        return valida_ano

    df = scrap_producao(ano)

    if not df.empty:
        df = df.to_json(orient='records', force_ascii=False, indent=4)
        return df
    
    else:
        return "Erro"
