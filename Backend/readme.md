# Flask
- 간단한 웹 사이트, 혹은 간단한 API 서버를 만드는 데에 특화 되어있는 Python Web Framework
- Werkzeug 툴킷과 Jinja2 템플릿 엔진에 기반을 둔다

=> Flask 서버를 만들 때는 항상 프로젝트 폴더 안에 static, templates 폴더와 app.py를 먼저 만들고 시작한다.

# Flask 기본 폴더구조

프로젝트 폴더 안에

- static 폴더 (이미지, css파일)
- templates 폴더 (html파일)
- app.py 파일 (통상적으로 flask 서버를 돌리는 파일 이름)

``html
# flask 시작 코드
from flask import Flask
app = Flask(__name__)    # Flask를 객체화 시켜서 app이라는 변수에 저장

# 고유 주소, 부분을 수정해서 URL을 나눌 수 있다, 
# url별로 함수명이 같거나 route('/')내의 주소가 같으면 안됨
@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  # 모듈이 실행 됨을 알림
   app.run('0.0.0.0',port=5000,debug=True)
   # 서버 실행, 파라미터로 debug 여부, port 설정 가능
``