from tkinter import *
import tkinter as tk


import Hello

window = tk.Tk()
 
window.title("Hello")
window.minsize(600,400)
 
def submit():
    label.configure(text= 'Hello ' + name.get())
 
    label = tk.Label(window, text = "Enter Text Here")
    label.grid(column = 0, row = 0)
     
     
    name = tk.StringVar()
    nameEntered = tk.Entry(window, width = 15, textvariable = name)
    nameEntered.grid(column = 0, row = 1)
     
     
    button = tk.Button(window, text = "Submit", command = submit)
    button.grid(column= 0, row = 2)
 
    window.mainloop()


#get text from input box and put it in variable
# build your html text with part 1, custom text, part2
# write out the html variable just like you're doing now

