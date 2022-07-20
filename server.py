from flask import Flask
from about import me
from data import mock_data
import json

app = Flask('server')


@app.get("/")
def home():
    return "Hello, world!"


@app.get("/test")
def test():
    return "this is just a simple test"


@app.get("/about")
def about_me():
    return "Daniel Avilez"


################################################################
########### API ENDPOINTS = PRODUCTS ###########################
################################################################

@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def about_json():
    return json.dumps(me)


@app.get("/api/products")
def get_products():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:  # added str because id is a number
            return json.dumps(prod)

    return "NOT FOUND !"


@app.get("/api/catagories")
def get_catagories():
    catagories = []
    for product in mock_data:
        catagories.append(product["catagory"])
    return json.dumps(catagories)

# get/api/catagories
# return the list of catagories
# 1 return ok
# 2 travel mock_data, and print the catagory of every product
# 3 put the catagory in a list and at the end of the for loop, return the list as json


app.run(debug=True)
