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

# Product Class/Model (for whatever objects we are making the application, it's important to create a class for that object)
class ProductClass(db.Model):
    # db is our sql element and Model gives us some predefined methods

    # defining our fields
    id = db.Column(db.Integer, primary_key=True) # the auto increment is by default true
    name = db.Column(db.String(100), unique = True) # always pass the datatype of the field to the Column() first
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    # constructor definition
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema Definition
class ProductSchema(ma.Schema):
    class Meta: # this is the class we use to declare which fields to show during a get request
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True) # many = True indicates that we are dealing with multiple products

# Run server
if __name__ == '__main__':
    app.run(debug=True)