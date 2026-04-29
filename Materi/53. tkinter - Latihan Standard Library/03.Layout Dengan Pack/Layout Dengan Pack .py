from tkinter import *

window = Tk()
window.geometry("500x500+600+400")
#side : TOP (Default), BOTTOM, LEFT, or RIGHT.
#fill : NONE (Default), X (Fill Horizontally), Y (Fill Vertically), BOTTH.
#expand : YES, NO
#padx, pady, ipadx, ipady (i = internal)

Button1 = Button(text="Button1")
Button1.pack(expand=YES, fill=BOTH, padx=50, pady=50)
window.mainloop()