class Dictionary:
    def __init__(self, current_dict):
        self.current_dict = current_dict

    # @classmethod
    def dict_read(self):
        for self.items in self.current_dict:
            print(self.items, ":", self.current_dict[self.items])


dict1 = {1: "Anubhav", 2: "Bangalore"}

read_dict = Dictionary(dict1)
read_dict.dict_read()