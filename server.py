from bson import ObjectId
from flask import Flask, request
from about import me
from data import mock_data
import random
import json
from config import db

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


def fix_mongo_id(obj):

    obj["id"] = str(obj["_id"])
    del obj["_id"]
    return obj


@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)


@app.post("/api/products")
def save_product():
    product = request.get_json()

    db.products.insert_one(product)
    fix_mongo_id(product)

    product["_id"] = str(product["_id"])
    del product["_id"]

    return json.dumps(product)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"

    fix_mongo_id(prod)
    return json.dumps(prod)


@app.get("/api/products_category/<category>")
def get_prods_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)


@app.get("/api/products_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod

    fix_mongo_id(solution)
    return json.dumps(solution)


@app.get("/api/catagories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        cat = product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)


# get/api/catagories
# return the list of catagories
# 1 return ok
# 2 travel mock_data, and print the catagory of every product
# 3 put the catagory in a list and at the end of the for loop, return the list as json


@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1

    return json.dumps({"count": count})


@app.get("/api/search/<text>")
def search_products(text):
    results = []

    text = text.lower()
    for prod in mock_data:
        if text in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)


app.run(debug=True)
