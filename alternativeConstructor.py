class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2026 - birth_year)

person = Person
person = person.from_birth_year("Anubhav", 1993)
print(person.name)
print(person.age)