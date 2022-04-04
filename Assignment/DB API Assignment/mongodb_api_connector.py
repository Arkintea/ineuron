# importing required packages
import pymongo
from flask import Flask, request, jsonify

# create flask app
app = Flask(__name__)


@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # get request body
    url = request.json['url_name']
    database = request.json['database_name']
    collection = request.json['collection_name']

    # create mongodb client
    client = pymongo.MongoClient(str(url))
    db = client[database]
    collection = db[collection]
    return jsonify({'data': str(list(collection.find()))})


# run flask app
if __name__ == '__main__':
    app.run(debug=True)
