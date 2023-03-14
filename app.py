from flask import Flask,render_template,request
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/details/<usernum>',method=["GET"])
def detail(usernum):
    pass

@app.route('/comment',method=["POST","GET"])
def comment():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass