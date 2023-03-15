from flask import Flask,render_template,request,jsonify,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__,static_folder="templates/assets")

client = MongoClient('mongodb+srv://kimes:1234abcd@cluster0.d5w5umq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
userComment = db.comment

@app.route('/')
def home():
    comments = list(userComment.find({},{'_id':False}))
    return render_template('index.html',comments=comments)

@app.route('/details/<usernum>',methods=["GET"])
def detail(usernum):
    pass

@app.route('/comment', methods=["POST"])
def comment():
    if request.method == "POST":
        form = request.form
        doc = {
            'name' : form.get('writer'),
            'title' : form.get('title'),
            'star' : int(form.get('star')),
            'comment' : form.get('comment')
        }
        userComment.insert_one(doc)
        print(doc)
        return redirect(url_for('home'))
    
# 디테일 페이지 코드

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

# 디테일 수정페이지 코드

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


if __name__ == '__main__':
    app.run(debug=True)