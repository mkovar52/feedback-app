import smtplib
from email.mime.text import MIMEText


def send_mail(customer, order_number, employee, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '16728ec620a1a5'
    password = '80d4fcc8bb61a2'
    message = f"<h3>-- Feedback Review --</h3><ul><li>Customer: {customer}</li><li>Order # {order_number}</li><li>Salesrep: {employee}</li><li>Score: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = "[ NEW ] Feedback Submission"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # -- Send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
