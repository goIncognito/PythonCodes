class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self._age = age           # protected
        self.__salary = 50000     # private

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Salary:", self.__salary)


class Employee(Person):
    def show_employee(self):
        print("Name (public):", self.name)
        print("Age (protected):", self._age)

        # This will cause an error if uncommented
        # print(self.__salary)


p = Person("Anubhav", 33)
print(p.name)
print(p._age)
# print(p.__salary)

p.show_details()

e = Employee("Bob", 25)
e.show_employee()
