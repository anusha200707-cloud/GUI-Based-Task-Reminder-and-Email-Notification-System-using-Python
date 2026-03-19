import tkinter as tk
from tkinter import messagebox
import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    name = name_entry.get()
    desc = desc_entry.get()
    deadline = deadline_entry.get()
    email = email_entry.get()

    if name and desc and deadline and email:
        task = {
            "name": name,
            "description": desc,
            "deadline": deadline,
            "email": email
        }

        tasks.append(task)
        save_tasks(tasks)

        task_listbox.insert(tk.END, f"{name} - {deadline}")

        # Clear input fields
        name_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Warning", "All fields are required!")

def check_reminders():
    if tasks:
        messagebox.showinfo("Reminder", "You have tasks pending!")
    else:
        messagebox.showinfo("Reminder", "No tasks available.")

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("400x500")


tk.Label(root, text="Task Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Description").pack()
desc_entry = tk.Entry(root, width=40)
desc_entry.pack(pady=5)

tk.Label(root, text="Deadline (YYYY-MM-DD)").pack()
deadline_entry = tk.Entry(root, width=40)
deadline_entry.pack(pady=5)

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

check_button = tk.Button(root, text="Check Reminders", command=check_reminders)
check_button.pack(pady=5)


task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)
tasks = load_tasks()

for task in tasks:
    task_listbox.insert(tk.END, f"{task['name']} - {task['deadline']}")
    

root.mainloop()