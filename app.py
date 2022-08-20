from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungletest

# HTML 화면 보여주기
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles':articles})



## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def posting():
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']

    doc = {
        'title': title_receive,
        'comment': comment_receive

    }
    db.articles.insert_one(doc)
    return jsonify({'msg': '이 요청은 POST!'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
