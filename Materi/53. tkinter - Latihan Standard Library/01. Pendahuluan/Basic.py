import tkinter as tk

# Membuat main Window
root = tk.Tk()

# Memberi judul
root.title("Aplikasi pertamaku")

# Memberikan Ukuran
root.geometry("300x200")

label = tk.Label(root, text="Hello Tkinter!")
label.place(x = 110, y= 40)

label = tk.Button(root, text="Click Me!", command = lambda: label.config(text="Kamu menekan ini!!"))
label.place(x = 110, y= 80)

root.mainloop()