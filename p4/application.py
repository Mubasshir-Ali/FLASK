from flask import Flask
from flask import render_template

# Ceate intance of Flask model is app
app = Flask(__name__)

# create dacurator is @app
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Debugger Mode is ON when we check any errors in runtime And when the site is complte then the Debugger Mode is OFF
app.run(debug = True)