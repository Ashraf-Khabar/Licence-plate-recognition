from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_template():
    # Any necessary data processing can be done here
    return render_template('index.html')


app.run()
