import os

from flask import Flask
from sqlalchemy import create_engine
import psycopg2
import sys,os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

alchemyEngine   = create_engine('postgresql+psycopg2://test:@127.0.0.1:5432/stockindex', pool_recycle=3600)
dbConnection    = alchemyEngine.connect()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=dbConnection,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    SCRIPT_FOLDER = os.path.join('scripts','analyses')
    sys.path.append( SCRIPT_FOLDER )

    script_dir = os.path.dirname( __file__ )
    mymodule_dir = os.path.join('scripts')

    sys.path.append( mymodule_dir )

    app = Flask(__name__)
    IMG_FOLDER = os.path.join('static', 'IMG')
    app.config['UPLOAD_FOLDER'] = IMG_FOLDER
    Bootstrap(app)
    datepicker(app)

    import breadth
    # print(dir(breadth))
    # print(breadth.generateBreadth())

    def picker(id=".datepicker", # identifier will be passed to Jquery to select element
            dateFormat='yy-mm-dd', # can't be explained more !
            maxDate='2023-08-30', # maximum date to select from. Make sure to follow the same format yy-mm-dd
            minDate='2017-12-01', # minimum date
            btnsId='.btnId' # id assigned to instigating buttons if needed
        ):
        return 

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

        return app