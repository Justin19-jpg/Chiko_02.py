import tkinter as Chiko

window = Chiko.Tk()
window.title("Simple Profile App")
window.geometry("600x600")
window.resizable(False, True)

frame = Chiko.Frame(Chiko, padx=20, pady=20)
frame.pack(anchor="w")

Chiko.Label(frame, text="PROFILE INFORMATION", font=("Arial", 16, "bold")).pack(anchor="w", pady=(0, 15))
Chiko.Label(frame, text="Full Name: Justin Solina", font=("Arial", 12)).pack(anchor="w", pady=5)
Chiko.Label(frame, text="Age: 19", font=("Arial", 12)).pack(anchor="w", pady=5)
Chiko.Label(frame, text="Course & Section: BSIT - 1C", font=("Arial", 12)).pack(anchor="w", pady=5)
Chiko.Label(frame, text="Birthday: October 5, 2006", font=("Arial", 12)).pack(anchor="w", pady=5)
Chiko.Label(frame, text='Personal Motto: "Dont do it by yourself, Do it with God ."',font=("Arial", 12),  wraplength=550, justify="left").pack(anchor="w", pady=5)

window.mainloop()
