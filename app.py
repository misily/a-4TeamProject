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
      
if __name__ == '__main__':
    app.run(debug=True)