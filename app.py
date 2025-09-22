from flask import Flask, render_template, request

app = Flask(__name__, template_folder='app/views')

@app.route('/index')
def index():
    return render_template('index/index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form.get('peso', 0))
    altura = float(request.form.get('altura', 0))
    imc = None
    if altura > 0:
        imc = peso / (altura ** 2)
    return render_template('resultado/resultado.html', peso=peso, altura=altura, imc=imc)

@app.route('/autor')
def autor():
    return render_template('autor/autor.html')

if __name__ == '__main__':
    app.run(debug=True)
