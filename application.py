import os

from flask import Flask, session, render_template, request
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
    return render_template('login.html')

@app.route("/logged_in", methods=["POST"])
def logged_in ():
    username = request.form.get("username")
    password = request.form.get("password")
    if db.execute("SELECT * FROM user_login WHERE username = :username AND password = :password", {"username": username, "password": password}).rowcount == 0:
        return render_template('error.html')

    #else:
      #  if db.execute("SELECT * FROM note_holder WHERE username = :username",{"username":session["username"]}).rowcount == 0:
       #     db.execute("INSERT INTO note_holder (username) VALUES (:username)",{"username":session["username"]})
        #    db.commit()
        #else:
         #   print("hi")
   # print(session["username"])
    return render_template('main.html')

@app.route("/search_location", methods=["POST"])
def search_location():
    print(session["username"])
    location_search = request.form.get("location")
    location_search = location_search.upper()
    # The syntax for db.execute does not work, though I tried a lot of different iterations on %x% with the variable in the middle to no success.
   # location_result = db.execute("SELECT id, zipcode, city, state FROM zip_data WHERE zipcode LIKE '%'+:location_search+'%' OR city LIKE '%'+:location_search+'%' OR state LIKE '%'+:location_search+'%'", {"location_search":location_search}).fetchall()
    location_result = db.execute("SELECT id, zipcode, city, state FROM zip_data WHERE city=:location_search",{"location_search":location_search}).fetchall()
    return render_template('search_location.html',location_result=location_result)

@app.route("/search_location/<int:location_id>")
def location(location_id):
    """Lists details about a single location."""

    # Make sure location exists.
    location_info = db.execute("SELECT * FROM zip_data WHERE id = :id", {"id": location_id}).fetchone()
    if location is None:
        return render_template("error.html")

    my_notes = db.execute("SELECT notes FROM note_holder WHERE username = :username", {"username":session["username"]}).fetchone()
    return render_template("location_info.html",location_info=location_info)

#@app.route("/logut")
#def logout ():
#    session.pop(session["username"], None)
#   print(session["username"])
#    return render_template("login.html")


# @app.route("/check_in")
# def check_in():

