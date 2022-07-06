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


app.run(debug=True)
