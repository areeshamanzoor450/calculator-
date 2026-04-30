import tkinter as tk
import math

# Function for button click
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Square
def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, num ** 2)
    except:
        entry.insert(0, "Error")

# Square Root
def sqrt():
    try:
        num = float(entry.get())
        if num < 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, math.sqrt(num))
    except:
        entry.insert(0, "Error")

# GUI Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=25, font=("Arial", 16))
entry.pack(pady=10)

# Buttons
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        action = lambda x=btn: calculate() if x=='=' else click(x)
        tk.Button(frame, text=btn, width=5, height=2, command=action).pack(side="left")

# Extra buttons
tk.Button(root, text="Clear", command=clear).pack(pady=5)
tk.Button(root, text="x²", command=square).pack(pady=5)
tk.Button(root, text="√x", command=sqrt).pack(pady=5)

root.mainloop()