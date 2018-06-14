# Composers

The aim of this project is to bring together the following items:
* **MongoDB** - all CRUD functionality (on **mlab**)
* **Flask** - to serve data from db to front end
* **dc.js** - the use of dc.js, d3.js and crossfilter.js in the front end to chart the data

I will be adding the following:
* passwords for users will be hashed
* calls to the database will be enclosed in a try - except

I will use **bootstrap** for layout and styling.  

I will also use a different .py file to store the database information so that
it is not stored on github.  

Version control will be by using **Git**.  

Finally I want this project to be deployed on **heroku**.



## Install libraries

I am using "Python 3.4.3"

~~~~
sudo pip3 install flask
sudo pip3 install flask-pymongo
sudo pip3 install bcrypt

pip3 freeze --local > requirements.txt
~~~~


## Set imports and start git

~~~~
import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
~~~~

create a flask object and prepare the run code.

~~~~python
app = Flask(__name__)
.
.
.
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  # debug=True allows the changes to be picked automatically in the browser
                            # Also produces debug statements in case of a bug
~~~~

Start Git
~~~~
git init
touch .gitignore
~~~~
In .gitignore include the cloud nine folders and the .py file which will have
the db connection information.

Built routes to implement CRUD for mongodb Database on mlab.



## To do

Heroku deployment
Push to GitHub
DC.js charts



