from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Loading the file .env in order to use :
load_dotenv()

# Init the Flask API app :
app = Flask(__name__)

# Configure the ORM with the connection string for ORACLE DB .
# The connection parameters are loaded by the .env file .
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
connection_string = f"oracle+cx_oracle://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

# Running the ORM :
db = SQLAlchemy(app)


# Define the model named 'user' in order to fetch data from the database .
# The model 'user' inherits from a base class named 'db.Model' to access to the methods and functions in db.Model .
class User(db.Model):
    __tablename__ = 'users'
    # define the column fields :
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_mail = db.Column(db.String(50))
    user_licence_plate = db.Column(db.String(50))
    user_city = db.Column(db.String(50))
    user_car_type = db.Column(db.String(50))


# The POST API in order to send mails to user :
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


# The get API in order to render a template named 'users.html' .
# The 'users.html' contains all the users and their fields .
@app.route('/users')
def get_users():
    # Fetch all the users from the database using the function 'all' .
    users = User.query.all()
    # return the 'users.html' with the parameter 'users' .
    # We have access to all parameters from the database : user_id, user_name, user_mail ...
    return render_template('users.html', users=users)


# The get API in order to render a template named 'index.html' .
# The index field .
@app.route('/')
def home():
    return render_template('index.html')


# The main function in order to run the project in the PORT: 5000 and the server localhost .
if __name__ == '__main__':
    # We are activating the debug mode in order to see all the errors, warning on the browser .
    app.run(debug=True)
