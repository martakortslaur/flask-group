import os
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

#Settings
MONGO_URI = "mongodb+srv://<username>:<h2rtmanng9sse>@cluster0-utrzr.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.first_database
collection = db.movies

@app.route("/")
def home():
    return "<h1>This is the home page</h1><br><p>Bonjour!</p>"

@app.route('playing_around_with_databases')
def playing_around_with_databases():
    return "This is where we will be playing around with databases"






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
        "descr" : "University city"
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
