import tkinter as tk
root = tk.Tk()
root.title("samim")
root.geometry("500x500")

num1 = tk.Entry(root)
num2 = tk.Entry(root)
num1.pack()
num2.pack()
resA = tk.Label(root , text="Result", foreground="black")
resA.pack()
def plus():
    res = int(num1.get()) + int(num2.get())
def mines():
    res = int(num1.get()) - int(num2.get())

btn = tk.Button(root , text="+" ,command= plus)
btn2 = tk.Button(root , text="-" ,command= mines)
# equal= tk.Button(root, text="equal", foreground="red",command= results)
btn.pack(), btn2.pack(), #equal.pack()
tk.mainloop()