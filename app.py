import os
from flask import Flask, render_template
from flask_mail import Mail
from dotenv import load_dotenv
from routes.submitRoutes import submitRoutes_blueprint
from controllers.extension import mail


load_dotenv()  # Load environment variables from .env file
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# ✅ Gmail SMTP Config
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("GMAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_APP_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("GMAIL_USER")

mail.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

# ✅ Register Blueprint
app.register_blueprint(submitRoutes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
