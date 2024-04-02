class Application:
    def __init__(self, Name):
        self.Name = Name

    @staticmethod
    def animal(self):
        return print("Dogs are Animal")
    
    @classmethod
    def mammal(self):
        if self.Name == "Dog":
            return "Dog is a mammal"

Application.mammal("Dog")