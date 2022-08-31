import json
import sys
sys.path.insert(1, '.')
from modules.calc_decimal import calc_decimal
from modules.get_phi import get_phi
from modules.get_triples import get_triples, get_pythag_by_corner
from flask import Flask, jsonify

# OUTPUT application/json
def format_payload(data):
	str = json.dumps(data, indent=4, separators=(',', ': '))
	return str, 200, { 'Content-type': 'application/json' }

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

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
    app.run(port=8080, host="0.0.0.0")
