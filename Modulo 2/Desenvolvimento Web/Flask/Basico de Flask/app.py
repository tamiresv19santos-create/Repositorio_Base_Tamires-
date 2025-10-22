## IMPORTANDO "partes do flask
from flask import Flask, render_template, request




## criando o APP e dizendo que ele está nesse arquivo com nome dele 
app = Flask(__name__)




### criando roras 

## / significa principal onde o site já vai de cara 
@app.route('/')
def ola_mundo():
    return "Olá mundo, Vihh, eu amo o Prof"



## Aqui vamos criar uma nova rota , dessa vez vai ser a / contato 
@app.route('/contato')
def contato():
    return "Página de contato, meu número é 707070-7070 é nada tá facin"





## sua vez crie uma nova rota dessa vez / hobbies, la coloque algo que você goste de fazer, exemplo : jogar bola 
@app.route('/hobbies')
def hobbies():
    hobbies = ["escutar musica","dançar","cozinhar","tirar foto do céu"]
    return render_template('hobbies.html')

## lembre-se de criar um template chamdo hobbiese.html

## executando o arquivo 
if __name__ == '__main__':
    app.run(debug=True)