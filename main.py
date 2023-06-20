# TODO Pull data from finance using yfinance

# TODO Load into workspace dataframe

# TODO Create analyses with numpy etc

# TODO Create visualisations with matplot lib

# TODO Host the results on a window. 
import sys
from flask import Flask
for p in sys.path:
    print( p )

app = Flask(__name__)

def home():
    return "some text on teh page"

if __name__ == "__main__":
    app.run(debug=True)
