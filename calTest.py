import tkinter as tk
root = tk.Tk()

root.title("samim")
root.geometry("400x500")

label = tk.Label(root, text="CALCULATOR", foreground="#000000", background="#2f4303")
label.pack()
num1 = tk.Entry()
operator = tk.Entry()
num2 = tk.Entry()

res = tk.Label(root, text="CALCULATOR", foreground="#000000")
res.pack()
num1.pack()
operator.pack()
num2.pack()

def re():
   
        # operator == "÷"
        result = int(num1.get()) + int(num2.get())
        res.config(result)
        print(result)
   
btn = tk.Button(root, text="equal", command=re)
btn.pack()

root.mainloop()