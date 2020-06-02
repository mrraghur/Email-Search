from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

#https://pythonspot.com/flask-web-app-with-python/
#https://pythonbasics.org/flask-tutorial-routes/
@app.route("/")
def index():
    return render_template(
    'index.html', static_url_path='/static')#static_folder='static')#,name=name)#</string:name>

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return str(name)#</string:name>

if __name__ == "__main__":
    app.run()
