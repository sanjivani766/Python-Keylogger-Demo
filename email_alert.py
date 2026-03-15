import smtplib

def send_alert(message):

    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "your_email@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)

    subject = "Activity Alert"
    body = message

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(sender, receiver, msg)

    server.quit()