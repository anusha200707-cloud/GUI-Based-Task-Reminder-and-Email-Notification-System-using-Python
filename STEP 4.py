from datetime import datetime

def check_deadlines():
    now = datetime.now()

    for task in tasks:
        deadline_str = task[2]  # deadline from CSV
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

        diff = deadline - now

        if 0 <= diff.total_seconds() <= 86400:
            messagebox.showinfo("Reminder", f"{task[0]} is due in 24 hours!")
        
        elif 86400 < diff.total_seconds() <= 172800:
            messagebox.showinfo("Reminder", f"{task[0]} is due in 48 hours!")