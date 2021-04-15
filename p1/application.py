from flask import Flask

# Ceate intance of Flask model is app
app = Flask(__name__)

# create dacurator is @app
@app.route("/")
def index():
    return "Hello World"

# Debugger Mode is ON when we check any errors in runtime And when the site is complte then the Debugger Mode is OFF
app.run(debug = True)
