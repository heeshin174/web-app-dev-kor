# Web Application Server

목표: Web Application Server을 이해하고 나만의 web app을 만들어보자.

## Documentations

1. Frontend Framework (client side)

- React JS (Meta): https://reactjs.org/
- Angular jS (Google): https://angularjs.org/
- Vue JS: https://vuejs.org/

2. Sytling (client side)

- Bootstrap: https://getbootstrap.com/docs/5.0
- React-Bootstrap (Reactjs framework): https://react-bootstrap.netlify.app/
- Material-UI (Reactjs framework): https://mui.com/
- React-icons (Reactjs framework): https://react-icons.github.io/react-icons
- Tailwindcss: https://tailwindcss.com/
- Google Font : https://fonts.google.com/
- React-transition-group (Reactjs framework): https://reactcommunity.org/react-transition-group/
- Redux js : https://redux.js.org/introduction/getting-started
- react-redux (Reactjs framework): https://react-redux.js.org/
- redux-thunk: https://github.com/reduxjs/redux-thunk

3. Backend Framework (server side)

- Express js: https://expressjs.com/
- Flask (python framework): https://flask.palletsprojects.com/en/2.0.x/
- Django (python framework): https://docs.djangoproject.com/en/4.0/
- nodemon (javascript framework): https://www.npmjs.com/package/nodemon)
- dotenv (javascript framework): https://github.com/motdotla/dotenv
- concurrently (javascript framework): https://github.com/open-cli-tools/concurrently

4. Databases (server side)

- Mongodb: https://www.mongodb.com/cloud
- Mongoose js (Mongodb framework): https://mongoosejs.com/
- Postgresql: https://www.postgresql.org/download/
- PG-Pool js (Postgresql framework) : https://node-postgres.com/api/pool

5. Cloud Services

- AWS (Amazon Web Services): https://aws.amazon.com/
- Azure (Microsoft): https://azure.microsoft.com/en-us/
- GCP (Google Cloud Platform): https://cloud.google.com/

6. APIs

- RapidApi: https://rapidapi.com/

7. Deployment

- github: https://github.com/
- Netlify: https://www.netlify.com/
- Heroku: https://www.heroku.com/

7. ETC

- Node js (Programming Language): https://nodejs.org/en/docs/
- Python (Programming Language): https://docs.python.org/3/
- Java (Programming Language): https://docs.oracle.com/en/java/javase/15/docs/api/index.html
- Docker (Container based development): https://www.docker.com/ & https://docs.docker.com/
- Postman (RESTful API): https://www.postman.com/downloads/
- VSCode (Microsoft IDE: Code Editor): https://code.visualstudio.com/
- Eclipse (Java IDE): https://www.eclipse.org/documentation/
- Goorm (Docker based Cloud IDE): https://www.goorm.io/
- Pythontutor (code visulaization): https://pythontutor.com/
- Figma (Design UI/UX): https://www.figma.com/
- Adobe photoshop (Design UI): https://www.adobe.com/products/photoshop
- Diagram.io (Design UI): https://app.diagrams.net/

8. Education

- Web Development In 2022 - https://www.youtube.com/watch?v=EqzUcMzfV1w&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=30&ab_channel=TraversyMedia
- 기계들의 대화법 REST API - https://www.youtube.com/watch?v=PmY3dWcCxXI&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=31&ab_channel=%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9
- 서버사이드 렌더링 - https://www.youtube.com/watch?v=iZ9csAfU5Os&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=32&ab_channel=%EB%93%9C%EB%A6%BC%EC%BD%94%EB%94%A9by%EC%97%98%EB%A6%AC
- 웹개발 개념정리 - https://www.youtube.com/watch?v=ED2rOHM1od0&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=33&ab_channel=%EA%B0%9C%EB%B0%9C%ED%95%98%EB%8A%94%EC%A0%95%EB%8C%80%EB%A6%AC
- Async Await: https://kiwanjung.medium.com/%EB%B2%88%EC%97%AD-async-await-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EC%A0%84%EC%97%90-promise%EB%A5%BC-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-955dbac2c4a4
- Closure & Hoisting: https://dongmin-jang.medium.com/javascript-closure-hoisting-7bf8eb5062b9
- Javascript closure: https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures
- w3school: https://www.w3schools.com/
- Leetcode: https://leetcode.com/
- redux 설명글: https://hwan1001.tistory.com/38

## Server vs Cilent

server와 cilent는 web application에서 computer가 하는 역할을 의미한다.
사람이 학교에서 학생, 선생님, 청소부와 같은 role를 맡는 것처럼,
Computer가 web app에서 server, cilent와 같은 role를 가진다.
한 computer가 server의 역할을 하고 있으면, 다른 computer가 cilent가 되어 이 server에 접근할 수 있다.
server computer는 정보를 저장하여 제공하고, cilent computer는 정보를 받는다.

```
      1.request (Web Application)       2.request
Client ------->      Server     ------>  Database
       <-------                 <------
      4.response                3.get data
```

Server는 한 computer가 맡는 role이다.
Web server는 한 computer를 web을 담당하는 server로 만드는 software를 의미한다.
Web Server는 program을 실행하는 것이 아니라 기본적인 html을 제공한다.
Web Server에 Application이 붙어 `Web Application Server`가 되면 program이 실행되고 server에서 어떤 연산이 이루어 진다는 의미이다.

## Web Application Server 운영 방식에 차이 이해하기

우리가 다른 해외로 파견을 나가 작업을 해야할 때, 큰 회사의 호텔을 이용하거나, 건물을 빌려 사용할 수 있다.

호텔을 이용하면, 빨래, 청소, 식사등 많은 것을 호텔 측에서 해주기 때문에, 나는 내가 할 작업에만 집중할 수 있다.
작업을 같이하는 인원에 변동이 생겨도, 호텔의 방을 더 빌리거나, 줄일 수 있기 때문에 인원수에 맞게 이용할 수 있다.
호텔이 모든 것을 관리하기 때문에 보안에 민감한 작업팀에게는 맞지 않다.

건물을 빌리면, 빨래, 청소, 식사등 많은 것을 직접해야 하기 때문에, 내가 할 작업에만 집중할 수 없다.
작업을 같이하는 인원에 변동이 생기면, 새로운 건물을 빌려야 한다.
인원수에 맞게
대신, 내가 모든 것을 관리하기 때문에 보안 문제에 더 안전하게 대처할 수 있다.

