import random
from tkinter import *
import tkinter as tk
from functools import partial

def password(Mirai,WannaCry):
    Mirai = int(Mirai.get())
    print(Mirai)
    pw = ""
    charact = "AbCdEfGhINbW@#$%^!sdhHY)(<>.j098135246"
    for i in range(Mirai + 1):
        pw += random.choice(charact)
    WannaCry.insert(tk.END , pw)

    return
def _clear():
    WannaCry.delete(0,END)
    Mirai.delete(0,END)
    return

Defcon = Tk()
Defcon.title("Password Gen")
Defcon.geometry("600x400")

Mirai = Entry(Defcon)
Mirai.grid(row = 2 , column = 500)

WannaCry = Entry(Defcon)
WannaCry.grid(row = 45 , column = 500,ipadx = 15)

Label(Defcon,text= "- Enter Length of Desired Password").grid(row=2,column=600)
Label(Defcon,text= "-Generated password").grid(row=45,column=600)

password = partial(password,Mirai,WannaCry)

Button(Defcon,text="Generate",command=password,bg="black",fg="cyan").grid(row=30,column=600)
Button(Defcon,text="Clear",command=_clear,bg="black",fg="cyan").grid(row=30,column=700)

Defcon.mainloop()