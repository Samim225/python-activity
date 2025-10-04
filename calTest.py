import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")
num1 = tk.Entry(root)
num2 = tk.Entry(root)
num1.pack()
num2.pack()
resultArea = tk.Label(root, text="Result: ", foreground="red", font=("consolas", 40))
resultArea.pack()
def sumNumbers():
    results = int(num1.get()) + int(num2.get())
    resultArea.config(text=f"{results}")
def minNumbers():
    results = int(num1.get()) - int(num2.get())
    resultArea.config(text=f"Result is: {results}")
def divNumbers():
    results = int(num1.get()) / int(num2.get())
    resultArea.config(text=f"Result is: {results}")
def multNumbers():
    results = int(num1.get()) * int(num2.get())
    resultArea.config(text=f"Result is: {results}")
btn = tk.Button(root, text="+", command=sumNumbers, bg="green" )
btn2 = tk.Button(root, text="–", command=minNumbers, bg="green" )
btn3 = tk.Button(root, text="×", command=multNumbers, bg="green" )
btn4 = tk.Button(root, text="÷", command=divNumbers, bg="green" )


btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()

root.mainloop()