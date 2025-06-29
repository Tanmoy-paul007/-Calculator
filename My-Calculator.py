from tkinter import *
# import parser
from math import factorial

root = Tk()
root.title("Tanmoy - Calculator")

i = 0   # Cursor position tracker

# Display input
display = Entry(root, font=("Arial", 50), bg='lightyellow', fg='blue', relief=SUNKEN, bd=10, insertwidth=5, width=10, justify='right')
display.grid(row=1, columnspan=6, sticky=N+E+W+S, padx=5, pady=10)


def get_variables(num):
    global i 
    display.insert(i, str(num))
    i = i+1

def get_operation(operator):
    global i
    display.insert(i, operator)
    i = i + len(operator)

def clear_all():
    global i
    display.delete(0, END)
    i = 0

def undo():
    global i
    current_text = display.get()
    if current_text:
        display.delete(0, END)
        display.insert(0, current_text[:-1])
        i = i-1
    else :
        display.insert(0, "Error")

def calculat():
    global i
    try:
        result = eval(display.get())
        clear_all()
        display.insert(0, result)
        i = i+ len(str(result))
    except:
        clear_all()
        display.insert(0,"Error")

def facto():
    # global i
    try:
        value = int(display.get())
        result = factorial(value)
        clear_all()
        display.insert(0, result)
        # i = i+ len(result)
    except:
        clear_all()
        display.insert(0, "Error")
        

# Connect Calculator to my PC Keybord
def key_event_handler(event):
    key = event.char
    if key in '0123456789.+-*/()':
        get_variables(key)
    elif key == '\r':  # Enter
        calculat()
    elif key == '\x08':  # Backspace 
        undo()

# Bind the keyboard
root.bind("<Key>", key_event_handler)


# Number buttons
Number = [ (1,2,0), (2,2,1), (3,2,2),
          (4,3,0), (5,3,1), (6,3,2),
          (7,4,0), (8,4,1), (9,4,2), (0,5,1)]

for (num , r , c ) in Number:
    Button(root, text=str(num), font=("Arial", 13), height=2, width=6, command=lambda n=num: get_variables(n)) .grid(row=r, column=c, sticky=N+S+E+W, padx=3, pady=3)

# Operator button3

Button(root, text=".",font=("Arial", 13), height=2, width=6, command=lambda: get_variables(".")) .grid(row=5, column=2, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="+",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("+")) .grid(row=2, column=3, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="Pi",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("*3.14")) .grid(row=2, column=4, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="-",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("-")) .grid(row=3, column=3, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="%",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("%")) .grid(row=3, column=4, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="*",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("*")) .grid(row=4, column=3, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="(",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("(")) .grid(row=4, column=4, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text=")",font=("Arial", 13), height=2, width=6, command=lambda: get_operation(")")) .grid(row=4, column=5, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="/",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("/")) .grid(row=5, column=3, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="Exp",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("**")) .grid(row=5, column=4, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="^2",font=("Arial", 13), height=2, width=6, command=lambda: get_operation("**2")) .grid(row=5, column=5, sticky=N+S+E+W, padx=3, pady=3)


# Control buttons

Button(root, text="AC",font=("Arial", 13), height=2, width=6, command=clear_all).grid(row=5, column=0, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="<-",font=("Arial", 13), height=2, width=6, command=undo).grid(row=2, column=5, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="x!",font=("Arial", 13), height=2, width=6, command=facto).grid(row=3, column=5, sticky=N+S+E+W, padx=3, pady=3)
Button(root, text="=",font=("Arial", 13), height=2, width=6, command=calculat).grid(row=6, columnspan=6, sticky=N+S+E+W, padx=3, pady=3)

root.bind("<Key>", key_event_handler) 

root.mainloop()

print (" Done By Tanmoy Paul ! A student of Daffodil international University")