from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuration - do NOT hardcode passwords!
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ahmadnadeem701065@gmail.com'
app.config['MAIL_PASSWORD'] = 'mylw crjy lvru bnsd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message(
        'Hallo',
        sender=app.config['MAIL_USERNAME'],
        recipients=['ahmadnadeem701065@gmail.com']
    )
    msg.body = 'Hallo, guten Tag. Das ist eine Test-E-Mail.'
    # mail.send(msg)
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
