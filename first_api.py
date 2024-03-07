from flask import Flask
import app

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world !'

@app.route('/nome/<ola_nome>')
def saudacao(ola_nome):
    return f'Olá {ola_nome}'


#instalar o servidor wsgi com pip install
if __name__ == '__main__':
    app.run()