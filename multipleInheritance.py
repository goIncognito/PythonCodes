# Parent 1
class Father:
    def skills(self):
        print("Programming, Problem Solving")

# Parent 2
class Mother:
    def skills(self):
        print("Cooking, Painting")

# Child inherits from both
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
    

c = Child()
c.skills()
