import tkinter as tk

operators = ["+", "-", "*", "/"]

def press(key):
    current = display.get()
    if key == "C":
        display.set("")
    elif key == "⌫":
        display.set(current[:-1])
    elif key == "=":
        try:
            result = eval(display.get())
            display.set(str(result))
        except Exception:
            display.set("Error")
    elif key in operators:
        if current == "" or current == "Error":
            return
        if current[-1] in operators:
            display.set(current[:-1] + key)
        else:
            display.set(current + key)
    else:
        if current == "Error":
            current = ""
        display.set(current + key)

root = tk.Tk()
root.title("Calculator")

display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=("Arial", 24), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, sticky="we")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "⌫",
]

row = 1
col = 0
for b in buttons:
    tk.Button(
        root, text=b, font=("Arial", 18), width=5, height=2,
        command=lambda b=b: press(b)
    ).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    root, text="+", font=("Arial", 18), width=5, height=2,
    command=lambda: press("+")
).grid(row=row, column=0)

tk.Button(
    root, text="=", font=("Arial", 18), width=17, height=2, bg="lightgreen",
    command=lambda: press("=")
).grid(row=row, column=1, columnspan=3)

def key_handler(event):
    if event.char in "0123456789.+-*/":
        press(event.char)
    elif event.keysym == "Return":
        press("=")
    elif event.keysym == "BackSpace":
        press("⌫")
    elif event.keysym == "Escape":
        press("C")

root.bind("<Key>", key_handler)

root.mainloop()
