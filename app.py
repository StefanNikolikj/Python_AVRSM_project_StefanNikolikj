from flask import Flask, request
import pymongo
import sqlite3
import json


app = Flask(__name__)


@app.route('/getName', methods = ['GET'])
def get_company_name():
    """
    This is the API required to obtain the data from SQLite

    :return: This sends the obtained data into the program file where it is used
    """
    c = sqlite3.connect("data.db").cursor()
    c.execute("SELECT * FROM COMPANIES")
    data = c.fetchall()
    return json.dumps(data)

@app.route('/postName', methods = ['POST'])
def post_company_name():
    """
    a function that posts the finished list of companies in MongoDB after the names are formatted

    :return:
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["data"]
    mycol = db["companies"]
    mydict = json.loads(request.data)
    x = mycol.insert_one(mydict)


@app.route('/')
def hello_world():
    """
    A simple space holder where the frond end code would be located, as it is the main page just has
    plain "Hello World!" on it

    :return:
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
