from abc import ABC, abstractmethod

class Animal(ABC):  #abstract class (cannot be instantiated due to @abstractmethod method)
    def __init__(self):
        print("Animal constructor")
    def eat(self):  #instance method
        print("animal eating")
    def who_am_i(self):
        print("I am an animal")

    @abstractmethod
    def breed(self):  #abstract method
        pass

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name=name
        print("Dog's constructor")

    def who_am_i(self):   #method overriding
        super().who_am_i()  #super
        print("Its a Dog")

    def breed(self):  #overriding abstract method
        pass

class Cat(Animal):
    def __init__(self,name):
        self.name=name
        Animal.__init__(self)       #have to call super constructor
        print("Cats constructor")

    def breed(self):  #overriding abstract method
        print(self.name)


d= Dog("r")
d.eat()
c=Cat("c")
c.eat()
