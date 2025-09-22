class Resultado:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        if self.altura > 0:
            return self.peso / (self.altura ** 2)
        return None
