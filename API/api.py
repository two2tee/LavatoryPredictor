import flask
from flask import request, jsonify
from repository import InMemoryRepository

app = flask.Flask(__name__)
app.config['DEBUG'] = True
repository = InMemoryRepository()

@app.route('/',methods=['GET'])
def home():
    return "Lavatory API"

@app.route('/api/v1/sessions',methods=['GET'])
def get():
    if 'id' in request.args:
        return jsonify(repository.read(request.args['id'])) 
    return jsonify(repository.read_all())

@app.route('/api/v1/sessions',methods=['POST'])
def post():
    if 'id' in request.args:
        body = request.json
    return jsonify(repository.read_all())

app.run()