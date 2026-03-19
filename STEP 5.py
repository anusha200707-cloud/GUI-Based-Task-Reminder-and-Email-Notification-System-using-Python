import smtplib
from email.mime.text import MIMEText

def send_email(to_email, task_name):
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password"

    subject = "Task Reminder"
    body = f'Your task "{task_name}" is due soon. Please complete it on time.'

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
    except:
        print("Email failed")