import tkinter as tk
import random as rn
import string

bg_colour = '#3d6465'

root = tk.Tk()
root.title("Generator")
root.eval("tk::PlaceWindow . center")

frame = tk.Frame(root, width=300, height=400, bg='#3d6466')
frame.grid(row=0, column=0, columnspan=4)

#widgets
tk.Label(frame, text="Password Generator",
        bg=bg_colour,
        fg='white',
        font = ("TkMenuFont", 20)
        ).grid(row=0, column=0, columnspan=4)

input = tk.StringVar()
entry = tk.Entry(frame, textvariable=input, fg='white', bg=bg_colour, justify='right', width=45, borderwidth=5)
entry.grid(row=1, column=0, padx=50, pady=10)

output_var = tk.StringVar()

output_label = tk.Label(frame, textvariable=output_var, bg=bg_colour, fg='white', font=("TkMenuFont", 14))
output_label.grid(row=2, column=0, columnspan=4, pady=10)

alphabets = list(string.ascii_letters)
numbers = list(string.digits)
special = ['!', '@', '#', '$', '%', '^', '&', '*']

password_list = [alphabets, numbers, special]

def display():
    n = int(input.get())
    if(n < 15):
        password = ""
        for i in range(0, n):
            password = password + rn.choice(rn.choice(password_list))
        output_var.set(password)
    else:
        output_var.set("Password length must be lessthan 15 characters")

def button_clear():
    input.set('')

button1 = tk.Button(root, text="Generate password", padx=10, pady=10, width=15, height=2, command=display, bg=bg_colour, fg='white')
button1.grid(row=3, column=2, padx=50, pady=10)

button2 = tk.Button(root, text="Clear", padx=10, pady=10, width=15, height=2, command=button_clear, bg=bg_colour, fg='white')
button2.grid(row=3, column=1, padx=50, pady=10)

root.mainloop()