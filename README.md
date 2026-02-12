# 🎉 Event Invitation & RSVP System (Flask)

A simple Flask web application for collecting event RSVPs, generating unique QR codes for guests, and sending confirmation emails with QR codes attached using Gmail SMTP.  
Perfect for event check-in, ticketing, and guest verification.

---

## 🚀 Features

- 📋 Event RSVP form (name, email, phone, guests, etc.)
- 📧 Automatic confirmation email via Gmail
- 🔐 Secure environment variables using `.env`
- 🧾 QR Code generation for each guest (with secret code)
- 📎 QR Code sent as email attachment
- 💬 Flash messages for successful submissions
- 🧩 Flask MVC structure (Controllers, Routes, Templates)
- 📁 Static file support (CSS, JS, Images)

---

## 🗂 Project Structure

2152_event_invitation/
│
├── app.py
├── extensions.py
├── .env
├── .gitignore
│
├── controllers/
│ ├── submitController.py
│ ├── emailController.py
│ └── qrcodeController.py
│
├── routes/
│ └── submitRoutes.py
│
├── templates/
│ └── index.html
│
└── static/
├── tooplate-event-invitation.css
├── tooplate-event-scripts.js
└── qrcodes/

yaml
Copy code

---

## ⚙️ Installation

### 1️⃣ Clone Project
```bash
git clone https://github.com/yourusername/2152_event_invitation.git
cd 2152_event_invitation
2️⃣ Create Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install flask flask-mail python-dotenv qrcode pillow
🔐 Environment Variables (.env)
Create a .env file in the project root:

env
Copy code
FLASK_SECRET_KEY=supersecretkey
GMAIL_USER=yourgmail@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
⚠️ Never commit .env to GitHub.

▶️ Run the App
bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000
📧 Gmail Setup
Enable 2-Step Verification on Gmail

Create App Password
👉 https://myaccount.google.com/apppasswords

Use the App Password in .env

🧪 Test Email Sending
Submit the RSVP form on the homepage.

You should receive:

Confirmation email

QR code image attached

🛠 Technologies Used
Python (Flask)

Flask-Mail (SMTP)

QRCode (qrcode + pillow)

HTML, CSS, JavaScript

Gmail SMTP

python-dotenv

📌 Future Improvements
Admin dashboard for RSVPs

QR code scanner & validation endpoint

Save RSVPs to database (SQLite/PostgreSQL)

Ticket PDF generation

WhatsApp confirmation integration

Webhooks for AI automation

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.

📜 License
MIT License

👨‍💻 Author
Built with ❤️ using Flask

yaml
Copy code

---


