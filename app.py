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

# 프로필 상세페이지 연결
@app.route('/profile')
def profile():
   return render_template('profile_detail.html') 

@app.route('/profile/input')
def input():
   return render_template('profile_detail_input.html') 
# 수정버튼 누르면 404에러 발생

@app.route('/details/<usernum>',methods=["GET"])
def detail(usernum):
    user = db.user_info.find_one({"usernum":usernum},{'_id':False})
    print(user)
    return render_template('myprofile.html',user=user)

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

# photo_url/title/name/MBTI/email/personallink/interest
@app.route("/detail_get", methods=["GET"])
def guestbook_get():
    all_info = list(db.user_info.find({},{'_id':False}))
    return jsonify({'result':all_info})

# 디테일 수정페이지 코드

@app.route('/write_post', methods=['POST'])
def write_post():
    user_num_receive = request.form['user_num_give']
    if (user_num_receive == 1):
        user_name_receive = '김은수'
    elif (user_num_receive == 2):
        user_name_receive = '김성광'
    elif (user_num_receive == 3):
        user_name_receive = '배현아'
    elif (user_num_receive == 4):
        user_name_receive = '이윤성'
    elif (user_num_receive == 5):
        user_name_receive = '유혜민'
    

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
        'usernum':user_num_receive,
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

if __name__ == '__main__':
    app.run(debug=True)