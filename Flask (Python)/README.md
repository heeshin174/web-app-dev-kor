# Flask
Flask is a micro web framework written in Python.
Flask는 Python으로 구동되는 Web Framework로, 간단하게 기능을 설명하면 내가 만든 program에 server를 구동시켜주는 편한 코드 모음이라고 할 수 있다.
다른 python Web Framework인 Django 보다 라이트한 특성때문에 간단한 API서버 구축에 적합하다.
By default, Flask runs on port 5000 in development mode.

Install Flask module
---- 
> $ pip install Flask 

Setup flask Project
----
> $ mkdir flaskapp

```
flaskWeb/
├─ newFlaskApp/
│  ├─ static/
│  │  ├─ css/
│  |  ├─ images
│  |  ├─ js
│  ├─ templates/
│  │  ├─ index.html
│  ├─ server.py
├─ flaskapp/
│  ├─ static/
│  │  ├─ css/
│  |  ├─ images
│  |  ├─ js
│  ├─ templates/
│  │  ├─ index.html
│  ├─ server.py
```

한 project를 모은 directory를 Web context라고 부르고,
Web context를 전부 모은 directory를 Web Application Server라고 부른다. 

위의 tree 구조에서:
Web Application Server = flaskWeb
Web context = newFlaskApp, flaskapp

templates은 html files을 모아두는 곳이다.
static은 정적이라는 의미로 서비스를 운영하는 데 변하지 않는 것, 
server에 요청하면 연산이 없이 바로 나가는 것들, images, css, js등이 해당된다.

여기서 중요한 점은 flask를 사용할 때 "templates", "static" 이라는 이름을 변경해선 안된다. 

python source code link: https://github.com/pallets/flask/