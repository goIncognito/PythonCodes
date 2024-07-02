class Arithmatic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b


class subtract(Arithmatic):
    @staticmethod
    def difference(a=8, b=4):
        return a - b


class Calc(subtract):
    def divide(self):
        return self.a / self.b


calculator = Calc(4, 5)
print(calculator.addition())
print(calculator.multiply())
print(calculator.divide())
print(calculator.difference())
        