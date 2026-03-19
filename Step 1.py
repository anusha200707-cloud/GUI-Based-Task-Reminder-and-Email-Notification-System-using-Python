import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to check reminders (basic)
def check_reminders():
    if tasks:
        messagebox.showinfo("Reminder", "You have tasks pending!")
    else:
        messagebox.showinfo("Reminder", "No tasks available.")

# Create main window
root = tk.Tk()
root.title("Task Reminder System")
root.geometry("400x400")

# Input field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Task List Display
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Check Reminder Button
check_button = tk.Button(root, text="Check Reminders", command=check_reminders)
check_button.pack(pady=5)

# Run GUI
root.mainloop()