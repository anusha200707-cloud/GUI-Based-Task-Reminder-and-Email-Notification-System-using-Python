import tkinter as tk
from tkinter import messagebox
import csv, os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

FILE = "tasks.csv"
tasks = []

# ---------------- FILE HANDLING ----------------

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    tasks.append(row)

def save_tasks():
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

# ---------------- EMAIL ----------------

def send_email(to_email, task_name):
    sender = "your_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText(f'Your task "{task_name}" is due soon.')
    msg["Subject"] = "Task Reminder"
    msg["From"] = sender
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
    except:
        print("Email failed")

# ---------------- FUNCTIONS ----------------

def add_task():
    data = [e1.get(), e2.get(), e3.get(), e4.get()]
    if "" in data:
        messagebox.showwarning("Warning", "Fill all fields")
    else:
        tasks.append(data)
        save_tasks()
        listbox.insert(tk.END, data[0] + " - " + data[2])
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)

def delete_task():
    try:
        i = listbox.curselection()[0]
        listbox.delete(i)
        tasks.pop(i)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select task")

def check_deadlines():
    now = datetime.now()
    for task in tasks:
        deadline = datetime.strptime(task[2], "%Y-%m-%d")
        diff = (deadline - now).total_seconds()

        if 0 <= diff <= 86400:
            messagebox.showinfo("Reminder", f"{task[0]} due in 24 hrs")
            send_email(task[3], task[0])

        elif 86400 < diff <= 172800:
            messagebox.showinfo("Reminder", f"{task[0]} due in 48 hrs")

# ---------------- AUTOMATION ----------------

def auto_check():
    check_deadlines()
    root.after(60000, auto_check)  # every 60 sec

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("400x550")

e1 = tk.Entry(root); e1.pack(pady=5)  # Name
e2 = tk.Entry(root); e2.pack(pady=5)  # Description
e3 = tk.Entry(root); e3.pack(pady=5)  # Deadline YYYY-MM-DD
e4 = tk.Entry(root); e4.pack(pady=5)  # Email

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Check Now", command=check_deadlines).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Load existing tasks
load_tasks()
for t in tasks:
    listbox.insert(tk.END, t[0] + " - " + t[2])

# Start automation
auto_check()

root.mainloop()