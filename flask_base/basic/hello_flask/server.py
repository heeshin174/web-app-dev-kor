# first web page with flask
from flask import Flask

app = Flask(__name__)

# url = http://127.0.0.1:5000/ 
# is equivalent to http://localhost:5000/
# 5000 port
@app.route("/")
def index():
    return '<h2> Hello World! </h2>'


# url = http://127.0.0.1:5000/Hello
@app.route("/Hello")
def helloWorld():
    return "Hello Flask!"   


# Dynamic Route
# Different url (profile page) for different user
# url = http://127.0.0.1:5000/user/heeshin
@app.route("/user/<username>")
def userProfile(username):
    return "<h3> This is a profile page for {} </h3>".format(username)

# url만 Amazon cloud를 이용하여 실제 domain으로 바꾸면
# 다른 web page처럼 모든 사용자가 접근이 가능하다.
if __name__ == '__main__':
    app.run()