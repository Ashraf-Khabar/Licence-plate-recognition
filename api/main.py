import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
    return render_template(os.path.join('index.html'))


if __name__ == '__main__':
    app.run(debug=True)
