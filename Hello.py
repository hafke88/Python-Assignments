import tkinter as tk
from tkinter import *


import webbrowser

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Web Page Generator!')
        self.master.config(bg='darkgrey')

        self.varStatement = StringVar()

        self.lblStatement = Label(self.master,text='Statement: ', font=("Helvetica", 16), fg='black', bg='darkgrey')
        self.lblStatement.pack()

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='darkgrey')
        self.lblDisplay.pack()

        self.txtStatement = Entry(self.master,text=self.varStatement, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtStatement.pack()

        self.btnSubmit = Button (self.master, text="Submit", command=self.submit)
        self.btnSubmit.pack()

        
    
           

        htmlText=
        '''<html>
        <body>
        <h1>'''
        +sm+
        '''</h1>         
        </body>
        </html>'''

        f = open("Hello.html", "w")
        f.write(htmlText)
        f.close()

        webbrowser.open("Hello.html", new=0, autoraise=True)

    def submit(self):
        sm = self.txtStatement.get()
        print('htmlText' + 'sm')

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()#this will keep window open until we close it
