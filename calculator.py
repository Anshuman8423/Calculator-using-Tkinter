# calculator.py
import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Main GUI window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.configure(bg="lightgray")

expression = ""
equation = tk.StringVar()

# Entry widget
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), justify="right", bd=10, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=8, height=2, bg="green", fg="white",
                  command=equalpress).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=8, height=2, bg="white",
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=34, height=2, bg="red", fg="white",
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
