# TODO Pull data from finance using yfinance

# TODO Load into workspace dataframe

# TODO Create analyses with numpy etc

# TODO Create visualisations with matplot lib

# TODO Host the results on a window. 
from flask import Flask, render_template
# import sys,os

# script_dir = os.path.dirname( __file__ )
# mymodule_dir = os.path.join( script_dir, '..', '..', 'data')
# sys.path.append( mymodule_dir )

app = Flask(__name__)

# I guess this is the "html string"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