회사가 server를 운영하는 방식인 On-premise방식과 Cloud computing service 방식을 각 각
건물을 빌리는 것과 호텔을 이용하는 것에 비유할 수 있다.

1. On-premise 방식:
   회사가 집적 물리적인 computer를 사서, 그 computer를 server로 만든다.
   이 방법은 computer를 직접 사야함으로 Cloud Computing service보다 더 많은 돈이 요구된다.
   black friday와 같이, 특정날에 사용자가 많아져 server를 늘리려면, 새로운 computer를 또 사야하고
   이 시즌이 지나면 그 computer는 다시 사용되지 않는다.
   server를 사용자에 맞게 scale-up, scale-down하기 쉽지 않아 자원에 낭비가 생긴다.
   대신, 회사가 집적 관리하기 떄문에 보안 문제에 더 안전하다.

2. Cloud Computing Service 방식:
   위에서 호텔이 여려 방을 제공한다고 했는데,
   cloud computing에서는 virtualization을 이용하여 한 물리적 computer에 여러대의 가상 computer를 만들 수 있다
   (virtualBox에 ubuntu를 설치하는 것을 생각하면 된다).
   대기업에서 제공하는 Cloud computing service를 이용하면, 회사는 물리적인 computer 자원을 사지않고
   저렴한 가격에 server를 운용할 수 있다.
   black friday와 같이, 특정날에 사용자가 많아지면, server를 늘리는 일에 아주 적합하다.
   server를 사용자에 맞게 scale-up, scale-down하기 쉽기 때문에, 자원에 낭비가 없고,
   내가 사용한 만큼만 돈을 지불하면 된다 (pay-as-you-use).

```
Amazon사의 AWS (Amazon web services),
Microsoft사의 Azure,
Google사의 GCP (Google cloud platform)등이 cloud computing service를 제공하는 대표적인 사이트이다.
```

각 방식의 장점 요약:
On-premise: security
Cloud Computing service: money, scale-up & down, fast set up

Cloud Computing service가 어디까지 service해주는 가에 따라 service를 세 가지로 나눌 수 있다.
Iaas (Infrastructure as a service): AWS EC2 가상 머신,
Paas (platform as a service): AWS Elastic Beanstalk,
Saas (Software as a service): youtube, evernote, dropbox, Amazon Web Services (AWS)

이런 cloud computing service의 엄청난 장점 덕분에 대세로 떠오르고 있다.
예로, brainless machine을 생각할 수 있다. 기존에 machine을 만드려먼 그 machine에 들어갈 비싼 computer 부품들을
직접사서 조립해야 했지만, 이젠 machine이 network에 연결만 되어 있으면 cloud Computing service의 computer를 가져다
사용하면 된다.

기존 machine: 실제 computer 부품 구매, 200만원
brainless machine: network를 사용하여 더 좋은 computer를 더 싸게 이용, 50만원

## Framework vs Library

- Framework를 한국어로 하면 frame (틀), work (작업), 즉 기본적인 틀을 만드는 작업이다.
  framework는 기본적인 사용방법이 존재하기 때문에 우리는 이 기본적인 뼈대에다가 살을 붙이면 된다.

- Library는 특정 기능에 대한 도구 or 함수들을 모은 집합입니다.
  즉, 프로그래머가 개발하는데 필요한 것들을 모아둔 것입니다.
  library는 단순 활용이 가능한 도구들의 집합

집을 만드는 작업이라고 하면,
framework는 집의 기본 구조를 제공하여, 우리는 그 구조에 더하면 되고,
library는 침대, 소파와 같은 가구로, 우리는 이 가구들로 집을 만들어야 한다.

## ⭐ Frontend framework vs Server-Side Web Framework
Web App dev는 크게 Frontend, Backend, Database로 나눌 수 있고, 이 세가지를 합쳐 Fullstack dev라고 한다.
이는 MVC (Model / View / Controll) software design pattern 라고도 불린다. 
Model–view–controller is a software design pattern commonly used for developing user interfaces that divide the related program logic into three interconnected elements.

- Model은 View와 Controll을 연결하는 연결고리 역할을 한다.
- View은 client가 웹사이트에 방문하여 실제로 보게되는 회면을 의미한다. HTML (HyperText Markup Language), CSS (Cascading Style Sheets), Javascript를 이용하여 View를 작성할 수 있다. 여기서 programming language는 오직 Javascript이다.
- Controll은 app의 functionalities를 의미한다.  

각각의 programming language마다 Web Application Server를 만드는 web app framework를 제공한다.

1. python: Django, Flask, FastAPI
2. Java: spring, spring boot, play
3. Javascript: Express, Fastify
4. php: Laravel

![This is an image](./img/server_side_web_framework.png)

`Frontend framework`은 pure Javascript, HTML이 아닌 web view를 더 쉽게 작성할 수 있게 만드는 framework이다.
SPA를 제공하는 frontend framework에는 크게 React JS, Vue JS, Angular JS가 있다.
**Single Page Application** (SPA)는 body가 비어있는 하나의 HTML을 가지고 Javascript를 이용해서 그 안에 Data만 변경하는 것을 말한다.
Server가 Client에 자료를 넘겨주면, Client computer가 그 정보를 가지고 HTML를 완성하기 때문에
CSR (Client Side Rendering)이라고 부른다. CSR은 HTMl이 비어있기 때문에 검색 엔진에 노출되어 검색되기 쉽지 않다.
SEO (Search Engine Optimization)에 약점을 가진다.

⭐ `React JS`: React는 Meta사에서 만든 Javascript frontend framework로 computer에 최신 버전의 `node js`를 설치하면 누구나
쉽게 사용할 수 있다.

그 밖에도 google사에서 만든 `Angular JS`,

`Vue JS`등 다양한 Web Application Frontend framework이 존재한다.
이 Web application framework은 사용방법이 거의 비슷하기 때문에 하나만 잘 이해하면, 나머지는 쉽게 사용할 수 있다.

`Figma`, `Adobe photoshop` 등 다양한 Moderm UI/UX (web view)를 실질적으로 코드를 작성하기 전에 디자인할 수 있는 program들이 많이 존재하므로, 이를 이용하여 웹사이트를 미리 디자인 해 볼 수도 있다. 

## Server-Side Rendering (SSD)

SSD는 CSD가 가진 검색 엔진에 대한 보완을 위해 등장한 개념으로, CSD와는 다르게 Server에서 HTML을 전부 완성한 후에 Client에게 보내준다.
이로 인해 이용자가 많을 경우 Server에 과부화가 걸릴 수도 있다.

