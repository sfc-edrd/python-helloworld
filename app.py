from flask import Flask, json
import logging

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(funcName)s %(message)s', level=logging.DEBUG,filename='app.py.log')


@app.route("/health")
def health():

	logging.info('endpoint was reached.')

	message = { "result" : "OK - healthy" }
	
	response = app.response_class(
		json.dumps(message),
		status=200,
		mimetype='application/json'
		)
	
	return response


@app.route("/metrics")
def metrics():

	logging.info('endpoint was reached.')

	message = {
		"UserCount": 140,
		"UserCountActive": 23}

	response = app.response_class(
		json.dumps({
			"status": "success",
			"code": 0,
			"data": message}),
		status=200,
		mimetype='application/json'
		)
	
	return response


@app.route("/")
def hello():

	logging.info('endpoint was reached.')
	
	return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# update
