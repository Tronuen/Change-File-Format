from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image
from os import listdir as ld

def test():
    from_ext = data1.get()
    to_ext = data2.get()
    mode = to_ext[1:]
    if to_ext==".jpg":
        mode = "jpeg"
        
    print(from_ext, to_ext, mode)

def convert_fonk():
    get_from_folder = 'C:/Users/<UserName>/Desktop/convert/'
    put_to_folder = 'C:/Users/<UserName>/Desktop/converted/'
    
    from_ext = data1.get()
    to_ext = data2.get()
    mode = to_ext[1:]
    if to_ext==".jpg":
        mode = "jpeg"
    
    files = [file for file in ld(get_from_folder) if file.endswith(from_ext)]

    for file in files:
        im = Image.open(get_from_folder+file).convert("RGB")
        im.save(put_to_folder+file.replace(from_ext, to_ext), mode)

window = Tk()
window.title("Change File Format")

window.geometry("450x250+500+200")
window.resizable(False, False)

title = Label(text ="Change Machine", fg="#08cfdd", font = ("Times", "20", "bold"))
title.place(x = 130, y = 10)

txt1 = Label(text="From", fg="#08cfdd", bg="white", font=("Open Sans", "13", "bold"))
txt1.place(x=70, y=70)
data1 = Entry(bd=2, font=("Times", "14", "normal"))
data1.place(x=130, y=70, width=70, height=30)

txt2 = Label(text="To", fg="#08cfdd", bg="white", font=("Open Sans", "13", "bold"))
txt2.place(x=260, y=70)
data2 = Entry(bd=2, font=("Times", "14", "normal"))
data2.place(x=300, y=70, width=70, height=30)

buton_cnvrt = Button(text="Convert", activeforeground="white", activebackground="#7fd6db", command=convert_fonk)
buton_cnvrt.place(x = 180, y = 150, width=100, height=50)


mainloop()