
from flask import Blueprint, Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from config import *

producao = Blueprint('producao', __name__ )

@producao.route('/', methods=['GET'])
def get_producao():

    ano = request.args.get('ano')
    if not ano:
        return get_producao_all()
    
    try:

        response = URL + "?ano=" + ano + "&opcao=opt_02"
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return jsonify({"title": title})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_producao_all():
    try:

        response = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2023&opcao=opt_02"
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        #title = soup.title.string.strip()
        return jsonify({"title": soup.string})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500