class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calc_instance = Calculator(num1=a, num2=b)

print("Addition Result: ", calc_instance.add())
print("Multiplication Result: ", calc_instance.multiply())
