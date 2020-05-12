class Person:
    """
    This is a person class
    """

    staticDefaultClass='NA'
    def __init__(self, name,age):
        self.name = name
        self.age=age

    def talk(self):
        print(f"talking {self.name}")

    def __str__(self):
        return f"{self.name}"
    def __len__(self):
        return self.age
    def __del__(self):
        return f"person with name: {self.name} was deleted"




if __name__=="__main__":
    print("Person.py is being run")
    person = Person(name="naveen", age=12)
    person.talk()
    print(Person.staticDefaultClass)
else:
    print("Person is being imported")


