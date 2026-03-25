import tkinter as tk 



window = tk.Tk()
window.geometry("650x300")
window.resizable(False,False)
window.title("Register and Log In System")

title1 = tk.Label(window, text="Welcome!", font=("Arial", 20, "bold"))
title1.pack(pady=5)

def open_reg():
    reg_win = tk.Toplevel()
    reg_win.title("Register Window")
    reg_win.geometry("450x300")
    reg_win.config(bg="green")
    reg_win.resizable(False,False)

    label1 = tk.Label(reg_win, text="Register Here:", font=("Arial", 15, "bold"), fg="white" , bg="green")
    label1.grid(row=0, column=0, padx=5, pady=10 )

    

    username = tk.Label(reg_win, text="Username:", font=("Arial", 12), bg="green" )
    password = tk.Label(reg_win, text="Password:", font=("Arial, 13"), bg="green")
     
    username.grid(row=1, column=0, pady=10)
    password.grid(row=2, column=0, pady=10)


    user_ent = tk.Entry(reg_win)
    pass_ent = tk.Entry(reg_win, show="*")

    user_ent.grid(row=1, column=1,columnspan=3, pady=5)
    pass_ent.grid(row=2, column=1, columnspan=5, pady=5)

    shw_pass_var = tk.IntVar()
    shw_pass = tk.Checkbutton(reg_win, text="Show Password", variable=shw_pass_var)
    shw_pass.grid(row=3, column=3)

    sb_btn = tk.Button(reg_win, text="Submit", relief="raised", bg="green", font=(10))
    sb_btn.grid(row=5, column=3, pady=10)



reg_btn = tk.Button(window, text="Register", bg="blue", height="4" , font=("Arial", 14, "bold"), state="normal", command=open_reg, relief="raised")
reg_btn.pack(fill="x")

log_btn = tk.Button(window, text="Log In", bg="green", height="4" , font=("Arial", 14, "bold"), state="normal", relief="raised")
log_btn.pack(fill="x", pady=10)




window.mainloop()
