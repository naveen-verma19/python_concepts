class Person:
    def __init__(self, name,age):
        self.name = name
        self.age=age

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age

    def __hash__(self):
        return hash(self.name+str(self.age))
    def __str__(self):  #used while printing this object alone
        return self.name+str(self.age)
    def __repr__(self):  #used while printing iterable of objects
        return self.__str__()
    def __lt__(self, other):  #used for sorting
        return self.age<other.age

p=Person('nav',12)
p2=Person('nav',25)
p3=Person('nav',12)
print(p==p2)
print(p!=p2)

persons=set()
persons.add(p) #error unhashable object
persons.add(p2)

print(persons)
#note that when you override equals you have to make sure that equal object also have equal hash values..
#because if two people having same name are equal(irrespective of age) then while hashing nav12 and nav25 should
#treated equals in a set


li=[p,p2,p3,p2,Person('',2),Person('',9)]
li.sort()
print(li)






#


