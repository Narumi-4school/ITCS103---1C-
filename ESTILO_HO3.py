import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x250")

result_label = tk.Label(window, text="Simple Calculator", font=("Times New Roman", 14))
result_label.pack(pady=10)

frame = tk.Frame(window, bg="lightblue", padx=20, pady=20)
frame.pack()

# Number entry request frame 
num_1 = tk.Label(frame, text="Enter 1st Number:")
num_1.grid(row=0, column=0, padx=10, pady=10)

num_2 = tk.Label(frame, text="Enter 2nd Number:")
num_2.grid(row=1, column=0, padx=10, pady=10)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=10)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=10)

# operarion function
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_label.config(text=f"The sum of {num1} and {num2} is {num1+num2}")

def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_label.config(text=f"The subtraction of {num1} and {num2} is {num1-num2}")

def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_label.config(text=f"The multiplication of {num1} and {num2} is {num1*num2}")

def divide():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result_label.config(text=f"The division of {num1} and {num2} is {num1/num2}")

# button commands 
b_add = tk.Button(frame, text="Add", width=10, command=add)
b_add.grid(row=2, column=0, pady=10)

b_sub = tk.Button(frame, text="Subtract", width=10, command=subtract)
b_sub.grid(row=2, column=1, pady=10)

b_mul = tk.Button(frame, text="Multiply", width=10, command=multiply)
b_mul.grid(row=3, column=0, pady=10)

b_div = tk.Button(frame, text="Division", width=10, command=divide)
b_div.grid(row=3, column=1, pady=10)

window.mainloop()