class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

#Use the Person class to create an object, and then execute the printname method:

x = Person("Erik", "Hafke")
y = Student("Jay", "Smith")

x.printname()
y.printname()
