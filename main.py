# TODO Pull data from finance using yfinance

# TODO Load into workspace dataframe

# TODO Create analyses with numpy etc

# TODO Create visualisations with matplot lib

# TODO Host the results on a window. 
from flask import Flask, render_template
import sys,os
from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_datepicker import datepicker

script_dir = os.path.dirname( __file__ )
SCRIPT_FOLDER = os.path.join(script_dir,'scripts','analyses')
sys.path.append( SCRIPT_FOLDER )

mymodule_dir = os.path.join( script_dir,'data')
sys.path.append( mymodule_dir )

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
# Bootstrap(app)
# datepicker(app)


import breadth

# def picker(id=".datepicker", # identifier will be passed to Jquery to select element
#            dateFormat='yy-mm-dd', # can't be explained more !
#            maxDate='2023-08-30', # maximum date to select from. Make sure to follow the same format yy-mm-dd
#            minDate='2017-12-01', # minimum date
#            btnsId='.btnId' # id assigned to instigating buttons if needed
#     ):
#     return 

# I guess this is the "html string"
@app.route("/")
def home():

    return render_template("home.html", currbreadth = breadth.generateBreadth())

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/graph")
def graph():
    AdvDecPlot = os.path.join(app.config['UPLOAD_FOLDER'], 'advdecplt2019.png')
    return render_template("graph.html",user_image=AdvDecPlot)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
