from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Init the Flask API app :
app = Flask(__name__)

# Configure the ORM with the connection string for ORACLE DB :
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://radar:radarpw@localhost:1521/orcl'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_mail = db.Column(db.String(50))
    user_licence_plate = db.Column(db.String(50))
    user_city = db.Column(db.String(50))
    user_car_type = db.Column(db.String(50))


@app.route('/send_email', methods=['POST'])
def send_email():
    user_email = request.form['user_email']
    try:
        # Send email to user
        # Construct the message
        msg = MIMEMultipart()
        msg['From'] = 'ashrafkhabaradm@gmail.com'
        msg['To'] = 'khabarachraf@gmail.com'
        msg['Subject'] = 'Test Email'
        message = 'Hello, this is a test email!'
        msg.attach(MIMEText(message))
        # Connect to the SMTP server and send the message
        smtp_server = 'gmail'
        smtp_port = 587
        smtp_username = 'ashrafkhabaradm@gmail.com'
        smtp_password = 'reygamjexgfarxfm'
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, user_email, msg.as_string())
        return jsonify({'status': 'OK'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'Not OK'})


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
