from flask import Flask


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


app.run(debug=True)
