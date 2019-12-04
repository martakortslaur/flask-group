import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page"

@app.route("/europe")
def europe():
    return "This is the europe home page"

@app.route("/north-america")
def america():
    return "This is the north american home page"

@app.route("/asia")
def asia():
    return "This is the asian home page"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
