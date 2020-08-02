import os
import shutil
from tkinter import *

root = Tk()
root.title = "Duplicator-Finder"

path=input("enter path")
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


    
