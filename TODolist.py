from tkinter import *
root = Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("To-Do List")

label0 = Label(root, text="To-Do List", font=("Arial", 24))
label0.pack()

task = Entry()
tasks = []

def add_task():
    new_task = task.get().strip()
    if new_task == "":
        label0.config(text="Please enter a task", foreground="#FF0000")
    elif new_task in tasks:
        label0.config(text="Task already exists!", foreground="#FF0000")
    else:
        tasks.append(new_task)
        global label
        label = Label(root, text=f"Task is: {new_task}", font=("consolas", 10))
        print(tasks)
        label0.config(text="To-Do List", foreground="#000000")
        label.pack()
    task.delete(0, END)  # پاک کردن بعد از اضافه شدن یا پیام
def rem_task():
    tasks.pop(0)
    label.destroy()
button = Button(root, text="add" , command=add_task)
button2 = Button(root, text="del" , command=rem_task)
button2.pack()
button.pack()
task.pack()

root.mainloop()
