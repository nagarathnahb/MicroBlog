from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ewnder_template('index.html')


