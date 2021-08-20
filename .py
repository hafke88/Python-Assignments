import tkinter
from tkinter import *
from tkinter import filedialog



#get used to the first three lines
#use as reference in future
#copy and paste
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Folder Browser')
        self.master.config(bg='darkgrey')


















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()#this will keep window open until we close it

