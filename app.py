from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

# Setting base directory
base_dir = os.path.abspath(os.path.dirname(__file__))
# What we did :
# Making sure that we can correctly locate the database file.
# The db file is in our root but we need to make sure the server knows the path.
# So we pass the path to the os package in os.path.abspath() and os.path.dirname(__file__) 
# gives the path of the current folder we are working on.

# Setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite') 
# this is going to look for the db.sqlite file in the current working directory (specified in base_dir)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we don't need this but if don't do this, we will get errors in the console :((

# Init db
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

# Run server
if __name__ == '__main__':
    app.run(debug=True)