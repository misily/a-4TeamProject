from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://kimes:1234abcd@cluster0.d5w5umq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('profile_detail_input.html')

@app.route('/write_post', methods=['POST'])
def write_post():
    user_name_receive = request.form['user_name_give']
    mbti_receive = request.form['mbti_give']
    email_receive = request.form['email_give']
    photo_url_receive = request.form['photo_url_give']
    interest_receive = request.form['interest_give']
    aboutme_receive = request.form['aboutme_give']
    javascript_receive = request.form['javascript_give']
    HTML_receive = request.form['HTML_give']
    CSS_receive = request.form['CSS_give']
    Python_receive = request.form['Python_give']
    Promise_receive = request.form['Promise_give']
    doc = {
        'user_name':user_name_receive,
        'mbti':mbti_receive,
        'email':email_receive,
        'photo_url':photo_url_receive,
        'interest':interest_receive,
        'aboutme':aboutme_receive,
        'javascript':javascript_receive,
        'HTML':HTML_receive,
        'CSS':CSS_receive,
        'Python':Python_receive,
        'Promise':Promise_receive
    }

    db.user_info.insert_one(doc)
    return jsonify({'msg': '저장되었습니다~!'})

# app.route("/write_post", methods=["POST"])
# def userinfo_give():
#     user_name_receive = request.form['user_name_give']
#     title_receive = request.form['title_give']
#     tags_receive = request.form['tags_give']
#     contents_receive = request.form['contents_give']
#     comments_receive = request.form['comments_give']
#     photo_url_receive = request.form['photo_url_give']
#     url_receive = request.form['url_give']

#     doc = {
#         'user_name':user_name_receive,
#         'title':title_receive,
#         'tags':tags_receive,
#         'contents':contents_receive,
#         'comments':comments_receive,
#         'photo_url':photo_url_receive,
#         'photo_url':url_receive
#     }

#     db.teamproject1.insert_one(doc)
#     return jsonify({'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)