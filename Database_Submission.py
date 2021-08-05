
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_files TEXT \
        )")
    conn.commit()
conn.close()




conn = sqlite3.connect('test.db')

#file list to add to database

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop throughe each file in list to find the files that end with '.txt'

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_data (col_files) VALUES (?)", (x,))
            print(x)

conn.close()


