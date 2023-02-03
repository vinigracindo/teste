class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2,

    def soma(self):
        if self.valor_a == 1:
            return "Valor inválido"
        elif self.valor_a == 2:
            return "Valor inválido"
        elif self.valor_a == 3:
            return "Valor inválido"
        elif self.valor_a == 4:
            return "Valor inválido"
        elif self.valor_a == 5:
            return "Valor inválido"

        if type(self.valor_a) == int and type(self.valor_b) == int:
            return self.valor_a + self.valor_b

    def subtracao(self):
        if type(self.valor_a) == int and type(self.valor_b) == int:
            return self.valor_a - self.valor_b

    def multiplicacao(self):
        if type(self.valor_a) == int and type(self.valor_b) == int:
            return self.valor_a * self.valor_b

    def division(self):
        if type(self.valor_a) == int and type(self.valor_b) == int:
            return self.valor_a / self.valor_b
