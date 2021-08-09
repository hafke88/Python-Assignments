# Parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)



p1 = Person("Erik", 33)
p1.myfunc()













