# Web Application Server 
목표: web application server을 이해하고 나만의 web app을 만들어보자.

Server vs Cilent
----
server와 cilent는 web application에서 computer가 하는 역할을 의미한다.
사람이 학교에서 학생, 선생님, 청소부와 같은 role를 맡는 것처럼,
Computer가 web app에서 server, cilent와 같은 role를 가진다.
한 computer가 server의 역할을 하고 있으면, 다른 computer가 cilent가 되어 이 server에 접근할 수 있다.
server computer는 정보를 저장하여 제공하고, cilent computer는 정보를 받는다.

```
      1.request       2.request
Client -------> Server ------>  Database
       <-------        <------
      4.response      3.get data
```

Web Application Server vs Web Server vs Server
----
Server는 한 computer가 맡는 role이다.
Web server는 한 computer를 web을 담당하는 server로 만드는 software를 의미한다.
Web Server는 program을 실행하는 것이 아니라 기본적인 html을 제공한다. 
Web Application Server에서 Application이 붙으면 program이 실행된다는 의미이다.

각각의 programming language마다 Web Application Server를 만드는 web app framework를 제공한다.

1. python: Django, Flask, CherrtPy
2. Java: spring, play
3. Javascript: express
4. php: Laravel

그 밖에도 google사에서 만든 Angular, 
Vue.js
Ruby on Rails등 다양한 Web application framework이 존재한다.

이 Web application framework은 사용방법이 거의 비슷하기 때문에 하나만 잘 이해하면,
나머지는 쉽게 사용할 수 있다.


Web Application Server 운영 방식에 차이 이해하기
----

우리가 다른 해외로 파견을 나가 작업을 해야할 때, 큰 회사의 호텔을 이용하거나, 건물을 빌려 사용할 수 있다. 

호텔을 이용하면, 빨래, 청소, 식사등 많은 것을 호텔 측에서 해주기 때문에, 나는 내가 할 작업에만 집중할 수 있다.
작업을 같이하는 인원에 변동이 생겨도, 호텔의 방을 더 빌리거나, 줄일 수 있기 때문에 인원수에 맞게 이용할 수 있다.
호텔이 모든 것을 관리하기 때문에 보안에 민감한 작업팀에게는 맞지 않다.

건물을 빌리면, 빨래, 청소, 식사등 많은 것을 직접해야 하기 때문에, 내가 할 작업에만 집중할 수 없다.
작업을 같이하는 인원에 변동이 생기면, 새로운 건물을 빌려야 한다. 
인원수에 맞게 
대신, 내가 모든 것을 관리하기 때문에 보안 문제에 더 안전하게 대처할 수 있다.

앞서 말했듯이 server는 한 computer가 맡는 role이다.
회사가 server를 운영하는 방식인 On-premise방식과 Cloud computing service 방식을 각 각 
건물을 빌리는 것과 호텔을 이용하는 것에 비유할 수 있다.

1. On-premise 방식: 
회사가 집적 물리적인 computer를 사서, 그 computer를 server로 만든다. 
이 방법은 computer를 직접 사야함으로 Cloud computing service보다 더 많은 돈이 요구된다.
black friday와 같이, 특정날에 사용자가 많아져 server를 늘리려면, 새로운 computer를 또 사야하고
이 시즌이 지나면 그 computer는 다시 사용되지 않는다. 
server를 사용자에 맞게 scale-up, scale-down하기 쉽지 않아 자원에 낭비가 생긴다.
대신, 회사가 집적 관리하기 떄문에 보안 문제에 더 안전하다.

2. Cloud computing service 방식: 
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

요약: 각 방식의 장점
On-premise: security 
Cloud computing service: money, scale-up & down, fast set up

Cloud computing service가 어디까지 service해주는 가에 따라 service를 세 가지로 나눌 수 있다.
Iaas (Infrastructure  as a service): AWS EC2 가상 머신,
Paas (platform as a service): AWS Elastic Beanstalk,
Saas (Software as a service): youtube, evernote, dropbox, Amazon Web Services (AWS)

이런 Cloud computing service의 엄청난 장점 덕분에 Cloud computing service이 대세로 떠오르고 있다.
예로 brainless machine을 생각할 수 있다. 기존에 machine을 만드려먼 그 machine에 들어갈 비싼 computer 부품들을
직접사서 조립해야 했지만, 이젠 machine이 network에 연결만 되어 있으면 Cloud computing service의 computer를 가져다 
사용하면 된다.

기존 machine: 실제 computer 부품 구매, 200만원 
brainless machine: network를 사용하여 더 좋은 computer를 더 싸게 이용, 50만원


framework와 library 차이 이해하기
----
* framework를 한국어로 하면 frame (틀), work (작업), 즉 기본적인 틀을 만드는 작업이다.
framework는 기본적인 사용방법이 존재하기 때문에 우리는 이 기본적인 뼈대에다가 살을 붙이면 된다.

* library는 특정 기능에 대한 도구 or 함수들을 모은 집합입니다. 
즉, 프로그래머가 개발하는데 필요한 것들을 모아둔 것입니다.
library는 단순 활용이 가능한 도구들의 집합

집을 만드는 작업이라고 하면, 
framework는 집의 기본 구조를 제공하여, 우리는 그 구조에 더하면 되고,
library는 침대, 소파와 같은 가구로, 우리는 이 가구들로 집을 만들어야 한다.


% 부록 Docker 이해하기 %
----
local computer에 다운되어 있는 environment와 server computer에 다운되어 있는 environment가 다르면
local에서 작성된 code는 server에서 호환성 문제로 작동이 안될 수도 있다.
이 문제를 해결하기 위해 container라는 개념이 등장하였고, 
Docker가 container를 제공하는 가장 큰 platform이다.
Docker는 서비스를 제공할 때, 아주 쉽고, 빠르고, 간단하게 같은 environment의 container를 만드는 것을 도와준다.

Dockerfile로 image를 만들고 (build),
image로 container를 실행한다 (run).

Dockerhub에서 공식적인 image을 다운 받을 수도 있고, 내가 customized한 image도 upload할 수 있다.

기본 구조: Dockerfile -build> Dokcer image -run> Docker container

* Dockerfile로 image를 build하는 commend
> $ docker bulid -t imageName
local computer에 이 이미지가 존재하지 않으면, Dockerhub에서 image을 다운 받는다.

* image로 container를 run하는 commend
> $ docker run -it imageName
> $ docker run -b imageName 
(d는 daemon의 약자로 뒤에서 작동한다.)


% 부록2 git으로 다른 programmer와 coller 하기 %
----
Git의 "main" branch는 항상 완전환 코드이어야 한다.
다른 사람이랑 협업을 할 경우에 issues, pull request를 잘 활용하여,
프로젝트를 성공적으로 완성해 보자.

issus: 코드에서 고쳐야 할 부분 
pull request: main branch에 merge하기 전에 내가 고친 코드를 다른 협업자가 관찰하고 이상이 없는 지 확인하는 단계

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