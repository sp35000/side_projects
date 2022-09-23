#!/usr/bin/python
# -- coding: utf-8
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '''
    <h1>Hello world</h1>
    <h2>Aqui temos uma tag h2</h2>
    <h3>E aqui uma tag h3</h3>
    <p>E aqui um parágrafo</p>
    '''
app.run()
