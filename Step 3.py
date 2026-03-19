import tkinter as tk
import csv, os
from tkinter import messagebox

file = "tasks.csv"
tasks = []

# Load tasks
if os.path.exists(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            tasks.append(row)

# Save all tasks
def save():
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

# Add task
def add():
    data = [e1.get(), e2.get(), e3.get(), e4.get()]
    if "" in data:
        messagebox.showwarning("Warning", "Fill all fields")
    else:
        tasks.append(data)
        save()
        listbox.insert(tk.END, data[0] + " - " + data[2])
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)

# Delete task
def delete():
    try:
        i = listbox.curselection()[0]
        listbox.delete(i)
        tasks.pop(i)
        save()
    except:
        messagebox.showwarning("Warning", "Select task")

# GUI
root = tk.Tk()
root.title("Task Manager")

e1 = tk.Entry(root); e1.pack()
e2 = tk.Entry(root); e2.pack()
e3 = tk.Entry(root); e3.pack()
e4 = tk.Entry(root); e4.pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Delete", command=delete).pack()

listbox = tk.Listbox(root)
listbox.pack()

# Show tasks
for t in tasks:
    listbox.insert(tk.END, t[0] + " - " + t[2])

root.mainloop()