import os
from flask import Flask, render_template  #, redirect, request, url_for, session
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# import bcrypt
from connect import getCollection, getDbName, getURI

app = Flask(__name__)

app.config["MONGO_DBNAME"] = getDbName()
app.config["MONGO_URI"] = getURI()

mongo = PyMongo(app)

# R     -----------------------
@app.route("/")
@app.route("/get_composers")
def get_tasks():
    return render_template("composers.html", composers=mongo.db.composers.find())
    
# C     -----------------------
@app.route("/add_composer")
def add_composer():
    return "This will render the 'addcomposer.html'"
    
@app.route("/insert_composer", methods=["POST"])
def insert_composer():
    return "This will only work with a POST. Used to create a new composer entry."

# U     -----------------------
@app.route("/edit_composer/<composer_id>")
def edit_composer(composerid):
    return "This will render the 'editcomposer.html'"

@app.route("/update_composer/<composer_id>", methods=["POST"])
def update_composer(composer_id):
    return "This will only work with a POST. Used to update a composer entry."

# D     -----------------------
@app.route("/delete_task/<composer_id>")
def delete_composer(composerid):
    return "This will render the 'deletecomposer.html'"

# @app.route("/")
# def home():
#     print(getDbName())
#     print(getURI())
#     return "Starting Composers Project " + getCollection()


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  # debug=True allows the changes to be picked automatically in the browser
                            # Also produces debug statements in case of a bug