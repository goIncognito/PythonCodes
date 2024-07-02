class Arithmatic:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

class Calc(Arithmatic):
    def divide(self):
        return self.a / self.b

calculator = Calc(4, 5)
print(calculator.addition())
print(calculator.multiply())
print(calculator.divide())
        