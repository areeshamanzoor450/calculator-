import tkinter as tk
import math


def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, num ** 2)
    except:
        entry.insert(0, "Error")

def sqrt():
    try:
        num = float(entry.get())
        if num < 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, round(math.sqrt(num), 4))
    except:
        entry.insert(0, "Error")



root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("320x450")
root.resizable(False, False)

entry = tk.Entry(root, width=22, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.pack(pady=15)


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
        if btn == "=":
            tk.Button(frame, text=btn, width=6, height=2, command=calculate).pack(side="left")
        else:
            tk.Button(frame, text=btn, width=6, height=2,
                      command=lambda x=btn: click(x)).pack(side="left")


extra_frame = tk.Frame(root)
extra_frame.pack(pady=10)

tk.Button(extra_frame, text="Clear", width=8, command=clear).grid(row=0, column=0)
tk.Button(extra_frame, text="⌫", width=8, command=backspace).grid(row=0, column=1)
tk.Button(extra_frame, text="x²", width=8, command=square).grid(row=1, column=0)
tk.Button(extra_frame, text="√x", width=8, command=sqrt).grid(row=1, column=1)

root.mainloop()