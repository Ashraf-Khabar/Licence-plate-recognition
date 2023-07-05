from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from model import Model

# Loading the file .env in order to use :
load_dotenv()

# Init the Flask API app :
app = Flask(__name__)
img_processor = Model("data/Cars389.png")

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
    

@app.route('/process_license_plate', methods=['POST'])
def process_license_plate():
    # Retrieve the uploaded image from the request
    file = request.files['image']
    # Save the image to a temporary file
    image_path = 'temp_image.jpg'
    file.save(image_path)
    # Process the image using the license plate detection model
    img_processor = Model(image_path)
    license_plate_number = img_processor.get_plate_number()
    # Query the database for a user with the given license plate number
    user = User.query.filter_by(user_licence_plate=license_plate_number).first()
    # Delete the temporary image file
    os.remove(image_path)
    message = []
    if user is None:
        message.append('User not found')
    else:
        message.append(user.user_name)
        message.append(user.user_licence_plate)
        message.append(user.user_city)
        message.append(user.user_mail)
        # Send email to the user
        send_email(user.user_mail, license_plate_number, user.user_city, user.user_name)
    return render_template('index.html', license_plate=license_plate_number, message=message)


def send_email(user_email, license_plate, city, name):
    try:
        # Construct the email message
        msg = MIMEMultipart()
        msg['From'] = 'ashrafkhabaradm@gmail.com'
        msg['To'] = user_email
        msg['Subject'] = 'Email Notification from RADAR.AI: Your vehicle is captured'
        
        # Construct the email body with the user's information
        body = f"""
            <html>
            <head>
                <!-- Add any necessary styles or scripts here -->
            </head>
            <body>
                <h2>License Plate Information:</h2><br>
                <p>License Plate: {license_plate}</p><br>
                <p>City: {city}</p><br>
                <p>Car Type: {name}</p><br>
                <!-- Add any additional user information here -->
            </body>
            </html>
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
        
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)


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
def index():
    return render_template('index.html', license_plate='', message='')


# The main function in order to run the project in the PORT: 5000 and the server localhost .
if __name__ == '__main__':
    # We are activating the debug mode in order to see all the errors, warning on the browser .
    app.run(debug=True)