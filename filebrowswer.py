import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Web Page Generator!')
        self.master.config(bg='darkgrey')

        
        self.lblStatement = Label(self.master,text='Click "Destination" to view daily files \nClick "Home" to view modified files \nClick "File Check" to intiate file check', font=("Helvetica", 16), fg='black', bg='darkgrey')
        self.lblStatement.pack()

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='darkgrey')
        self.lblDisplay.pack()

        self.btnBrowseOne = Button (self.master, text="Browse...", command=self.get_daily)
        self.btnDestination.pack()

        self.btnBrowseTwo = Button (self.master, text="Browse...", command=self.get_copied)
        self.btnHome.pack()

        self.btnCheckforFiles = Button (self.master, text="Check for files...", command=self.get_files)
        self.btnFileCheck.pack()

        self.btnCloseProgram = Button (self.master, text="Close Program", command=self.get_close)
        self.btnFileCheck.pack() 

    
  
    def get_daily(self):
        print("hello")
##        sm = self.txtStatement.get()
   

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()#this will keep window open until we close it
        
        
