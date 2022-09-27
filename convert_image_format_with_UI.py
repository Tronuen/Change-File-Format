from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image
from os import listdir as ld
import os


get_from_folder = os.environ['HOMEPATH'] + '\Desktop\convert\\'
put_to_folder = os.environ['HOMEPATH'] + '\Desktop\converted\\'


def convert_all(to_ext, mode):
    for file in ld(get_from_folder):
        x, from_ext = os.path.splitext(file)
        im = Image.open(get_from_folder + file).convert("RGB")
        im.save(put_to_folder + file.replace(from_ext, to_ext), mode)

def convert_fonk():
    from_ext = "." + cb1.get()
    to_ext = "." + cb2.get()
    
    mode = to_ext[1:]
    if to_ext==".jpg":
        mode = "jpeg"
        
    if from_ext==".all":
        convert_all(to_ext, mode)
        return
    
    files = [file for file in ld(get_from_folder) if file.endswith(from_ext)]

    for file in files:
        im = Image.open(get_from_folder + file).convert("RGB")
        im.save(put_to_folder + file.replace(from_ext, to_ext), mode)
        

window = Tk()
window.title("Change File Format")

window.geometry("450x250+500+200")
window.resizable(False, False)

title = Label(text = "Change Machine", fg = "#08cfdd", font = ("Times", "20", "bold"))
title.place(x = 130, y = 10)

txt1 = Label(text = "From", fg = "#08cfdd", bg = "white", font = ("Open Sans", "13", "bold"))
txt1.place(x = 70, y = 70)

extensions = ['all', 'jpg', 'jpeg', 'png', 'webp']
var1 = StringVar()
var1.set("all")
cb1 = Combobox(master = window, textvariable = var1, values = extensions)
cb1.place(x=130, y=70, width=70, height=30)

txt2 = Label(text = "To", fg = "#08cfdd", bg = "white", font = ("Open Sans", "13", "bold"))
txt2.place(x = 260, y = 70)

var2 = StringVar()
var2.set("jpg")
cb2 = Combobox(master = window, textvariable = var2, values = extensions[1:])
cb2.place(x=300, y=70, width=70, height=30)

buton_cnvrt = Button(text = "Convert", activeforeground = "white", activebackground = "#7fd6db", command = convert_fonk)
buton_cnvrt.place(x = 180, y = 150, width = 100, height = 50)


mainloop()