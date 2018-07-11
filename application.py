import os
import requests, json

from flask import Flask, session, render_template, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#this is OK!
@app.route("/")
def index():
    return render_template('login.html')



@app.route("/register")
def registration ():
    return render_template('registration.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/on_submit", methods=["POST"])
def on_submit ():
    username = request.form.get("username")
    password = request.form.get("password")

    db.execute("INSERT INTO user_login (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})
    db.commit()
    #db.execute("INSERT INTO check_in(username) VALUES(:username)", {"username":username})
    #db.commit()
    return render_template('login.html')

@app.route("/logged_in", methods=["POST"])
def logged_in ():
    username = request.form.get("username")
    password = request.form.get("password")
    if db.execute("SELECT * FROM user_login WHERE username = :username AND password = :password", {"username": username, "password": password}).rowcount == 0:
        return render_template('error.html', message="Incorrect username and/or password. Try logging in again.")
    else:
        session['user'] = username
        return render_template('main.html')

@app.route("/search_location", methods=["POST"])
def search_location():
    location_search = request.form.get("location")
    # Change the search for location to upper case since that's how it is in the database
    location_search = location_search.upper()
    # I couldn't get the syntax for a LIKE search to work, though I tried a lot of different iterations on %x% with the variable in the middle to no success.
    # Any feedback on how to do one (I left my final example below) would be appreciated!
   # location_result = db.execute("SELECT id, zipcode, city, state FROM zip_data WHERE zipcode LIKE '%'+:location_search+'%' OR city LIKE '%'+:location_search+'%' OR state LIKE '%'+:location_search+'%'", {"location_search":location_search}).fetchall()
    location_result = db.execute("SELECT id, zipcode, city, state FROM zip_data WHERE city=:location_search",{"location_search":location_search}).fetchall()
    return render_template('search_location.html',location_result=location_result)

@app.route("/search_location/<int:location_id>")
def location(location_id):
    """Lists details about a single location."""

    # Make sure location exists.
    location_info = db.execute("SELECT * FROM zip_data WHERE id = :id", {"id": location_id}).fetchone()
    if location is None:
        return render_template("error.html", message="No such location exists")

    comments = db.execute("SELECT comment FROM location_comments WHERE ref_id = :id", {"id":location_id}).fetchall()
    weather = requests.get(f"https://api.darksky.net/forecast/55d231cd30289abbca6266f1bdb90dc0/{location_info.latitude},{location_info.longitude}")
    weather_json = weather.json()

    if db.execute("SELECT * FROM location_comments WHERE username=:username AND ref_id=:location_id", {"username":session['user'], "location_id":location_id}).rowcount == 0:
        return render_template("location_info.html",location_info=location_info,comments=comments,weather_json=weather_json)
    else:
        return render_template("location_info_noform.html", location_info=location_info,comments=comments,weather_json=weather_json)

@app.route("/check_in", methods=["POST"])
def check_in():
    comment = request.form.get("comment")
    location_id = request.form.get("location_id")
    db.execute("INSERT INTO location_comments (ref_id, comment, username) VALUES (:id, :comment, :username)", {"id":location_id, "comment":comment, "username":session['user']})
    db.commit()
    db.execute("UPDATE zip_data SET check_in = check_in+1 WHERE :id=id", {"id":location_id})
    db.commit()
    return render_template("thanks.html")

@app.route("/api/zipcode/<lookup_zipcode>")
# I called it "lookup_zipcode" instead of "zip" because "zip" seems to have a specific meaning in Python
def location_api(lookup_zipcode):
   #Return details about a single location.

    # Make sure location exists.
    zip_result = db.execute("SELECT * FROM zip_data WHERE zipcode=:lookup_zipcode",{"lookup_zipcode":lookup_zipcode}).fetchone()
    if zip_result is None:
        return jsonify({"error": "Zipcode does not exist"}), 404
    return jsonify({
            "place_name": zip_result.city,
            "state": zip_result.state,
            "latitude": zip_result.latitude,
            "longitude": zip_result.longitude,
            "zip": zip_result.zipcode,
            "population": zip_result.population,
            "check_ins": zip_result.check_in
        })




@app.route("/logout")
def logout ():
    session.pop('user', None)
    return render_template("login.html")

@app.route("/main")
def main_return ():
    return render_template("main.html")


