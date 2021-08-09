
#Parent Class User
class User:
    name = "Erik"
    email = "hafke88@gmail.com"
    password = "KillBill69"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter you email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 50.00
    department = "Silky Smooth"
    pin_number = "0528"

    #Same method as parent class "User"
    #Difference is we're using pin instead of password to login

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter you email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")


#Second Child Class Assistant
class Assistant(User):
    base_pay = 40.00
    department = "Silky Smooth"
    id_number = "6660"

   #Same method as parent class "User"
    #Difference is we're using id instead of password to login

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter you email: ")
        entry_id = input("Enter your id: ")
        if (entry_email == self.email and entry_id == self.id_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.") 

    
#The following code invokes the methods inside each class User, Employee, and As

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

assistant = Assistant()
assistant.getLoginInfo()
