import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://orm:ormpw@localhost:1521/orcl'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'testing'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


@app.route('/users')
def get_users():
    users = User.query.all()
    user_dicts = [user.__dict__ for user in users]
    for user_dict in user_dicts:
        user_dict.pop('_sa_instance_state')  # remove the '_sa_instance_state' key from the dictionary
    return jsonify(user_dicts)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
