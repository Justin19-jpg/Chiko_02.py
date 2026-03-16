import tkinter as tk

window = tk.Tk()
window.resizable(True,True)
window.configure(bg="Pink")
window.title("Profile Builder")
window.geometry("500x500")

label = tk.Label(window,text="Profile Builder",bg="pink")
label.grid(row=0,column=3,columnspan=3)

label = tk.Label(window,text="",bg="lightgreen")
label.grid()

u_entry = tk.Entry(text="First Name")
u_entry.place(y=50,x=30)

tk.Entry()

u_entry = tk.Entry(text="Last Name")
u_entry.place(y=50,x=90)

tk.Entry()

window.mainloop()

