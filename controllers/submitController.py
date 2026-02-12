from flask import request, redirect, url_for, flash
from controllers.emailController import send_email
from controllers.qrcodeController import generate_qr_image_path

def submit():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        phone = request.form.get("phone")
        attending = request.form.get("attending")
        guests = request.form.get("guests")
        dietary = request.form.get("dietary")

        print(f"Received RSVP: {first_name} {last_name}, Email: {email}, Phone: {phone}, Attending: {attending}, Guests: {guests}, Dietary Restrictions: {dietary}")

        # ✅ Generate QR Code Image File
        qr_path = generate_qr_image_path(first_name, last_name)

        # ✅ Email Content
        
        if attending == "no":
            email_content = f"""
            <h1>Event RSVP Confirmation</h1>
            <p>Thank you <b>{first_name} {last_name}</b> for your RSVP!</p>

            <p>We're sorry you can't make it. We hope to see you at future events!</p>

            <p>Your details:</p>
            <ul>
                <li>Email: {email}</li>
                <li>Phone: {phone}</li>
                <li>Attending: {attending}</li>
                <li>Guests: {guests}</li>
                <li>Dietary Restrictions: {dietary}</li>
            </ul>

            <p><b>Secret Code:</b> AB111</p>
            """
            send_email(email, "Event RSVP Confirmation", email_content)
        elif attending == "maybe":
            email_content = f"""
            <h1>Event RSVP Confirmation</h1>
            <p>Thank you <b>{first_name} {last_name}</b> for your RSVP!</p>

            <p>We're sorry you are unsure about attending. Please let us know if you can make it closer to the event date.</p>

            <p>Your details:</p>
            <ul>
                <li>Email: {email}</li>
                <li>Phone: {phone}</li>
                <li>Attending: {attending}</li>
                <li>Guests: {guests}</li>
                <li>Dietary Restrictions: {dietary}</li>
            </ul>

            
            """
            send_email(email, "Event RSVP Confirmation", email_content)
        else:
            email_content = f"""
            <h1>Event RSVP Confirmation</h1>
            <p>Thank you <b>{first_name} {last_name}</b> for your RSVP!</p>

            <p>Your event QR code is attached to this email.</p>

            <p>We have received your details:</p>
            <ul>
                <li>Email: {email}</li>
                <li>Phone: {phone}</li>
                <li>Attending: {attending}</li>
                <li>Guests: {guests}</li>
                <li>Dietary Restrictions: {dietary}</li>
            </ul>

            <p><b>Secret Code:</b> AB111</p>
            <p>Show your QR code at the entrance.</p>
            """

            send_email(email, "Event RSVP Confirmation", email_content, qr_path)

        flash(
            f"Thanks {first_name}! Your form was submitted successfully ✅ "
            f"A confirmation email has been sent to {email}.",
            "success"
        )

        return redirect(url_for("home"))
