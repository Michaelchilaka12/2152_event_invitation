from flask_mail import Message
from controllers.extension import mail
import threading


def _send_async(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print("Async email error:", e)

def send_email(to, subject, html_content, attachment_path=None, app=None):
    msg = Message(subject, recipients=[to])
    msg.html = html_content

    if attachment_path:
        with open(attachment_path, "rb") as f:
            msg.attach(
                filename="event_qr_code.png",
                content_type="image/png",
                data=f.read()
            )
     # Run email in background thread (no blocking)
    if app:
        threading.Thread(target=_send_async, args=(app, msg)).start()
    else:
        try:
            mail.send(msg)
        except Exception as e:
            print("Error sending email:", e)
