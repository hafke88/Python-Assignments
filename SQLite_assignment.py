import sqlite3
connection = sqlite3.connect("test.db")

c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

connection = sqlite3.connect(':memory') #one-time use database

c.execute("DROPT TABLE IF EXISTS People") #deleting table us drop statement

connection.close()#close connection, frees up any resources currently in memory that are no longer needed

with sqlite3.connect("test.db") as connection:
    #perform any SQL operations using connection here

#running more than one line of SQL code at a time
    import sqlite3
    with sqlite3.connect('test.db') as connection:
        c= connection.cursor()
        c.executescript("""DROP TABLE IF EXISTS People;
                        CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                        INSERT INTO People VALUES('Ron', 'Obvious', '42');
                        """)

    peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

#part 6
import sqlite3

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter you age: "))
personData= (firstName, lastName, age)

#execute insert statement for supplied person data
with sqlite3.connect('test.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

c.execute("UPDATE People SET Age=? Where FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))



#part 7
import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People Values(?, ?, ?)",
                  peopleValues)

#select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print (row)


#part 8

        c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
        while True:
            row = c.fetchone()
            if row is None:
                break
            print(row)



