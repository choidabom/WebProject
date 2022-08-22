# Flask
- 간단한 웹 사이트, 혹은 간단한 API 서버를 만드는 데에 특화 되어있는 **Python Web Framework**
- Werkzeug 툴킷과 Jinja2 템플릿 엔진에 기반을 둔다

=> Flask 서버를 만들 때는 항상 프로젝트 폴더 안에 static, templates 폴더와 app.py를 먼저 만들고 시작한다.

## Flask 기초: 기본 폴더구조

프로젝트 폴더 안에 static 폴터, templates 폴더, app.py로 구성되어 있다.

- **static 폴더 (이미지, css파일)**
- **templates 폴더 (html파일)**
- **app.py 파일 (통상적으로 flask 서버를 돌리는 파일 이름)**

```python
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
```

## Flask 기초: HTML 파일 불러오기
1. 간단한 index.html 파일을 templates 안에 만든다.
- templates 폴더의 역할
    - HTML 파일을 담아두고, 불러오는 역할을 한다.
2. html 파일 불러오기
- **flask 내장함수 render_template를 이용**

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
```
<!-- http://localhost:5000/ 에서 해당 html이 뜨는 것을 확인한다. -->

## Flask 기초: HTML 파일 내 이미지를 불러오기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
			integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
		  crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <h1>서버를 만들었다!</h1>
    <!-- <img src="../static/rome.jpg"/> => 일반 HTML에서 파일을 불러온다면 이런 방식으로 쓰임.-->

    <!-- Flask에서 띄울 때 이미지를 불러오는 방법은 다음과 같다. -->
    <img src="{{ url_for('static', filename='rome.jpg') }}"/>
</body>
</html>
```
- 위와 같이 적으면 flask가 html 정보를 보내줄 때 {{ }} 안의 내용을 상황에 맞게 바꿔 보내준다.
- 따옴표와 중괄호의 위치에 주의해야함.
- 저장 후에 app.py를 실행하고 http://localhost:5000/에 가서 개발자 도구 > Elements에 가서 보면 <img src="/static/rome.jpg"/> 처럼 들어가 있다..!

## API 만들기
- **GET** : 데이터 조회(Read)
- **POST** : 데이터 생성(Create), 변경(Update), 삭제(Delete)

#### GET
- 통상적으로! 데이터 조회(Read)를 요청할 때
   - 예) 영화 목록 조회
- 데이터 전달: URL 뒤에 물음표를 붙여 key=value로 전달
   - 예) google.com?q=북극곰

#### POST
- 통상적으로! 데이터 생성(Create), 변경(Update), 삭제(Delete)
   - 예) 회원가입, 회원탈퇴, 비밀번호 수정
- 데이터 전달: 바로 보이지 않는 HTML body에 key:value 형태로 전달

### GET 요청 API코드
```python
@app.route('/test', methods=['GET']) # url: /test, type: GET
def test_get():
   title_receive = request.args.get('title_give') # 'title_give'값 가져오기
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
```

### GET 요청 확인 Ajax코드
```python
$.ajax({
    type: "GET",
    url: "/test?title_give=봄날은간다", # URL뒤에 ?를 붙여 key=value로 전달
    data: {},
    success: function(response){
       console.log(response)
    }
  })
```

### POST 요청 API코드

```python
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give'] # 'title_give'로 가져온 값
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
```

### POST 요청 확인 Ajax코드
```python
$.ajax({
    type: "POST",
    url: "/test",
    data: { title_give:'봄날은간다' }, # API코드에 가져온 값 이름이랑 똑같이 해줘야함
    success: function(response){
       console.log(response)
    }
  })
  
# (INTERNAL SERVER ERROR) 서버쪽에서 에러가 났을 때
# app.py의 에러를 확인 해야됨
```