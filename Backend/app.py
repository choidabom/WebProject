# flask 기초: 서버 실행하기
# flask 시작 코드
# 파일 이름은 아무렇게나 해도 상관없지만,
# 통상적으로 flask 서버를 돌리는 파일은 app.py라고 이름을 짓는다.

from flask import Flask, render_template
# NameError: name 'render_template' is not defined/ 와 같은 에러가 떠서
# import에 render_template 추가하니 된다.

app = Flask(__name__)

# URL 별로 함수명이 같거나,
# route('/')내의 주소가 같으면 안 된다.

@app.route('/')
def home():
   return render_template('index.html')

print('Hello World')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)


# 파일을 실행해 터미널에 아래와 같은 메시지가 뜨면 성공!
# 서버를 유지하는 동안 파이썬 코드가 계속 실행 중이므로 Process finished with exit code 0.가 나오지 않습니다.

# 이제 크롬에서 http://localhost:5000/ 으로 접속했을 때 화면에 This is Home!이 나오면 성공!

# 터미널 창을 클릭하시고, ctrl + c 을 누르시면 서버를 종료할 수 있습니다. 맥에서도 Cmd가 아니라 Ctrl!

# Flask 기초: URL나누기

