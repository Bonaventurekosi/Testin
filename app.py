from flask import Flask
from flask import render_template
from flask import request 

app = Flask(__name__)

@app.route("/")
@app.route('/homepage')
def hello() :
    return "This is it"


app.run(host='0.0.0.0', port=81, debug=True)