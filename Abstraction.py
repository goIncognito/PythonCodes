from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started with key")

    def stop(self):
        print("Car stopped")



class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike has stopped")


if __name__ == "__main__":
    car = Car()
    car.start()
    car.stop()

    bike = Bike()
    bike.start()
    bike.stop()
