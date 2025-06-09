import smtplib
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "" # you can set your database URI here, e.g., 'sqlite:///site.db' or 'postgresql://user:password@localhost/dbname'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


'''mail configuration'''
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmadnadeem701065@gmail.com'
app.config['MAIL_PASSWORD'] = 'mylw crjy lvru bnsd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Define model correctly
# -----------------------
class Newsletter(db.Model):
    email = db.Column(db.String, primary_key=True, nullable=False)

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-increment ID
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=True)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-increment ID
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    

# Ensure tables are created
# -----------------------
with app.app_context():
    db.create_all()


# Routes
# -----------------------
@app.route('/')
def index():
    return "Welcome to the backend Service!"

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    email = data.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    existing = Newsletter.query.filter_by(email=email).first()
    if not existing:
        db.session.add(Newsletter(email=email))
        db.session.commit()

    # Always send confirmation
    try:
        msg = Message(
            'Newsletter Subscription Confirmation',
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = f"Hi {email},\n\nThanks for subscribing to our newsletter! We'll keep you updated on upcoming events and services.\n\nBest regards,\nMuhammad Ahmad Nadeem"
        mail.send(msg)
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

    return jsonify({"message": "Subscribed and confirmation email sent!"}), 201


@app.route('/meeting', methods=['POST'])
def meet():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    date = data.get('date')
    message = data.get('message')

    if not all([name, email, date]):
        return jsonify({"error": "Name, email, and date are required"}), 400

    try:
        date_obj = datetime.fromisoformat(date)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    db.session.add(Meeting(name=name, email=email, date=date_obj, message=message))
    db.session.commit()

    try:
        msg = Message(
            'Meeting Scheduled',
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = (
            f"Hi {name},\n\nYou have successfully scheduled a meeting on {date_obj.strftime('%Y-%m-%d %H:%M:%S')}."
            "\nOur team will contact you soon.\n\nBest regards,\nMuhammad Ahmad Nadeem"
        )
        mail.send(msg)
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

    return jsonify({"message": "Meeting scheduled and email sent!"}), 201


@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([name, email, subject, message]):
        return jsonify({"error": "All fields are required"}), 400

    db.session.add(Contact(name=name, email=email, subject=subject, message=message))
    db.session.commit()

    try:
        msg = Message(
            'Contact Confirmation',
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = (
            f"Hi {name},\n\nThank you for reaching out about \"{subject}\"."
            f"\nWe received your message:\n\n{message}\n\nWe’ll get back to you shortly."
            "\n\nBest regards,\nMuhammad Ahmad Nadeem"
        )
        mail.send(msg)
    except Exception as e:
        return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

    return jsonify({"message": "Message received and confirmation email sent!"}), 201

#Run app
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)