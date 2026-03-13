import tkinter as chiko

window = chiko.Tk()
window.title("Sîmplè Càlçülâtèr")
window.configure(bg="skyblue")
window.geometry("500x500")
window.resizable(True ,True)

result_label = chiko.Label(window, text="Simple Calculator ", bg="white")
result_label.grid(row=0, column=0, columnspan=2, pady=10)

chiko.Label(window, text="Enter 1st Number:", bg="White").grid(row=1,column=0, padx=10, pady=10)

chiko.Label(window, text="Enter 2nd Number:", bg="White").grid(row=2, column=0, padx=10, pady=10)

entry1 = chiko.Entry(window)
entry1.grid(row=1, column=1, pady=10)

entry2 = chiko.Entry(window)
entry2.grid(row=2, column=1, pady=10)

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    answer = num1 + num2
    result_label.config(text="The sum " + str(num1) + " + " + str(num2) + " is " + str(answer))

chiko.Button(window, bg="white",text="Add", padx=90, command=add).grid(row=3, column=0, pady=10)


def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    answer = num1 - num2
    result_label.config(text="The difference " + str(num1) + " - " + str(num2) + " is " + str(answer))

chiko.Button(window, bg= "white",text="Subtract", padx=60, command=subtract).grid(row=3, column=1, pady=10)

def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    answer = num1 * num2
    result_label.config(text="The product " + str(num1) + " * " + str(num2) + " is " + str(answer))
    

chiko.Button(window, bg="White",text="Multiply", padx=66, command=multiply).grid(row=4, column=0, pady=10)

def divide():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    answer = num1 / num2 
    result_label.config(text="The quotient " + str(num1) + " / " + str(num2) + " is " + str(answer))

chiko.Button(window, bg="White",text="Divide", padx=76, command=divide).grid(row=4, column=1, pady=10)

window.mainloop()
