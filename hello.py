# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1><b>Hello World!</b></h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

from flask import request
@app.route('/contextorequisicao')
def contextorequisicao():
    requisicao = request.headers.get('User-Agent')
    return f'<p>Your browser is {requisicao}</p>'

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    codigo = request.args['codigo']
    return f'<p>{codigo}</p>'

from flask import make_response
@app.route('/objetoresposta')
def objetoresposta():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

from flask import redirect
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

from flask import abort
@app.route('/abortar')
def abortar():
    abort(404)