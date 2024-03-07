from flask import Flask

app = Flask(__name__)

@app.route('/')
def produto():
    return f'Hello world !'

@app.route('/nome/<ola_nome>')
def saudacao(ola_nome):
    return f'Olá {ola_nome}'


#instalar o servidor wsgi com pip install
if __name__ == '__main__':
    app.run()