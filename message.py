from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200")

w = Label(root, text='Sobota', font="10")
w.pack()

messagebox.showinfo("showinfo", "Sobota")

root.mainloop()

