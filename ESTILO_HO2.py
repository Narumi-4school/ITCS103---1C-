import tkinter as tk 

window = tk.Tk()
window.geometry("400x500")
window.resizable(False,False)
window.configure(bg="lightblue")

label = tk.Label(window,text="Student Profile",      
font=("Arial", 16), fg="Black",     
bg="lightblue",  width=20,height=2,anchor="center")

label.pack(side="top", padx=10, pady=20, fill="x",
expand=False)

studentname = tk.Label(window,text="Name: Dwyane Ashley G. Estilo",
font=("Times New Roman", 10), fg="black",
bg="lightblue", width= 12,height=2,anchor="w") 

studentage = tk.Label(window,text="Age: 19",
font=("Times New Roman", 10), fg="black",
bg="lightblue", width= 12,height=2,anchor="w")

studentcourse = tk.Label(window,text="Course: BSIT",
font=("Times New Roman", 10), fg="black",
bg="lightblue", width= 12,height=2,anchor="w")

studentbirthday = tk.Label(window,text="Birthday: April 27, 2006",
font=("Times New Roman", 10), fg="black",
bg="lightblue", width= 12,height=2,anchor="w")

studentmotto = tk.Label(window,text="Motto: ",
font=("Times New Roman", 10), fg="black",
bg="lightblue", width= 12,height=2,anchor="w")

studentmottoo = tk.Label(window,text="The grass is not always green at the other side",
font=("Times New Roman", 10, "italic"), fg="black",
bg="lightblue", width= 12,height=2,anchor="center")

studentname.pack(padx=10, pady=5, fill="x")
studentage.pack(padx=10,pady=5, fill="x")
studentcourse.pack(padx=10, pady=5, fill="x")
studentbirthday.pack(padx=10, pady=5, fill="x")
studentmotto.pack(padx=10, pady=5, fill="x")
studentmottoo.pack(padx=10, pady=5, fill="x")
                
window.mainloop()