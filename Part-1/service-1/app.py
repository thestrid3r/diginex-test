import json
from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


@app.route('/reverse', methods=['POST'])
def reverse():
    data = json.loads(request.data)
    # print(data)
    try:
        for keys in data:
            if "messages" in data:
                val = data.get('messages')
                val = val[::-1]
                return_data = {"messages": val}
                return json.dumps(return_data)
            break
    except:
        abort(500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
