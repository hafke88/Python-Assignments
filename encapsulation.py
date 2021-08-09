#Protected Variable
class Protected:
    def __init__(self):
        self.__privateVar = 22

obj = Protected()
obj._protectedVar= 44 #protected. denoted with single underscore
print(obj._protectedVar)








#Private Variable
class Protected:
    def __init__(self):
        self.__privateVar = 22 #private. denoted with double underscore

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(44)#setting a new value for private variable
obj.getPrivate()
