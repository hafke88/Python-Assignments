import sqlite3

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter you age: "))

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People Values ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)

    
