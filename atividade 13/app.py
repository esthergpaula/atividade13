from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/1', methods = ['post'])
def exercicio_1():

    pri = int(request.form['primeiro'])
    seg = int(request.form['segundo'])
    ter = int(request.form['terceiro'])
    menor = int(min(pri, seg, ter))
    maior = int(max(pri, seg, ter))
    media = (pri+seg+ter)//3

    return f'{menor} é o menor número /// {maior} é o maior número /// {media} é a média de {pri}, {seg} e {ter}'

@app.route('/2', methods = ['POST'])
def exercicio_2():
    peso = int(request.form['peso'])
    altura = float(request.form['altura'])
    imc = (peso / (altura * altura))

    if imc <= 18.5:
        return f'{imc:.2f} abaixo do peso'
    elif imc >= 18.6 and imc <= 24.9:
        return f'{imc:.2f} peso ideal (parabéns)'
    elif imc >= 20.0 and imc <= 29.9:
        return f'{imc:.2f} levemente acima do peso'
    elif imc >= 30.0 and imc <= 34.9:
        return f'{imc:.2f} Obesidade grau 1'
    elif imc >= 35.0 and imc <= 39.9:
        return f'{imc:.2f} Obesidade grau 2 (severa)'
    else:
        return f'{imc:.2f} Obesidade 3 (mórbida)'



if __name__ == 'main':
    app.run()