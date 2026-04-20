from tkinter import * # import semua

window = Tk()
lebar= 500
tinggi= 400
x = 500
y = 100
# window.resizable(0,0)
# window.resizable(False, False)
# untuk mematikan resize

# window.minsize(lebar,tinggi)
# window.maxsize(lebar,tinggi)

window.title("belajar TKInter")
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

newx = int((screenWidth/2) - (lebar/2))
newy = int((screenHeight/2) - (tinggi/2))
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")


window.mainloop()
