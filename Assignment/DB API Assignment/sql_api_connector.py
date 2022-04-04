# importing required packages
from flask import Flask, request, jsonify
import mysql.connector as conn

# create flask app
app = Flask(__name__)


@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # get request body
    user = request.json['username']
    passwd = request.json['password']
    query = request.json['query_data']

    # create cursor
    my_db = conn.connect(host='localhost', user=str(user), passwd=str(passwd))
    cursor = my_db.cursor()

    # get data from database
    cursor.execute(query)
    return jsonify({'data': str(cursor.fetchall())})


# run flask app
if __name__ == '__main__':
    app.run(debug=True)
