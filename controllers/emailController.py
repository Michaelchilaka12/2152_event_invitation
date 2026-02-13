from flask_mail import Message
from controllers.extension import mail

def send_email(to, subject, html_content, attachment_path=None):
    msg = Message(subject, recipients=[to])
    msg.html = html_content

    if attachment_path:
        with open(attachment_path, "rb") as f:
            msg.attach(
                filename="event_qr_code.png",
                content_type="image/png",
                data=f.read()
            )
    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
