#===============================================================#
#                                                               #
#                    Welcome to tippay.py!                      #
#            This is the python wrapper for tippay.             #
#        This template will document the way you use it.        #
#                                                               #
#===============================================================#

import flask
import tippay # you import tippay (requires flask)

app = flask.Flask(__name__) # you init your flask app

tippay = tippay.instance(app) # create a tippay instance and pass in your flask app

def callback(name):print(name + " tipped 100 cycles!") # I defined a callback here. It can be whatever function you desire.

python = tippay.product("pythontiptest",100,"https://tippaypy.hellscaped.repl.co/thanks",callback) # You create the product. Argument 1 is name, 2 is price, 3 is redirect url, 4 is callback.

@app.route("/") 
def root():
  return "please test tippay.py by tipping 100 cycles: " + tippay.url(python) # You pass the product into the this function to get a tippay url.

@app.route("/thanks")
def thanks():
  return "thanks 4 testing tippay python" #And this is the callback.

app.run(host='0.0.0.0', port=8080)
