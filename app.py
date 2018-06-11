import os
from flask import Flask, render_template  #, redirect, request, url_for, session
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# import bcrypt

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug = True)  # debug=True allows the changes to be picked automatically in the browser
                            # Also produces debug statements in case of a bug