from tkinter import *

window = Tk()
def eventButton(event):
    # print(event)
    # print(event.x) # mengambil lokasi X nya saja
    print(event) # mengambil lokasi y nya saja
    
# window.bind("<Button>", eventButton)
window.bind("<Key> ", eventButton) # untuk tombol keybaord
window.mainloop()