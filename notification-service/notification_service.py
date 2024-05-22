from flask import Flask, jsonify, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(recipient, subject, body):
    sender = 'your_email@example.com'
    password = 'your_email_password'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    
    if not recipient or not subject or not body:
        return jsonify({'error': 'Recipient, subject and body are required'}), 400
    
    success = send_email(recipient, subject, body)
    
    if success:
        return jsonify({'message': 'Notification sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send notification'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
