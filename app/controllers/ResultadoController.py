from flask import Blueprint, render_template, request
from app.models.Resultado import Resultado

resultado_bp = Blueprint('resultado', __name__)

@resultado_bp.route('/')
def enunciado():
    return render_template('index/index.html')

@resultado_bp.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form.get('peso', 0))
    altura = float(request.form.get('altura', 0))
    resultado = Resultado(peso, altura)
    imc = resultado.calcular_imc()
    return render_template('resultado/resultado.html', peso=peso, altura=altura, imc=imc)
