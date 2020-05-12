from random import random


class Point:
    default_color = 'red' # access by Point.default_color and shared across all objects

    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def draw(self):
        print(f"drawing{self.__x} {self.__y}")


    @classmethod
    def zero(cls):
        """
         Class methods are used as factory methods. they can also modify the cls but not the instance(self)
         """
        cls.name="name"
        return cls(0,0)

    @classmethod
    def random(cls):
        return cls(random.randint(-100,100),random.randint(-100,100))


    @staticmethod
    def stat():
        """
        Static methods
        its just a normal function but it can only be called by this class name
        """

        return "I cant access anything in this class.."

    """
    properties
    """

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """
    MAGIC METHODS
    """
    def __str__(self):
        return f"{self.x,self.y}"



if __name__=="__main__":
    #access class attributes
    print(Point.default_color)

    #classmethod
    p=Point.zero()

    #instance method
    p2=Point(1,2)

    print(p2.x)






