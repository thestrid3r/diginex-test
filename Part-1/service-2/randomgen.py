import json
import os
from random import seed, random
import requests
from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


URL = os.environ["BACKEND_URL"]  # url of reverse api app
seed(1)  # seeding random generator


@app.route('/api', methods=['POST'])
def reverse():
    data = json.loads(request.data)
    for keys in data:
        if "messages" in keys:
            val = data.get('messages')  # reading from requests
            req = {"messages": val}  # payload
            payload = json.dumps(req)
            headers = {
                'content-type': "application/json",
            }
            response = requests.request(
                "POST", URL, data=payload, headers=headers)
            get_req = {}
            get_req = response.json()
            get_req.update({"rand": random()})
            return json.dumps(get_req)

        return abort(500, "invalid request received")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
