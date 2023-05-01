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
    # user_email = request.form['user_email']
    user_email = 'khabarachraf@gmail.com'
    try:
        # Send email to user
        # Construct the message
        msg = MIMEMultipart()
        msg['From'] = 'ashrafkhabaradm@gmail.com'
        msg['To'] = user_email
        msg['Subject'] = 'Email Notification from RADAR.AI : Your vehicule is captured'
        body = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy1Thrge38hDQT9Xb0a1rKGfGgpeI8U27d8xEU" crossorigin="anonymous">
                <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
                <title>Email from RADAR.AI</title>
                            <style>
                body{margin-top:20px;}
                .mail-seccess {
                    text-align: center;
                    background: #fff;
                    border-top: 1px solid #eee;
                }
                .mail-seccess .success-inner {
                    display: inline-block;
                }
                .mail-seccess .success-inner h1 {
                    font-size: 100px;
                    text-shadow: 3px 5px 2px #3333;
                    color: #006DFE;
                    font-weight: 700;
                }
                .mail-seccess .success-inner h1 span {
                    display: block;
                    font-size: 25px;
                    color: #333;
                    font-weight: 600;
                    text-shadow: none;
                    margin-top: 20px;
                }
                .mail-seccess .success-inner p {
                    padding: 20px 15px;
                }
                .mail-seccess .success-inner .btn{
                    color:#fff;
                }
            </style>
            </head>
            <body>
                
                <section class="mail-seccess section">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-6 offset-lg-3 col-12">
                                <!-- Error Inner -->
                                <div class="success-inner">
                                    <h1><i class="fa fa-envelope"></i><span>This is email from RADAR.AI</span></h1>
                                    <p>Thank you for using our service.</p>
                                    <a href="http://localhost:5000/" class="btn btn-primary btn-lg">Go Home</a>
                                </div>
                                <!--/ End Error Inner -->
                            </div>
                        </div>
                    </div>
                </section>
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            </body>
            
        """
        msg.attach(MIMEText(body, 'html'))
        # Connect to the SMTP server and send the message
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = os.getenv('SMTP_PORT')
        smtp_username = os.getenv('SMTP_USERNAME')
        smtp_password = os.getenv('SMTP_PASSWORD')
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, user_email, msg.as_string())
        return jsonify({'status': 'OK'})
    except Exception as e:
        return jsonify({
            'error': e,
            'status': 'Not OK'
        })


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
