from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

# Configure Flask-Mail
# Your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()  # Receive data from JSON body

    name = data.get('name')
    email = data.get('email')
    message_body = data.get('message')

    # Create the email
    msg = Message(subject="Contact Form Submission",
                  sender=os.getenv('MAIL_USERNAME'),
                  recipients=['yunisnur30@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message_body}"

    # Send the email

    try:
        mail.send(msg)
        return jsonify({"status": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"status": f"Failed to send email: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)