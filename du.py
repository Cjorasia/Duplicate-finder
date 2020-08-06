import os
import shutil
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title = "Duplicator-Finder"


                            # EXIT FUNCTION #
#=========================================================================================================================#
def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes':
       root.destroy()

    else:
        messagebox.showinfo('Return','You will now return to the application screen')
#=========================================================================================================================#

# exit button
ext = Button (root, text='Exit',command=ExitApplication,bg='brown',fg='white')
ext.pack()


# enter word Label
lbl = Label(root, text = "Enter path here")
lbl.pack(side = LEFT)

# Word Input
ent = Entry(root, bd = 5, textvariable = word)
ent.pack(side = RIGHT)
ent.focus()


path = input("enter path")

unique = dict()

if(os.path.exists(path)==False):
    print("Error: path not found")

for path,folders,files in os.walk(path):
    for filename in files:
        if filename not in unique:
            unique[filename] = filename
        else:
            print(filename + ' is a duplicate of ' + unique[filename])
            file_path = os.path.join(path, filename)
            print(file_path)
            source= file_path
            destination='Documents'
            print(path)
            shutil.move(source,destination)

root.mainloop()
    
