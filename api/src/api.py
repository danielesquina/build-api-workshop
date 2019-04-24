import datetime

from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from flask import send_file
# Setup Flask app.
flask_app = Flask(__name__)
flask_app.config['JSON_AS_ASCII'] = False  # Needed for proper UTF-8 support.

# Setup CORS - this is needed for a proper communication with the frontend.
CORS(flask_app)


@flask_app.route('/test', methods=['GET'])
def test():
    """
    This endpoint returns the current server time and a static text.
    :return: Current server time and text JSON formatted.
    """
    response = {
        'time': datetime.datetime.now().strftime('%m/%d/%Y - %H:%M:%S'),
        'text': 'This is a test.'
    }
    return jsonify(response), 200


@flask_app.route('/names', methods=['GET'])
def names():
    response = {'firstname': 'Alexandra', 'lastname':'Volkova', 'firstname2': 'Daniel', 'lastname2':'Esquina',}
    return jsonify(response), 200

@flask_app.route('/calc', methods=['GET'])
def calc():
    n1=request.args.get('num1')
    n2=request.args.get('num2')
    op=request.args.get('op')
    if op == '-' :
        response = {'result': int(n1)-int(n2)}
    if op == '*' : 
        response = {'result': int(n1)*int(n2)}
    else: return jsonify({'indefinido':'indefinido'}), 404
    return jsonify(response), 200

"""
@flask_app.route('/image', methods=['GET'])
def image():
    n=request.args.get('nom')
    send_from_directory('',n)
    response = {'descarga': 'bien'}
    return jsonify(response), 200
"""

@flask_app.route('/image')
def image():
    n=request.args.get('img')
    return send_file(n, mimetype='image/jpg'), 200