## Database

Database와 web app을 연결하여 쉽고 간단하게 data를 읽고 쓸 수 있다.
Database는 크게 Relational database (sql)와 Not only Relational database (Nosql)로 나눌 수 있다.
`sql (Structured Query Language)`

⭐ `postgresql` - Relational database의 대표주자

⭐ `Mongo Database` - Not only Relational database의 대표주자
![This is an image](./img/Database.png)

## Deploy Frontend Projects

⭐ `Netlify` - https://www.netlify.com/

`heroku`,

`Github`등을 이용해 내가 만든 웹사이트를 배포할 수 있다.

## APIs (Application Programming Interface)

API는 식당에서의 종업원과 같은 역할을 한다고 이해하면 쉽다.
Server는 음식을 만드는 요리사, Client는 음식을 주문하는 손님이다.
종업원은 손님에게 주문을 받아 요리사에게 넘겨주고, 요리사가 만든 요리를 손님에게 내어주는 역할을 한다.  
Programming에서 API는 Server와 Client을 연결해주는 역할을 한다.

## ⭐ REST APIs

APIs that conform to the REST architectural style and interacts with RESTful service
REST: Representational State Transfer

Below is a table summarizing recommended return values of the primary HTTP methods in combination with the resource URIs:

| HTTP Verb | CRUD   | Entire Collection (e.g. /customers) | Specific Item (e.g. /customers/{id})                                       |
| --------- | ------ | ----------------------------------- | -------------------------------------------------------------------------- |
| POST      | Create | 201 (Created)                       | 404 (Not Found), 409 (Conflict) if resource already exists..               |
| GET       | READ   | 200 (OK)                            | 404 (Not Found), if ID not found or invalid.                               |
| PUT/PATCH | UPDATE | 405 (Method Not Allowed)            | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
| DELETE    | DELETE | 405 (Method Not Allowed)            | 200 (OK). 404 (Not Found), if ID not found or invalid.                     |

