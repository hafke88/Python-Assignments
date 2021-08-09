from abc import ABC, abstractmethod
class scotchwhiskey(ABC):
    def paySlip(self,amount):
        print("Your purchase amount: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(scotchwhiskey):
    def payment(self,amount):
        print('You just bought a {} bottle of Scotch\nThat is one expensive bottle of Scotch!'.format(amount))

obj = CreditCardPayment()
obj.paySlip("$550")
obj.payment("$550")
