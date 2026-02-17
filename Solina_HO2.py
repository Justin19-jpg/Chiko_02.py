import tkinter as Chiko

window = Chiko.Tk()
window.title("Simple Profile App")
window.geometry("600x600")
window.configure(bg="lightgreen")
window.resizable(False, True)

frame = Chiko.Frame(window, bg="lightgreen", padx=20, pady=20)
frame.pack(anchor="nw")

Chiko.Label(frame,text="PROFILE INFORMATION",font=("Arial", 16, "bold"),bg="lightgreen").pack(anchor="w", pady=15)
Chiko.Label(frame, text="Full Name: Justin Solina", font=("Arial", 12), bg="lightgreen").pack(anchor="w", pady=5)
Chiko.Label(frame, text="Age: 19", font=("Arial", 12), bg="lightgreen").pack(anchor="w", pady=5)
Chiko.Label(frame, text="Course & Section: BSIT - 1C", font=("Arial", 12), bg="lightgreen").pack(anchor="w", pady=5)
Chiko.Label(frame, text="Birthday: October 5, 2006", font=("Arial", 12), bg="lightgreen").pack(anchor="w", pady=5)
Chiko.Label(frame,text='Personal Motto: "Don\'t do it by yourself, do it with God."',font=("Arial", 12),bg="lightgreen",wraplength=550,justify="left").pack(anchor="w", pady=5)

window.mainloop()
