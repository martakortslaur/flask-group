import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the home page</h1><br><p>Bonjour!</p>"

@app.route("/europe")
def europe():
    return render_template("index.html")

@app.route("/estonia")
def estonia():
    city_01 = {
        "name" : "Tallinn",
        "descr" : "Capital"
    }
    city_02 = {
        "name" : "Tartu",
        "descr" : "University"
    }
    cities = [city_01, city_02]
    return render_template("country.html", cities=cities)

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
