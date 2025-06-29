from tkinter import *
from math import factorial

root = Tk()
root.title('Tkinter Calculator')

i = 0  # Cursor position tracker

# Display input
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

def get_variables(num):
    global i
    display.insert(i, str(num))
    i += 1

def get_operation(operator):
    global i
    display.insert(i, operator)
    i += len(operator)

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
        i -= 1
    else:
        display.insert(0, "Error")

def calculate():
    global i
    try:
        result = eval(display.get())
        clear_all()
        display.insert(0, result)
        i = len(str(result))
    except:
        clear_all()
        display.insert(0, "Error")

def fact():
    try:
        value = int(display.get())
        result = factorial(value)
        clear_all()
        display.insert(0, result)
    except:
        clear_all()
        display.insert(0, "Error")

# Number buttons
numbers = [ (1,2,0), (2,2,1), (3,2,2),
            (4,3,0), (5,3,1), (6,3,2),
            (7,4,0), (8,4,1), (9,4,2), (0,5,1) ]
for (num, r, c) in numbers:
    Button(root, text=str(num), command=lambda n=num: get_variables(n)).grid(row=r, column=c, sticky=N+S+E+W)

# Operator buttons
Button(root, text=".", command=lambda: get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)
Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N+S+E+W)
Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky=N+S+E+W)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N+S+E+W)

# Control buttons
Button(root, text="AC", command=clear_all).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text="<-", command=undo).grid(row=2, column=5, sticky=N+S+E+W)
Button(root, text="x!", command=fact).grid(row=3, column=5, sticky=N+S+E+W)
Button(root, text="=", command=calculate).grid(row=6, columnspan=6, sticky=N+S+E+W)

root.mainloop()
