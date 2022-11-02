# system stuff
import json
import sys

# sys.path.insert(1, '.')

from flask import Flask, jsonify

# Import my math stuff.
from modules.calc_decimal import calc_decimal
from modules.get_phi import get_phi
from modules.get_triples import get_triples, get_pythag_by_corner


# OUTPUT application/json
# ... and make it pretty.
# Consider extracting this into a module, just to clean things up a bit.
def format_payload(data):
	str = json.dumps(data, indent=4, separators=(',', ': '))
	return str, 200, { 'Content-type': 'application/json' }



# Flask for Python API.
app = Flask(__name__)


# ... And start routing ...
@app.route("/")
def hello():
	# Would be much better to have the default go to a document page, or at least something entertaining.
	return "Hello, World! Welcome to my cool math api!"

# Accept a denominator, and return the reciprocal.
# This gives the same information as /dc/denom, but without all of the other, probably less interesting, numerators.
@app.route("/reciprocal/<param_denom>")
def reciprocal(param_denom):
	denom = int(param_denom)
	data = calc_decimal(1, denom, 10)
	return format_payload({ "Denominator": denom, "data": data })

@app.route("/dc/<param_denom>")
def dc(param_denom):
	denom = int(param_denom)
	data = list(map(lambda num: calc_decimal(num, denom, 10), range(1, denom)))
	return format_payload(data)


@app.route('/pythag/<corner>', methods=['GET'])
def pythag(corner):
	return format_payload(get_pythag_by_corner(corner))

@app.route('/pythag-c/<param_c_from>/<param_c_to>', methods=['GET'])
def pythag_c(param_c_from, param_c_to):
	c_from = int(param_c_from)
	c_to = int(param_c_to)	
	return format_payload(get_triples(range(c_from, c_to + 1)))

@app.route('/pythag-clist/<param_clist>', methods=['GET'])
def pythag_clist(param_clist):
	clist = list(map(lambda x: int(x), param_clist.split(',')))
	return format_payload(get_triples(clist))



@app.route('/phi', defaults={'power': 4})
@app.route('/phi/<power>', methods=['GET'])
def phi(power: int):
	power = int(power)
	return format_payload(get_phi(power))

if __name__ == '__main__':

    # Run the app
    app.run(port=5000, host="0.0.0.0")
