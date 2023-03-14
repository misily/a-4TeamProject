from flask import Flask
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://kimes:1234abcd@cluster0.d5w5umq.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)