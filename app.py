from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from api.producao import producao


app = Flask(__name__)
app.register_blueprint(producao, url_prefix='/producao')

items = []

@app.route('/')

def home():
    return "Hello, Flask!"

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message":"Hello, World!"})

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if 0 <= item_id < len(items):
        items[item_id].update(data)
        return jsonify(items[item_id])
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        removed = items.pop(item_id)
        return jsonify(removed)
    return jsonify({"error": "Item not found"}), 404

@app.route('/scrape/title', methods=['GET'])
def scrape_title():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return jsonify({"title": title})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = [
        {"id": 1, "nome": "Alice", "email": "alice@example.com"},
        {"id": 2, "nome": "Bob", "email": "bob@example.com"},
        {"id": 3, "nome": "Charlie", "email": "charlie@example.com"}
    ]
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)

