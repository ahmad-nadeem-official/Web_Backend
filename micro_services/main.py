import smtplib
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://neondb_owner:npg_gUZdJnv5DWz7@ep-purple-leaf-a4rxbe21-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

def send_thank_you_email(to_email):
    from_email = "ahmadnadeem701065@gmail.com"
    password = "*******************"  # Replace with your actual password

    subject = "Thanks for Subscribing!"
    body = f"Hi {to_email}!\n\nThanks for subscribing to our newsletter. Stay tuned for updates!\n\n- Ahmad Nadeem"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())


# Define model correctly
class Newsletter(db.Model):
    email = db.Column(db.String, primary_key=True, nullable=False)

# Ensure tables are created
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to the Newsletter Service!"

# Define route correctly
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    email = data.get('email')

    existing = Newsletter.query.filter_by(email=email).first()
    if not existing:
       new_subscriber = Newsletter(email=data['email'])
       db.session.add(new_subscriber)
       db.session.commit()
       return jsonify({"message": "Subscribed successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
