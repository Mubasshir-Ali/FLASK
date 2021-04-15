from flask import Flask

# Ceate intance of Flask model is app
app = Flask(__name__)

# create dacurator is @app
@app.route("/")
def index():
    return "Hello World \
        We Are Pakistani \
            We Love Our Country \
        "

@app.route("/about")
def about():
    return '''
    <h1>PIAIC Quarter 3 Islamabad</h1>
    We are providing latest art of technology.
    '''

# Debugger Mode is ON when we check any errors in runtime And when the site is complte then the Debugger Mode is OFF
app.run(debug = True)