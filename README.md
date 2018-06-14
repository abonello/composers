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


### Push to GitHub
~~~~
git remote add origin https://github.com/abonello/composers.git
git push -u origin master
~~~~

### Heroku deployment
Create Procfile
~~~~python
web: python app.py
~~~~

~~~~
heroku login
heroku apps
~~~~

Creating the app on heroku site allows for more control of server.  
Name of app: **composers-music**  
If I create the app from command line the git remotes will be created automatically.
Since I created the app in the website I have to create the git remotes manually.

~~~~
git remote add heroku https://git.heroku.com/composers-music.git
~~~~

To see the remotes available run:
~~~~
git remote -v
~~~~
The results are:
~~~~
    heroku  https://git.heroku.com/composers-music.git (fetch)
    heroku  https://git.heroku.com/composers-music.git (push)
    origin  https://github.com/abonello/composers.git (fetch)
    origin  https://github.com/abonello/composers.git (push)
~~~~

Next I will push the project to heroku.
~~~~
git push -u heroku master
~~~~

To deploy on heroku I had to do some changes to the code.

1. I am using os.getenv instead of os.environ.get. I am not sure why but this is working.
2. I cannot have a file that is included in the .gitignore and sent to heroku but not to github.
    The log in details are stored as environment variables on heroku instead. (Same as for 
    PORT and IP).

To see the heroku logs run
~~~~
heroku logs
~~~~

After changes remember to run
~~~~
git push -u heroku master
heroku ps:scale web=1
~~~~

~~~~
git push -u origin master
~~~~





## To do



DC.js charts



