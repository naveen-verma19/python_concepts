class Person:

    def __init__(self, name,age):
        self.__name = name #mangling for private
        self.__age=age    #cant touch them
        self._donttouchit=2 #warned to user to not use them.. but still accessible

    def __str__(self):    #MAGIC properties or dunder properties
        return f"{self.__name}"

p=Person("name",12)

# print(p.__name) #error

#hack to access private
print(p._Person__name)

print(p._donttouchit)

print(dir(Person))
"""
Mangling format
(atleast 2 _ here) abcd (at most 1 here)

__a
__a_
___a
___a_

"""