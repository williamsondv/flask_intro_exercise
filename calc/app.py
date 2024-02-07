# Put your app in here.
from flask import Flask
from flask import request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    return operations.add(int(request.args['a']), int(request.args['b']))

@app.route('/sub')
def sub():
    return operations.sub(int(request.args['a']), int(request.args['b']))

@app.route('/mult')
def mult():
    return operations.mult(int(request.args['a']), int(request.args['b']))

@app.route('/div')
def div():
    return operations.div(int(request.args['a']), int(request.args['b']))

@app.route('/math/<operation>')
def all_in_one(operation):
    dict = {"add" : operations.add,"sub" : operations.sub,"mult" : operations.mult,"div" : operations.div}
    return dict[operation](int(request.args["a"]), int(request.args["b"]))