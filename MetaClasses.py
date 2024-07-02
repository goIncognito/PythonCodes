class Application:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def animal(self):
        return print("Dogs are Animal")
    
    @classmethod
    def mammal(self):
        if self.name == "Dog":
            return "Dog is a mammal"

Application.mammal("Dog")