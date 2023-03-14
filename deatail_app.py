from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://kimes:1234abcd@cluster0.d5w5umq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
   return render_template('detail.html')

@app.route("/detail_post", methods=["POST"])
def guestbook_post():
    user_name_receive = request.form['user_name_give']
    title_receive = request.form['title_give']
    tags_receive = request.form['tags_give']
    contents_receive = request.form['contents_give']
    comments_receive = request.form['comments_give']
    photo_url_receive = request.form['photo_url_give']
    url_receive = request.form['url_give']

    doc = {
        'user_name':user_name_receive,
        'title':title_receive,
        'tags':tags_receive,
        'contents':contents_receive,
        'comments':comments_receive,
        'photo_url':photo_url_receive,
        'photo_url':url_receive
    }

    db.teamproject1.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/detail_get", methods=["GET"])
def guestbook_get():
    all_recommend = list(db.teamproject1.find({},{'_id':False}))
    return jsonify({'result':all_recommend})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)