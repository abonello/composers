import os
from flask import Flask, render_template, request, redirect, url_for #, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# import bcrypt
from connect import getDbName, getURI # Does not work in Heroku

app = Flask(__name__)

# Use the following to run locally will need the import
app.config["MONGO_DBNAME"] = getDbName()
app.config["MONGO_URI"] = getURI()
# collection = getCollection()

# Use the following to run from heroku - remove the import
# app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
# app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


# 2 digit date and month
def formatNumber(n):
    '''If the user inputs a date or month with one digit
        an extra 0 is added in front. '''
    if len(n) == 1:
        return "0{}".format(n)
    else:
        return n

# R     -----------------------
@app.route("/")
@app.route("/get_composers")
def get_composers():
    return render_template("composers.html", composers=mongo.db.composers.find())
    
# C     -----------------------
@app.route("/add_composer")
def add_composer():
    # return "This will render the 'addcomposer.html'"
    all_periods = mongo.db.periods.find()
    periods_list=[]
    for period in all_periods:
        periods_list.append(period['name'])
    return render_template("addcomposer.html", periods=periods_list)

@app.route("/insert_composer", methods=["POST"])
def insert_composer():
    # return "This will only work with a POST. Used to create a new composer entry."
    # composers = mongo.db.composers
    # composers.insert_one(request.form.to_dict())
    # print("What arrives from FORM:")
    # print(request.form)
    dataFromForm = request.form.to_dict()
    # print("Turned into a DICTIONARY:")
    # print(dataFromForm)
    
    data = {}
    data['first_name'] = dataFromForm['first_name']
    data['last_name'] = dataFromForm['last_name']
    # dob = "{}/{}/{}".format(formatNumber(dataFromForm['dob-date']), formatNumber(dataFromForm['dob-month']), dataFromForm['dob-year'])
    # dod = "{}/{}/{}".format(formatNumber(dataFromForm['dod-date']), formatNumber(dataFromForm['dod-month']), dataFromForm['dod-year'])
    data['dob'] = "{}/{}/{}".format(formatNumber(dataFromForm['dob-date']), formatNumber(dataFromForm['dob-month']), dataFromForm['dob-year'])
    data['dod'] = "{}/{}/{}".format(formatNumber(dataFromForm['dod-date']), formatNumber(dataFromForm['dod-month']), dataFromForm['dod-year'])
    data['period'] = dataFromForm['period']
    data['nationality'] = dataFromForm['nationality']
    data['information'] = dataFromForm['info']
    # print("This is DATA:")
    # print(data)
    composers = mongo.db.composers
    composers.insert_one(data)
    
    return redirect(url_for("get_composers"))

# U     -----------------------
@app.route("/edit_composer/<composer_id>")
def edit_composer(composer_id):
    the_composer = mongo.db.composers.find_one({"_id": ObjectId(composer_id)})
    all_periods = mongo.db.periods.find()
    periods_list=[]
    for period in all_periods:
        periods_list.append(period['name'])
    return render_template("editcomposer.html", composer=the_composer, periods=periods_list)

@app.route("/update_composer/<composer_id>", methods=["POST"])
def update_composer(composer_id):
    print("Update composer with id {}".format(composer_id))
    # return "This will only work with a POST. Used to update a composer entry."
    dataFromForm = request.form.to_dict()
    data = {}
    data['first_name'] = dataFromForm['first_name']
    data['last_name'] = dataFromForm['last_name']
    data['dob'] = "{}/{}/{}".format(formatNumber(dataFromForm['dob-date']), formatNumber(dataFromForm['dob-month']), dataFromForm['dob-year'])
    data['dod'] = "{}/{}/{}".format(formatNumber(dataFromForm['dod-date']), formatNumber(dataFromForm['dod-month']), dataFromForm['dod-year'])
    data['period'] = dataFromForm['period']
    data['nationality'] = dataFromForm['nationality']
    data['information'] = dataFromForm['info']
    composers = mongo.db.composers
    composers.update({"_id": ObjectId(composer_id)}, data)
    return redirect(url_for('get_composers'))

# D     -----------------------
@app.route("/delete_composer/<composer_id>")
def delete_composer(composer_id):
    # return "This will render the 'deletecomposer.html'"
    mongo.db.composers.remove({"_id": ObjectId(composer_id)})
    return redirect(url_for('get_composers'))



# @app.route("/")
# def home():
#     print(getDbName())
#     print(getURI())
#     return "Starting Composers Project " + getCollection()


if __name__ == "__main__":
    # app.run(host=os.environ.get('IP'),      # Use to run locally
    #         port=int(os.environ.get('PORT')),
    #         debug = True)  # debug=True allows the changes to be picked automatically in the browser
                            # Also produces debug statements in case of a bug
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True) # Use for heroku. This works locally too.