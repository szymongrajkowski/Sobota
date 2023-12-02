from tkinter import *
from tkinter import ttk

root = Tk ()
root.geometry ("350x170")

# See solution Exercise 65: https://www.my-courses.net/2020/07/solution-exercise-65-greatest-common.html
def gcd ( m , n ):
    d = m
    while ( m%d != 0 or n%d != 0):
        d = d - 1
    return d

# See solution Exercise 66: https://www.my-courses.net/2020/07/solution-exercise-66-least-common.html
def lcm ( m , n ):
    M = m
    while ( M%m != 0 or M%n != 0 ):
        M = M + 1
    return M

def action (event):
    # we get the selected value from the combobox list
    select = comboList.get ()
    
    # retrieve the value of m from the entry input field
    m = int (entry_m.get ())
    # retrieve the value of n from the entry input field
    n = int (entry_n.get ())
    
    if (select == "GCD"):
        lblResult ['text'] = " GCD(m , n)  = " + str (gcd (m, n))
    else:
        lblResult ['text'] = " LCM(m , n)  = " + str (lcm (m, n))
        
# Creation of the label and input field for the integer m
lbl_m = Label (root, text = "Enter value of m:")
entry_m = Entry (root)
lbl_m.place (x = 10, y = 20)
entry_m.place (x = 150, y = 20)

# Creation of the label and input field for the integer n
lbl_n = Label (root, text = "Enter value of n:")
lbl_n.place (x = 10, y = 50)
entry_n = Entry (root)
entry_n.place (x = 150, y = 50)

lblChoose = Label (root, text = "Choose function:")
lblChoose.place (x = 10, y = 80)

# Creation of the combobox list to select GCD or LCM
comboList = ttk.Combobox(root , values = ["GCD" , "LCM"])
comboList.place (x = 150, y = 80, width = 165)
comboList.bind ("<<ComboboxSelected>>", action)

# Create a label that displays the result
lblResult = Label (root, text = "Result:")
lblResult.place (x = 150, y = 110)

root.mainloop ()