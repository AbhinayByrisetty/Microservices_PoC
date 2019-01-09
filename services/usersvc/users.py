import requests
import os
import simplejson as json
from flask import Flask, jsonify, make_response

app = Flask(__name__)

with open("/database/users.json", "r") as f:
    usr = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"

@app.route('/users', methods=['GET'])
def users():
    ''' Returns the list of users '''

    resp = make_response(json.dumps(usr, sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp

@app.route('/users/<username>', methods=['GET'])
def user_data(username):
    ''' Returns info about a specific user '''

    if username not in usr:
        return "Not found"

    return jsonify(usr[username])

@app.route('/users/<username>/lists', methods=['GET'])
def user_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://todosvc-service:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

if __name__ == '__main__':
    app.run(port=5000, debug=False, host='0.0.0.0')
