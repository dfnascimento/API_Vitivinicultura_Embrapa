from flask import Flask
from flasgger import Swagger
from api.producao import producao
from api.processamento import processamento
from api.comercializacao import comercializacao
from api.importacao import importacao
from api.exportacao import exportacao
from utils import gera_logger

app = Flask(__name__)


app.register_blueprint(producao, url_prefix='/producao')
app.register_blueprint(processamento, url_prefix='/processamento')
app.register_blueprint(comercializacao, url_prefix='/comercializacao')
app.register_blueprint(importacao, url_prefix='/importacao')
app.register_blueprint(exportacao, url_prefix='/exportacao')


swagger = Swagger(app)

if __name__ == '__main__':
    gera_logger()
    app.run(debug=True)

