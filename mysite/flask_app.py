
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

bootstrap = Bootstrap(app)