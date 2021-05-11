from flask import Flask

app = Flask(__name__)

@app.route('/') # Los decoradores son funciones que rodean a funciones. Decorador de la instancia app
# Debajo de un decorador siempre va a haber una función
def index():
    return 'Hola, mundo!'

@app.route('/adios')
def bye():
    return 'Hasta luego, cocodrilo'