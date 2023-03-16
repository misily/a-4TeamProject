from flask import Flask,render_template,request,jsonify,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__,static_folder="templates", static_url_path='')

client = MongoClient('mongodb+srv://kimes:1234abcd@cluster0.d5w5umq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
userComment = db.comment

@app.route('/')
def home():
    comments = list(userComment.find({},{'_id':False}))
    return render_template('index.html',comments=comments)

# 프로필 상세페이지 연결
@app.route('/profile/<usernum>',methods=["GET"])
def profile(usernum):
    user = db.user_info.find_one({'usernum':int(usernum)},{'_id':False})
    print(user)
    modify = url_for('input',usernum=usernum)
    return render_template('user_profile.html',user=user,modify=modify)

@app.route('/profile/<usernum>/input',methods=["GET","POST"])
def input(usernum):
    if request.method == "GET":
        user = db.user_info.find_one({'usernum':int(usernum)},{'_id':False})
        return render_template('profile_detail_input.html',user=user) 
    elif request.method == "POST":
        form = request.form
        doc = {
            'mbti': form['mbti'],
            'email':form['email'],
            'photo_url':form['photo_url'],
            'interest':form['interest'],
            'aboutme':form['aboutme'],
            'javascript':form['Javascript'],
            'HTML':form['HTML'],
            'CSS':form['CSS'],
            'Python':form['Python'],
            'Promise':form['Promise']
        }
        db.user_info.update_one({"usernum": int(usernum)}, {"$set": doc})
        print(doc)
        return redirect(url_for('profile', usernum=int(usernum)))
        
# 수정버튼 누르면 404에러 발생

@app.route('/details/<usernum>',methods=["GET"])
def detail(usernum):
    user = db.user_info.find_one({'usernum':usernum},{'_id':False})
    print(user)
    return render_template('user_profile.html',user=user)

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
        user_name_receive = '유혜민'
    elif (user_num_receive == 5):
        user_name_receive = '이윤성'
    

    mbti = request.form['mbti_give']
    email = request.form['email_give']
    photo_url = request.form['photo_url_give']
    blog_url = request.form['blog_url_give']
    interest = request.form['interest_give']
    aboutme = request.form['aboutme_give']
    javascript = request.form['javascript_give']
    HTML = request.form['HTML_give']
    CSS = request.form['CSS_give']
    Python = request.form['Python_give']
    Promise = request.form['Promise_give']
    
    doc = {
        'usernum':user_num,
        'user_name':user_name,
        'mbti':mbti,
        'email':email,
        'photo_url':photo_url,
        'blog_url':blog_url,
        'interest':interest,
        'aboutme':aboutme,
        'javascript':javascript,
        'HTML':HTML,
        'CSS':CSS,
        'Python':Python,
        'Promise':Promise
    }

if __name__ == '__main__':
    app.run(debug=True)