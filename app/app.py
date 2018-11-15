from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('service_mongo', 27017)
db = client.tododb

@app.route('/')
def root():
    return jsonify({'staaatus': 'upa!!'})

@app.route('/view')
def view():
    result = list(db.tododb.find({}, {'_id': 0}))
    return jsonify(result)

@app.route('/new', methods=['GET'])
def new():
    doc = {
        'username': request.args.get('username'),
        'password': request.args.get('password')
    }
    db.tododb.insert_one(doc)

    return jsonify({'status': 'done'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port='5000')
