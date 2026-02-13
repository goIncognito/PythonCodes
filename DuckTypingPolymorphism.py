class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Cash:
    def pay(self, amount):
        print(f"Paid {amount} in cash")

def make_payment(payment_method, amount):
    payment_method.pay(amount)


make_payment(CreditCard(), 500)
make_payment(UPI(), 300)
make_payment(Cash(), 100)