Postman: Great program to build an RESTful web services.
- **Postman** [Postman](https://www.postman.com/downloads/)  

### 기타 Links

- Web Development In 2022 - https://www.youtube.com/watch?v=EqzUcMzfV1w&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=30&ab_channel=TraversyMedia
- 기계들의 대화법 REST API - https://www.youtube.com/watch?v=PmY3dWcCxXI&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=31&ab_channel=%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9
- 서버사이드 렌더링 - https://www.youtube.com/watch?v=iZ9csAfU5Os&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=32&ab_channel=%EB%93%9C%EB%A6%BC%EC%BD%94%EB%94%A9by%EC%97%98%EB%A6%AC
- 웹개발 개념정리 - https://www.youtube.com/watch?v=ED2rOHM1od0&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=33&ab_channel=%EA%B0%9C%EB%B0%9C%ED%95%98%EB%8A%94%EC%A0%95%EB%8C%80%EB%A6%AC
- Async Await: https://kiwanjung.medium.com/%EB%B2%88%EC%97%AD-async-await-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EC%A0%84%EC%97%90-promise%EB%A5%BC-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-955dbac2c4a4
- Closure & Hoisting: https://dongmin-jang.medium.com/javascript-closure-hoisting-7bf8eb5062b9
- Javascript closure: https://developer.mozilla.org/ko/docs/Web/JavaScript/Closures

## % 부록1 Docker 이해하기 %

local computer에 다운되어 있는 environment와 server computer에 다운되어 있는 environment가 다르면
local에서 작성된 code는 server에서 호환성 문제로 작동이 안될 수도 있다.
이 문제를 해결하기 위해 container라는 개념이 등장하였고,
Docker가 container를 제공하는 가장 큰 platform이다.
Docker는 서비스를 제공할 때, 아주 쉽고, 빠르고, 간단하게 같은 environment의 container를 만드는 것을 도와준다.

Dockerfile로 image를 만들고 (build),
image로 container를 실행한다 (run).

Dockerhub에서 공식적인 image을 다운 받을 수도 있고, 내가 customized한 image도 upload할 수 있다.

기본 구조: Dockerfile -build> Dokcer image -run> Docker container

- Dockerfile로 image를 build하는 commend

  > $ docker bulid -t imageName
  > local computer에 이 이미지가 존재하지 않으면, Dockerhub에서 image을 다운 받는다.

- image로 container를 run하는 commend
  > $ docker run -it imageName
  > $ docker run -b imageName
  > (d는 daemon의 약자로 뒤에서 작동한다.)

## % 부록2 git으로 다른 programmer와 collaboration 하기 %

Git의 "master" branch는 항상 완전환 코드이어야 한다.
다른 사람이랑 협업을 할 경우에 issues, pull request를 잘 활용하여,
프로젝트를 성공적으로 완성해 보자.

issus: 코드에서 고쳐야 할 부분
pull request: master branch에 merge하기 전에 내가 고친 코드를 다른 협업자가 관찰하고 이상이 없는 지 확인하는 단계

Git 사용법:

1. 소스 코드를 다운 받기

   > $ git clone https:...

2. Always start your branch with what is in the remote/main, so after you have cloned the repository locally
   모든 branch를 출력
   > $ git branch

branchName brannch로 이동

> $ git checkout branchName

> Your branch is up to date with 'origin/main'.

3. 새로운 branch를 만들어서 main branch 에서 만든 branch로 이동하기
   now that your local matched the most up to date stuff, switch to a branch for your own work.

> $ git switch -c branchName

4. 소스 코드에 변화를 만든 후, pull request하여 다른 협업자가 볼 수 있게 하기
   Do your thing, make some cool stuff, then when your ready to push, open terminal back up and make sure your in the base directory for the project:

Stage all your changes for commit

> $ git add .

Commit your changes

> $ git commit -m "My Commit Message, what did I do today?"

Push your commit to a remote branch (probably want to use your same local branch name)

> $ git push --set-upstream origin branchName

이 커멘드는 내가 main branch에 있을 때 사용이 가능한 경우로,
맨 처음 아무 소스 코드가 없을 경우, 맨 처음 main branch에 push하는 것이다.
main은 항상 완벽한 코드이어야 함으로 main에 직접적으로 push하는 것은 맨 처음이 마지막이다.
나중에는 위에 서술된 새로운 branch를 만들어서 pull request를 한다.

> $ git push -u origin master

## % 부록3 Amazon사의 cloud service인 AWS (Amazon Web Service) 사용하기 %

1. AWS IAM - User를 생성하고, create access key를 사용하여, API에 접근하기

2. AWS S3 - bucket을 만들어 파일 저장하기

3. AWS SES (Simple Email Service) - email 보내기

4. AWS EC2 가상환경 - virtualBox와 같이 가상 환경을 제공

5. AWS Lambda - 함수

6. AWS Elastic Beanstalk - 간단히 코드를 배포할 때 사용


# Javascript

Javascript는 web browser를 위해 등장한 programming language이기 때문에 다른 프로그래밍 언어들과는 차별점을 가진다.

1. Javascript는 비동기 프로그래밍언어(asynchronous programming) 이다.
자바스크립트의 비동기 처리란 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 특성을 의미합니다.
데이터를 불러오는데 오래걸리는 것들을 기다리지 않는다.

2. variable을 지정했는데 값을 아직 assign 안한 경우, 이 변수의 값은 undefined이 된다.

- Javascript에서 string안에 값을 변경하려면 back tic `${variable}`을 사용해야 한다.

```
const name = "Shin";
console.log(`Hello ${name}!`);
```

- object는 **{} curly braces**를 이용해서 정의한다.



## 💥 Callback vs Promises vs Async Await:

Javascript는 asynchronous programming로 데이터를 요청하는 데 시간이 많이 걸리는 line이 있으면, 그 code의 값을 기다리지 않고 다음 code를 시작한다.

비동기 처리 사례는 setTimeout()입니다. setTimeout()은 Web API의 한 종류입니다. 코드를 바로 실행하지 않고 지정한 시간만큼 기다렸다가 로직을 실행합니다. 아래 코드를 보겠습니다.

```
// #1
console.log('Hello');
// #2
setTimeout(function() {
	console.log('Bye');
}, 3000);
// #3
console.log('Hello Again');
```

비동기 처리에 대한 이해가 없는 상태에서 위 코드를 보면 아마 다음과 같은 결과값이 나올 거라고 생각할 겁니다.

```
‘Hello’ 출력
3초 있다가 ‘Bye’ 출력
‘Hello Again’ 출력
```

그런데 실제 결과 값은 아래와 같이 나오죠.

```
‘Hello’ 출력
‘Hello Again’ 출력
3초 있다가 ‘Bye’ 출력
```

setTimeout() 역시 비동기 방식으로 실행되기 때문에 3초를 기다렸다가 다음 코드를 수행하는 것이 아니라 일단 setTimeout()을 실행하고 나서 바로 다음 코드인 console.log('Hello Again');으로 넘어갔습니다. 따라서, ‘Hello’, ‘Hello Again’를 먼저 출력하고 3초가 지나면 ‘Bye’가 출력됩니다.

### Call Back Function으로 비동기 프로그램이 가진 문제 해결하기

콜백 함수의 동작 방식은 일종의 식당 자리 예약과 같습니다. 일반적으로 맛집을 가면 사람이 많아 자리가 없습니다. 그래서 대기자 명단에 이름을 쓴 다음에 자리가 날 때까지 주변 식당을 돌아다니죠. 만약 식당에서 자리가 생기면 전화로 자리가 났다고 연락이 옵니다. 그 전화를 받는 시점이 여기서의 콜백 함수가 호출되는 시점과 같습니다. 손님 입장에서는 자리가 날 때까지 식당에서 기다리지 않고 근처 가게에서 잠깐 쇼핑을 할 수도 있고 아니면 다른 식당 자리를 알아볼 수도 있습니다.

자리가 났을 때만 연락이 오기 때문에 미리 가서 기다릴 필요도 없고, 직접 식당 안에 들어가서 자리가 비어 있는지 확인할 필요도 없습니다. 자리가 준비된 시점, 즉 데이터가 준비된 시점에서만 저희가 원하는 동작(자리에 앉는다, 특정 값을 출력한다 등)을 수행할 수 있습니다.

### Promise

“A promise is an object that may produce a single value some time in the future”

Promise가 왜 필요한가요?
프로미스는 주로 서버에서 받아온 데이터를 화면에 표시할 때 사용합니다. 
일반적으로 웹 애플리케이션을 구현할 때 서버에서 데이터를 요청하고 받아오기 위해 아래와 같은 API를 사용합니다.

```
app.get('url 주소/products/1', function(response) {
  // ...
});
```

위 API가 실행되면 서버에다가 ‘데이터 하나 보내주세요’ 라는 요청을 보내죠. 그런데 여기서 데이터를 받아오기도 전에 마치 데이터를 다 받아온 것 마냥 화면에 데이터를 표시하려고 하면 오류가 발생하거나 빈 화면이 뜹니다. 이와 같은 문제점을 해결하기 위한 방법 중 하나가 Promise이다.

There are 3 states of the Promise object:

프로미스를 사용할 때 알아야 하는 가장 기본적인 개념이 바로 Promise의 상태(states)입니다. 여기서 말하는 상태란 프로미스의 처리 과정을 의미합니다. new Promise()로 프로미스를 생성하고 종료될 때까지 3가지 상태를 갖습니다.

- Pending(대기) : Initial State, before the Promise succeeds or fails. 비동기 처리 로직이 아직 완료되지 않은 상태
- Fulfilled(이행) : Completed Promise. 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
- Rejected(실패) : Failed Promise, throw an error. 비동기 처리가 실패하거나 오류가 발생한 상태

The Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.
If the promise gets rejected, it will jump to the catch() method.

프로미스 에러 처리는 가급적 catch()를 사용한다.

`mongoose.connect()`는 Promise를 return한다. Promise가 성공적으로 return되면, .then()에 정의된 callback function을 Promise가 reject되면 에러가 발생하여 .catch()에 정의된 callback function을 실행한다.

```
mongoose
  .connect()
  .then(() => console.log("MongoDB Connected..."))
  .catch((err) => console.log(err.massage));
```

### 💥 Async & Await

Await is basically syntactic sugar (사람이 이해하기 쉽게 만든 것) for Promises. It makes your asynchronous code look more like synchronous/procedural code, which is easier for humans to understand.

async와 await는 자바스크립트의 비동기 처리 패턴 중 가장 최근에 나온 문법입니다. 기존의 비동기 처리 방식인 콜백 함수와 프로미스의 단점을 보완하고 개발자가 읽기 좋은 코드를 작성할 수 있게 도와주죠. 여기서 개발자가 읽기 좋은 코드란 code를 위에서 아래로 순차대로 실행할 수 있는 코드를 의미합니다. 우리는 위에서부터 아래로 한 줄 한 줄 차근히 읽으면서 사고하는 것이 편합니다. 그렇게 프로그래밍을 배웠으니까요.
async/await의 기반은 promise라는 사실은 매우 중요하다. 사실, 우리가 쓰는 모든 async 함수는 promise를 리턴하고, 모든 await 함수는 일반적으로 promise가 됩니다.

The await keyword is used in an async function to ensure that all promises returned in the async function are synchronized. Await eliminates the use of callbacks in .then() and .catch(). In using async and await, async is prepended when returning a promise, await is prepended when calling a promise. try and catch are also used to get the rejection value of an async function.

async & await 기본 문법:

이제 async await의 기본 문법을 알아보겠습니다.

```
async function 함수명() {
  await 비동기_처리_메서드_명();
}
```

먼저 함수의 앞에 async 라는 예약어를 붙입니다. 그러고 나서 함수의 내부 로직 중 HTTP 통신을 하는 비동기 처리 코드 앞에 await를 붙입니다. 여기서 주의하셔야 할 점은 **비동기 처리 메서드가 꼭 프로미스 객체를 반환**해야 await가 의도한 대로 동작합니다.

일반적으로 await의 대상이 되는 비동기 처리 코드는 Axios 등 프로미스를 반환하는 **API 호출 함수**입니다.

async & await 예외 처리:

async & await에서 예외를 처리하는 방법은 바로 try catch입니다. 프로미스에서 에러 처리를 위해 .catch()를 사용했던 것처럼 async에서는 catch {} 를 사용하시면 됩니다.

```
app.get("/", async (req, res) => {
  try {
    const items = await Item.find().sort({ date: -1 });
    if (!items) throw Error("No items");

    res.status(200).json(items);
  } catch (err) {
    console.error(err.message);
  }
});
```

### Promise를 Async/Await으로 변환하기

Promise 방식:
```
function getFirstUser() {
    return getUsers()
       .then(function(users) {
          return users[0].name;})
       .catch(function(err) {
        return {
          name: 'default user'
        };
    });
}
```

Async/Await 방식:
```
async function getFirstUser() {
    try {
        let users = await getUsers();
        return users[0].name;
    } catch (err) {
        return {
            name: 'default user'
        };
    }
}
```

자, 이제 promise로 구현하는 법과 async/await로 구현하는 법이 있다는 걸 알았습니다. 그럼 왜 promise를 알아야 하는걸까요?

1. 기다리지(await) 않는 상황
   만약 그냥 호출한다면,
   
   `let users = getFirstUser();`
   
   기다리지(await) 않았지만, 자동으로 error를 뿜지 않습니다!
   사실, await를 써야하는 의무는 없어요. 단지 쓰지 않는다면, user는 resolved 값이 아니라 promise 객체를 가리킬거에요. 그리고 많은 것들을 할 수 없게 되겠죠.
   javascript는 엄격한 타입선언을 하지 않기 때문에, user 변수로 무언가를 할때까지 드러나지 않을거고 아마 내가 원하는 곳에서 null 값을 줄거에요.
   비동기 함수가 저절로 wait 하지 않는다는 사실을 잊지 마세요.
   당신이 반드시 await 해야합니다. 하지 않는다면 예상한 값 대신에 promise 객체를 받게 될거에요.
   물론 promise 객체를 받아오도록 의도한거라면 괜찮아요. 그러면 promise 객체로 더 많은 것을 컨트롤 할 수 있습니다. 예를 들면 memoizing promises 같은 것들이요.

이 글의 중요한 점은 
💥 **promise를 이해하지 못하면 async/await를 사용하면서 진짜 진짜 이해하기 어려운 케이스와 버그를 만나게 된다**


## 💥 Javascript Closure & Hoisting

호이스팅(Hoisting)의 개념: 함수 안에 있는 선언들을 모두 끌어올려서 해당 함수 유효 범위의 최상단에 선언하는 것을 말한다.

- 자바스크립트 함수는 실행되기 전에 함수 안에 필요한 변수값들을 모두 모아서 유효 범위의 최상단에 선언한다.
  자바스크립트 Parser가 함수 실행 전 해당 함수를 한 번 훑는다.
  함수 안에 존재하는 변수/함수선언에 대한 정보를 기억하고 있다가 실행시킨다.
  유효 범위: 함수 블록 {} 안에서 유효

- 즉, 함수 내에서 아래쪽에 존재하는 내용 중 필요한 값들을 끌어올리는 것이다.
  실제로 코드가 끌어올려지는 건 아니며, 자바스크립트 Parser 내부적으로 끌어올려서 처리하는 것이다.
  실제 메모리에서는 변화가 없다.

Hoisting 대상:

**var 변수 선언**과 **function 함수선언문**에서만 호이스팅이 일어난다.
  var 변수/함수의 **선언**만 위로 끌어 올려지며, **할당**은 끌어 올려지지 않는다.
  let/const 변수 선언과 함수표현식에서는 호이스팅이 발생하지 않는다.

```
// Javascript에서는 변수/함수가 program에 정의되어 있으면, program내에 어느 곳에서도 접근이 가능하다.
// getName()의 호출보다 getName()의 정의가 더 늦게 되지만, 함수선언문으로 정의된 함수는 접근가능하다. 
getName();  // Shin

// x는 정의되어 있지만, 7이란 값을 받기 전이므로, x의 값은 undefined이다.
console.log(x); // undefined
// y는 program에 정의되어 있지 않기 때문에, error가 발생한다.
console.log(y); // uncaught referenceError: y is not defined

// arrow function이나 함수표현식으로 작성한 함수는 var변수에 담겨있기 때문에, 
// 함수를 assign하기 전에는 위의 x처럼 variable로 다뤄진다.
getID(); // uncaught typeError: getID is not a function
getID; // undefined

var x = 7;
function getName() {
    console.log("Shin");
}

var getID = () => {
    console.log("ID1");
};
```

간단한 예시 (var 변수 vs let/const 변수)

```
console.log("hello");
var myname = "HEEE"; // var 변수
let myname2 = "HEEE2"; // let 변수
```

```
// 위의 결과와 동일하다.
// 이처럼 var로 정의된 변수들은 값을 assign하기 전에 프로그램의 맨 위로 올라오게 된다.
var myname; // [Hoisting] "선언"
console.log("hello");
myname = "HEEE"; // "할당"
let myname2 = "HEEE2"; // [Hoisting] 발생 X
```


간단한 예시 (함수선언문 vs 함수표현식)

```
foo();
foo2();

function foo() { // 함수선언문
console.log("hello");
}
var foo2 = function() { // 함수표현식
console.log("hello2");
}
```

```
// 위와 동일
var foo2; // [Hoisting] 함수표현식의 변수값 "선언"

function foo() { // [Hoisting] 함수선언문
console.log("hello");
}

foo();
foo2(); // undefined

foo2 = function() {
console.log("hello2");
}
```

Hoisting 함수선언문과 함수표현식에서 서로 다르게 동작하기 때문에 주의해야 한다.
변수에 할당된 함수표현식은 끌어 올려지지 않기 때문에 이때는 변수의 스코프 규칙을 그대로 따른다.

**Hoisting 우선순위:**

- 같은 이름의 var 변수 선언과 함수 선언에서의 호이스팅
- 변수 선언이 함수 선언보다 위로 끌어올려진다.

```
var myName = "hi";

function myName() {
console.log("yuddomack");
}

function yourName() {
console.log("everyone");
}

var yourName = "bye";

console.log(typeof myName);
console.log(typeof yourName);
```

```
// Hoisting의 결과
// 1. [Hoisting] 변수값 선언
var myName;
var yourName;

// 2. [Hoisting] 함수선언문
function myName() {
console.log("yuddomack");
}
function yourName() {
console.log("everyone");
}

// 3. 변수값 할당
myName = "hi";
yourName = "bye";

console.log(typeof myName); // > "string"
console.log(typeof yourName); // > "string"
```

값이 할당되어 있지 않은 변수와 값이 할당되어 있는 변수에서의 호이스팅

```
var myName = "Heee"; // 값 할당
var yourName; // 값 할당 X

function myName() { // 같은 이름의 함수 선언
console.log("myName Function");
}
function yourName() { // 같은 이름의 함수 선언
console.log("yourName Function");
}

console.log(typeof myName); // > "string"
console.log(typeof yourName); // > "function"
```

- 값이 할당되어 있지 않은 변수의 경우, 함수선언문이 변수를 덮어쓴다.
- 값이 할당되어 있는 변수의 경우, 변수가 함수선언문을 덮어쓴다.

TIP Hoisting 사용 시 주의:

- 코드의 가독성과 유지보수를 위해 Hoisting이 일어나지 않도록 한다.
  호이스팅을 제대로 모르더라도 함수와 변수를 가급적 코드 상단부에서 선언하면, Hoisting 인한 스코프 꼬임 현상은 방지할 수 있다.
  let/const를 사용한다.
  
- var를 쓰면 혼란스럽고 쓸모없는 코드가 생길 수 있다. 그럼 왜 var와 호이스팅을 이해해야 할까?
  ES6를 어디에서든 쓸 수 있으려면 아직 시간이 더 필요하므로 ES5로 트랜스컴파일을 해야한다.
  따라서 아직은 var가 어떻게 동작하는지 이해하고 있어야 한다.


## JavaScript 모듈 시스템

1. Node.js의 module 시스템: CommonJS (module.exports, require)
2. Javascript ES6부터는 브라우저 단에서도 쉽게 JavaScript의 모듈화가 가능하도록 모듈 시스템이 추가되었다. (export, import)
   ES6 fashion을 사용하려면 ES6를 ES5로 바꿔주는 babel complier가 필요하다.

### CommonJS (module.exports, require)

Node.js 환경에서 실행되는 JavaScript는 모듈 시스템으로서 CommonJS 방식을 지원한다. 이 방식에서는 `module.exports` 객체를 이용하여 자신의 데이터를 외부로 내보낼 수 있고, `require()` 함수를 이용하여 외부 모듈의 데이터를 불러올 수 있다. 만약 Babel 등의 컴파일러를 사용한다면 뒤에서 설명할 ES6 기반의 모듈 내보내기 및 불러오기 방식을 사용해도 알아서 module.exports 객체 및 require() 함수 기반의 방식으로 변환될 것이다.

자신의 데이터를 외부로 내보내려면 module.exports 변수에 내보내고자 하는 데이터들을 담은 객체를 지정해주면 된다.

```
// Item.js file
const Item = mongoose.model("item", ItemSchema);

// export Item variable, so that other files can access Item variable.
module.exports = Item;
```

외부 모듈의 데이터를 불러오려면 require("경로") 함수의 반환 값을 변수에 대입하면 된다. require() 함수가 반환하는 것은 해당 모듈의 module.exports 객체이다.

```
// Items.js file
const Item = require(".models/Item");
```

### ES6 with babel complier (export, import)

이는 브라우저 단에서도 쉽게 JavaScript의 모듈화가 가능하도록 ES6부터 도입된 방식이다. 모듈화 시스템답게 각각의 모듈(파일)마다 독립적인 파일 스코프를 가지고 있어서, 모듈 내에 var로 선언한 변수는 더 이상 window 객체의 프로퍼티가 아닌 파일 스코프의 변수로 존재하게 된다. 즉 기본적으로는 다른 모듈의 데이터를 참조할 수 없기 때문에 충돌도 발생하지 않는다.

이때 다른 모듈의 데이터를 참조하거나 자신의 데이터를 노출시키고 싶을 때 사용하는 것이 바로 export, import 키워드이다.

```
이러한 모듈 시스템을 브라우저에서 사용하려면 <script> 태그에 type="module" 어트리뷰트를 추가해야 한다.
그러면 그 안에 작성된 JavaScript 코드들은 ES6 기반의 모듈 내보내기 및 불러오기 방식을 지원하게 된다.
이때 불러오는 파일이 모듈임을 명확히 하기 위해 <script type="module"> 태그로 불러오는 JavaScript 파일의 확장자는 mjs로 설정하도록 권장되고 있다.
```

ES6 기반의 모듈 시스템은 CommonJS 방식에 비해 코드의 직관성이 좋고, 비동기 방식으로 작동하면서 불러오는 모듈의 실제로 사용되는 부분들만 로드하기 때문에 성능적으로도 효율적이라고 할 수 있다. 그러나 이는 아래와 같은 단점들을 가지고 있어서 아직까지는 Webpack 등의 모듈 번들러를 이용하여 미리 의존성이 해결된 형태의 번들 JavaScript 파일을 제공하는 방식이 더 선호되는 경향이 있다.

- IE(인터넷 익스플로러)를 포함한 몇몇 구형 브라우저는 ES6 모듈 시스템을 지원하지 않는다.
- 브라우저의 ES6 모듈 시스템을 사용하더라도 어차피 트랜스파일링이나 번들링은 필요하다.
  = 아직 지원하지 않는 기능(Bare import 등)들이 꽤 있다. (ECMAScript modules in browsers 참고)
- 점차 해결되고는 있지만 아직 몇 가지 이슈가 있다. (ECMAScript modules in browsers 참고)

모듈 내보내기 (export)

```
// Named Export : 정해진 이름으로 내보내기
export 변수/함수/클래스 선언문;
export { 변수명/함수명/클래스명 };
export { 변수명/함수명/클래스명 as 다른 이름 };

// Default Export : 기본 내보내기 (이름을 정하지 않음. 최대 하나만 가능.)
export default 선언문 또는 값;
export { 변수명/함수명/클래스명 as default };
```

모듈 불러오기 (import)

```
import A, { B, C } from 경로; // A는 Default Export, B와 C는 Named Export

import { B as b, C as c } from 경로; // 원하는 이름으로 로드

import \* as obj from 경로; // Export 된 모든 것들을 하나의 객체 형태로 로드 (불필요한 것도 가져오면 번들링 시 비효율을 야기)

import { default as A } from 경로; // "import A from 경로"와 동일 (default)
```

### ReactJS에서 NPM 패키지 모듈 불러오기

NPM 패키지 모듈들은 **CommonJS**를 기본 모듈 시스템으로 채택한다.

즉, 모듈을 내보내고 불러오는 것에 있어 require, module.exports 등을 사용한다는 말이다.

그러나 실제로 ReactJS 등의 라이브러리를 활용하여 Frontend 개발을 할 때는 NPM 패키지 모듈을 불러오기 위해 ES6 문법의 코드를 작성하는 경우가 많다(import, export 등). 

그런데 왜 문제가 발생하지 않을까? 이는 Babel 등의 컴파일러가 import, export 등의 코드를 CommonJS 기반의 코드로 변환해주기 때문이다. 
그러고 나면 Webpack에 의해 JavaScript 모듈들의 번들링이 가능해진다. 변환 규칙은 대략 다음과 같다(실제로는 더 복잡할 수 있다).


### ES6 import 사용법

Node has experimental support for ES modules. To enable them we need to make some changes to the package.json file. Before following the steps make sure that Node is installed. Below are the steps to achieve the same.

CommonJS를 모듈 시스템을 채택했던 Node.js에서는 import, export와 같은 ES 모듈을 사용하려면 Babel과 같은 트랜스파일러(transpiler)를 사용했어야 했는데요. 

ode.js 버전 13.2부터 ES 모듈 시스템에 대한 정식 지원이 시작됨에 따라 다른 도구 없이 Node.js에서 손쉽게 ES 모듈을 사용할 수 있게 되었습니다. 🎉

1. 프로젝트 단위로 ES 모듈 적용: 

In the package.json file add **“type” : “module”**. Adding this enables ES6 modules.
The package.json file should look like this:

Node.js에서 ES 모듈을 사용하는 두번째 방법은 package.json 파일 설정을 통해 전체 파일에 적용하는 것입니다. 모든 파일의 확장자를 일일이 바꾸지 않고, 프로젝트 전체에 ES 모듈을 적용하고 싶을 때 적합한 방법입니다.

먼저 프로젝트의 package.json 파일을 열고, 최상위에 type 항목을 module로 설정합니다.

package.json 생성

> `npm init`

```
//package.json
{
  "name": "index",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

2. 파일 단위로 ES 모듈 적용:

Node.js에서 ES 모듈을 사용하는 방법은 파일의 확장자를 js 대신에 mjs를 사용하는 것입니다. 프로젝트에서 부분적으로 ES 모듈을 사용할 때 가장 쉽고 빠르게 적용할 수 있는 방법입니다.

time.js와 time.test.js 파일의 확장자를 mjs 바꾸고, ES 모듈의 import와 export 키워드를 사용하도록 코드를 수정합니다.

```
// time.mjs
import moment from "moment";

export function now() {
return moment().format();
}
```

```
// time.test.mjs
import { now } from "./time";

console.log("Now:", now());
```

time.test.mjs 파일을 실행을 해보면 Node.js가 time 모듈을 찾지 못하는 현상을 보게 되실 겁니다.

$ node src/time.test.mjs
internal/modules/run_main.js:54
internalBinding('errors').triggerUncaughtException(
^

Error [ERR_MODULE_NOT_FOUND]: Cannot find module 

이 부분이 Node.js에서 ES 모듈울 처음 사용할 때 가장 많이 실수를 하게되는 부분인데요. Node.js에서 import 키워드로 프로젝트 내부 모듈을 불러올 때는 반드시 **확장자까지 포함**해서 경로를 명시를 해줘야 합니다. 이는 브라우저에서 import가 작동하는 방식과 맞추기 위해서 의도적으로 설계된 부분이라고 합니다.

확장자를 포함해서 경로를 명시해주면 정상적으로 작동합니다.

```
// time.test.mjs
import { now } from "./time.mjs";

console.log("Now:", now());
$ node src/time.test.mjs
Now: 2020-05-23T18:10:20-04:00
```

이상으로 Node.js에서 ES 모듈의 import와 export 키워드를 사용하는 2가지 방법에 대해서 알아보았습니다. 참고로 Node.js 버전 13.2 미만에서도 버전 12 이상에서는 Node.js를 실행할 때 --experimental-module 옵션을 넘기면 동일한 방법으로 ES 모듈을 사용할 수 있으니 참고바라겠습니다.

## JSX에 대해 

react js는 js 대신 jsx라는 특수한 extension을 사용한다. 하지만 js를 사용해도 아무런 문제는 없다.

아래 변수 선언을 살펴봅시다.

> `const element = <h1>Hello, world!</h1>;`

위에 희한한 태그 문법은 문자열도, HTML도 아닙니다.

JSX라 하며 JavaScript를 확장한 문법입니다. UI가 어떻게 생겨야 하는지 설명하기 위해 React와 함께 사용할 것을 권장합니다. JSX라고 하면 템플릿 언어가 떠오를 수도 있지만, JavaScript의 모든 기능이 포함되어 있습니다.

JSX는 React “엘리먼트(element)” 를 생성합니다.

React는 JSX 사용이 필수가 아니지만, 대부분의 사람은 JavaScript 코드 안에서 UI 관련 작업을 할 때 시각적으로 더 도움이 된다고 생각합니다. 또한 React가 더욱 도움이 되는 에러 및 경고 메시지를 표시할 수 있게 해줍니다.

아래 예시에서는 name이라는 변수를 선언한 후 중괄호로 감싸 JSX 안에 사용하였습니다.

```
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

JSX의 중괄호 안에는 유효한 모든 JavaScript 표현식을 넣을 수 있습니다. 예를 들어 2 + 2, user.firstName 또는 formatName(user) 등은 모두 유효한 JavaScript 표현식입니다.

컴파일이 끝나면, JSX 표현식이 정규 JavaScript 함수 호출이 되고 JavaScript 객체로 인식됩니다.

즉, JSX를 if 구문 및 for loop 안에 사용하고, 변수에 할당하고, 인자로서 받아들이고, 함수로부터 반환할 수 있습니다.

### ES7+ React/Redux/React-Native snippets

VScode extension인 `ES7+ React/Redux/React-Native snippets`을 download하면 `rafce`만 code에 입력하면 arrow function이 자동적으로 완성된다.

이는 React Js 코드 특히 components를 작성할 떄, 매우 간편하게 사용할 수 있다.

```
// rafc
import React from 'react';

export const $1 = () => {
  return <div>$0</div>;
};

// rafce
import React from 'react';

const $1 = () => {
  return <div>$0</div>;
};

export default $1;
```

## Bootstrap and Reactstrap  or Material-Ui

`bootstrap`은 frontend dev에 대한 구조를 미리 만들어둔 프레임워크로 UI stlye에 대한 기본적인 css, js를 제공합니다.
react js 뿐만 아니라 frontend dev 전체에 사용할 수 있는 매우 유용한 프레임워크입니다.

1. client/public에 있는 index.html에 bootstrap homepage에 있는 css link tag, js script tag을 copy & paste해서 bootstrap을 사용하는 방법이 있고,
2. source code를 copy & paste하는 방법이 있고,
3. npm package manager를 이용해 `npm install bootstrap`을 이용하여 사용할 수 있다.

bootstrap: https://getbootstrap.com/docs/5.1/getting-started/download/

`reactstrap`은 bootstrap component를 react component로 사용할 수 있게 만들어 주는 framework이다.

`material-ui`은 `reactstrap`처럼 다른 프로그래머가 미리 만들어둔 react component를 가져다 쓸 수 있기 떄문에 매우 편하다.
이처럼 다른 사람이 만들어둔 source code를 찾아 copy & paste만 잘해도 된다.

reactstrap: https://reactstrap.github.io/?path=/docs/components-navbar--navbar

material-ui는 react js에서 쓸 수 있는 react components을 모아둔 framework이다.

material-ui가 2022년 기준 react js에서 가장 많이 쓰이는 framework이다.

`material-ui`은 `reactstrap`처럼 다른 프로그래머가 미리 만들어둔 react component를 가져다 쓸 수 있기 떄문에 매우 편하다.
이처럼 다른 사람이 만들어둔 source code를 찾아 copy & paste만 잘해도 된다.

material-ui: https://mui.com/

## Curly brackets  {} vs Parentheses () in Javascript Arrow Function

### In Javascript:

- Curly brackets: after an arrow function they represent a code block, which consists of zero or more grouped statements within the curly brackets.

arrow function에서 body부분에 Curly brackets가 쓰이면 이는 code block, 즉 여러개의 code를 묶어 놓은 것으로 인식하기 떄문에 `return` keyword가 다른 function들 처럼
반드시 필요하다.

`return`이 없으면, 이 함수는 local variable만 생성할 뿐 값을 만들어 내지 않기 떄문에, 값이 `undefined`가 된다.

```
const jsBrackets = x => {
return x > 3 ? true : false
}
```

If the function can be written on one line (as the example above can, it can be shortened to exclude both the curly brackets and the return word, as below.

`const jsBrackets = x => x > 3 ? true : false`

- Parentheses: are used instead of curly brackets after an arrow function to return an object. 

For example, they are used in map, filter, and reduce functions.

```
const numbers = [1,2,3,4]
// OKAY
numbers.map(number => number \* 2)
numbers.map(number => (number \* 2))
numbers.map(number => {return number \* 2})

// 위의 세 경우와 다르게 return keyword가 없는 code block은 반환값이 없어 undefined값이 된다.
const newnumbers = numbers.map(number => {number \* 2});
console.log("newnumbers");
```

이를 확인하려면, browser에서 F12를 열거나, 마우스 오른쪽 클릭 후 inspect를 클릭해 개발자 모드로 들어간다.

Source tab에서 js파일에 breakpoint를 걸고 실행시켜보면, scope/global scope을 통해 값을 볼 수 있다.

### Using JSX in React:

- Curly brackets: are a special syntax to let the JSX parser know that it needs to interpret the contents between them as javascript instead of text.

`const items =this.state.toDoList.map((item) => <li>{item}</li> )`

Since {item} is in curly brackets JSX interprets that as to find the variable item back in javascript land and to insert it within the `<li></li>`s.

- Parentheses: are used to wrap multiline codes of Javascript after the return statement in order for your code to compile.

```
render () {
return ( <li> {item}</li>,
<SomeComponent /> )
}
```

If you only have one line of code, you don’t need the parentheses.

```
render () {
return <li> {item}</li>
}
```

```
// jsx syntax
const items = { {id: 1, name: eggs}, {id: 2, name: milk} }
{ items.map(item => (
 <tr key={items.id}>
    <td>{ items.name }</td>
 <tr>
)) }
```

react js를 이용할 때, javascript 코드를 jsx syntax에서 사용하고 싶으면 curly brackets {} 안에서 정의하면 된다.
react js에서 array를 하나씩 iterate해야할 경우 `array.map()` 함수를 이용하고, 그 안에 callback함수인 arrow function을 정의한다.

react js는 jsx이기 때문에 `array.map((param) => {body})`가 아니라 `array.map((param) => (body))`처럼 body에도 parentheses를 사용해야 한다.

`map()`은 javascript code이기 때문에 `{ array.map((param) => (body))}`과 같이 curly brackets {} 안에서 정의하면 된다.
