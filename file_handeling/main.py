import tkinter as tk
root = tk.Tk()
root.title("Exam")
root.geometry("500x500")

def prnt():
    label = tk.Label(root, text="سلام دنیا", font=("consolas", 20))
    label.pack()

btn = tk.Button(root, text="Click me", command=prnt)
btn.pack()

root.mainloop()
