
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory

import os
import datetime
import shutil


#get used to the first three lines
#use as reference in future
#copy and paste
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 300))
        self.master.title('Check Files!')
        self.master.config(bg='darkgrey')

        #create buttons
        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1, command=self.browse)
        self.btnBrowse.grid(row=1, column=0, padx=(50,50), pady=(30,0), sticky=NE)

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=self.browse1)
        self.btnBrowse1.grid(row=3, column=0, padx=(50,50), pady=(30,0), sticky=NE)

        self.btnCheckForFiles = Button(self.master, text="Check for files...", width=12, height=2, command=self.CheckForFiles)
        self.btnCheckForFiles.grid(row=5, column=0, padx=(50,50), pady=(30,0), sticky=NE)

        self.btnCloseProgram = Button(self.master, text="Close Program", width=12, height=2, command=self.CloseProgram)
        self.btnCloseProgram.grid(row=5, column=2, padx=(50,50), pady=(30,0), sticky=E)

        #create text box
        self.txtBrowse = tk.Entry(self.master)
        self.txtBrowse.grid(row=1, column=0, rowspan=1, columnspan=3, padx=(40,40), pady=(30,0),sticky=N+E)

        self.txtBrowse1 = tk.Entry(self.master)
        self.txtBrowse1.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(40,40), pady=(30,0),sticky=N+E)
        

    #button functions
    def browse(self):
        files = filedialog.askdirectory()
        self.txtBrowse.insert(0, files)
        
    def browse1(self):
        files1 = filedialog.askdirectory()
        self.txtBrowse1.insert(0, files1)


    def CheckForFiles(self):
        #get the text from the entry widget and save it to a variable named source
        source = self.txtBrowse.get()
        destination = self.txtBrowse1.get()
        #gets a list of the files and the source path and saves it to a variable named fileList
        filelist = os.listdir(source)
        #iterates through the list of files 
        for item in filelist:
            #defines the entire path, which includes the path and the file name
            fullpath = source + "/" + item
            # Get last modified date and today's date
            modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(fullpath))
            todaysDate = datetime.datetime.today()

            # calculates the time 24 hours ago and saves it to a variable named modifyDateLimit
            modifyDateLimit = todaysDate - datetime.timedelta(days=1)
            if modifyDate > modifyDateLimit:
                shutil.copy(fullpath, destination)
                
    def CloseProgram(self):
        self.destroy()
        exit()
        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()#this will keep window open until we close it
