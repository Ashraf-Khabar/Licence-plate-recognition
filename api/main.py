from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
