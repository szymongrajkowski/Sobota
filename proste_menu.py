from tkinter import *
from tkinter import messagebox

class MenuBar(Menu):
    def __init__(self, ws):
        Menu.__init__(self, ws)

        file = Menu(self, tearoff=False)
        file.add_command(label="Nowy")
        file.add_command(label="Nowe okno")
        file.add_command(label="Otwórz")
        file.add_command(label="Zapisz")
        self.add_cascade(label="Plik",underline=0, menu=file)
        





    def exit(self):
        self.exit

    def about(self):
            messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')


class MenuDemo(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    ws=MenuDemo()
    ws.title('Python Guides')
    ws.geometry('300x200')
    ws.mainloop()
