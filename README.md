# Web Application Development Korean ver

목표: Web Application Development을 이해하고 나만의 web app을 만들어보자.

아래의 내용은 간단한 개념위주로, 개념만 공부해서는 이해하기 힘들다. **실제 project를 만들면서** 필요한 부분들을 이 곳에서 참고히면 된다.

## Table of Contents

0. [Web Development Loadmap](https://github.com/heeshin174/Web_App_Dev_Kor#0-web-development-loadmap)

- [FrontEnd](https://github.com/heeshin174/Web_App_Dev_Kor#2-front-end-client-side)
  1. [HTML](https://github.com/heeshin174/Web_App_Dev_Kor#1-html)
  2. [CSS](https://github.com/heeshin174/Web_App_Dev_Kor#2-css)
  3. [JavaScript](https://github.com/heeshin174/Web_App_Dev_Kor#3-javascript)
  4. [TypeScript](https://github.com/heeshin174/Web_App_Dev_Kor#4-typescript)
  5. [React.js](https://github.com/heeshin174/Web_App_Dev_Kor#5-reactjs)
  6. [Vue.js](https://github.com/heeshin174/Web_App_Dev_Kor#6-vuejs)
  7. [Next.js](https://github.com/heeshin174/Web_App_Dev_Kor#7-nextjs)
  8. [Remix](https://github.com/heeshin174/Web_App_Dev_Kor#8-remix)
  9. [Redux](https://github.com/heeshin174/Web_App_Dev_Kor#9-redux)

- [BackEnd](https://github.com/heeshin174/Web_App_Dev_Kor#3-back-end-server-side)
  1. [Web Application Development](https://github.com/heeshin174/Web_App_Dev_Kor#1-web-application-development)
  2. [Express.js](https://github.com/heeshin174/Web_App_Dev_Kor#2-expressjs)
  3. [Flask.py (Python)](https://github.com/heeshin174/Web_App_Dev_Kor#3-flaskpy-python)
  4. [Postgresql](https://github.com/heeshin174/Web_App_Dev_Kor#4-postgresql)
  5. [Mongodb](https://github.com/heeshin174/Web_App_Dev_Kor#5-mongodb)
  6. [RocketRs (Rust)](https://github.com/heeshin174/Web_App_Dev_Kor#6-rocketrs-rust)

## 0. Web Development Loadmap

- [Youtube Link](https://www.youtube.com/watch?v=TTLHd3IyErM&list=PLg8KC9DusHl_fxr5tZgwvoHE5SbPnKm_q&index=2)
  1. [Basic Setup](https://github.com/heeshin174/Web_App_Dev_Kor#1-basic-setup)
  2. [Front-End](https://github.com/heeshin174/Web_App_Dev_Kor#2-front-end-client-side)
  3. [Back-End](https://github.com/heeshin174/Web_App_Dev_Kor#3-back-end-server-side)
  4. [Tools](https://github.com/heeshin174/Web_App_Dev_Kor#4-tools)
  5. [Testing](https://github.com/heeshin174/Web_App_Dev_Kor#5-testing)
  6. [Publish](https://github.com/heeshin174/Web_App_Dev_Kor#6-publish)
  7. [기타 유용한 links](https://github.com/heeshin174/Web_App_Dev_Kor#%EA%B8%B0%ED%83%80-%EC%9C%A0%EC%9A%A9%ED%95%9C-links)

### 1. Basic Setup

- Computer
  - MacOS
  - Windows (+ **WSL**: Window subsystem for Linux)
  - Linux
- Browser
  - **Chrome**
  - Edge
  - Safari (MacOS)
  - **Brave browser**
- Text Editor
  - ⭐ **VSCode** (+ VSCode extension)
  - IntelliJ
  - Emac
  - Vim
  - Atom
- Terminal
  - **Window Terminal** (Windows, + Ubuntu)
  - **Iterm2** (MacOS)
  - Powershell (Windows)
  - Bash
  - zsh
- Other Tools
  - Programming Langauges (Node.js, Python, Java, ...)
  - nvm (Node Version Manager)
  - Git/Github
- OS별 개발환경 세팅:
  - Macbook developer setup: https://www.youtube.com/watch?v=B26yiuC5zPM
    - Homebrew (MacOS package manager): https://brew.sh/
  - Window developer setup (+ WSL): https://nomadcoders.co/windows-setup-for-developers
    - Chocolatey (Window package manager): https://chocolatey.org/

#### Windows Developer Setup (WSL)

1. Microsoft Store에서 `Windows Terminal`와 `Ubuntu` 다운로드
2. Google에 `WSL2` 검색 후 Terminal로 설치. 그 후 `Ubuntu`를 WSL1에서 WSL2로 update
3. Google에 `VSCode` 검색 후 download, 그 후 VSCode extension 설치

이제 `Windows Terminal`로 `Ubuntu`를 실행할 수 있다. `Ubuntu`를 메인 terminal로 설정한다.
`Ubuntu`에서 실행하는 것은 Linux console를 사용한다. 즉, 내 컴퓨터에 설치된 Windows랑 다른 새로운 Linux OS 컴퓨터가 하나 더 있다고 생각하면 된다.
Linux환경에서 제일 위에 있는 root folder로 가보면 다음의 폴더들을 볼 수 있다.

```
bin dev home lib lib64 lost+found mnt proc run snap sys usr
boot etc init lib32 libx32 media opt root sbin srv tmp var
```

여기서 중요한 folders는 `home`과 `mnt`이다. `mnt`는 내 Windows환경의 파일들을 Linux와 연결하여 Linux console로 실행할 수 있게 해준다. `home`은 내 Linux환경의 메인 directory이다. 둘 중에 어디에다가 코드를 작성할 지는 자유지만, `mnt`는 내 Windows환경과 연결되어 있기 때문에 Linux환경에 문제가 생겨도 파일들을 잃지 않는다. `home`은 내 Windows와 연결되어 있지 않기 때문에 Linux환경에 문제가 생기면 파일들을 잃어버린다.

그럼으로 `mnt` folder를 이용하여, 내 Windows환경과 연결하여 사용하는 것을 추천한다.

4. Ubuntu Terminal에 `code`입력 후, VSCode 서버를 Linux환경에 설치.
5. Google에 `install nvm` (Node Version Manager) 검색 후 download, 그 후 nvm을 이용하여 `Node.js` 설치

Window환경에 따로 programming languages나 다른 git 같은 tool를 설치하여 사용할 수 있지만, 우리는 Linux환경에 개발에 필요한 모든 tools을 설치할 것이다. 그 이유는 Linux환경을 이용하면, Linux가 제공하는 모든 **Unix command**를 Terminal에 쉽게 사용가능하다. 우리는 Terminal로 파일들을 생성, 조작하고 프로그램들을 설치하는 것에 익숙해져야 한다. 만약 설치가 안된다면, 앞에 sudo를 붙여 root권한을 준다

> `sudo apt-get update`

> `sudo apt-get upgrade`

Node.js를 설치할 때에는 Long Time Support (LTS)가 붙어있는 최신버젼을 다운받는다.

그외에 사용하고 싶은 프로그래밍 언어들도 Google에 검색 후, Linux환경으로 다운받으면 된다.

6. Google에 `install zsh` 검색 후 download `zsh`

> `sudo apt install zsh`

7. Google에 `install Oh my zsh` 검색 후 curl를 사용하여 download `Oh my zsh`

`Window Terminal`을 열고, `설정`을 선택, 그 후 `Json 파열 열기`을 클릭.
`MesloLGS NF` font를 설치 후, 아래와 같이 추가.
`schemes`는 TerminalSplash 웹사이트에서 복사 붙여넣기 하면된다.

```
"profiles": {
    "defaults": {
      "fontFace": "MesloLGS NF"
      "colorScheme": "Aurelia"
    },
    "schemes": [{
      "name": "Aurelia",
      "background": "#1a1a1a",
      "black": "#000000",
      "blue": "#579BD5",
      "brightBlack": "#797979",
      "brightBlue": "#9CDCFE",
      "brightCyan": "#2BC4E2",
      "brightGreen": "#1AD69C",
      "brightPurple": "#975EAB",
      "brightRed": "#EB2A88",
      "brightWhite": "#EAEAEA",
      "brightYellow": "#e9ad95",
      "cyan": "#00B6D6",
      "foreground": "#EA549F",
      "green": "#4EC9B0",
      "purple": "#714896",
      "red": "#E92888",
      "white": "#EAEAEA",
      "yellow": "#CE9178"
    }]
}
```

8. Google에 `powerlevel10k` 검색 후, oh my zsh를 사용하여 download.

- `powerlevel10k`는 zsh terminal를 꾸밀 수 있는 프로그램이다.
- `powerlevel10k`는 `MesloLGS NF` font를 요구하기 때문에, default font를 위와 같이 설정한다.

- VScode에서 `ctrl + ,`입력 후, `terminal` 검색:

  1. Terminal > Integrated: Font Family > `MesloLGS NF`
  2. Terminal > Integrated > Default profile > `Ubuntu`

- `.zshrc` file을 열고, 다음의 코드를 추가한다. `.zshrc`는 `Oh my zsh` terminal setting을 바꿀 수 있는 환경설정 파일이다.

  > `code ~/.zshrc`

  1. `ZSH_THEME="powerlevel10k/powerlevel10k"`
  2. `LS_COLORS="ow=01;36;40" && export LS_COLORS`
  3. `alias python=python3.8`
  4. add the following code to use `nvm`

```
export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
   [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
```

- Oh my zsh: https://github.com/ohmyzsh/ohmyzsh
- powerlevel10k (A Zsh theme): https://github.com/romkatv/powerlevel10k#oh-my-zsh
- TerminalSplash: https://terminalsplash.com/

### 2. Front-End (Client side)

Front-End은 사용자가 웹사이트를 방문시 보게되는 화면/User Interface (UI)을 의미한다. Front-End의 기본은 `HTML`, `CSS`, `Javascript`이다. 이는 web browser가 읽을 수 있는 파일들이 이 세가지 밖에 없기 때문이다.
React.js, Typescript 등등 outside library/framework로 만들어 native `HTML`, `CSS`, `Javascript`로 작성되지 않은 파일들은 browser가 읽을 수 없기 떄문에 결국에는 이 세가지로 변환해주어야 한다.

- `HTML`: Structural 뼈대
- `CSS`: Presentational 살점
- `Javascript`: behavioral 행동

![htmlcssjs](img/htmlcssjs.gif)

- [HTML](https://github.com/heeshin174/Web_App_Dev_Kor#1-html)
  - [HTML Tags](https://github.com/heeshin174/Web_App_Dev_Kor#html-tags)
  - [Page Structure](https://github.com/heeshin174/Web_App_Dev_Kor#page-structure)
  - [Semantic Tags](https://github.com/heeshin174/Web_App_Dev_Kor#semantic-tags)
  - [SEO (Search Engine Optimazation)](https://github.com/heeshin174/Web_App_Dev_Kor#seo-search-engine-optimazation)

* [CSS](https://github.com/heeshin174/Web_App_Dev_Kor#2-css)
  - [Styling](https://github.com/heeshin174/Web_App_Dev_Kor#styling)
  - [Layouts](https://github.com/heeshin174/Web_App_Dev_Kor#layouts)
    - [Float](https://github.com/heeshin174/Web_App_Dev_Kor#float)
    - [Flexbox](https://github.com/heeshin174/Web_App_Dev_Kor#flexbox)
    - [Grid](https://github.com/heeshin174/Web_App_Dev_Kor#grid)
  - [Responsive Design](https://github.com/heeshin174/Web_App_Dev_Kor#responsive-design)
  - [Animation](https://github.com/heeshin174/Web_App_Dev_Kor#animation)
  - Library and Framework
    - Bootstrap: https://getbootstrap.com/docs/5.0
    - Tailwindcss: https://tailwindcss.com/docs/installation
    - styled-components: https://styled-components.com/docs
    - Postcss: https://postcss.org/
  - 기타
    - FontAwesome (icons): https://fontawesome.com/
    - Devicon (icons representing programming tools): https://devicon.dev/
    - Google Font (text style): https://fonts.google.com/
    - CSS Gradient: https://cssgradient.io/
    - Color Space: https://mycolor.space/
    - Shape Divider (SVG): https://www.shapedivider.app/
    - Haikei (SVG): https://haikei.app/
    - Cool Backgrounds: https://coolbackgrounds.io/
    - Dribble: https://dribbble.com/

+ [Javascript](https://github.com/heeshin174/Web_App_Dev_Kor#3-javascript)
  - **ES6+ Syntax**
    - Basic
      - let, const
      - [function](https://github.com/heeshin174/Web_App_Dev_Kor#function)
      - if, for, switch, while
      - object
      - [Array](https://github.com/heeshin174/Web_App_Dev_Kor#array)
    - Advanced
      - Prototype
      - [Hoisting](https://github.com/heeshin174/Web_App_Dev_Kor#hoisting)
      - [Closure](https://github.com/heeshin174/Web_App_Dev_Kor#closure)
      - Callback Function
  - **Browser APIs**
    - DOM Manipulation
    - Events
    - Fetch API (+ Async/Await, Error handler)
  - ⭐ [**Typescript**](https://github.com/heeshin174/Web_App_Dev_Kor#4-typescript): https://www.typescriptlang.org/
    - Types
    - Object-oriented Programming (OOP)
  - FrontEnd Library & Framework
    - ⭐ [**React**](https://github.com/heeshin174/Web_App_Dev_Kor#5-reactjs): https://reactjs.org/
    - [Vue](https://github.com/heeshin174/Web_App_Dev_Kor#6-vuejs): https://vuejs.org/
    - Angular: https://angularjs.org/
    - **Svelte**: https://svelte.dev/docs
    - React JS with Typescript: https://create-react-app.dev/docs/adding-typescript/
  - Meta Library & Meta Framework (Meta-Framework: 기존 framework 위에 만들어진 framework)
    - React based
      - [Server-Side Rendering (SSR)](https://github.com/heeshin174/Web_App_Dev_Kor#client-side-rendering-csr-vs-server-side-rendering-ssr)
        - ⭐ [**Next.js**](https://github.com/heeshin174/Web_App_Dev_Kor#7-nextjs): https://nextjs.org/docs/
        - [Remix](https://github.com/heeshin174/Web_App_Dev_Kor#8-remix): https://remix.run/docs/en/v1
      - Managing and centralizing application state
        - redux-toolkit: https://redux-toolkit.js.org/
        - react-redux: https://react-redux.js.org/
        - redux-thunk: https://github.com/reduxjs/redux-thunk
      - CSS Framework
        - react-bootstrap (components): https://react-bootstrap.github.io/getting-started/introduction
        - Material-UI (components): https://mui.com/
      - Static Site Generators (SSG)
        - Gatsby
      - Other React libraries
        - MDX (Markdown for the component era): https://mdxjs.com/
        - react-icons (icons): https://react-icons.github.io/react-icons
        - react-typed (Dynanic text): https://github.com/ssbeefeater/react-typed
        - react-transition-group: https://reactcommunity.org/react-transition-group
        - react-beautiful-dnd (drag and drop): https://github.com/atlassian/react-beautiful-dnd
        - react-scroll (smooth scroll): https://github.com/fisshy/react-scroll
        - react-router: https://reactrouter.com/docs/en/v6
        - SWR (React Hooks for Data Fetching): https://swr.vercel.app/
    - Vue based
      - Server-Side Rendering (SSR)
        - ⭐ **Nuxt.js**
      - CSS Framework
        - Vuetify: https://next.vuetifyjs.com
    - redux (state관리 library): https://redux.js.org/introduction/getting-started

`Frontend library/framework`은 web application을 더 쉽게 작성할 수 있게 만들어 주는 outside library/framework을 말한다.
**Single Page Application** (SPA)는 body가 비어있는 하나의 HTML을 가지고 Javascript를 이용해서 그 안에 Data만 변경하는 것을 말한다.
Server가 Client에 자료를 넘겨주면, Client computer가 그 정보를 가지고 HTML를 완성하기 때문에 CSR (Client Side Rendering)이라고 부른다. CSR은 HTMl이 비어있기 때문에 검색 엔진에 노출되어 검색되기 쉽지 않아 SEO (Search Engine Optimization)에 약점을 가진다.
SPA를 제공하는 frontend framework에는 크게 React JS, Vue JS, Angular JS가 있다. 이들은 사용방법이 거의 비슷하기 때문에 하나만 잘 이해하면, 나머지는 쉽게 사용할 수 있다.

- ⭐ **`React JS`**: React는 Meta사에서 만든 Javascript frontend library로 computer에 최신 버전의 `Node.js`를 설치하면 누구나 사용할 수 있다.
- **VanillaJS** is just a way to refer to native (non-extended and standards-based) JavaScript

### 3. Back-End (Server side)

Back-End은 사용자가 웹사이트를 방문시 서버쪽에서 실행 할 UX (user experience)을 의미한다.
API key같은 외부에 노출되서는 안되는 environmental variables들은 서버쪽에서 다뤄, 사용자가 접근하지 못하게 해야한다. 또한 데이터를 저장할 database의 logic 역시 back-end에서 다뤄야 하는 요소들중 하나이다.

- [Server](https://github.com/heeshin174/Web_App_Dev_Kor#1-web-application-development)

+ Library and Framework
  - [Javascript](https://github.com/heeshin174/Web_App_Dev_Kor#3-javascript)
    - [Express.js](https://github.com/heeshin174/Web_App_Dev_Kor#2-expressjs): https://expressjs.com/
  - Python
    - [Flask](https://github.com/heeshin174/Web_App_Dev_Kor#3-flask-python): https://flask.palletsprojects.com
    - Django: https://docs.djangoproject.com/en/4.0/
  - Rust
    - [Rocket](https://github.com/heeshin174/Web_App_Dev_Kor#6-rocketrs-rust): https://rocket.rs/ 

- Database
  - SQL
    - Postgresql: https://www.postgresql.org/download/
      - PG-Pool js: https://node-postgres.com/api/pool
  - NOSQL
    - Mongodb: https://www.mongodb.com/cloud
      - Mongoose js: https://mongoosejs.com/
  - Prisma (PlanetScale에 hosting된 serverless database와 연결): https://www.prisma.io/
  - PlanetScale (serverless database): https://planetscale.com/

- SendGrid (Email API): https://sendgrid.com/
- JWS (Json Web Token): https://jwt.io/

- Javascript Library/Framework
  * Next.js (Server side rendering): https://nextjs.org/docs/getting-started
  * Remix (Server side rendering): https://remix.run/docs/en/v1
  * Gatsby.js (Server side generator): https://www.gatsbyjs.com/
  * nodemon (javascript library: auto reload server): https://www.npmjs.com/package/nodemon
  * dotenv (javascript library: set environmental variables): https://github.com/motdotla/dotenv
  * concurrently (javascript library: start client and server together): https://github.com/open-cli-tools/concurrently
  * Axios (javascript library: XMLHttpRequests): https://axios-http.com/docs/intro
  * bcryptjs (hashing password): https://www.npmjs.com/package/bcryptjs

- Cloudflare Streams (realtime live streaming for live commerce): https://www.cloudflare.com/products/cloudflare-stream/
- Cloudflare Images: https://www.cloudflare.com/products/cloudflare-images/

각각의 programming language마다 Web Application Server를 만드는 web app framework를 제공한다.

1. python: Django, Flask, FastAPI
2. Java: spring, spring boot, play
3. Javascript: Express, Fastify
4. php: Laravel
5. Rust: Rocket

![serverside-web-framework](./img/server_side_web_framework.png)

- Web Framework benchmarks (Which web framework is high performance?): https://www.techempower.com/benchmarks/

#### Full-stack (Client + Server)

Web App dev는 크게 Frontend, Backend로 나눌 수 있고, 이를 합쳐 Fullstack dev라고 한다. Full-stack은 front-end와 back-end를 합친 것으로 서버쪽과 사용자쪽 모두를 다룬다. 이는 MVC (Model / View / Controll) software design pattern 라고도 불린다.

- Model–view–controller is a software design pattern commonly used for developing user interfaces that divide the related program logic into three interconnected elements.
  - Model은 View와 Controll을 연결하는 연결고리 역할을 한다.
  - View은 client가 웹사이트에 방문하여 실제로 보게되는 회면을 의미한다. HTML (HyperText Markup Language), CSS (Cascading Style Sheets), Javascript를 이용하여 View를 작성할 수 있다. 여기서 programming language는 오직 Javascript이다.
  - Controll은 app의 functionalities를 의미한다.

추천조합:

- MERN stack in Typescript
  - Mongo database
  - Express.js (server)
  - React.js (front-end)
  - Node.js
  - Next.js (Server-side rendering)
  - Redux.js (state managing)
- PERN stack in Typescript
  - Postgresql database
  - Express.js (server)
  - React.js (front-end)
  - Node.js
  - Next.js (Server-side rendering)
  - Redux.js (state managing)

#### Database

Database와 web app을 연결하여 쉽고 간단하게 data를 읽고 쓸 수 있다.
Database는 크게 Relational database (sql)와 Not only Relational database (Nosql)로 나눌 수 있다.
`sql (Structured Query Language)`

- `postgresql` - Relational database의 대표주자
-  `Mongo Database` - Not only Relational database의 대표주자

![This is an image](./img/Database.png)

### 4. Tools

- Git
- Github
- Docker (Container based development): https://www.docker.com/ & https://docs.docker.com/
- APIs
  - RapidApi: https://rapidapi.com/
  - public-apis (links collection): https://github.com/public-apis/public-apis
  - public-apis: https://public-apis.xyz/page/1
  - themmoviedb (movie database): https://www.themoviedb.org/

### 5. Testing

- 다른 Operating system에서도 내 웹사이트가 잘 작동하는지 확인한다.
  Windows 사용자면, MacOS에서도 접속해본다.
- 다른 Web browser에서도 내 웹사이트가 잘 작동하는지 확인한다.
  Chrome, Edge, 등 여러 browser로 접속해본다.
- Mobile로 접속하면, 어떤 화면이 나오고 Tablet로 접속하면 어떤 화면이 나오는 지 확인한다.
- 같은 code가 여러 곳에 반복되지 않는지 확인한다.
  만약 여러번 반복된다면, 함수로 만들어서 코드를 재사용 (reuse)한다.

### 6. Publish

- Cloud service provider
  - ⭐ **AWS** (Amazon Web Services): https://aws.amazon.com/
  - Azure (Microsoft): https://azure.microsoft.com/en-us/
  - GCP (Google Cloud Platform): https://cloud.google.com/
- Client side service provider
  - Github Pages: https://github.com/
  - Netlify: https://www.netlify.com/
  - Heroku: https://www.heroku.com/
- Server side service provider
  - Vultr: https://www.vultr.com/
  - Digitalocean: https://www.digitalocean.com/
  - ⭐ **Vercel**: https://vercel.com/

### 기타 유용한 Links

- Programming Langauges
  - Node.js: https://nodejs.org/en/docs/
  - Python: https://docs.python.org/3/
  - Java: https://docs.oracle.com/en/java/javase/15/docs/api/index.html
  - Typescript: https://www.typescriptlang.org/
  - C/C#/C++
  - Rust: https://www.rust-lang.org/
  - Closure (Functional): https://clojure.org/
  - Dr.Racket (educational Functional): https://racket-lang.org/

- Tools
  - Postman (RESTful API): https://www.postman.com/downloads/
  - VSCode (Microsoft IDE: Code Editor): https://code.visualstudio.com/
  - Eclipse (Java IDE): https://www.eclipse.org/documentation/
  - GoormIDE (Docker based Cloud IDE): https://www.goorm.io/
  - Pythontutor (code visulaization): https://pythontutor.com/
  - Figma (Design UI/UX): https://www.figma.com/
  - Adobe photoshop (Design UI): https://www.adobe.com/products/photoshop
  - Diagram.io (Design UI): https://app.diagrams.net/
  - Jsbin (간단한 code 실행): https://jsbin.com/
  - Quicktype (Api로 얻은 Json data를 각종 다른 언어로 변환): https://quicktype.io/
  
- Educations
  - Web Development In 2022 - https://www.youtube.com/watch?v=EqzUcMzfV1w&list=PLg8KC9DusHl8zGjAWYGGJygm3rWoEahJQ&index=30&ab_channel=TraversyMedia
  - Async Await: https://kiwanjung.medium.com/%EB%B2%88%EC%97%AD-async-await-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EC%A0%84%EC%97%90-promise%EB%A5%BC-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-955dbac2c4a4
  - w3school: https://www.w3schools.com/
  - Leetcode: https://leetcode.com/
  - react로 만든 웹 github로 deploy하기: https://codingapple.com/unit/react-build-deploy-github-pages/

## 1. HTML

- [HTML Tags](https://github.com/heeshin174/Web_App_Dev_Kor#html-tags)
- [Page Structure](https://github.com/heeshin174/Web_App_Dev_Kor#page-structure)
- [Semantic Tags](https://github.com/heeshin174/Web_App_Dev_Kor#semantic-tags)
- [SEO (Search Engine Optimazation)](https://github.com/heeshin174/Web_App_Dev_Kor#seo-search-engine-optimazation)

**`HyperText Markup Language (HTML)` is the standard markup language for creating web pages and documents designed to be displayed in a web browser.**

사용자가 웹브라우저로 특정 URL에 접속하면 서버가 그 사이트의 `HTML`, `CSS`, `Javacsript`를 보내주고 웹브라우저가 이를 해석하여 사용자에게 보여준다. 그 중 `HTML`은 웹사이트안에 실제 들어있는 내용물 (content) 자체를 의미한다.

HTML는 **tree structure**를 가진다. Every tree node is an object. Tags are element nodes and form the tree structure: `<html>` is at the root, then `<head>` and `<body>` are its children, etc.

- `<html>`
  - `<head>`
    - `<link>`
    - `<title>`
    - ...
  - `<body>`
    - `<header>`
      - `<nav>`
    - `<section>`
    - ...
    - `<footer>`

예시: `index.html` file 

`index.html`은 웹사이트의 홈페이지를 의미하는 naming이다.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- This is a icon next to the title -->
    <link rel="icon" type="image/x-icon" href="favicon.ico" />
    <!-- This is my css file -->
    <link rel="stylesheet" href="%PUBLIC_URL%/css/siteload.css" />
    <!-- This is a CDN link to outside css files -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.14.0/devicon.min.css"
      integrity="sha384-FRAhrKywb1Kn/9XWPRV318sBdwbeeQ3GutvYcHRw44tLLOjThIDqxOdfl9OqKbra"
      crossorigin="anonymous"
    />
    <title>My Website Title</title>
  </head>
  <body>
    <div class="siteLoading" id="siteLoading">
      <div class="siteLoading-frame">
        <img
          class="siteLoading-image"
          src="%PUBLIC_URL%/loader.gif"
          alt="loader"
        />
      </div>
    </div>

    <div id="root">
    <header>
      <h1> This is my H1 tag </h1>
    <header>
    <!-- This is an navigation bar of application  -->
    <nav>
      <ul>
        <li>HOME</li>
        <li>ABOUT</li>
        <li>DATA</li>
      </ul>
    </nav>
      <section id="about">about</section>
      <section id="data">data</section>
    <footer>
      This is my footer
    </footer>
    </div>
  </body>

  <!-- This is a javascript code -->
  <script>
    var el = document.getElementById("siteLoading");
    setTimeout(() => {
      el.remove();
    }, 2000);
  </script>
  <noscript>Sorry, your browser does not support JavaScript!</noscript>
  <!-- This is my javascript file -->
  <script type="text/javascript" src="path-to-javascript-file.js"></script>
</html>
```

위의 코드를 browser로 연 결과:

![html1](img/html1.png)

- HTML 확장자에서 `! + tab`을 입력하면, HTML template를 얻을 수 있다.

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>

</body>
</html>
```

### HTML Tags

- HTML Tags References: https://www.w3schools.com/tags/ref_byfunc.asp

- `<div>` and `<span>` tags 

div tag defines a division or a section in an HTML document. `<div>` is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript. `<div>` is easily styled by using the class or id attribute.

- `<span>` is an inline container used to mark up a part of a text, or a part of a document.
- `<span>` tag is easily styled by CSS or manipulated with JavaScript using the class or id attribute.
- `<div>` is a block-level element and `<span>` is an inline element.

- `<a>` HTMLAnchorElement: `href` attribute에 주어진 hyperlink에 GET request 보내기

```
<a href:"#home">Go to homepage</a>  // id=home인 HTMLElement로 이동
<a href:"https://www.google.com">This is google Link</a>
```

- `<button>` HTMLButtonElement: 클릭 시 `onClick` attribute에 주어진 javascript code 실행.

`<button name="btn1" type="submit" onClick=javascripCodeOnly()>Click me</button>`

- `<input>` HTMLInputElement: specifies an input field where the user can enter data.

```
<input type="button">
<input type="checkbox"> (여러개 중 원하는만큼 선택할 수 있는 component)
<input type="color">
<input type="date">
<input type="datetime-local">
<input type="email" placeholder="example@gmail.com"> (email값 입력)
<input type="file"> (file upload)
<input type="hidden">
<input type="image"> (image upload)
<input type="month">
<input type="number">
<input type="password"> (password값 입력)
<input type="radio"> (여러개 중 한개만 선택할 수 있는 component)
<input type="range">
<input type="reset"> (양식 초기화용 버튼)
<input type="search">
<input type="submit"> (양식 제출용 버튼)
<input type="tel"> (전화번호 입력)
<input type="text"> (default value)
<input type="time">
<input type="url"> (url값 입력)
<input type="week">
```

- `<form>` creates an HTML form for user input, such as Login

```
<form action={form 데이터가 전송되는 백엔드 url} method={http request (GET / POST)} onSubmit={submit 버튼 클릭시 실행할 javascript code}>
	<p>
		<strong>아이디</strong>
		<input type="text" name="name" value="아이디 입력">
	</p>
	<p>
		<strong>비밀번호</strong>
		<input type="password" name="password" value="비밀번호 입력">
	</p>
	<p>
		<strong>성별</strong>
		<input type="radio" name="gender" value="M">남자
		<input type="radio" name="gender" value="F">여자
	</p>
	<p>
		<strong>응시분야</strong>
		<input type="checkbox" name="part" value="eng">영어
		<input type="checkbox" name="part" value="math">수학
	</p>
	<p>
		<input type="submit" value="제출">
	</p>
</form>
```

![login](img/form1.png)

- Application navigation bar

```
<nav class="navbar navbar-default navbar-fixed-bottom">
  <div class="container">
    <p>HOME</p>
    <p>LINK</p>
    <p>LINK</p>
  </div>
</nav>
```

![nav](img/nav.png)

- Dropdown list

```
<select>
	<option value="ktx">KTX</option>
	<option value="itx">ITX 새마을</option>
	<option value="mugung">무궁화호</option>
</select>
```

![Dropdown](img/form2.png)

### Page Structure

![htmllayout](img/htmllayout.png)

```
<header> - Defines a header for a document or a section
<nav> - Defines a set of navigation links
<section> - Defines a section in a document
<article> - Defines an independent, self-contained content
<aside> - Defines content aside from the content (like a sidebar)
<footer> - Defines a footer for a document or a section
<details> - Defines additional details that the user can open and close on demand
<summary> - Defines a heading for the <details> element
```

### Semantic Tags

Semantic elements = **tag을 사용하는 것만으로도 의미를 가지는 Element**. A semantic element clearly describes its meaning to both the browser and the developer.

예시: nav tag가 사용되었으면, "이 element는 사용자를 다른 pages로 안내하려는 목적으로 사용되었구나" 하고 바로 알 수 있다.

```
Examples of non-semantic elements: <div> and <span> - Tells nothing about its content.
Examples of semantic elements: <form>, <table>, and <article> - Clearly defines its content.
```

- Semantic Tags

```
<header>: Defines a header for a document or a section
<nav>: Defines a set of navigation links
<section>: Defines a section in a document
<article>: Defines an independent, self-contained content
<aside>: Defines content aside from the content (like a sidebar)
<footer>: Defines a footer for a document or a section
<main>:  Specifies the main content of a document
<time>: Defines a date/time
<details>: Defines additional details that the user can open and close on demand
<summary>: Defines a heading for the <details> element
```

### SEO (Search Engine Optimazation)

`Search Engine Optimazatoin (SEO)`는 내가 만든 web site가 Google, Naver와 같은 검색 엔진에 많이 노출되게 하는 방법을 의미한다. 이 검색 엔진에 노출이 되려면, 서버가 가지고 있는 HTML이 텅 비어있으면 안된다. 이는 검색 엔진이 서버의 HTML파일을 확인하면서 검색 엔진에 노출시키는 구조이기 때문이다.

React.js, Vue.js와 같은 Frontend library/framework로 만들어진 사이트, Client-Side Rendering (CSR),의 경우 서버는 텅 빈 html을 사용자에게 넘겨주고, 사용자의 컴퓨터에서 HTML이 완성되는 구조이기 때문에 검색엔진에 노출되기 어렵다. 그럼으로 Server-Side Rendering (SSR)을 지원하는 Next.js나 Nuxt.js등을 이용하여 검색 엔진에 많이 노출되게 할 수 있다.

## 2. CSS

- [Styling](https://github.com/heeshin174/Web_App_Dev_Kor#styling)
- [Layouts](https://github.com/heeshin174/Web_App_Dev_Kor#layouts)
  - [Float](https://github.com/heeshin174/Web_App_Dev_Kor#float)
  - [Flexbox](https://github.com/heeshin174/Web_App_Dev_Kor#flexbox)
  - [Grid](https://github.com/heeshin174/Web_App_Dev_Kor#grid)
- [Responsive Design](https://github.com/heeshin174/Web_App_Dev_Kor#responsive-design)
- [Animation](https://github.com/heeshin174/Web_App_Dev_Kor#animation)

[CSS Properties Refernece](https://www.w3schools.com/cssref/default.asp)

**`Cascading Style Sheets (CSS)`는 HTML을 꾸미기 위해 사용한다.**

With CSS, you can control the color, font, the size of text, the spacing between elements, how elements are positioned and laid out, what background images or background colors are to be used, different displays for different devices and screen sizes, and much more!

CSS can be added to HTML documents in 3 ways:

1. Inline - by using the style attribute inside HTML elements

- `<h1 style="color:blue;">A Blue Heading</h1>`

2. Internal - by using a `<style>` element in the `<head>` section

```
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: powderblue;
  }
  h1 {
    color: blue;
  }
  p {
    color: red;
  }
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

3. External - by using a `<link>` element to link to an external CSS file

```
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
...
</html>
```

**CSS사용법 예시:**

- 자주 사용할 색상을 :root에 변수로 저장하면, 모든 Element에 다음의 색상을 쉽게 이용가능하다.

```
:root {
  --primary-gold: #ffd700;
  --primary-orange: #ffa500;
  --primary-white: #ffffff;
  --primary-violet: #a35ee0;
  --primary-black: #000000;
  --primary-brown: #483b3b;
  --primary-bg: #2b2b2b;
  --primary-mint: #11abb0;
}

.col h1 {
  color: var(--primary-white);
  width: 600px;
  line-height: 130%; 
  font-size: 4rem;
}
/* line-height: 줄 사이 간격 */
```

- body tag에는 `margin: 8px`이 default로 설정되어 있다. 이를 없에기 (Wild card/전체 선택: \*)

```
* {
  margin:0;
  paddign: 0;
  box-sizing: border-box;
}
```

- 사용할 font를 import하기 (Google-font)

```
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;900&display=swap");

body {
  font-family: "Roboto", sans-serif;
  font-weight: 900;
}
/* font-weight가 900이면 bold, 300이면 normal이다. */
```

- `id=box`인 HTMLElement의 style 변경 (id selector: #)

```
#id {
  background: url("../../img/istockphoto-1032782930-640x640.jpg") no-repeat;
  weight: 90vh /* vh는 view height로 현재 보이는 화면의 90%를 채운다 */
}
/* background를 주어진 url로 교체 */
```

- `class=hero`인 HTMLElement의 style 변경 (class selector: .)

```
.hero {
  position: relative;
  background: url("../../img/istockphoto-1032782930-640x640.jpg") no-repeat;
  background-size: cover;
  background-position: center;
  height: 754px;
  margin-top: 70px;
}

/* HTMLElement전에 empty content를 만들고 gradient 추가 */
.hero::before {  
  content: "";
  background: linear-gradient(to right, black, transparent);
  position: absolute;
  left: 0;
  height: 754px;
  width: 20%;
}
```

- `class=col`인 HTMLElement의 자식인 첫번째 h1 tag의 style 변경

```
<div class="col">
  <h1>This is first child</h1>
  <h1>This is second child</h1>
  <h1>This is third child</h1>
</div>

.col h1:first-child {
  color: var(--primary-white);
  width: 600px;
  line-height: 130%;
  font-size: 4rem;
}
```

- `class=col`인 HTMLElement의 자식인 세번째 h1 tag의 style 변경

```
.col h1:nth-child(3) {
  color: var(--primary-gold);
  animation: slide 2s;
  margin-top: 64px;
  margin-bottom: 64px;
  font-weight: inherit;
}
```

### Styling

- margin (top/bottom/left/right)
- border (top/bottom/left/right)
- padding (top/bottom/left/right)

![Styling](img/cssstyle.png)

- `Padding`은 content와 한 몸처럼 styles의 영향을 받고, `margin`은 content와 별개로 styles의 영향을 받는다.
- `Border`는 테두리를 의미한다. border를 이용하면, 박스를 만들고 밑줄을 추가하는 등 여러가지를 할 수 있다.
- content에 밑줄을 추가: `border-bottom: 5px`

- The `border` property is a shorthand property for:

```
border: border-width border-style (required) border-color
```

`border: 1px solid black` is equivalent to

```
border-width: 1px
border-style: solid
border-color: black
```

- `border-style: solid/dotted/double`

### Layouts

- `position: absolute`는 모니터의 왼쪽 위가 (0, 0)이 되고 그에 맞는 width와 height를 줄 수 있다.
- `position: relative`는 content의 왼쪽 아래가 (0, 0)이 되고 그에 맞는 width와 height를 줄 수 있다.

![position](img/absoluterelative.jpg)

```
.absBox {
  position: absolute;
  width: 400px;
  height: 400px;
}

.relBox {
  position: relative;
  width: 400px;
  height: 200px;
}
```

#### Float

float은 이미지와 텍스트를 어떻게 정렬할 것인지 나타내기 위해 등장한 개념이다. `float:left`는 이미지를 왼쪽으로, `float:center`는 이미지를 가운데로, `float:right`는 이미지를 오른쪽으로 정렬한다.

![float](img/float-common-use.png)

#### Flexbox

`Flexbox`에는 **flex container**와 **flex item**이 존재한다. flex container는 flex item들을 담는 박스가 된다.

![flexbox](img/flexbox.jpg)

- `display: flex;`를 주면 그 HTMLElement는 flex container가 되고, 그 container의 직속 children들이 flex item이 된다.

```
.container {
  display: flex;
  flex-direction: row (default)/column/reverse-row;
}
```

- `flex-direction: row`일 경우: main axis는 horizontal line이고, cross axis는 vertical line이다. x-axis가 중심축이다.
- `flex-direction: column`일 경우: main axis는 vertical line이고, cross axis는 horizontal line이다. y-axis가 중심축이다.
- `flex-direction`을 지정하지 않으면 row가 기본값이다.

`flex container`에 적용할 수 있는 속성과 `flex item`에 적용할 수 있는 속성이 다르다.

![flexbox2](img/flexbox2.png)

`flex-container`에 지정 가능한 속성:

```
- display: flex
- flex-direction: row (default)/column
- flex-wrap: nowrap (default)/wrap/wrap-reverse
- flex-flow: column wrap;
- justify-content: flex-start (default)/flex-end/left/right/center/space-around/space-evenly/space-between
- align-content: flex-start (default)/flex-end/left/right/center/space-around/space-evenly/space-between  
- align-items: left/center/right/baseline
/* main axis: justify-content */
/* cross axis:  align-content, align-items */
```

- `flex-wrap`는 기본값으로 nowrap이다. 이는 한 `flex-container`에 아무리 많은 `flex-item`이 들어서도 다른 line을 생성하지 않는다. 즉, 아무리 item이 많아도 한 row에 때려박는다. flex-wrap:wrap이 되면 flex-container에 container보다 많은 flex-item이 들어서면 다른 line으로 자동적으로 이동한다. 즉, item의 크기가 container의 크기를 넘어서면 다른 row을 자동적으로 생성한다.

- The `flex-flow` property is a shorthand property for:

```
flex-flow: flex-direction + flex-wrap;
```

`flex-flow: column wrap` is equivalent to

```
flex-direction: column;
flex-wrap: wrap;
```

`flex-item`에 지정 가능한 속성 (속성의 기본값은 모두 0이다)

```
- order: 0
/* item들 사이에 순서를 지정 */
- flex-grow: 0

.item1 {
  flex-grow: 2
}
.item2 {
  flex-grow: 1
}
.item3 {
  flex-grow: 1
}

/* item1이 item2, item3보다 2배의 비율로 크기를 유지하면서 커진다. */

- flex-shrink: 0
- flex-basis: 0

.item1 {
  flex-basis: 60%
}
.item2 {
  flex-basis: 30%
}
.item3 {
  flex-basis: 10%
}
/* item1, item2, item3이 화면의 크기와 상관없이 위의 비율을 유지한다. */

- align-self: center; /* item별로 정렬 */
```

- flex-grow를 지정하지 않으면, 화면의 크기가 커져도, 본인 고유의 크기를 유지한다. 하지만, flex-grow가 0이 아닌 item들은 그 숫자에 맞게, flex-container를 모두 채우려고 크기가 커진다. flex-grow는 화면이 커졌을 때 item들이 어떤 비율로 커질 것인지를 나타낸다.
- flex-shrink는 flex-grow와 반대로 화면이 작아졌을 때 item들이 어떤 비율로 작아질 것인지를 나타낸다.

#### Grid

`Grid`에는 **grid container**와 **grid item**이 존재한다. grid container는 grid item들을 담는 박스가 된다.

- `display: grid;`를 주면 그 HTMLElement는 grid container가 되고, 그 container의 직속 children들이 grid item이 된다.

Flexbox와 Grid의 큰 차이점은

- Flex: one dimension layout 
- Grid: two dimension layout

https://studiomeal.com/archives/533

### Responsive Design

**Responsive Design**는 브라우저의 크기에 따라 보이는 화면이 달라지는 것을 뜻한다. 컴퓨터를 기준으로 웹사이트를 만들게 되면, mobile로 보게되면 화면이 작아서 다 보이지 않게 된다.

- 화면의 width가 600px보다 작을 경우 `class=logo`인 HTMLElement 안보이게 하기

```
@media only screen and (max-width: 600px) {
  .logo {
    display: none;
  }
}
```

### Animation

`@keyframe`을 이용하면 Animation을 구현할 수 있다. 자세한 내용은 https://www.w3schools.com/css/css3_animations.asp 참고.

## 3. Javascript

### What is Javascript?

**JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. Javascript는 웹환경에서 가장 많이 쓰이는 프로그래밍언어이다.**

맨 처음 Javascript는 web browser에 귀속된 programming language이였다. 각 browser마다 Javascript 해석엔진이 달랐는데, Chrome에서 사용하는 해석엔진인 'v8'이 browser와 독립적으로 출시되면서 프로그래밍언어로서 급부상했다. Javascript를 이용하여 웹서버, 모바일앱, mechine learning 등을 할 수 있지만, Javascript의 근본은 웹개발을 할 때 사용하는 것이다. Web 환경에서 JavaScript를 사용하는 가장 큰 이유는 **HTML 조작과 변경**이다. HTML을 조작하고, 변경하면서 우리는 이쁘고, 실용적인 웹페이지를 만들 수 있다.

Javascript는 web을 위해 등장한 언어이기 때문에 다른 프로그래밍 언어들과는 차별점을 가진다.

- Javascript는 동기 프로그래밍 (synchronous programming) 언어이지만, 비동기 프로그래밍 (asynchronous programming)을 지원한다.
  자바스크립트의 비동기 처리란 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 특성을 의미한다.
  코드를 위에서 부터 한줄 씩 실행하기는 하지만, 데이터를 불러오는데 오래걸리는 것들을 기다리지 않는다.

- JavaScript is a `dynamically typed language`로 변수타입의 지정이 필요없이 알아서 타입을 정해준다.
  It means that JS does not require the explicit declaration of the variables before they're used. 변수의 타입을 직접 지정해주지 않아도, JavaScript가 알아서 변수의 타입을 정해준다. 이는 한 variable에 여러 타입이 assign되는 상황을 가능하게 만든다. 작은 project를 만들 때에는 편리하지만, 큰 project를 만들고, team 단위로 만들게 되면 이런 높은 자유도는 오히려 독이 되어 어디서 어떻게 잘 못 되었는 지 알기 어렵게 만든다.

```
// static typing in Java
int age = 10; // age의 타입을 int형으로 정해놨기 때문에 다른 types은 올 수 없다.

age = "Hello"; (x) // error를 만든다.
age = 20;  (o)

// dynamic typing in Javascript
let age; // 현재 age의 타입: undefined
age = 10; // age에 정수형 (Integer)값이 들어오면서, age의 타입이 int로 변환된다.

age = "Hello"; // age에 문자형 (String)값이 들어오면서, age의 타입이 string로 변환된다.
```

왜 Javascript가 비동기적인지를 생각해보면, 만약에 Javascript가 동기적으로만 처리된다면 우리는 서버가 모든 데이터를 불러올 때까지 아무 버튼도 누를수 없다.

### Web browser 동작원리

Javascript를 실행하는 것은 web browser이다. 그럼으로 Web browser가 어떻게 Javascript를 해석하는 지, Javascript 해석엔진과 web browser의 동작원리를 알 필요가 있다. 

Javascript는 동기적으로 처리되는 동기 프로그래밍 (synchronous programming) 언어이지만, web browser의 Javascript 해석엔진이 비동기 프로그래밍 (asynchronous programming)을 지원한다. Javacript는 single thread이다. 그럼으로, 한번에 하나의 코드만 call stack에서 실행할 수 있다. 그럼 어떻게 자바스크립트는 싱글스레드이면서 비동기을 지원하는 것일까? 

동기적이란 한 번에 한 줄의 코드를 위에서 부터 차례로 실행하는 것을 의미한다. 비동기적이란 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 것을 의미한다. Javascript에서 비동기적인 처리를 지원하는 함수는 `setTimeout()`, `event listener`, `ajax`이다. Web browser는 Javascript 코드를 위에서 부터 하나씩 실행하다가 위의 함수들을 만나면 시간이 오래걸리는 걸로 간주하고 Web Apis (대기실)로 옮겨논 다음에 call stack에 아무것도 없을 때, 이를 실행한다. 

- **Call Stack:** 실행
- **Web Apis**: 대기실
- **Callback Queue (Task Queue)**: 대기 순번

![callstack](img/callstack1.gif)

- Javascript engine
  - 자바스크립트 엔진의 대표적인 예는 Google V8 엔진이다. V8은 Chrome과 node.js에서 사용한다.
  - 엔진의 2개 구성요소
    - Memory Heap : 메모리 할당이 일어나는 공간
    - Call Stack : memory에 존재하고, 호출 스택이 쌓이는 공간 
      - 자바스크립트는 기본적으로 작업을 싱글스레드로 처리한다. 즉, 단 하나의 호출 스택을 사용한다. 
      - 호출 스택에 쌓인 함수나 코드를 위에서부터 아래로 차례차례 실행한다. 그리고 하나의 작업이 끝나면 pop하고 바로 아래의 함수나 코드를 실행한다. 작업을 차례대로 실행하므로 하나의 작업이 끝날 때까지 또 다른 작업을 실행하지 않는다.
      - Memory Heap에서 작업 수행에 필요한 변수나 함수들을 찾아서 작업을 수행하는 공간이다.
  - Garbage Collector(GC)
    - 콜스택과 메모리 힙을 배우면서 각각의 공간은 무제한이 아니고 한정적임을 알 수 있다. 공간이 무한정 하다면야 크게 효율성에 대해서 고려하지 않을 수도 있지만, 콜스택과 메모리 힙은 언제나 한정적이기 때문에 이를 효율적으로 관리할 필요가 있다.
    - 자바스크립트는 이 공간을 효율적으로 관리하기 위해서, 더 이상 효용가치가 없다고 판단되는 변수, 함수 등을 함수 실행 종료 후 메모리 힙에서 제거하는 동작을 수행한다.
    - 필요한 데이터만 메모리 힙에 저장함으로써 메모리를 더욱 여유롭게 관리한다. 따라서 자바스크립트는 Garbage Collected Language라고 말할 수 있으며, 이러한 역할을 수행해주는 도구를 Garbage Collector라고 한다.

- Javascript runtime
  - Javascript engine 밖에서도 자바스크립트에 관여하는 요소들이 있다. Wep API, Task Queue, Event Loop등이다. 런타임은 특정 언어로 만든 프로그램들을 실행할 수 있는 환경이다. Node.js나 크롬등의 브라우저들은 자바스크립트가 구동되는 환경이기 때문에, 이를 자바스크립트 런타임이라고 한다.
  - Web APIs
    - 브라우저에서 제공하는 APIs.
    - JavaScript 코드를 사용하여 접근할 수 있으며 window나 element에 대한 간단한 작업에서부터 WebGL이나 Web Audio와 같은 API를 사용해 복잡한 그래픽 및 오디오 효과를 만들어내는 것까지 가능하다.
    - 예를 들어, setTimeout, ajax, DOM 등이 있다.
  - Event Loop
    - Callback Event Queue에서 하나 씩 꺼내 동작시키는 Loop.
    -  자바스크립트는 단일 스레드 기반 언어이기 때문에 한번에 하나씩 작업을 진행한다. 그러나 자바스크립트가 사용되는 환경을 생각해보면 많은 작업이 동시에 처리되고 있는 걸 볼 수 있다. 예를 들면, 웹브라우저는 애니메이션 효과를 보여주면서 마우스 입력을 받아서 처리하고, Node.js기반의 웹서버에서는 동시에 여러 개의 HTTP 요청을 처리하기도 한다. 어떻게 스레드가 하나인데 이런 일이 가능할까? 질문을 바꿔보면 '자바스크립트는 어떻게 동시성(Concurrency)을 지원하는 걸까'?
    - 자바스크립트는 enevt loop를 이용해서 비동기 방식으로 동시성을 지원한다.
    - 자바스크립트 엔진에서 제공되는 것이 아닌 브라우저나 node.js에서 지원한다.
  - Callback Queue (Task Queue)
    - 자바스크립트의 런타임 환경의 Callback Queue는 처리할 메세지 목록과 실행할 콜백 함수들의 리스트이다. 버튼 클릭 같은 이벤트나 DOM 이벤트, http 요청, setTimeout 같은 비동기 함수는 Web API를 호출하며 Web API는 콜백 함수를 Callback Queue에 밀어 넣는다.
    -  Callback queue는 대기하다가 Call Stack에 아무 것도 없으면 event loop를 돌려 해당 콜백 함수를 call stack에 넣는다. Event loop의 기본 역할은 큐와 스택 두 부분을 지켜보고 있다가 스택이 비는 시점에 콜백을 실행시켜 주는 것이다.
    - 브라우저에서는 이벤트가 발생할 때마다 메세지가 추가되고 이벤트 리스너가 첨부된다. 콜백 함수의 호출은 호출 스택의 초기 프레임으로 사용되며 자바스크립트가 싱글 스레드 이므로 스택에 대한 모든 호출이 반환될 때까지 메세지 폴링 및 처리가 중지 된다. 동기식 함수 호출은 이와 반대로 새 호출 프레임을 스택에 추가한다.

![javascriptengine](img/javascriptengine.svg)

⭐ 요약:
  - Call Stack은 한번에 하나씩만 실행 가능하다.
  - Call Stack에 시간이 오래걸리는 무거운 연산이 실행되면 그 동안은 다른 행동들은 할 수 없다.
  - Web broswer는 javascript 코드를 수행하는 중에 무거운 연산을 해야될 경우 callback queue로 옮겨 call stack이 할 일이 없을 경우에만 실행하도록 만든다.

### ES6+ Syntax

Javascript syntax를 배울 때 중요한 점은 **if, for, var, let, function, array, object등 Javascript에서 사용하는 문법은 HTML을 조작하고, 변경하기 위해 등장했다는 것이다.**

JavaScript Data Type:
- Primitive data types: immutable datum represented directly at the lowest level of te language 
  - number, string, boolean, null, undefined
- object (function, array, data, regexp)

자바스크립트는 null과 undefined 타입을 제외하고 모든 것을 object로 다룬다.

#### Javascript로 HTML 조작하기 (DOM Manipulation)

**바꾸고 싶은 HTMl 요소 선택 (Selector) + 그 요소의 뭘 바꾸고 싶은지 선택 + 어떤 값으로 바꿀지**

요소의 뭘 바꾸고 싶은지는 매우 많기 때문에, 전부 다 외울 수는 없고, 구글에 검색해서 사용한다.

```
// index.html
// 1. 웹문서에서 id가 "hello"인 Element를 얻어, 그 안에 값을 "안녕"으로 변경하기.
// 2. 웹문서에서 id가 "hi"인 Element를 얻어, 그 안에 색상을 "red"로 변경하기.
// 3. 웹문서에서 id가 "hi"인 Element를 얻어, 그 안에 크기을 "30px"로 변경하기.
<body>
 <h2 id="hello">안녕하세요</h2>
 <h3 id="hi">하이</h3>
<script>
 document.getElementById('hello').innerHTML = "안녕";
 document.getElementById('hi').style.color = "red";
 document.getElementById('hi').style.fontSize = '30px';
</script>
</body>
```

- `variable = value;`에서 `=`은 assgin (대입)이다. `<=`로 생각하면 이해하기 쉽다.

`age = 10; // age라는 variable에 숫자 10을 assgin한다.`

- variable을 지정했는데 값을 아직 assign 안한 경우, 이 변수의 값은 undefined이 된다.

- `//`는 single-line comment `/* */`는 multi-line comment로 컴퓨터는 인식하지 못하고, 사람간에 설명이 필요할 때 사용한다.

```
// name is not defined here. 
// name를 변수가 선언되기도 전에 사용하면 error가 발생한다.
console.log(name); 

// name is undefined here. name = undefined
let name; 
name = "Shin"; // name is "Shin" here.
```

- 문자는 `""` (double quote), `''` (single quote), `` (back tic) 사이에 넣는다.
- 위의 기호들 사이에 있으면, 문자 자료형 `String`이 된다. double quote와 single quote는 아무런 차이가 없지만, single quote를 더 선호한다.

- **Template Literals**: back tic의 경우 `${variable}`을 사용해서 다른 곳에서 정의한 값을 문자열 사이에 넣을 수 있다.

```
const name = "Shin";
console.log("Hello" + name + "!"); // Bad: Hello Shin
console.log(`Hello ${name}!`); // Good: Hello Shin
```

#### If statement

```
if (condition1) {
   // if condition1 is true
   // do this code
} else if (condition2){
   // if condition2 is true
   // do this code
} else {
  // otherwise
}
```

또는 **Conditional (ternary) operator** = `{ cond ? tb : fb}`

#### Function

**Function은 긴 코드를 한 단어로 압축하고 싶을 때 사용한다.** Function은 parameters를 받아 값을 return한다. 즉, input를 받아 output를 만드는 게 함수이다. 

`return` keyword은 함수를 종료시키기 때문에 return 뒤에는 아무것도 올 수 가 없다. 함수 내에서 정의한 변수들은 local variable (지역변수)로 함수 밖에서는 사용할 수 없다. 그럼으로, 함수 내에서 바뀐 값을 함수 밖에서 이용하고 싶으면 return사용해야 한다.  

Javascript에서 function을 정의하는 방법에는 크게 3가지가 있다:

```
// 1. 함수 선언식: Function Declarations
function add(x, y) {
     return x + y;
}

// 2. 함수 표현식: Function Expressions
const add = function(x, y) {
  return x + y;
}

// 3. 함수 표현식에서 Arrow Function
const add = (x, y) => {
   return x + y;
}
```

함수 선언식과 표현식의 차이점은 함수 선언식은 Hoisting에 영향을 받지만, 함수 표현식은 영향을 받지 않는다. broswer는 자바스크립트를 실행하기 전에 파일 전체를 훓는다. 이 때, 함수 선언식으로 작성된 함수들은 미리 memory에 올려놔 언제든지 사용가능 하도록 만든다.

- 함수 표현식: 코드에 도달하면 생성. 변수의 생성과 같다.
- 함수 선언식: 실행전에 메모리에 입력. 코드에 도달하기전에 메모리에 있기 때문에, 언제 어디서든 호출이 가능하다.

함수 선언식은 코드를 구현한 위치와 관계없이 broswer가 자바스크립트를 해석할 때 맨 위로 끌어 올려진다. 이 말은 함수 선언식은 어디서든 호출이 가능하고, function이 선언 되기 전에 코드에서도 함수가 이 파일내에 선언만 되어 있다면 사용할 수 있다.

```
// 함수 표현식은 함수가 선언되기 전 코드에서도 함수를 호출할 수 있다.
console.log(add(1,2)); // 3

function add(x, y) {
     return x + y;
}

//  함수 선언식은 함수가 선언되기 전 코드에서는 함수를 호출할 수 없다.
// 그 이유는 함수 선언식에서는 함수를 변수랑 똑같이 대하기 때문이다.
console.log(add(1,2)); // error. add is not a function.

const add = function (x, y) {
     return x + y;
}
```

더 자세한 내용은 Hoiesting부분을 참고하자.

함수 표현식의 장점:

1. 함수 표현식이 호이스팅에 영향을 받지 않는다.
2. 클로져 (Closure) 로 사용 가능하다. 클로져는 함수를 실행하기 전에 해당 함수에 변수를 넘기고 싶을 때 사용된다.
3. 콜백 (callback function)으로 사용 가능하다. (다른 함수의 인자로 넘길 수 있음)

그럼으로 함수 선언식보다는 함수 표현식을 지향하는 것이 좋다.

#### Arrow Function

Arrow Function은 함수를 더욱 간결하게 만들기 위해 등장한 개념이다.

- Curly brackets: after an arrow function they represent a code block, which consists of zero or more grouped statements within the curly brackets.

Arrow function에서 body부분에 Curly brackets가 쓰이면 이는 code block, 즉 여러개의 code를 묶어 놓은 것으로 인식하기 떄문에 `return` keyword가 다른 function들 처럼
반드시 필요하다.

`return`이 없으면, 이 함수는 local variable만 생성할 뿐 값을 만들어 내지 않기 떄문에, 값이 `undefined`가 된다.

```
// return이 있는 code block (o)
const jsBrackets = x => {
return x > 3 ? true : false
}
jsBrackets(5); // true

// return이 없는 code block (x)
const jsBrackets = x => {
 x > 3 ? true : false
}
jsBrackets(5); // undefined

// return이 없는 괄호 (o)
// return문이 없으면 대괄호를 일반괄호로 바꾼다.
const jsBrackets = x => (
 x > 3 ? true : false
)
```

If the function can be written on one line (as the example above can, it can be shortened to exclude both the curly brackets and the return word, as below.

`const jsBrackets = x => x > 3 ? true : false`

- Parentheses: are used instead of curly brackets after an arrow function to return an object.

For example, they are used in map, filter, and reduce functions.

```
const numbers = [1,2,3,4]
// OKAY
numbers.map(number => number \* 2);
numbers.map(number => (number \* 2 ));
numbers.map(number => {return number \* 2 });

// 위의 세 경우와 다르게 return keyword가 없는 code block은 반환값이 없어 undefined값이 된다.
const newnumbers = numbers.map(number => {number \* 2});
console.log("newnumbers"); // newnumbers = [undefined, undefined, ...]
```

이를 확인하려면, browser에서 F12를 열거나, 마우스 오른쪽 클릭 후 inspect를 클릭해 개발자 모드로 들어간다.

Source tab에서 js파일에 breakpoint를 걸고 실행시켜보면, scope/global scope을 통해 값을 볼 수 있다.

요약:

1. parameter가 하나인 경우 일반 괄호 생략가능
2. parameter가 없거나, 두 개 이상인 경우 일반 괄호 생략 불가능
3. 함수 본문이 한 줄일 경우 return과 대괄호 생략가능
4. 본문이 object를 return할 경우, return을 생략 후 일반괄호 사용가능. 대괄호는 사용불가.
5. 함수 본문이 한 줄 이상일 경우, 일반괄호 사용 불가능, return과 대괄호 생략 불가능

```
const x = a => {
  return a + 1;
}
const add = (x, y) => {
  return x + y;
}
const sayHello = (name) =>  `Hello ${name}`;
const add = (x, y) => ( x + y );
const add = (x, y) => {
  const result = x + y;
return result };
```

#### Array

**Array (배열)는 여러 변수들을 하나로 묶어놓은 묶음이다.**

Array을 만들 때, Javascript의 안좋은 점이 들어난다. Javascript는 array내에 같은 type만 담을 수 있는 것이 아니라, 다른 type들도 섞어서 담을 수가 있다. 이렇게 되면, error을 일으킬 확률이 높으니 array 내에는 같은 type만 담을 수 있도록 한다.

- Object는 **{} curly braces**를 이용해서 정의한다.
- Array는 **[] square brackets**를 이용해서 정의한다.

Array인 객체에는 `map()`, `filter()`, `forEach()` 등 다양한 함수들을 사용할 수 있다.

0. `Array.length`는 현재 배열의 길이를 반환

1. `Array.push("name")`: 배열 끝에 요소 추가

2. `Array.pop()`: 배열 끝에 요소 제거

3. `Array.unshift("name")`: 배열 앞에 요소 추가

4. `Array.shift()`: 배열 앞에 요소 제거

5. `Array.slice(n, m)`: n부터 m까지의 index에 있는 값 반환

```
let arr = [0,1,2,3,4,5];
arr.slice(1,4); // [2,3,4]
```

Python의 `Array[n:m+1]`과 동일하다.

6. `Array.concat(arr1, ...)`: 두개 이상의 배열을 합쳐 새배열을 반환

```
let arr = [1,2];
arr.concat([3,4]); // [1,2,3,4]
```

7. `Array.includes(args)`: 배열이 특정 값을 포함하는 지 boolean 값을 반환

```
let arr = [1,2];
arr.includes(2); // true
arr.includes(6); // false
```

8. `Array.map(callbackFunction(currentValue, index, array), thisArg)`

- currentValue: 배열 내 현재 값
- index: 배열 내 현재 index 값
- array: 원본 배열
- thisArg: callbackFunctoin 내에서 this로 사용될 값

`Array.map()`은 Array내의 모든 요소를 돌면서 주어진 함수의 결과를 모아 **같은 길이의 새로운 배열을 return**합니다. 만약 return 값이 없으면 error를 일으키니 사용시 return 값이 무엇인지 항상 체크한다.

map함수는 콜백 함수의 리턴을 모아서 새로운 배열을 만드는 것이 목적

```
const numbers = [1,2,3,4,5];
const numbersMap = numbers.map(num => num *2); // [2, 4, 6, 8, 10]

//학생과 해당 학생의 점수
const testArray = [
  {name: '김학생', score: 100},
  {name: '윤학생', score: 90},
  {name: '나학생', score: 80},
];

//맵을 활용하여 점수만 가져와 새로운 배열 생성
const ResultMap = testArray.map((x)=> {
  if(x.score >= 90) {
    return x.name;
  }
});

console.log(ResultMap); // ['김학생', '윤학생', undefined]
```

조건을 이용해서 원하는 데이터를 가져오고 싶었지만, map은 해당 조건이 안 맞을 경우 return 없기 때문에 undefined가 들어간 결과 배열을 가져왔다.

9. `Array.filter(callbackFunction(currentValue, index, array), thisArg)`

- currentValue: 배열 내 현재 값
- index: 배열 내 현재 index 값
- array: 원본 배열
- thisArg: callbackFunctoin 내에서 this로 사용될 값

filter와 map의 가장 큰 차이가 있는 게 바로 반환 결과이다.

map의 경우 return 값을 지정하지 않았을 경우, 강제로 undefined를 넣어주는 반면, filter의 경우 retrun 값을 지정하지 않거나, 지정한 조건에 모든 값이 해당하지 않을 경우 빈 배열이 반환된다.

```
// 배열 내 원하는 숫자 데이터만 가져오고 싶을 경우
const numberList = [1,11,3,25,9,10,15];
const numberResultMap = numberList.filter((x) =>
{
  return x <= 10;
});

console.log(numberResultMap); // [1, 3, 9, 10]
```

```
// 배열 내 특정 단어를 포함하는 데이터만 가져오고 싶을 경우
const List = ['김사원','윤대리','한주임','윤상무','김주임','최사장','황차장', '김과장'];

//indexOf는 해당 글자를 포함하지 않을 경우 -1을 반환한다.
//주임직급을 가진 사람만 가져오기
const ListResultMap = List.filter((x) => {
   return x.indexOf('주임') !== -1;
});

console.log(ListResultMap); // ["한주임", "김주임"]
```

```
//학생과 해당 학생의 점수
const testArray = [
  {name: '김학생', score: 100},
  {name: '윤학생', score: 90},
  {name: '나학생', score: 80},
];

//맵을 활용하여 점수만 가지와 새로운 배열 생성
const ResultMap = testArray.filter((x) => {
  if(x.score >= 90)
  {
    return x.name;
}});
console.log(ResultMap); // [{name: '김학생', score: 100}, {name: '윤학생', score: 90}]
```

filter를 이용해 해당 배열의 결과를 가져와보니 undefined는 사라지고, 90점이 넘는 데이터를 가지고 오는 것을 확인할 수 있었다. 하지만, 또다른 문제로 이름만 가지고 오는 것이 내가 원하는 결과였지만, filter를 이용해 return 되는 건 해당 조건이 만족하는 object 전체가 들어오는 문제가 있다.

즉, filter는 object 전체를 가져온다. (x.name이라고 해당 object에 name만 가져오라는 조건을 주었지만, 객체 전체를 return 해버린다. 🙄)

```
// Filter와 map을 동시에 활용한 예시
//학생과 해당 학생의 점수
const testArray = [ {name: '김학생', score: 100}, {name: '윤학생', score: 90}, {name: '나학생', score: 80}, ];

// 1. filter를 이용해 90점 이상한 객체를 가져온다.
// 2. map을 이용하여 해당 객체에 이름을 가져온다.
const ResultMap = testArray.filter((x)=> x.score >= 90).map((x)=> x.name);
console.log(ResultMap); // ['김학생', '윤학생']
```

이처럼 filter와 map을 동시에 활용해서 조건에 부합하는 object를 가져온 뒤, object의 특정 key의 value값을 가져와 새로운 배열을 만드는 것이 가능한 걸 알 수 있었다.

10. `Array.prototype.flat()`

- 중첩 배열 삭제 / 빈공간 삭제

```
// 중첩 다차원 배열 평평하게
const array = [1, [2, 3], [4, 5]];
array.flat(1); // 결과 : [1,2,3,4,5]

// 데이터 정리도 가능
const entries = ["bob", "sally", , , , , , , , "cindy"];
entries.flat(); // 결과 ['bob', 'sally', 'cindy'];
```

### Object-oriented programming (OOP) 객체 지향형 언어

80년대 초 소프트웨어가 하드웨어의 빠른 변화를 못 쫓아감. 해결책으로 객체지향 언어를 도입 (절차적 -> 객체지향)
절차적은 프로그램이 순서대로 실행되는 것을 의미한다.

- OOP의 장점
  - 코드의 재사용성이 높다 (reusable)
  - 유지보수가 용이
    - 소프트웨어의 빠른 변화를 간단히 따라갈 수 있다.
  - 중복 코드 제거 

OOP = 기존 프로그래밍 언어 + 객체지향 개념(규칙)

- OOP의 핵심 개념
  1. encapsulation 캡슐화
  2. polymorphism 다형성
  3. Inheritance 상속
  4. Abstraction  추상화

객체지향 개념을 공부할 때에는 최소한의 핵심이론을 가지고 실습을 많이 해야한다.
이해보다는 다른 사람이 작성한 것을 따라해보고, 실습 위주로 가야한다.

- 실습 
  - 웹: Javascript, Spring
  - 모바일: 안드로이드 앱

#### Class and Object 

- class의 정의: class란 Object를 정의해 놓은 것
- class의 용도: class는 object를 생성하는 데 사용

- object의 정의: 실제로 존재한느 것. 사물 또는 개념
- object의 용도: 객체가 가지고 있는 기능과 속성에 따라 다름

- class는 설계도, object는 설계도로 만든 실제 제품과 같다.
  - class는 붕어빵틀, object는 붕어빵
  - class는 cookiecutter, object는 cookie

#### Object의 구성요소 - 속성과 기능

OOP 개념은 다른 많은 과학기술과 마찬가지로 군사적 목적으로 처음 시작되었다.
실제 세계를 컴퓨터 안에 옮겨, 컴퓨터 안에서 미사일을 발사하는 시행착오를 겪어 실전에서 오차를 줄일 수 있다.
이처럼, OOP는 실제 세계인 Hardware를 Software화 시켜 컴퓨터 안에서 돌아가게 하는 게 목적이다.

우리가 현재 Computer로 할 수 있는 일이 많아진 이유 역시, 동영상 player, Audio player등 Hardware를 software화 시켜 computer에 설치했기 때문에 가능한 일이다.

예: Tv라는 Hardware를 software화 시켜 컴퓨터에 설치해 컴퓨터 내에서 Tv를 볼 수 있게 만든다.
  - Tv라는 객체는 속성과 기능으로 이루어져 있다.
  - 속성은 variables로 기능은 method로 표현하여 software화 할 수 있다.
    - Tv 속성: 크기, 길이, 높이, 색상, 볼륨, 채널, ...
    - Tv 기능: 켜기, 끄기, 볼륨 높이기, 볼륨 낮추기, 채널 변경하기, ...

핵심은 Hardware를 분석 및 관찰하면, 객체는 속성과 기능으로 이루어져 있고, 속성은 변수로, 기능은 method를 사용하여 Software로 만들 수 있다.

#### Class

클래스 이름은 명사들의 조합으로 이루어지며 첫 글자는 대문자로 지정하는 것이 관례이다.

```
class Classname {
    // constructor() { } --> 멤버변수 선언 및 기타 초기화
    // getter, setter
    // method
}
```

Class를 이용해 객체를 생성하려면, `new` 예약어를 사용한다.

`var|let|const 변수이름 = new Classname();`

일반적으로 Javascript에서의 객체 선언은 const 키워드를 사용함.

위와 같이 정의하면 변수는 클래스 안에 정의된 모든 기능을 부여받은 특수한 형태의 변수가 되는데 이를 객체라고 하고, 객체는 자신에게 기능을 점(.)을 통해 접근할 수 있다.

```
객체.멤버변수 = 값;
객체.method();
```

User Class

```
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    // setter and getter
    set name(value){
        if(!value){
            console.log("name 입력하세요.");
            return;
        }
        this._name = value;
    }

    get name(){
        return this._name;
    }

    get email(){
        return this._email;
    }

    set email(value){
        if(!value){
            console.log("email을 입력하세요.");
            return ;
        }
        this._email = value;
    }

    // method
    // User.prototype.printName();
    printName() { 
      console.log(`Hello, I am ${this.name}`);
    }
}

// User라는 이름을 가진 함수를 만듭니다. 함수 본문은 생성자 메서드 constructor에서 가져옵니다. 생성자 메서드가 없으면 본문이 비워진 채로 함수가 만들어집니다.
// printName같은 클래스 내에서 정의한 메서드를 User.prototype에 저장합니다.

const user1 = new User("Shin", "example@email.com");
console.log(user1); // User { _name: 'Shin', _email: 'example@email.com' }
console.log(user1.name); // Shin
console.log(user1.email); // example@email.com
console.log(user1.printName()); // Hello, I am Shin

const user2 = new User("John", "john@email.com");
console.log(user2); // User { _name: 'John', _email: 'john@email.com' }
console.log(user2.name); // John
console.log(user2.email); // john@email.com
console.log(user2.printName()); // Hello, I am John
```

기존 문법

```
function User(name, email) {
  this.name = name;
  this.email = email;

  // 모든 함수의 prototype은 'constructor' property를 기본으로 갖고 있기 때문에
  // constructor property를 명시적으로 만들 필요가 없습니다.

  // method
  this.printName = function() { 
      console.log(`Hello, I am ${this.name}`);
    }
}

const user1 = new User("Shin", "example@email.com");
console.log(user1.printName()); // Hello, I am Shin
```

위 둘의 방식에 차이가 없다면 `class` keyword 없이도 클래스 역할을 하는 function를 선언할 수 있기 때문에 클래스는 '편의 문법’에 불과하다고 이야기합니다. 참고로 기능은 동일하나 기존 문법을 사람이 쉽게 읽을 수 있게 만든 문법을 편의 문법 (syntactic sugar, 문법 설탕)이라고 합니다. 하지만, class는 function으로 만든 것보다 더 많은 것을 제공한다.

class로 만든 함수엔 특수 내부 property인 `[[IsClassConstructor]]: true`가 이름표처럼 붙습니다. 이것만으로도 두 방법엔 분명한 차이가 있음을 알 수 있다.
자바스크립트는 다양한 경우에 `[[IsClassConstructor]]: true`를 활용합니다. class 생성자를 new와 함께 호출하지 않으면 에러가 발생하는데 이 때 `[[IsClassConstructor]]: true`가 사용된다.

#### Class inheritance 

JavaScript에서는 클래스간 상속의 관계를 만들기 위해, 다음 두 가지 방법을 사용할 수 있다.

1. Prototype Chain
2. Class

Class의 기능을 다른 클래스에 상속시킨 후 추가적인 기능을 명시하여 원래의 기능을 확장하는 방법으로, class를 정의할 때 클래스 이름 뒤에 `extends` keyword를 명시하고 상속받고자 하는 부모 클래스의 이름을 지정한다.

```
// 부모 class
class Protoss {
    /** 모든 객체가 갖는 명사적 특성들을 멤버변수로 정의 */
    constructor(name, hp, dps){
        this._name = name; // 이름
        this._hp = hp; // 체력(health point)
        this._dps = dps; //초당공격력(damage per Second)
        console.log("[%s] 체력 : %d, 공격력 : %d", name, hp, dps);        
    }

    /** 객체가 수행해야 하는 동작들을 함수 형태로 정의 */
    move(position){
        console.log("%s(이)가 %s까지 이동합니다.",  this._name, position);
    }

    attack(target){
        console.log("%s(이)가 %s(을)를 공격합니다. 데미지: %d", this._name, target, this._dps);
    }
}

// 부모 class를 상속받는 자식 class
class Zealot extends Protoss {
  sword(target){
    this.attack(target);
    console.log("근접 공격");        
  }
}

class Scout extends Protoss {
  constructor(name, hp, dps) {
    super(name);
    super(hp);
    super(dps);
    // Scout class만 가지는 멤버변수
    this.isFly = true;
  }

  fire(target) {
    this.attack(target);
    console.log("비행 공격");
  }
}

const zealot1 = new Zealot("Zealot", "80", "100");
const scout1 = new Scout("Scout", "100", "80");
```

### synchronous programming 이해하기 (💥 Callback/Promises/Async Await)

**Javascript는 asynchronous programming로 데이터를 요청하는 데 시간이 많이 걸리는 line이 있으면, 그 code의 값을 기다리지 않고 다음 code를 시작한다.**

위의 말을 이해하려면, 동기 (Synchronous)와 비동기(Asynchronous)가 무엇인지 부터 알아야 한다.

- **동기** 방식은 서버에서 요청을 보냈을 때 응답이 돌아와야 다음 동작을 수행할 수 있다. 기존의 프로그래밍 언어들처럼 code를 위에서 아래로 차근차근 실행하는 것을 말한다.

- **비동기** 방식은 반대로 요청을 보냈을 때 응답 상태와 상관없이 다음 동작을 수행 할 수 있다. 즉 A작업이 시작하면 동시에 B작업이 실행된다. A작업은 결과값이 나오는대로 출력된다.

비동기적인 프로그래밍의 문제는 아직 데이터가 다 불러오지 못해 값이 undefined인 변수를 그 다음 code에서 가져다 쓰는 것이다.

```
// http://comics.naver.com로 가서 webtoon 데이터 좀 가져다 주세요!
const webtoon = fetch('http://comics.naver.com');

console.log(webtoon) // undefined
// ... 아직 데이터가 도착 안했어.
```

비동기 처리 사례는 setTimeout()이다. setTimeout()은 Web API의 한 종류로 코드를 바로 실행하지 않고 지정한 시간만큼 기다렸다가 로직을 실행한다.

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

setTimeout() 역시 비동기 방식으로 실행되기 때문에 3초를 기다렸다가 다음 코드를 수행하는 것이 아니라, 일단 setTimeout()을 실행하고 나서 바로 다음 코드인 console.log('Hello Again');으로 넘어간다. 따라서, ‘Hello’, ‘Hello Again’를 먼저 출력하고 3초가 지나면 ‘Bye’가 출력됩니다.

그러면, Javascript에서 동기적인 프로그래밍을 하는 방법은 무엇이 있을까?

동기적인 프로그래밍을 하는 방법에는 크게 3가지가 존재한다.

1. Callback Function
2. Promise object
3. Async and Await

### CallBack Function으로 비동기 프로그램이 가진 문제 해결하기

**콜백함수(Callback Function)란 파라미터로 함수를 전달받아, 함수의 내부에서 실행하는 함수이다.**

콜백함수를 이용하면, 코드를 위에서 부터 차례로 시작하는 동기적 프로그래밍을 할 수 있습니다.

- **콜백함수 정의: 함수에 parameter로 들어가는 함수**
- **콜백함수 용도: 코드를 위에서 부터 순차적으로 실행하고 싶을 때 사용**

```
// 콜백함수는 이미 우리의 코드 속에서 자주 사용되고 있다.
// 예를 들어, forEach 함수의 경우 함수 안에 익명의 함수를 넣어서 forEach 문을 동작시킨다
let number = [1, 2, 3, 4, 5];

number.forEach(x => {
    console.log(x * 2);
});
```

콜백함수 사용원칙:

1. 익명 함수(anonymous function)를 콜백함수로 사용할 수 있다.

함수의 내부에서 실행되기 때문에 이름을 붙이지 않아도 된다.

2. 다른 곳에 정의된 함수를 콜백함수로 사용할 수 있다.

함수를 변수 or 다른 함수의 변수처럼 사용할 수 있다. 함수를 콜백함수로 사용할 경우, 함수의 이름만 넘겨주면 된다.

```
function first() {
  console.log("first");
}

function second() {
  console.log("second");
}

// 위의 함수를 first 먼저 실행하고, second를 그 후에 실행하고 싶은 경우
// fist 함수에 callback function을 만들면 된다.
function first(callback) {
  console.log("first");
  callback();
}

// first 함수 실행해주세요. 근데 parameter에 second를 집어 넣어서요.
first(second);
// "first"
// "second"
```

콜백함수 사용시 주의사항:

- 콜백함수를 너무 많이 사용하면 코드가 지저분해진다. (callback hell)

```
function add(x, callback) {
    let sum = x + x;
    console.log(sum);
    callback(sum);
}

add(2, function(result) {
    add(result, function(result) {
        add(result, function(result) {
            console.log('finish!!');
        })
    })
})

// 4
// 8
// 16
// finish!!
```

콜백지옥 해결 방안 : Promise의 return 사용하여 callback Hell을 탈출할 수 있다.

### Promise

**A promise is an object that may produce a single value some time in the future**

Promise가 왜 필요한가요? 프로미스를 사용하면 비동기 메서드에서 마치 동기 메서드처럼 값을 반환할 수 있습니다. 다만 최종 결과를 반환하지는 않고, 대신 프로미스를 반환해서 미래의 어떤 시점에 결과를 제공합니다.

프로미스는 주로 데이터를 받는데 오래걸리는 코드를 동기 프로그래밍처럼 사용하고 싶을 때 사용합니다. 일반적으로 웹 애플리케이션을 구현할 때 서버에서 데이터를 요청하고 받아오기 위해 아래와 같은 API를 사용합니다.

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

프로미스 에러 처리는 가급적 `catch()`를 사용한다.

```
// `mongoose.connect()`는 Promise를 return한다.
// Promise가 성공적으로 return되면, .then()에 정의된 callback function을 Promise가 reject되면 에러가 발생하여 .catch()에 정의된 callback function을 실행한다.
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

#### Promise를 Async/Await으로 변환하기

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

### Hoisting

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
var 변수/함수의 **선언**만 위로 끌어 올려지며, **할당**은 끌어 올려지지 않는다. 즉, 변수에 값이 할당대기 전까지는 `undefined`이였다가 값이 할당되면 그제서야 제대로 된 값을 가진다. `let/const`를 이용한 변수 선언과 함수 표현식에서는 호이스팅이 발생하지 않는다.

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

// 위와 동일
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

**Hoisting 우선순위:** 같은 이름의 var 변수 선언과 함수 선언에서의 호이스팅에서는 변수 선언이 함수 선언보다 위로 끌어올려진다.

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
  console.log("Shin");
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

Hoisting 주의사항:
  - 코드의 가독성과 유지보수를 위해 Hoisting이 일어나지 않도록 한다.
  - 호이스팅을 제대로 모르더라도 함수와 변수를 가급적 코드 상단부에서 선언하면, Hoisting 인한 스코프 꼬임 현상은 방지할 수 있다.
  - 변수 선언시 `var`대신 `let/const`를 사용한다.

### Closure

**“A closure is the combination of a function and the lexical environment within which that function was declared.”** 클로저는 함수와 그 함수가 선언됐을 때의 어휘적 환경(Lexical environment)과의 조합이다. 위 정의에서 중요한 키워드는 “함수가 선언됐을 때의 렉시컬 환경(Lexical environment)”이다. Closure means that an inner function always has access to the vars and parameters of its outer function, even after the outer function has returned. 

Closure는 자바스크립트 고유의 개념이 아니라 함수를 일급 객체로 취급하는 함수형 프로그래밍 언어(Functional Programming language: 얼랭(Erlnag), 스칼라(Scala), 하스켈(Haskell), 리스프(Lisp)…)에서 사용되는 중요한 특성이다.

```
let one = 1;
function outerFunc() {
  var x = 10;
  var innerFunc = function () { console.log(x + one); };
  innerFunc();
}

outerFunc(); // 10
// 1. innerFunc 함수 스코프(함수 자신의 스코프를 가리키는 활성 객체) 내에서 변수 x를 검색한다. 검색이 실패하였다.
// 2. innerFunc 함수를 포함하는 외부 함수 outerFunc의 scope에서 변수 x를 검색한다. 검색이 성공하였다.

// global (전역) lexical environment:
// one: 1
// outerFunc: function
//
//  /|\ 참조
//   | 
// 
// 내부 outerFunc lexical environment: 
// x = 10
//
//  /|\ 참조
//   | 
// 
// 내부 innerFunc lexical environment: 
```

스코프(Scope)는 함수를 호출할 때가 아니라 **함수를 어디에 선언**하였는지에 따라 결정되고 이를 **Lexical scoping**이라 한다. 위 예제의 함수 innerFunc는 함수 outerFunc의 내부에서 선언되었기 때문에 함수 innerFunc의 상위 스코프는 함수 outerFunc이다. 함수 innerFunc가 전역에 선언되었다면 함수 innerFunc의 상위 스코프는 전역 (global) 스코프가 된다.

```
function outerFunc() {
  var x = 10;
  var innerFunc = function () { console.log(x); };
  return innerFunc;
}

/**
 *  함수 outerFunc를 호출하면 내부 함수 innerFunc가 반환된다.
 *  그리고 함수 outerFunc의 실행 컨텍스트는 소멸한다.
 */
var inner = outerFunc();
inner(); // 10
```

함수 outerFunc는 내부함수 innerFunc를 반환하고 생을 마감했다. 즉, 함수 outerFunc는 실행된 이후 call stack에서 제거되었으므로 함수 outerFunc의 변수 x 또한 더이상 유효하지 않게 되어 변수 x에 접근할 수 있는 방법은 달리 없어 보인다. 그러나 위 코드의 실행 결과는 변수 x의 값인 10이다. 이미 life-cycle이 종료되어 실행 컨텍스트 스택에서 제거된 함수 outerFunc의 지역변수 x가 다시 부활이라도 한 듯이 동작하고 있다. 뭔가 특별한 일이 일어나고 있는 것 같다.

이처럼 자신을 포함하고 있는 외부함수보다 내부함수가 더 오래 유지되는 경우, 외부 함수 밖에서 내부함수가 호출되더라도 외부함수의 지역 변수에 접근할 수 있는데 이러한 함수를 클로저(Closure)라고 부른다.

다시 MDN의 정의로 돌아가 보자.

“A closure is the combination of a function and the lexical environment within which that function was declared.”
클로저는 함수와 그 함수가 선언됐을 때의 렉시컬 환경(Lexical environment)과의 조합이다.

위 정의에서 말하는 “함수”란 반환된 내부함수를 의미하고 “그 함수가 선언될 때의 Lexical environment”란 내부 함수가 선언됐을 때의 스코프를 의미한다. 즉, 클로저는 반환된 내부함수가 자신이 선언됐을 때의 환경(Lexical environment)인 스코프를 기억하여 자신이 선언됐을 때의 환경 밖에서 호출되어도 그 환경(scope)에 접근할 수 있는 함수를 말한다. 이를 조금 더 간단히 말하면 클로저는 자신이 생성될 때의 환경(Lexical environment)을 기억하는 함수다라고 말할 수 있겠다.

클로저에 의해 참조되는 외부함수의 변수 즉 outerFunc 함수의 변수 x를 자유변수(Free variable)라고 부른다. 클로저라는 이름은 자유변수에 함수가 닫혀있다(closed)라는 의미로 의역하면 자유변수에 엮여있는 함수라는 뜻이다.

실행 컨텍스트의 관점에 설명하면, 내부함수가 유효한 상태에서 외부함수가 종료하여 외부함수의 실행 컨텍스트가 반환되어도, 외부함수 실행 컨텍스트 내의 활성 객체(Activation object)(변수, 함수 선언 등의 정보를 가지고 있다)는 내부함수에 의해 참조되는 한 유효하여 내부함수가 스코프 체인을 통해 참조할 수 있는 것을 의미한다.

즉 외부함수가 이미 반환되었어도 외부함수 내의 변수는 이를 필요로 하는 내부함수가 하나 이상 존재하는 경우 계속 유지된다. 이때 내부함수가 외부함수에 있는 변수의 복사본이 아니라 실제 변수에 접근한다는 것에 주의하여야 한다.

이를 그림으로 표현하면 아래와 같다.

![closure1](img/closure1.png)
![closure1](img/closure2.png)

Closure 사용이유:
  1. 상태 유지: 현재 상태를 기억하고 변경된 최신 상태를 유지
  2. 전역변수의 사용을 억제해 의도되지 않은 변경을 방지
     - 변수의 값은 누군가에 의해 언제든지 변경될 수 있어 오류 발생의 근본적 원인이 될 수 있다. 상태 변경이나 가변(mutable) 데이터를 피하고 불변성(Immutability)을 지향하는 함수형 프로그래밍에서 부수 효과(Side effect)를 최대한 억제하여 오류를 피하고 프로그램의 안정성을 높이기 위해 클로저는 적극적으로 사용된다.
  3. 정보의 은닉: encapsulation 

- Closure 예시

```
// 함수를 인자로 전달받고 함수를 반환하는 고차 함수
// 이 함수가 반환하는 함수는 클로저로서 카운트 상태를 유지하기 위한 자유 변수 counter을 기억한다.
function makeCounter(predicate) {
  // 카운트 상태를 유지하기 위한 자유 변수
  var counter = 0;
  // 클로저를 반환
  return function () {
    counter = predicate(counter);
    return counter;
  };
}

// 보조 함수
function increase(n) {
  return ++n;
}

// 보조 함수
function decrease(n) {
  return --n;
}

// 함수로 함수를 생성한다.
// makeCounter 함수는 보조 함수를 인자로 전달받아 함수를 반환한다
const increaser = makeCounter(increase);
console.log(increaser()); // 1
console.log(increaser()); // 2

// increaser 함수와는 별개의 독립된 렉시컬 환경을 갖기 때문에 카운터 상태가 연동하지 않는다.
const decreaser = makeCounter(decrease);
console.log(decreaser()); // -1
console.log(decreaser()); // -2
```

함수 makeCounter는 보조 함수를 인자로 전달받고 함수를 반환하는 **high-order function** (고차 함수)이다. 함수 makeCounter가 반환하는 함수는 자신이 생성됐을 때의 렉시컬 환경인 함수 makeCounter의 스코프에 속한 변수 counter을 기억하는 클로저다. 함수 makeCounter는 인자로 전달받은 보조 함수를 합성하여 자신이 반환하는 함수의 동작을 변경할 수 있다. 이때 주의해야 할 것은 함수 makeCounter를 호출해 함수를 반환할 때 반환된 함수는 자신만의 독립된 렉시컬 환경을 갖는다는 것이다. 이는 함수를 호출하면 그때마다 새로운 렉시컬 환경이 생성되기 때문이다. 위 예제에서 변수 increaser와 변수 decreaser에 할당된 함수는 각각 자신만의 독립된 렉시컬 환경을 갖기 때문에 카운트를 유지하기 위한 자유 변수 counter를 공유하지 않아 카운터의 증감이 연동하지 않는다. 따라서 독립된 카운터가 아니라 연동하여 증감이 가능한 카운터를 만들려면 렉시컬 환경을 공유하는 클로저를 만들어야 한다. 

⭐ 요약:
  - Closure는 함수와 lexical environment의 조합으로 함수가 생성될 당시의 외부 변수를 기억하므로 내부함수가 외부함수의 맥락(context)에 접근할 수 있는 것을 가리킨다.
  - Closure는 특정 상황에서 발생하는 ‘현상’이고 함수는 이 현상이 나타나기 위한 ‘조건’에 해당한다’.

### Module System

1. Node.js의 module 시스템: CommonJS (module.exports, require)
2. Javascript ES6부터는 브라우저 단에서도 쉽게 JavaScript의 모듈화가 가능하도록 모듈 시스템이 추가되었다. (export, import)
   ES6 fashion을 사용하려면 ES6를 ES5로 바꿔주는 babel complier가 필요하다.

#### CommonJS (module.exports, require)

**NPM 패키지 모듈들은 CommonJS를 기본 모듈 시스템으로 채택헀다.**

Node.js 환경에서 실행되는 JavaScript는 모듈 시스템으로서 CommonJS 방식을 지원한다. 이 방식에서는 `module.exports` 객체를 이용하여 자신의 데이터를 외부로 내보낼 수 있고, `require()` 함수를 이용하여 외부 모듈의 데이터를 불러올 수 있다. 만약 Babel 등의 컴파일러를 사용한다면 뒤에서 설명할 ES6 기반의 모듈 내보내기 및 불러오기 방식을 사용해도 알아서 module.exports 객체 및 require() 함수 기반의 방식으로 변환될 것이다.

자신의 데이터를 외부로 내보내려면 `module.exports` 변수에 내보내고자 하는 데이터들을 담은 객체를 지정해주면 된다.

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

#### ES6 import/export 사용법

이는 브라우저 단에서도 쉽게 JavaScript의 모듈화가 가능하도록 ES6부터 도입된 방식이다. 모듈화 시스템답게 각각의 모듈(파일)마다 독립적인 파일 스코프를 가지고 있어서, 모듈 내에 var로 선언한 변수는 더 이상 window 객체의 프로퍼티가 아닌 파일 스코프의 변수로 존재하게 된다. 즉 기본적으로는 다른 모듈의 데이터를 참조할 수 없기 때문에 충돌도 발생하지 않는다.

이때 다른 모듈의 데이터를 참조하거나 자신의 데이터를 노출시키고 싶을 때 사용하는 것이 바로 export, import 키워드이다.

CommonJS를 모듈 시스템을 채택했던 Node.js에서는 import, export와 같은 ES 모듈을 사용하려면 Babel과 같은 트랜스파일러(transpiler)를 사용했어야 했는데요.

Node.js 버전 13.2부터 ES 모듈 시스템에 대한 정식 지원이 시작됨에 따라 다른 도구 없이 Node.js에서 손쉽게 ES 모듈을 사용할 수 있게 되었습니다. 🎉

1. 프로젝트 단위로 ES6 모듈 적용:

Node.js에서 ES6 모듈을 사용하는 방법은 package.json 파일 설정을 통해 전체 파일에 적용하는 것입니다. 모든 파일의 확장자를 일일이 바꾸지 않고, 프로젝트 전체에 ES 모듈을 적용하고 싶을 때 적합한 방법입니다.

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

```
// 모듈 내보내기 (export)
// Named Export : 정해진 이름으로 내보내기
export 변수/함수/클래스 선언문;
export { 변수명/함수명/클래스명 };
export { 변수명/함수명/클래스명 as 다른 이름 };

// Default Export : 기본 내보내기 (이름을 정하지 않음. 최대 하나만 가능.)
export default 선언문 또는 값;
export { 변수명/함수명/클래스명 as default };

// 모듈 불러오기 (import)

import A, { B, C } from 경로; // A는 Default Export, B와 C는 Named Export

import { B as b, C as c } from 경로; // 원하는 이름으로 로드

import \* as obj from 경로; // Export 된 모든 것들을 하나의 객체 형태로 로드 (불필요한 것도 가져오면 번들링 시 비효율을 야기)

import { default as A } from 경로; // "import A from 경로"와 동일 (default)
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

```
$ node src/time.test.mjs
internal/modules/run_main.js:54
internalBinding('errors').triggerUncaughtException(
^

Error [ERR_MODULE_NOT_FOUND]: Cannot find module
```

이 부분이 Node.js에서 ES 모듈울 처음 사용할 때 가장 많이 실수를 하게되는 부분인데요. Node.js에서 import 키워드로 프로젝트 내부 모듈을 불러올 때는 반드시 **확장자까지 포함**해서 경로를 명시를 해줘야 합니다. 이는 브라우저에서 import가 작동하는 방식과 맞추기 위해서 의도적으로 설계된 부분이라고 합니다.

확장자를 포함해서 경로를 명시해주면 정상적으로 작동합니다.

```
// time.test.mjs
import { now } from "./time.mjs";

console.log("Now:", now());
$ node src/time.test.mjs
Now: 2020-05-23T18:10:20-04:00
```

ES6 기반의 모듈 시스템은 CommonJS 방식에 비해 코드의 직관성이 좋고, 비동기 방식으로 작동하면서 불러오는 모듈의 실제로 사용되는 부분들만 로드하기 때문에 성능적으로도 효율적이라고 할 수 있다. 그러나 이는 아래와 같은 단점들을 가지고 있어서 아직까지는 Webpack 등의 모듈 번들러를 이용하여 미리 의존성이 해결된 형태의 번들 JavaScript 파일을 제공하는 방식이 더 선호되는 경향이 있다.

- IE(인터넷 익스플로러)를 포함한 몇몇 구형 브라우저는 ES6 모듈 시스템을 지원하지 않는다.
- 브라우저의 ES6 모듈 시스템을 사용하더라도 어차피 트랜스파일링이나 번들링은 필요하다.
  = 아직 지원하지 않는 기능(Bare import 등)들이 꽤 있다. (ECMAScript modules in browsers 참고)
- 점차 해결되고는 있지만 아직 몇 가지 이슈가 있다. (ECMAScript modules in browsers 참고)

### 최신 문법 정리 (ES6 ~ ES12)

#### Ternary Operator

if statement를 간편하게 사용할 수 있는 문법: List processing (Lisp)의 `(if condition truebranch falsebranch)`와 동일하다.

condition을 계산 후, condition이 false면 falsebranch를 실행하고, otherwise truebranch를 실행한다.

> `{condition ? truebranch : falsebranch}`

```
// Bad Code
function getResult(score) {
  let result;
  if (score > 5) {
    result = '👍';
  } else if (score <= 5) {
    result = '👎';
  }
  return result;
}

// Good Code
function getResult(score) {
  return score > 5 ? '👍' : '👎';
}
```

#### Nullish coalescing operator ??

variable이 null/undefined인 경우와 아닌 경우를 나누어, nullCheckException을 방지하는 error checking 문법이다. 

> `{ leftExpr ?? rightExpr }`

leftExpr가 null이거나 undefined인 경우 rightExpr를, 아니면 leftExpr를 반환한다.

```
// Bad Code
function printMessage(text) {
  let message = text;
  if (text == null || text == undefined) {
    message = 'Nothing to display 😜';
  }
  console.log(message);
}

// Good Code
function printMessage(text) {
  const message = text ?? 'Nothing to display 😜';
  console.log(message);
}
```

#### Logical OR operator ||

> `{ leftExpr || rightExpr }`

leftExpr가 falsy인 경우에만 rightExpr가 실행된다.
leftExpr가 true인 경우, rightExpr의 값에 상관없이 무조건 true이기 때문에 편의를 위해 leftExpr만 실행한다.

falsy에 해당되는 값:
  - boolean false
  - int 0
  - int -0
  - undefined
  - null
  - NaN (Not a Number)
  - string '' (empty string)

```
// Logical OR operator ||
function printMessage(text) {
  const message = text || 'Nothing to display 😜';
  console.log(message);
}
```

#### Destructuring Assignment 

구조분해 할당 (destructuring assignment) 문법

- 객체, 배열안의 속성을 해체하여 그 값을 변수로 한번에 빼서 사용하기 위한 자바스크립트 expression이다.

Array/Object Destructuring:

Array

```
// Array Destructuring
const arr = ['가', '나', '다', '라'];

// Bad Code
const ga = arr[0];
const na = arr[1];
const da = arr[2];
const ra = arr[3];

// Good Code
const [ ga, na, da, ra ] = arr
```

Object

```
// Object Destructuring
const person = {
  name: 'Julia',
  age: 20,
  phone: '0107777777',
};

// Bad Code
function displayPerson(person) {
  displayAvatar(person.name);
  displayName(person.name);
  displayProfile(person.name, person.age);
}

// Good Code
function displayPerson(person) {
  const { name, age } = person;
  displayAvatar(name);
  displayName(name);
  displayProfile(name, age);
}

// person object에 있는 name과 age가 자동으로 { name, age }의 변수로 할당된다.
// `person.`의 반복을 줄일 수 있다.
// 만약 person.name을 다른 변수의 이름으로 하고 싶다면 {key:newkey} 을 이용한다.
const { name: rename, age: myage } = person;
// rename이라는 변수명에 person.name의 값이 할당된다.
// myage이라는 변수명에 person.age의 값이 할당된다.
```

#### Spread Syntax ( ... )

- 전개연산자
- 객체나 배열의 안의 요소들을 펼쳐 복사에 이용. 자기 자신 객체,배열은 영향 안받음
- 함수의 argument에 쓰이면, 나머지 연산자로 작용. 나머지 인자값들을 모아 배열로 생성

Spread syntax ( ... ) allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected.

```
const obj1 = { key: 'key1' };
const obj2 = { key: 'key2' }; 
const array = [obj1, obj2]; 

// array copy 
const arrayCopy = [...array]; 
console.log(arrayCopy); // [ { key: 'key1' }, { key: 'key2' } ]

const arrayCopy2 = [...array, { key: 'key3' }]; 
obj1.key = 'newKey'; 
// array배열은 래퍼런스 값을 갖고있는 배열이다. 그래서 전개연산자로 복사하여도 
// 레퍼런스 변수는 복사로 취급하지만, 그걸 잇는 주소연결은 똑같다. 

console.log(array); // [ { key: 'newKey' }, { key: 'key2' } ] 
console.log(arrayCopy2); // [ { key: 'newKey' }, { key: 'key2' }, { key: 'key3' } ] 

// object copy  
const obj3 = { ...obj1 }; 
console.log(obj3); // { key: 'key1' } 
 
// array concatenation 
const fruits1 = ['🍑', '🍓']; 
const fruits2 = ['🍌', '🥝']; 
const fruits = [...fruits1, ...fruits2]; 
console.log(fruits); // [ '🍑', '🍓', '🍌', '🥝' ] 
 
// object merge 
const dog1 = { dog: '🐕' }; 
const dog2 = { dog: '🐶' }; 
const dog = { ...dog1, ...dog2 }; 
console.log(dog); // { dog: '🐶' }
```

Array

```
// Spread Syntax - Array
let fruits = ['🍉', '🍊', '🍌'];

// fruits.push('🍓');
fruits = [...fruits, '🍓'];
console.log(fruits);

// fruits.unshift('🍇');
fruits = ['🍇', ...fruits];
console.log(fruits);

const fruits2 = ['🍈', '🍑', '🍍'];

let combined = fruits.concat(fruits2);
combined = [...fruits, '🍒', ...fruits2];
console.log(combined);
```

Object

```
// Spread Syntax - Object
const item = { type: '👔', size: 'M' };
const detail = { price: 20, made: 'Korea', gender: 'M' };

// Bad Code
item['price'] = detail.price;

// Bad Code
const newObject = new Object();
newObject['type'] = item.type;
newObject['size'] = item.size;
newObject['price'] = detail.price;
newObject['made'] = detail.made;
newObject['gender'] = detail.gender;
console.log(newObject);

// Bad Code
const newObject2 = {
  type: item.type,
  size: item.size,
  price: detail.price,
  made: detail.made,
  gender: detail.gender,
};
console.log(newObject);

// Good Code
const shirt0 = Object.assign(item, detail);
console.log(shirt0);

// Better! Code
const shirt = { ...item, ...detail, price: 30 };
console.log(shirt);
```

#### Optional Chainging ?.

- `?.` 문법
- property가 없는 중첩 객체를 에러 없이 안전하게 접근할 수 있다
- **`?.`은 `?.`'앞’의 평가 대상이 undefined나 null이면 평가를 멈추고 undefined를 반환. 평가대상이 true이면 쭉쭉 이어나가 최종값을 반환**

```
const person1 = {
  name: 'Ellie',
  job: {
    title: 'S/W Engineer',
    manager: {
      name: 'Bob',
    },
  },
};

const person2 = {
  name: 'Bob',
};

// Bad Code
function printManager(person) { // 중첩 객체의 값을 불러오는 함수
  console.log(person.job.manager.name);
}

printManager(person1); // Bob
printManager(person2); // error

// Bad Code
function printManager(person) {
  console.log(person.job && person.job.manager && person.job.manager.name);
}

printManager(person1); // Bob
printManager(person2); // undefined


// Good Code
function printManager(person) {
  console.log(person?.job?.manager?.name);
}

printManager(person1); // Bob
printManager(person2); // undefined
``` 

`?.()` 함수 접근

```
let user1 = {
  admin() {
    alert("관리자 계정입니다.");
  }
}

let user2 = {};

user1.admin?.(); // 관리자 계정입니다.
user2.admin?.(); // undefined
```

`?.[]` key 접근

```
let user1 = {
  firstName: "Violet"
};

let user2 = null; // user2는 권한이 없는 사용자라고 가정해봅시다.

let key = "firstName";

alert( user1?.[key] ); // Violet
alert( user2?.[key] ); // undefined

alert( user1?.[key]?.something?.not?.existing); // undefined
delete user?.name; // user가 존재하면 user.name을 삭제합니다.
```

#### Template Literals `${ variable}`

- Template Literals이란 자바스크립트에서 문자열을 입력하는 선진적인 방식입니다.
- Template Literals은 표현식/문자열 삽입, 여러 줄 문자열, 문자열 형식화, 문자열 태깅 등 다양한 기능을 제공합니다.

```
// Template Literals (Template String)
const person = {
  name: 'Julia',
  score: 4,
};

// Bad Code
console.log(
  'Hello ' + person.name + ', Your current score is: ' + person.score
);

// Good Code
const { name, score } = person;
console.log(`Hello ${name}, Your current score is: ${score}`);
```

- **Multi-line strings**
  - 템플릿 리터럴을 사용하면 여러 개행 줄의 문자열도 나눠서 작성할 필요가 없이 한번에 작성 가능합니다.

```
// 기존 문법
console.log("string text line 1\n" + "string text line 2");

//템플릿 리터럴
console.log(`string text line 1
string text line 2`);
```

- **Raw strings (원래 문자열)**
  - Raw string은 이스케이프 문자를 해석하지 않은 일반 문자열입니다.
  - `String.raw` 태그함수를 사용하면 템플릿 문자열을 입력한 대로 출력할 수 있습니다.

```
let s = String.raw`xy\n${1+1}z`;
console.log(s); //xy\n2z
```

태그 함수를 만들어 원래의 문자열을 반환하려면 첫 번째 인자의 raw 프로퍼티를 사용하면 됩니다.

```
let tag = function(strings) {
    console.log(strings);
    return strings.raw[0];
}

let str = tag`Hello\nWorld.`;
console.log(str); //Hello\nWorld.
```

#### Tagged Template Literal

- Template Literal의 발전된 형태의 하나로 Tagged Template Literal이 있다.
- 함수의 실행을 Template Literal로 구현
- 태그를 사용하여 Template Literal을 함수로 파싱할 수 있습니다.

```
let person = 'Lee'; 
let age = 28; 
let tag = function(strings, personExp, ageExp) { 
  console.log(strings); 
  // 첫 인수는 배열이 들어오고 
  console.log(personExp); 
  // 나머지 인수는 ${변수}값이 들어온다. 
  console.log(ageExp); 
}; 
  
let output = tag`that ${person} is a ${age}`;
// strings = [ 'that ', ' is a ', '' ]
// personExp = Lee
// ageExp = 28
```

- Tagged templates는 데이터 별로 상황(조건)이 다른 경우 유용하게 쓰일 수 있습니다.

```
const ramenList = [
    {
        brand: '농심',
        items: ['신라면','짜파게티','참치마요','둥지냉면']
    },
    {
        brand: '삼양',
        items: ['삼양라면', '불닭볶음면']
    },
    {
        brand: '오뚜기',
        itmes: []
    }
];

console.log(`구매가능한 ${ramenList[0].brand}의 라면 : ${ramenList[0].items}`);
//구매가능한 농심의 라면 : 신라면,짜파게티,참치마요,둥지냉면
console.log(`구매가능한 ${ramenList[1].brand}의 라면 : ${ramenList[1].items}`);
//구매가능한 삼양의 라면 : 삼양라면,불닭볶음면
console.log(`구매가능한 ${ramenList[2].brand}의 라면 : ${ramenList[2].items}`);
//구매가능한 오뚜기의 라면 : undefined
```

위와 같이 ramenList 데이터가 들어오는 경우, 오뚜기의 라면 데이터는 아직 추가가 안되어 있고, 그 결과 undefined라는 결과가 나왔습니다. 이런 경우에 tagged templates로 해결할 수 있습니다.

```
function fn(strings, brand, items) {
    if(undefined === items) {
        return = brand + "의 라면은 재고가 없습니다!";
    } else {
        return = strings[0] + brand + strings[1] + items;
    }
}

console.log(fn`구매가능한 ${ramenList[0].brand}의 라면 : ${ramenList[0].items}`);
//구매가능한 농심의 라면 : 신라면,짜파게티,참치마요,둥지냉면
console.log(fn`구매가능한 ${ramenList[1].brand}의 라면 : ${ramenList[1].items}`);
//구매가능한 삼양의 라면 : 삼양라면,불닭볶음면
console.log(fn`구매가능한 ${ramenList[2].brand}의 라면 : ${ramenList[2].items}`);
//오뚜기의 라면은 재고가 없습니다!
```

#### Array Loops 

- Array를 looping할 때, for loop이 아니라
- `Array.prototype.map()`, `Array.prototype.filter()`, `Array.prototype.reduce()`등을 활용한다.

```
// Looping
const items = [1, 2, 3, 4, 5, 6];

// Bad Code
function getAllEvens(items) {
  const result = [];
  for (let i = 0; i < items.length; i++) {
    if (items[i] % 2 === 0) {
      result.push(items[i]);
    }
  }
  return result;
}

function multiplyByFour(items) {
  const result = [];
  for (let i = 0; i < items.length; i++) {
    result.push(items[i] * 4);
  }
  return result;
}

function sumArray(items) {
  let sum = 0;
  for (let i = 0; i < items.length; i++) {
    sum += items[i];
  }
  return sum;
}

const evens = getAllEvens(items);
const multiple = multiplyByFour(evens);
const sum = sumArray(multiple);
console.log(sum);

// Good Code
const evens = items.filter((num) => num % 2 === 0);
const multiple = evens.map((num) => num * 4);
const sum = multiple.reduce((a, b) => a + b, 0);
console.log(sum);

// Good Code
const result = items
  .filter((num) => num % 2 === 0)
  .map((num) => num * 4)
  .reduce((a, b) => a + b, 0);
console.log(result);
```

#### Async/await

- 비동기적 코드를 동기적으로 실행할 수 있게 도와주는 문법
- Async/await은 Promise를 사용하여 동기적 프로그래밍을 가능하게 한다.

```
// Promise -> Async/await

// Bad Code
function displayUser() {
  fetchUser() //
    .then((user) => {
      fetchProfile(user) //
        .then((profile) => {
          updateUI(user, profile);
        });
    });
}

// Good Code
async function displayUser() {
  const user = await fetchUser();
  const profile = await fetchProfile(user);
  updateUI(user, profile);
}
```

#### Quiz

- Remove duplicates from list: list->set->list

```
// Remove Duplicates!
const array = ['🐶', '🐱', '🐈', '🐶', '🦮', '🐱'];
console.log(array);

const newSet = new Set(array)
const newList = [newSet]

console.log(newSet);
// Set(4) { '🐶', '🐱', '🐈', '🦮' }
console.log([new Set(array)]);
// [ Set(4) { '🐶', '🐱', '🐈', '🦮' } ]
console.log([...new Set(array)]);
// [ '🐶', '🐱', '🐈', '🦮' ]
```

## 4. [Typescript](https://www.typescriptlang.org/)

### What is Typescript

TypeScript is a programming language developed and maintained by Microsoft. It is a strict syntactical superset of JavaScript and adds optional static typing to the language. 여기서 알 수 있듯이, Typescript는 Javascript의 superset으로 Java와 같이 변수를 선언할 때, 그 변수의 type을 지정해 주어야만 한다. 그럼 그냥 Javascript를 쓰면 되는 데, 왜 browser가 인식도 못하는 Typescript를 사용하는 가?에 대한 의문이 든다. 여기서 우리는 먼저 Javascript에 대한 이해가 필요하다.

- JavaScript is a `dynamically typed language`이다. JavaScript에서는 변수의 타입을 직접 지정해주지 않아도, JavaScript가 알아서 변수의 타입을 정해준다. 그럼으로 한 variable의 type이 여러 코드가 실행됨에 따라 계속 변화하는 것이 가능하다. 작은 project를 만들 때에는 편리하지만, 큰 project를 만들고, team 단위로 만들게 되면 이런 높은 자유도는 에러가 발생했을 시 오히려 독이 되어 어디서 어떻게 잘 못 되었는 지 알기 어렵게 만든다.

**Typescript를 이용하면, 변수의 type을 지정해 주어야만 하기 떄문에, 어디선가 error가 발생하면 꽤 자세하게 무엇이 잘 못 되었는 지를 알려준다.**

```
let decimal: number = 6; // decimal에는 정수 타입만 오는 것이 가능하고, 6이란 정수를 assign한다.
decimal = "Hello"; // error. decimal은 정수라니까...
```

## 5. [ReactJs](https://reactjs.org/)

### What is React.js

**React.js**는 web app을 만들 수 있는 Javascript library이다. React.js is a JavaScript library for building user interfaces. 

#### Web app은 무엇이고, 왜 사용하는가

A1. **page간 이동에 새로고침이 필요없이 부드럽게 넘어가기 때문에**
A2. UI가 보이는 동시에 클릭이 가능하다. viewable and interactable at the same time.

Web-app은 Single Page Application (SPA)이라고 불리는 웹페이지로, 하나의 html을 가지고, 그 안에 내용물만을 변경하여 사용자에게 보여준다. 웹사이트 내에서 page loading이 덜 걸리고, page간 이동에 새로고침이 필요없이 부드럽게 넘어가기 때문에 사용한다.

Web app를 만들 수 있는 frontend framework에는 React 말고도 Vue/Angular등 다른 tools도 많이 있다.

#### Web app을 만드는데 굳이 React를 사용하는 이유는 무엇인가

- A1. **React는 사용자가 가장 많은 library이기 때문에 교육자료도 많고, 참고할 자료도 매우 많다.**
- A2. **다른 framework와 마찬가지로, React는 component단위로 Element를 관리하기 때문에, 이를 함수처럼 사용할 수 있고 재사용(reusable)이 쉽다.**

React가 web app을 만드는 library/framework들 중에 사용자가 가장 많아서 react를 배운다면 취업시장에서 유리하고 교육용 자료들을 쉽게 찾을 수 있다.

### Framework vs Library

- Framework를 한국어로 하면 frame (틀), work (작업), 즉 기본적인 틀을 만드는 작업이다.
  Framework는 **정해진 사용방법이 존재**하기 때문에 우리는 framework가 요구하는 대로 따라해야지만 원하는 결과를 얻을 수 있다. 

- Library는 특정 기능에 대한 도구 or 함수들을 모은 집합이다.
  즉, 프로그래머가 개발하는데 필요한 것들을 모아둔 코드 더미들로, library는 단순 활용이 가능한 도구들의 집합이다.

집을 만드는 작업이라고 하면,

- Framework는 집의 기본 구조를 제공하여 우리는 그 구조에 필요한 가구, 침구, 벽지등을 추가하는 것이다.
- Library는 침대, 소파와 같은 가구들을 의미한다. 우리는 이 가구들로 직접 집을 만들어야 한다.

프로그래밍에서 차이:

- You, the developer, use a library. You call a library when and where you need to.
- In contrast, a framework call your code. 

개발자가 Library를 내 코드로 호출하고, framework는 반대로 framework가 내 코드를 호출한다. Framework를 사용할 떄 framework가 요구하는 대로 코드를 특정 장소와 폴더안에 입력해야만 제대로 작동하는 것을 볼 수 있다. 이는 framework가 설계될 때 이미 큰 틀이 설계되어 있고, 개발자는 framework가 요구하는 틀을 따라가야 한다. 즉, Library가 코드의 자유도가 더 높고, framework가 코드의 자유도가 더 낮다. 뭐가 더 좋고 나쁨은 없으나, 큰 project를 만들 때에는 여러 개발자와 함께 만들기 때문에 개발자들 사이에 자유도가 낮은 framework가 더 유리하고, 작은 project를 만들때에는 자유도가 높은 library가 더 편하다.

- Framework: 어떤 동작을 수행하기 위한 코드 작성 방법이 정해져 있기 때문에, 다른 개발자의 코드를 보고 한 눈에 알아볼 수 있고 에러를 빨리 찾을 수 있다.
             개발자들 사이 너도 나도 같은 방법을 사용.  
- Library: 개발자가 자유롭게 코드를 가져다 쓰기 때문에 자유도가 높다. 다른 개발자의 코드를 한 눈에 알아보기 힘들 수 있다.

```
          call
Developer ------> Library
Developer <------ Framework
          call

// Library
import API from Library
const mydata = API()

// Framework
- Flask: need to put all HTML files in "templates" folder to work
- Next.js: need to put all Javascript files in "pages" folder to route
```

예시:
- Libraray: React.js, Bootstrap, ...
- Framework: Vue.js, Flask, Django, ...

### JSX extension

React.js는 `.js` 대신 `.jsx` 라는 특수한 extension을 사용한다. JSX stands for JavaScript XML. It is simply a syntax extension of JavaScript. 하지만 js를 사용해도 react가 알아서 jsx로 인식하기 때문에 아무런 문제는 없다 (Button.js === Button.jsx). 보통은 component를 만들때, .jsx 확장자를 이용하여 다른 js files과 차별점을 둘 때 사용하면 좋다.

아래 변수 선언을 살펴봅시다.

> `const element = <h1>Hello, world!</h1>;`

위에 희한한 태그 문법은 문자열도, HTML도 아닙니다.

JSX라 하며 JavaScript를 확장한 문법입니다. UI가 어떻게 생겨야 하는지 설명하기 위해 React와 함께 사용된다. JSX라고 하면 템플릿 언어가 떠오를 수도 있지만, JavaScript의 모든 기능이 포함되어 있습니다.

JSX는 React “Element” 를 생성합니다.

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

#### ReactJS에서 NPM 패키지 모듈 불러오기

NPM 패키지 모듈들은 **CommonJS**를 기본 모듈 시스템으로 채택한다. 즉, 모듈을 내보내고 불러오는 것에 있어 require, module.exports 등을 사용한다는 의미이다.

그러나 실제로 React.jS 등의 라이브러리를 활용하여 Frontend 개발을 할 때는 NPM 패키지 모듈을 불러오기 위해 ES6 문법의 코드를 작성하는 경우가 많다 (import/export).

그런데 왜 문제가 발생하지 않을까? 이는 Babel 등의 컴파일러가 import, export 등의 코드를 CommonJS 기반의 코드로 변환해주기 때문이다. 그러고 나면 Webpack에 의해 JavaScript 모듈들의 번들링이 가능해진다.

### Basic ReactJs Syntax

- React의 If문: If문은 condition이 true면 truebranch, false면 falsebranch를 실행한다.

```
// React if (1)
const condition = () => {
  if (true) {
    return <p>truebranch</p>
  } else {
    return <p>falsebrance</p>
  }
}

// React if (2) ternary operator
{ condition ? <p>truebranch</p> : <p>falsebrance</p> }
```

- React의 for문: `<ul>{ todos.map(todo => <li key={todo}>{todo}</li>) }</ul>`

- React의 state 변경

```
const [human, setHuman] = useState(['Park', 18, 'male'])

let humanCopy = [...human];
humanCopy[0] = 'Kim';
setHuman(humanCopy);
```

#### List와 Key

먼저 JavaScript에서 리스트를 어떻게 변환하는지 살펴봅시다.

아래는 map()함수를 이용하여 numbers 배열의 값을 두배로 만든 후 map()에서 반환하는 새 배열을 doubled 변수에 할당하고 로그를 확인하는 코드입니다.

```
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((number) => number \* 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```

React에서 배열을 Element List로 만드는 방식은 이와 거의 동일 합니다.

- 여러개의 컴포넌트 렌더링 하기

엘리먼트 모음을 만들고 중괄호 `{}`를 이용하여 JSX에 포함 시킬 수 있습니다.

아래의 JavaScript의 `Array.prototype.map()` 함수를 사용하여 numbers 배열을 반복 실행합니다. 각 항목에 대해 `<li>` Element를 반환하고 엘리먼트 배열의 결과를 listItems에 저장합니다.

```
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>
  <li>{number}</li>
);

// listItems 배열을 <ul>element 안에 포함하고 DOM에 rendering합니다.
ReactDOM.render(

  <ul>{listItems}</ul>,
  document.getElementById('root')
);

<ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>4</li>
    <li>5</li>
</ul>
```

- 기본 리스트 컴포넌트

일반적으로 컴포넌트 안에서 리스트를 렌더링합니다.

이전 예시를 numbers 배열을 받아서 순서 없는 엘리먼트 리스트를 출력하는 컴포넌트로 리팩토링할 수 있습니다.

```
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) =>
        <li>{number}</li>
    );

    return (
        <ul>{listItems}</ul>
    );
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
    <NumberList numbers={numbers} />,
    document.getElementById('root')
);
```

이 코드를 실행하면 리스트의 각 항목에 `key`를 넣어야 한다는 경고가 표시됩니다. `key`는 element list를 만들 때 포함해야 하는 특수한 문자열 attribute입니다. 다음 섹션에서 key의 중요성에 대해서 더 설명하겠습니다. 이제 `numbers.map()` 안에서 리스트의 각 항목에 key를 할당하여 키 누락 문제를 해결하겠습니다.

```
function NumberList(props) {
    const numbers = props.numbers;
    const listItems = numbers.map((number) =>
          <li key={number.toString()}>
               {number}
          </li>
    );

    return (
       <ul>{listItems}</ul>
);
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
     <NumberList numbers={numbers} />,
     document.getElementById('root')
);
```

- Key

Key는 React가 어떤 항목을 변경, 추가 또는 삭제할지 식별하는 것을 돕습니다. key는 엘리먼트에 안정적인 고유성을 부여하기 위해 배열 내부의 엘리먼트에 지정해야 합니다.

```
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>

  <li key={number.toString()}>
    {number}
  </li>
);
```

Key를 선택하는 가장 좋은 방법은 리스트의 다른 항목들 사이에서 해당 항목을 고유하게 식별할 수 있는 문자열을 사용하는 것입니다. 대부분의 경우 데이터의 ID를 key로 사용합니다.

```
const todoItems = todos.map((todo) =>

  <li key={todo.id}>
    {todo.text}
  </li>
);
```

렌더링 한 항목에 대한 안정적인 ID가 없다면 최후의 수단으로 항목의 인덱스를 key로 사용할 수 있습니다.

```
const todoItems = todos.map((todo, index) =>
// Only do this if items have no stable IDs

  <li key={index}>
    {todo.text}
  </li>
);
```

항목의 순서가 바뀔 수 있는 경우 key에 인덱스를 사용하는 것은 권장하지 않습니다. 이로 인해 성능이 저하되거나 컴포넌트의 state와 관련된 문제가 발생할 수 있습니다. Robin Pokorny’s가 작성한 글인 인덱스를 key로 사용할 경우 부정적인 영향에 대한 상세 설명을 참고하시길 바랍니다. 리스트 항목에 명시적으로 key를 지정하지 않으면 React는 기본적으로 인덱스를 key로 사용합니다.

Key로 컴포넌트 추출하기
키는 주변 배열의 context에서만 의미가 있습니다.

예를 들어 ListItem 컴포넌트를 추출 한 경우 ListItem 안에 있는 `<li>` 엘리먼트가 아니라 배열의 `<ListItem />` 엘리먼트가 key를 가져야 합니다.

예시: 잘못된 Key 사용법

```
function ListItem(props) {
const value = props.value;
return (
// 틀렸습니다! 여기에는 key를 지정할 필요가 없습니다.

<li key={value.toString()}>
{value}
</li>
);
}

function NumberList(props) {
const numbers = props.numbers;
const listItems = numbers.map((number) =>
// 틀렸습니다! 여기에 key를 지정해야 합니다.
<ListItem value={number} />
);
return (

<ul>
{listItems}
</ul>
);
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
<NumberList numbers={numbers} />,
document.getElementById('root')
);
예시: 올바른 Key 사용법

function ListItem(props) {
// 맞습니다! 여기에는 key를 지정할 필요가 없습니다.
return <li>{props.value}</li>;
}

function NumberList(props) {
const numbers = props.numbers;
const listItems = numbers.map((number) =>
// 맞습니다! 배열 안에 key를 지정해야 합니다.
<ListItem key={number.toString()} value={number} />
);
return (

<ul>
{listItems}
</ul>
);
}

const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
<NumberList numbers={numbers} />,
document.getElementById('root')
);
```

경험상 map() 함수 내부에 있는 엘리먼트에 key를 넣어 주는 게 좋습니다.

Key는 형제 사이에서만 고유한 값이어야 한다.
Key는 배열 안에서 형제 사이에서 고유해야 하고 전체 범위에서 고유할 필요는 없습니다. 두 개의 다른 배열을 만들 때 동일한 key를 사용할 수 있습니다.

```
function Blog(props) {
const sidebar = (

<ul>
{props.posts.map((post) =>
<li key={post.id}>
{post.title}
</li>
)}
</ul>
);
const content = props.posts.map((post) =>
<div key={post.id}>
<h3>{post.title}</h3>
<p>{post.content}</p>
</div>
);
return (
<div>
{sidebar}
<hr />
{content}
</div>
);
}

const posts = [
{id: 1, title: 'Hello World', content: 'Welcome to learning React!'},
{id: 2, title: 'Installation', content: 'You can install React from npm.'}
];
ReactDOM.render(
<Blog posts={posts} />,
document.getElementById('root')
);
```

React에서 key는 힌트를 제공하지만 컴포넌트로 전달하지는 않습니다. 컴포넌트에서 key와 동일한 값이 필요하면 다른 이름의 prop으로 명시적으로 전달합니다.

```
const content = posts.map((post) =>
<Post
    key={post.id}
    id={post.id}
    title={post.title} />
);
```

위 예시에서 Post 컴포넌트는 props.id를 읽을 수 있지만 props.key는 읽을 수 없습니다.

JSX에 map() 포함시키기
위 예시에서 별도의 listItems 변수를 선언하고 이를 JSX에 포함했습니다.

```
function NumberList(props) {
const numbers = props.numbers;
const listItems = numbers.map((number) =>
<ListItem key={number.toString()}
              value={number} />
);
return (

<ul>
{listItems}
</ul>
);
}
```

JSX를 사용하면 중괄호 안에 모든 표현식을 포함 시킬 수 있으므로 map() 함수의 결과를 인라인으로 처리할 수 있습니다.

```
function NumberList(props) {
const numbers = props.numbers;
return (

<ul>
{numbers.map((number) =>
<ListItem key={number.toString()}
                  value={number} />
)}
</ul>
);
}
```

이 방식을 사용하면 코드가 더 깔끔해 지지만, 이 방식을 남발하는 것은 좋지 않습니다. JavaScript와 마찬가지로 가독성을 위해 변수로 추출해야 할지 아니면 인라인으로 넣을지는 개발자가 직접 판단해야 합니다. map() 함수가 너무 중첩된다면 컴포넌트로 추출 하는 것이 좋습니다.


### Curly brackets {} vs Parentheses () in JSX Arrow Function

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

react.js를 이용할 때, javascript 코드를 jsx syntax에서 사용하고 싶으면 curly brackets {} 안에서 정의하면 된다.
react.js에서 array를 하나씩 iterate해야할 경우 `array.map()` 함수를 이용하고, 그 안에 callback함수인 arrow function을 정의한다.

react.js는 jsx이기 때문에 `array.map((param) => {body})`가 아니라 `array.map((param) => (body))`처럼 body에도 parentheses를 사용해야 한다.

`map()`은 javascript code이기 때문에 `{ array.map((param) => (body))}`과 같이 curly brackets {} 안에서 정의하면 된다.

## 6. VueJs

### What is Vue.js

#### Vue Js가 무엇이고, 왜 사용하는가

Vue Js는 Web app을 만들 수 있는 Javascript Front-end Framework이다.

#### Web app은 무엇이고, 왜 사용하는가

**page간 이동에 새로고침이 필요없이 부드럽게 넘어가기 때문에**

Web-app은 Single Page Application (SPA)이라고 불리는 웹페이지로, 하나의 html을 가지고, 그 안에 내용물만을 변경하여 사용자에게 보여준다. 웹사이트 내에서 page loading이 덜 걸리고, page간 이동에 새로고침이 필요없이 부드럽게 넘어가기 때문에 사용한다.

Web app를 만들 수 있는 frontend framework에는 Vue 말고도 React/Angular등 다른 tools도 많이 있다.

#### Web app을 만드는데 굳이 Vue를 사용하는 이유는 무엇인가

**Vue는 문법이 쉽고 하나로 정해져 있기 떄문에, 문법 몇개만 외워주면 초보도 쉽게 output를 낼 수 있다.**

- A1. Vue가 더 쉽기 때문이다. React나 Vue 중 본인에게 맞는 거 사용하면 되는데, Javascript를 잘 하지 못한다면 Vue를 먼저 사용해본다.
- A2. Vue는 문법이 하나로 정해져 있기 때문에 여러 개발자사이의 코딩 스타일을 통일시킨다. 다른 개발자가 나와 같은 방법만을 사용해야 함으로 한 눈에 이해하기 쉽다.

1. React가 사용자가 Vue보다 더 많음에도, 굳이 Vue를 배우는 이유는 Vue의 문법이 더 쉽기 때문이다. Vue는 사용법이 쉬운데 다른 어려운 frameworks와 동일하게 좋은 웹앱을 만들 수 있기 때문에, 웹앱 입문자라면 React보다는 Vue를 추천한다.

- if문 비교

```
// if문은 condition이 true면 truebranch, false면 falsebranch를 실행한다.
// React if (1)
const condition = () => {
  if (true) {
    return <p>truebranch</p>
  } else {
    return <p>falsebranch</p>
  }
}

// React if (2)
{ condition ? <p>truebranch</p> : <p>falsebranch</p> }

// Vue if
<template>
  <div>
    <p v-if="condition">truebranch</p>
    <p v-else>falsebranch</p>
  </div>
</template>
```

- for loop 비교

```
// React for
<ul>{ todos.map(todo => <li key={todo}>{todo}</li>) }</ul>

// Vue for
<template>
  <ul>
    <li v-for="todo in todos" :key="todo">{{ todo }}}/li>
  </ul>
</template>
```

- state변경 비교

```
// React의 state 변경
const [human, setHuman] = useState(['Park', 18, 'male'])

let humanCopy = [...human];
humanCopy[0] = 'Kim';
setHuman(humanCopy);

// Vue의 state 변경
return {
  human: ['Park', 18, 'Male'],
}

this.human[0] = 'Kim'
```

2. 자유도가 높은 코드는 특정 행동을 수행하는 코드를 여러 방법으로 작성할 수 있기 때문에, 다른 개발자가 나와 다른 방법을 사용하면 한 눈에 이해하기 어렵다. 그럼으로, 여러 개발자와 협업할 때, error를 만들어 내기 쉽다. Vue는 자유도가 낮기 때문에 다른 개발자의 코드라도 이해하기가 쉽다. Vue는 코드를 짤때 맞는 방법이 정해져 있어, 여러 개발자사이의 코딩 스타일을 통일시킨다.

Vue를 사용하면, 특정 행동을 수행하는 코드를 다른 개발자가 나와 같은 방법만을 사용해야 함으로 한 눈에 이해하기 쉽다. Vue는 문법이 쉽고 하나로 정해져 있기 떄문에, 문법 몇개만 외워주면 초보도 쉽게 output를 낼 수 있다.

- `<HTML>`을 여러개 만들고 싶다.

```
// React
1. { map }
2. forEach
3. for | for in | for of

// Vue
1. v-for
```

- `<HTML>`을 조건부로 보여주고 싶다.

```
// React
1. if | else
2. Conditional (ternary) operator = { cond ? tb : fb}
3. && ||
4. enum

// Vue
1. v-if | v-else
```

### Vue 개발환경

Vue로 Project를 만들면서, Vue의 문법들을 공부해보자.

1. 최신 버젼의 `Node.js` 설치 (`npm`을 사용하기 위해)
2. VScode code editor와 VScode extension 설치 (`Vue` code를 쉽게 입력하기 위해)

- `Vue Language Features (Volar)`
- `html css support`: (`ctrl + space`: view a list of id and class attribute suggestions )
- `TypeScript Vue Plugin (Volar)`

3. 기본적인 HTML, CSS and JavaScript 개념
4. [Vue 문법 몇가지](https://vuejs.org/guide/introduction.html)

#### Vue로 project 만드는 방법은

A. **project 1. 생성 => 2. 개발 => 3. 배포**

1. Vue의 최신버전으로 프로젝트 생성

Terminal에 다음의 코드를 입력

This command will install and execute `create-vue`, the official Vue project scaffolding tool.

> $ `npm init vue@latest`

```
✔ Project name: … <your-project-name>
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes
✔ Add Cypress for testing? … No / Yes

Scaffolding project in ./<your-project-name>...
Done.
```

아직 익숙하지 않으면 전부 `No`을 선택

2. 개발

Install dependencies and start the dev server

your-project-name로 이동

> $ `cd <your-project-name>`

dependencies 설치

> $ `npm install` 또는 `npm i`

> $ `npm run dev` 또는 VSCode에서 Open Editor 및에 `NPM SCRIPTS`에서 `dev` 실행 버튼 클릭

- web browser에 `localhost:{{port}}` 입력
- dev server를 종료하려면 terminal에서 `Ctrl + C` 입력
- `src/App.vue` 가 우리의 메인 웹페이지이다.
- 현재 project에 맞게, src directory의 files 수정 & 추가하면 된다.

```
// App.vue
<template></tempalte> // HTML Code
<script></script> // Javascript Code
<style></style> // CSS Code
```

- `src` directory: source code 저장
- `public` directory: HTML file 및 기타 파일 저장
- `package.json`: 이 project에 사용되는 dependencies의 이름 저장
- `node_modules` directory: 실제 설치된 dependencies 저장

3. 배포

When you are ready to ship your app to production, run the following:

> `npm run build`

This will create a production-ready build of your app in the project's `./dist` directory.
Vue files을 웹 broswer가 이해할 수 있는 HTML, CSS, Javascript로 변환 후 `./dist` 폴더에 생성

`./dist` 폴더의 files만 있으면 웹사이트 생성가능.

### Databinding in Vue js

#### Databinding이 무엇이고, 왜 사용하는가

- A1. **Databinding은 Javascript data를 HTML에 꽃아 넣는 문법이다.**
- A2. **Databinding은 Javascript로 HTML을 조작하고, 변경하기 위해 사용한다.**
- A3. **Vue의 실시간 자동 rendering을 쓰기 위해서 사용한다.**
- A4. **안바뀔꺼 같은 data는 databinding할 필요없이 HTML에 hardcoding하고, 자주 변하는 데이터들은 script tag에 저장한 후 HTML에 꽂아 넣는다.**

계속 변하는 data를 hardcoding해놓으면, 그 값을 변경하기 어렵다. 하지만 Databinding을 이용하면, 계속 변하는 데이터에 대해 값을 쉽게 변경할 수 있다.

실시간 자동 rendering: script tag에 정의된 data를 변경하면, 그 data와 연결된 HTML에도 실시간으로 변경된다.

#### Vue에서 Databinding을 하는 방법은 무엇인가

Element의 text content을 Databinding할 경우 `{{데이터이름}}`, HTML Attribute를 Databinding할 경우 `:속성="데이터이름"`

- script tag에 Javascript형식으로 변수에 data를 assign한 후, template tag에 `{{}}` double curly braces을 사용하여 그 변수의 값을 사용할 수 있다.

`{{데이터이름}}`

```
<script>
const name = "Shin";
</script>

<template>
<p>Hello My name is {{name}}<p>
</template>

// Hello My name is Shin
```

- HTML Attribute 역시 binding이 가능하다. `:` colon을 HTML Attribute 앞에 붙인 후, 변수명을 `""`을 사용하면 된다.

`:속성="데이터이름"`

```
<script>
const blueColor = 'color : blue';
</script>

<template>
<p :style="blueColor">This is blue color<p>
</template>
```

기존 Javascript에서 databinding을 사용할려면 `document.getElementById("name").innerHTML = "이름"`과 같은 긴 문법을 사용해야 했지만, Vue에서는 databinding을 아주 쉽게 할 수 있다. `{{}}` 안에 변수명을 집어넣으면 끝이다.

안바뀔꺼 같은 data는 databinding할 필요없이 HTML에 hardcoding하고, 자주 변하는 데이터들은 script tag에 저장한 후 HTML에 꽂아 넣는다.

⭐ 기타 다른 Vue 문법은 vuejs.org 공식 문서를 참고하자!

## 7. [NextJs](https://nextjs.org/docs)

### What is Next.js?

`Next.js`는 react.js에 **Server Side Rendering (SSR)** 기능을 더한 meta-framework이다. `Next.js`, `Remix`는 react가 가진 Client-Side Rendering (CSR) 문제를 해결하기 위해 등장했다. React로 만든 웹은 자동으로 Client-Side Rendering이 된다. `Next.js`는 `React.js`로 만든 웹을 **Static & Server Side Rendering**를 가능하게 만들어 준다. `Remix.js` 역시 SSR을 지원하지만, `Next.js`가 프로그래머들 사이에서 가장 인기가 많은 이유는 배우기 쉽고, 사용하기 쉽기 때문이다.

### Client-Side Rendering (CSR) vs Server-Side Rendering (SSR)

- Time To View (TTV): 사용자가 화면 UI를 보는 데까지 걸리는 시간. 즉 page가 **Viewable**이 되는 데 걸리는 시간
- Time To Interact (TTI): 화면 UI를 클릭하면 반응하는 데까지  걸리는 시간. 즉 page가 **Interactable**이 되는 데 걸리는 시간

- Client-Side Rendering (CSR)방식: 사용자가 웹사이트로 접근한 후에야 그 웹를 만드는 데 필요한 모든 Javascript를 다운받고, browser가 React를 실행시켜 UI를 만든다. (TTI = TTV)
  1. Server sending Response to Browser
  2. Browser Downloads Javascript files
     - 하나의 div element가 들어있는 HTML file
     - HTML file에 UI를 추가할 javascript
     - framework/library source code
  3. Browser executes React.js
     - browser가 다운받은 react source code를 이용해, javascript를 실행시키고 화면을 만든다. 
  4. Page now **Viewable** and **Interactable** 
     - 사용자는 모든 component가 전부 다 로딩된 후에야, 화면을 보는 것이 가능하고 웹사이트의 기능들을 사용할 수 있다.

![clientsiderendering](img/CSR.png)

- CSR방식의 장점: 
  1. Rich site interactions
     - 처음 화면이 보이는 순간부터 interactable이 되어, 모든 버튼들이 잘 작동한다.
  2. Fast website rendering after the initial load.
     - 처음 화면이 보이는 순간부터, 다른 page로의 전환에 새로고침이 필요없다.
  3. Great for web applications.
  4. Robust selection of JavaScript libraries.

- CSR방식의 문제: framework/library source code를 다운받아야 하므로, 웹사이트가 크면 클수록 사용자에게 보여주는 데 오랜 시간이 필요하다.
  1. Initial loading may take too long: 
     - framework/library source code를 다운받는 데 시간이 걸릴 수 있다. 
     - 웹사이트가 클수록 사용자는 로딩시간이 오래걸리고 흰 화면만 보게 된다
  2. Low Search Engine Optimization (SEO): 
     - UI를 만들기 전에는 HTML file에 달랑 하나의 div element만 존재하여, google, naver등의 검색엔진에 노출되기 어렵다.

- Server-Side Rendering (SSR)방식: TTV < TTI
  1. Server sending Response to Browser
  2. Browser renders the page now **Viewable** and browser downloads js files.
  3. Browser executes React.js
  4. Page now **Interactable** 

![serversiderendering](img/SSR-server-side-rendering-infographic.png)

- SSR방식의 장점: 
  1. Initial page load is faster
  2. Great Search Engine Optimization (SEO)
    - 모든 content가 HTML file안에 있기 때문에, 검색엔진에 노출되기 쉽다.
  3. Great for static sites

- SSR방식의 문제: 
  1. Frequent server requests.
     - Server가 HTML을 전부 완성한 후에 Client에게 보내기 때문에 이용자가 많을 경우 Server에 과부화가 걸릴 수도 있다.
  2. An overall slow page rendering.
  3. Full page reloads.
     - 화면전환시 서버에서 새로운 화면을 받아와야 하므로, 화면이 깜박거리는 이슈가 있다.
  4. Non-rich site interactions.
     - 처음 화면이 빠르게 보이는 대신 화면이 viewable이 되는 순간과 interactable 되는 순간의 시간차가 있기 때문에, 이 사이에는 보는 것만 가능하고, 어떤 동작을 취할 수는 없다. 

### pages

`Next.js`는 framework이기 때문에, `Next.js`가 정해놓은 규칙, 틀을 따라가야지만 원하는 결과를 얻을 수 있다. `Next.js`가 요구하는 틀 중 가장 유용하고, 중요한 틀은 `pages`이다. `pages` directory안에 React component를 만들어 export하면, 기존 React.js에서 사용하던 routing 방식인 `react-router-dom`을 사용하지 않고, Next.js가 자동으로 그 `.js`, `.jsx`, `.ts`, `.tsx` extentsion의 이름으로 routing 해준다.

`pages` directory안에 `about.js`라는 React component를 만들어 export하면, it will be accessible at `/about`.

- `pages/about.js` file

```
function About() {
  return <div>This is About page</div>
}

export default About
// go to https://localhost:{PORT}/about
```

#### Pages with Dynamic Routes

`Next.js` supports pages with dynamic routes. For example, if you create a file called `pages/posts/[id].js`, then it will be accessible at `posts/1`, `posts/2`, etc.

- React.js의 Dynamic Routes:  `posts/:id.js`
- Next.js의 Dynamic Routes:  `pages/posts/[id].js`

### Pre-rendering

By default, Next.js **pre-renders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Pre-rendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive. (This process is called hydration.)

#### Two forms of Pre-rendering

Next.js has two forms of pre-rendering: **Static Generation** and **Server-side Rendering**. The difference is in when it generates the HTML for a page.

1. **Static Generation** (Recommended): The HTML is generated at build time and will be reused on each request. 
   - If a page uses **Static Generation**, the page HTML is generated at **build time**. That means in production, the page HTML is generated when you run `next build`. This HTML will then be reused on each request. It can be cached by a CDN. In Next.js, you can statically generate pages with or without data.
2. **Server-side Rendering**: The HTML is generated on **each request**.
   - 사용자가 서버에 HTML, CSS, Javascript를 요청할 때마다 서버가 Javascript를 이용하여, HTML를 만든다.

Importantly, Next.js lets you choose which pre-rendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

We recommend using Static Generation over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use Client-side Rendering along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by client side JavaScript.

### getServerSideProps

`page`다음으로 중요한 `Next.js`문법은 `getServerSideProps` method 이다. If you export a function called `getServerSideProps` (Server-Side Rendering) from a page, Next.js will pre-render this page on each request using the data returned by getServerSideProps.

`getServerSideProps` only runs on server-side and never runs on the browser. 

#### Using getServerSideProps to fetch data at request time

The following example shows how to fetch data at request time and pre-render the result.

```
function Page({ data }) {
  // Render data...
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}

export default Page
```

### getStaticProps

다음으로 중요한 `Next.js`문법은 `getStaticProps` method이다. If you export a function called `getStaticProps` (Static Site Generation) from a page, Next.js will pre-render this page at build time using the props returned by `getStaticProps`.

#### When should I use getStaticProps?

You should use `getStaticProps` if:

- The data required to render the page is available at build time ahead of a user’s request
  - `getStaticProps` always runs on the server and never on the client.
  - `getStaticProps` always runs during `next build` and generate HTML files
- The data comes from a headless CMS
- The data can be publicly cached (not user-specific)
- The page must be pre-rendered (for SEO) and be very fast 
  - getStaticProps generates HTML and JSON files, both of which can be cached by a CDN for performance

#### Using getStaticProps to fetch data from a CMS

The following example shows how you can fetch a list of blog posts from a CMS.

```
// posts will be populated at build time by getStaticProps()
function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}

export default Blog
```

## 8. Remix

## 9. Redux

### What is Redux

`Redux` is an open-source JavaScript library for managing and centralizing application state. It is most commonly used with libraries such as React or Angular for building user interfaces. Redux is a predictable **state container** for JavaScript apps. Redux는 일명 **상태 (state)관리 library**이다. React.js와 같이 사용할 시 `react-redux`를 사용한다. `Redux`는 `redux-toolkit`으로 쓰면 더 쉽고 거기에 typescript로 작성하면 큰 프로젝트 스케일링하기도 편하다.


## % 부록0: 유용한 VSCode 기능 알아보기 %

- `단어 + tab`: Snippets를 이용하여 자동완성 기능을 적극활용한다.
- Debug tool를 이용하여 프로그램을 디버깅할 수 있다 (내가 확인하고 싶은 코드 옆에 breakpoint 생성 후 debug 실행).

### 유용한 VScode extension

- `Prettier`: save시 auto code formatting.
  1. `CTRL + ,`로 setting 열기
  2. `save` 검색 후 `format on save` 체크
  3. `prettier` 검색 후 `Prettier: Tab width`를 `2`로 변경
  4. `quote` 검색 후 `Javascript/Typescript > preferences: Quote style`을 `single`로 변경

- `Live Server`: HTML/CSS/Javascript의 server 실행
- `Material icon theme`: file icon 변경
- `ES7+ React/Redux/React-Native snippets`: React 개발환경시 코드 자동완성
- `Auto rename tag`: HTML에서 tag이름 변경 시, 뒤의 tag도 같이 변경
- `HTML CSS Support`: HTML에서 CSS file의 자동완성
- `Volar`: Vue 개발환경
- `bracket pair colorizer2`: 괄호마다 색생추가
- `CSS peek`: HTML에서 CSS peek가능
- `indent-rainbow`: indentation마다 색상추가
- `open in browser`: HTML을 browser로 열기
- `ESLint`
- `GitLens — Git supercharged`: git을 이용해, 코드 변경자 확인
- `Community Material Theme`: VScode 색상변경
- `Remote Remote - WSL`: Windows로 WSL 실행시만 설치

### keyboard snippets

우리는 코드를 짤 때, 최대한 마우스를 사용하지 않도록 해야 된다. keyboard snippets을 이용하면, 키보트만으로도 우리가 하고 싶은 것을 빠르게 할 수 있다.

- In VScode, go to `Help > Keyboard Shortcuts References`. 우리가 사용가능한 유용한 키보드 단축기들을 볼 수 있다.

#### Navigation

- `Ctrl + P`: 이 폴더 내에 다른 file name을 입력 후, 그 file로 이동 (파일간 이동)
- `Ctrl + G`: 이 파일 내에 Line 이동 (파일 내 이동)
- `pageUp/pageDown`: Move to (next/previous) page in file
- `Alt + (pageUP/pageDown)`: Scroll page up/down
- `F12`: Go to Definition (선택된 코드가 정의된 file로 워프)
- `Alt + F12`: peek Definition (현재 file에서 확인)
- `Ctrl + (Left/Right)`: 단어 단위로 왼쪽/오른쪽으로 이동
- `Ctrl + (Up/Down)`: Scroll line up/down
- `Home/End`: Go to beginning/end of line
  - In labtop:
  - `Fn + leftArrow`: End
  - `Fn + rightArrow`: Home
  - `Fn + downArow`: pageDown
  - `Fn + upArrow`: pageUp
- `Ctrl + (Home/End)`: Go to beginning/end of file
- `Ctrl + (1/2/3)`: 새로운 split editor 생성 후, 그곳으로 cursor이동
- `Ctrl + F4`: 현재 split editor 종료

- `Ctrl + click`: Go to definition

#### Basic editing

- `tab`: 자동완성 (현재치고 있는 코드를 자동완성)
- `Ctrl + X`: Cut line (empty selection)
- `Ctrl+ shift + k`: Delete Line
- `Ctrl + L => DEL`: Delete Line
- `Ctrl + C`: Copy
- `Ctrl + V`: Paste
- `Ctrl + Z`: Undo
- `Ctrl + S`: Save
- ``Ctrl + `(back tic)``: Open terminal
- ``Ctrl + Shift + `(back tic)``: Create new terminal
- `Ctrl + shift + R`: Refactoring (drag된 코드를 변수로 만들기, 함수로 만들기, 새로운 file로 옮기기, ...)
- `F2`: Renaming (변수 이름 변경하기: 이 변수와 연관된 모든 다른 file에서 사용중인 변수명도 함께 바꿔준다.)
- `Ctrl + F`: Find (F2를 사용하는 것이 더 편리하다).
- `Ctrl + H`: Renaming (F2를 사용하는 것이 더 편리하다).
- `Ctrl + L`: 한 줄 선택
- `Alt + (Up/Down)`: 한 줄을 위/아래로 옮기기
- `shift + alt + (Up/Down)`: 한 줄을 아래줄에 복사후 붙여넣기 (Copy & Paste)
- `shift + (Arrow)`: Arrow로 움직인 영역만큼만 drag
- `shift + Ctrl + (Arrow)`: 단어 단위로 Arrow로 움직인 영역만큼만 drag
- `Ctrl+ /`: Toggle line comment
- `Ctrl+ (]/[)`: Indent/outdent line
- `Terminal에서 (Up/Down)`: 이전에 Terminal에 입력했었던 command 보기
- `Del`: 커서 뒤의 한 캐릭터 삭제
- `Ctrl + Del`: 커서 뒤의 한 단어 삭제
- `Ctrl + A`: 현재 파일의 모든 문장 drag
- `Ctrl + ,`: Setting 열기

- `Alt + click`: Multi-cursor (Alt + Click를 여러 군데 찍으면, 한번에 여러 곳에 typing할 수 있다).

### Terminal (Unix shell) Command

- `ls`: list files in current directory (list)
- `ls -l`: list files detail in current directory (list -long)
- `ls -a`: list all files in current directory (list -all)
- `mkdir + fileName`: make directory
- `cd`: change directory
- `chmod +x fileName` : make it executable (change mode)
- `cd dirName`: change directory
- `cd ..`: change directory backword
- `rm fileName`: remove file
- `rm -r dirName`: remove directory
- `rm -f fileName`: force to remove file
- `rm- rf dirName`: force to remove directory
- `./executableFile.exe`: execute the file
- `mv oldName newName`: rename the file
- `mv file1 file2 dir`: move the files `file1` and `file2` to the `dir1` directory
- `cat fileName`: see the whole text file in terminal
- `pwd`: show current path you are in
- `man (1/2/3) malloc`: show manual page for malloc
- `clear`: clear all text in terminal
- `find . -type file -name "*.json"`: 현제 folder의 내부에 존재하는 모든 json 파일을 반환
- `touch fileName`: fileName이 존재하면 파일 열기, 존재하지 않으면 새로운 파일 생성
- `echo + text`: Terminal에 text 출력
- `echo + text > fileName`: fileName에 text를 덮어 씌우기
- `echo + text >> fileName`: fileName에 text를 append
- `vi fileName`: Vim text editor로 fileName열기
- `nano fileName`: nano text editor로 fileName열기
- `code fileName`: VSCode text editor로 fileName열기

### Emmets

에밋(Emmet)은 HTML, XML, XSL 문서 등을 편집할 때 빠른 코딩을 위해 사용하는 플러그인이다. 매우 간단한 몇 가지 코드만 입력하면, 자동으로 완전한 HTML 코드를 생성해 준다. Emmet은 Visual Studio Code에 내장되어 있으며 확장이 필요하지 않습니다.

예시:

ul box안에 li tag를 5개 만들고 싶다.

- `ul>li*5` + tab

```
<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>
```

div box안에 container라는 class를 주고, class가 title과 title$인 p tag를 3개 만들고 싶다.

- `div.container>p.title.title${$}*3` + tab

```
<div class="container">
	<p class="title title1">1</p>
	<p class="title title2">2</p>
	<p class="title title3">3</p>
</div>
```

- `div>(header>ul>li*2>a)+footer>p` + tab

```
<div>
  <header>
    <ul>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
    </ul>
  </header>
  <footer>
    <p></p>
  </footer>
</div>
```

더미 dummy 용 텍스트 입력하기

- `p>lorem` + tab

- `p>lorem4` + tab

```
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus quibusdam eligendi commodi, nisi reprehenderit corporis, libero laudantium quo blanditiis unde maiores voluptatum quam mollitia necessitatibus facilis aspernatur minima ullam cupiditate.</p>

<p>Lorem ipsum dolor sit.</p>
```

css에서 display를 none으로 하고 싶다.

- `dn` + tab = `display:none;`

css에서 margin-top을 20px으로 하고 싶다.

- `mt20` + tab = `margin-top:20px;`

Emmets은 html, css을 생성할 때만 가능한 것으로, react 개발환경인 jsx에서는 사용할 수 없다.

Enable Emmet support for JSX:

- In VScode, go to `File > Preferences > Settings > Open setting (setting.json) `

We will add the following lines anywhere in this setting:

```
"emmet.includeLanguages": {
  "javascript": "javascriptreact",
  "typescript": "typescriptreact"
}
```

이제 HTML, CSS뿐만 아니라 react js 개발환경에서도 Emmet을 사용할 수 있다.

### ES7+ React/Redux/React-Native snippets

VScode extension인 `ES7+ React/Redux/React-Native snippets`을 download하면 `rafce`만 code에 입력하면 arrow function이 자동적으로 완성된다.

이는 React Js 코드, 특히 components를 작성할 떄, 매우 간편하게 사용할 수 있다.

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

## % 부록1: git으로 다른 programmer와 collaboration 하기 %

### Git이 무엇이고, 왜 사용하는지

깃(Git)은 software의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

1. project version들을 쉽게 관리하려고
2. project source code를 저장하고, 다른 programmer와 공유하고, 협업하기 위해서

### Git 환경설정

Git을 다운받은후 Terminal에 다음을 입력해 설정한다.

> $ `git config --global user.name "my_name"`, 

> $ `git config --global user.email "myEmail@example.com"`

### Git으로 처음 project 시작하기 

git을 사용할 project folder에서 terminal에 `git init`을 입력

`git init`은 맨 처음에 새로운 project를 위한 git repository를 만들 때만 사용하는 command이다. 즉, 기존에 진행되어 이미 source code가 github server에 올라간 project들은 `git init`을 할 필요가 없다.

`git init`을 한 project는 내 컴퓨터 내에서만 git을 사용하는 것이다. 그럼으로 github server로 project를 올리려면 새로 git repository를 생성 후 직접 연결해주어야 한다.

`git remote ...`로 내 컴퓨터와 github server를 연결해 온라인에서 다른 프로그래머와 협업할 수 있다.

### Git workflow

![gitworkflow2](img/git-workflow-1.png)

1. Download source code

> $ `git clone https:...` or `Download zip file`

또는 이미 한 번 다운 받은 적이 있는 project의 최신 버전은 `git pull` command를 이용한다.

> $ `git pull origin master` 

2. branch에 source code 복사하기

branchName branch를 생성 후 바로 이동

> $ `git checkout -b branchName`

또는 Move to the existing branch:

> $ `git switch -c branchName`

3. 소스 코드에 변화를 만든 후, pull request하여 다른 협업자가 볼 수 있게 하기

Do your thing, then when your ready to push, open terminal back up and make sure your in the base directory for the project:

Stage all your changes for commit

> $ `git add .`

Commit your changes

> $ `git commit -m "My Commit Message, what did I do today?"`

Push your commit to a remote branch (probably want to use your same local branch name)

> $ `git push --set-upstream origin branchName`

또는

> $ `git push -u orgin branchName`

`git push -u origin master` command는 main branch에 code를 push 하는 것입니다. master branch는 항상 완벽하게 작동하는 코드이어야 함으로 master branch에 직접적으로 push하는 것은 지양해야 합니다. 위에 서술된 방법으로, 새로운 branch를 만들어서 pull request를 하여 다른 개발자의 code review를 받은 후 문제가 없으면 master branch에 merge하면 된다.

요약:

![gitworkflow1](img/gitworkflow.jpg)

1. Download source code: `git clone https:...`
2. Create new branch or change to new existing branch
   - Create and move to new branch: `git checkout -b <branchName>`
   - Move to the existing branch: `git switch -c <branchName>`
3. Make changes to the code
4. Once you finish, create pull request 
   - `git add .`
   - Commit your work: `git commit -m "what i did"`
   - push your work to that branch: `git push -u origin <branchName>`

### Git의 `master` branch는 항상 완전환 코드이어야 한다.

다른 사람이랑 협업을 할 경우에 git의 `issues`, `pull request` 탭을 잘 활용하여, 프로젝트를 성공적으로 완성해 보자.

- issues: 코드의 문제점 제시 
  - 코드에서 고쳐야 할 부분들을 우리팀 전체가 볼 수 있게 만들어, 추후에 고칠 수 있게 하는 것. 이 프로젝트가 public이라면, 아무나 issues에 코드의 문제점을 제시할 수 있다.
- pull request: master branch에 merge하기 전에 내가 고친 코드를 다른 협업자가 관찰하고 이상이 없는 지 확인하는 단계

### Git Command

Initialize repository

> $ `git init`

project내 모든 branch를 출력

> $ `git branch`

Create branch called v1

> $ `git branch v1`

기존의 branchName brannch로 이동

> $ `git checkout branchName`

새로운 branchName branch를 생성 후, 바로 그 branch로 이동

> $ `git checkout -b branchName`

Create branch called fix-19 based on the code in the fix-18 branch

> $ `git checkout -b fix-18 fix-19`

#### git clone/pull로 최신 버젼의 project 가져오기 

💣 `git pull` =` git fetch` +` git merge`

pull과 fetch의 차이점은 병합을 하냐 안 하냐의 차이다.

- `git pull`
  - 원격저장소에 있는 프로젝트의 변경사항을 그대로 로컬저장소에 옮겨와 자동으로 병합
  - 팀 단위로 사용하는 계정이 아닌 개인적으로 깃허브를 사용하는 사람들이라면 git pull 명령어를 가장 많이 사용할 것이다.
  - "변경 사항을 가져옴과 동시에 자동으로 병합이 되기 때문에 무엇이 추가되고 병합되었는지 확인이 안 됨"

- `git fetch`
  - 원격저장소에 있는 프로젝트의 변경사항을 가져오기만 한 후 병합(merge)은 따로 깃 입문자 또는 깃허브를 개인적으로 사용하는 사람이라면 git fetch 명령어는 거의 사용하지 않을 것이다.
  - "다른 사람이 수정한 부분을 확인하고 병합할 수 있다는 장점이 있음"

- `git clone`
  - clone이라는 단어처럼 원격저장소의 내용을 새로운 폴더에 그대로 복사하는 것!
  - 맨 처음 project의 source code를 복사할 경우에만 사용

1. 맨 처음에 터미널을 열고 `git clone https:...`를 입력 해 local storage로 source code 복사한다. 
2. `git remote -v`로 연결된 저장소 확인

```
> $ git remote -v
origin  https://github.com/heeshin174/Web_App_Dev_Kor.git (fetch)
origin  https://github.com/heeshin174/Web_App_Dev_Kor.git (push)
```

3. 다른 협력자가 올린 최신 버젼의 코드를 내가 다운받은 파일에 덮어씌우기

저장소 연결 확인 후 `git pull` 입력

> $ `git pull`

만약 안된다면 다음 command 입력

> $ `git pull origin master`

### Git 특정 commit으로 돌아가기

#### 이전 commit source code 보고 돌아오기

이전 커밋의 소스를 확인하고 싶을 경우, 두 가지 방법이 있다.

1. 커밋 메시지 보고 특정 커밋으로 되돌리기

> $ `git log`

    - 명령 입력 후, 위 아래 방향키로 원하는 버전 커밋 찾기
    - 'commit' 문구 뒤의 해시코드 앞에서 4자리 이상 복사

```
commit 405d3263fab12e39a5b32a0edf80dd84eb6fd8f1 (HEAD -> master, origin/master, origin/HEAD)
Author: heeshin174 <heeshin174@gmail.com>
Date:   Sat Feb 19 23:21:53 2022 -0600

    add closure

commit 63fd02899e6766e338ef288cb64cd0fb8331a078
Author: heeshin174 <heeshin174@gmail.com>
Date:   Fri Feb 18 13:50:57 2022 -0600

...
```

> $ `git checkout 4자리이상의커밋해시코드`

    - 현재 소스가 해당 버전으로 돌아간다.

> $ `git checkout branchName`

- 되돌아오기(해당 브랜치의 최신 커밋으로 돌리기)

2. 단계별로 되돌아가기

> $ `git checkout head~1`

    - 최신 커밋으로부터 한단계 전으로 되돌린다.
    - 1에 해당하는 부분을 바꿔서 원하는 단계만큼 지정할 수 있다.

> $ `git checkout branchName`

- 되돌아오기(해당 브랜치의 최신 커밋으로 돌리기)

#### 이전 버전으로 되돌리기

되돌렸다가 돌아오지 않고 아예 되돌리고 싶은 경우에도 두 가지 방법이 있지만,
웬만하면 `revert` 를 권장한다.

1. 되돌리는 버전을 새로 커밋하기(권장 O)

> $ `git revert head~1` 혹은 `git revert 4자리이상의커밋해시코드`

    - 앞서 설명한 checkout 의 두 가지 방법 모두 똑같이 revert 에 적용 가능하다.
    - revert 명령시 해당 커밋 버전으로 새로 커밋하게 되므로, 커밋 메시지 입력창이 나타난다.
     - i 입력 후 커밋메시지 수정하기. :wq 입력하여 저장 후 종료하기

2. 되돌리는 버전 이후의 커밋을 삭제하기(권장 X)

> `git reset --hard head~1` 혹은 `git reset --hard 4자리이상의커밋해시코드`

    - 앞서 설명한 checkout 의 두 가지 방법 모두 똑같이 reset 에도 에 적용 가능하다.
    - 남아있는 추가됐던 파일 지우기

## 1. Web Application Development

### 1. What is SERVER?

**Server는 Client에게 Network를 통해 http요청을 받아서 정보, data, 서비스등을 전달하는 Computer이다.**

위의 Server에 대한 정의를 쉽게 이야기하면, **Server는 요청을 받아 그 요청을 처리하는 기계이다.** Web Server에서 요청은 `http request`을 의미한다.

- **Server: Client의 요청을 받으면 요청한 내용을 보내주는 program이 실행중인 Computer**
- **Web Server: Client의 http요청을 받으면 요청한 내용을 보내주는 program이 실행중인 Computer**
- **Client: 서버에게 요청을 보내는 Computer**
- Server 개발자: 요청을 받으면 요청한 내용을 보내주는 program을 만드는 사람.
- 네이버웹툰 Web Server 개발자가 만드는 code: 어떤 사람이 `comic.naver.com`으로 접속하면, 네이버웹툰 메인 html파일을 전송해주셈

Server와 Client는 web application에서 computer가 하는 역할을 의미한다. 사람이 학교에서 학생, 선생님, 청소부와 같은 role를 맡는 것처럼,
computer가 web app에서 server, client의 역할을 한다. 한 computer가 server의 역할을 하고 있으면, 다른 computer가 client가 되어 이 server에 데이터를 요청할 수 있다.

Server는 식당의 종업원 (Server)과 같은 일을 한다. 손님이 메뉴판에 있는 음식을 주문하면, 그 음식을 가져다 주는 것처럼, Client가 Server에 데이터를 요청하면, 그 데이터를 가져다 주는 역할을 한다.

Client가 Web Server에게 할 수 있는 http요청은 크게 4가지이다:

1. GET요청: 읽기
2. POST요청: 쓰기
3. PUT요청: 수정
4. DELETE요청: 삭제

여기서 알아야 할 점은 client가 http request를 보내는 code를 작성해야지만 server와 정보를 주고 받을 수가 있다는 점이다. 사용자는 GET요청를 browser의 URL 입력창에서 쉽게 작성이 가능하다. 다른 POST/PUT/DELETE 요청들은 Server 개발자가 웹페이지에 버튼들을 만들어 놓아서 사용자가 웹페이지내에서 쉽게 http request를 할 수 있도록 만들어 놓을 수 있다.

즉, 웹 서버개발자가 http요청을 하는 버튼들을 웹페이지에 잘 만들어 놓으면, 사용자는 내용을 입력 후 클릭만으로 http요청을 할 수 있다.

1. GET요청은 읽기 요청으로 서버에 "나 이런 URI을 가진 페이지를 읽고 싶음"이라는 요청을 보낼 수 있다. 우리가 Server에 가장 많이 하는 요청으로 Chrome, Edge와 같은 browser로 URI만 검색하면 GET요청을 할 수 있다.

2. POST요청은 생성 요청으로 서버에 "서버에 내가 작성한 블로그 포스트, 글, 댓글등을 생성해 주세요"라는 요청을 보낼 수 있다.

3. PUT요청은 수정 요청으로 서버에 "서버에 있는 블로그 포스트, 글, 댓글등을 수정해 주세요"라는 요청을 보낼 수 있다.

4. DELETE요청은 수정 요청으로 서버에 "서버에 있는 블로그 포스트, 글, 댓글등을 삭제해 주세요"라는 요청을 보낼 수 있다.

### 2. What is APIs (Application Programming Interface)?

**API는 한 program에서 다른 program으로 data를 주고받기 위한 방법을 의미한다.**

API는 식당에서의 메뉴판과 같은 역할을 한다고 이해하면 쉽다. 식당의 API는 메뉴판으로, 식당과 손님이 음식을 주고받기 위한 방법이다.
식당은 메뉴판을 만들어 놓고, 손님이 음식을 주문 하기 전까지는 아무것도 하지 않는다. 또한 손님이 메뉴판에 없는 음식을 주문하면, 식당은 그 주문은 받을 수가 없다.

이와 마찬가지로, 서버도, 메뉴판, 즉 API를 만들어 놓아야지만 그 API를 가지고 client와 data를 주고 받을 수 있다. Server는 client에게 **요청 (request)**을 받지 않으면, 아무것도 하지 않는다. 또한, 손님은 메뉴판에 없는 요리는 주문할 수 없는 것처럼, client는 server에 정의되지 않은 API를 가지고 요청은 할 수 없다.

```
// 식당에서의 Server와 Client
1. 손님이 식당에 있는 메뉴판을 보고 종업원에게 주문 요청
2. 종업원은 손님의 주문을 받아 요리사에게 전달
3. 종업원은 요리사의 음식을 받아 손님에게 전달

      1                    2
손님    ------->   종업원   ------>   요리사
       <-------            <------
      4                    3

// Web application에서의 Server와 Client
1. Client는 Server가 보여주는 API을 보고 Server에게 HTTP 요청 (http request)
2. Server는 Client의 http요청을 받아 Database에게 전달
3. Server는 Database의 data를 받아 Client에게 전달 (response)

// Database가 없는 web server의 경우, 서버 내에서 요청을 처리한다.

      1.http request          2.request
Client ------->      Server     ------>  Database
       <-------                 <------
      4.response                3.get data
```

위에서 API는 서버와 사용자가 데이터를 주고 받기 위한 방법이라고 했는데, 여기서 방법이란 그냥 개발자가 만들어 놓은 코드를 의미한다. 웹 서버의 경우, 서버 개발자가 사용자의 http요청을 받았을 때 서버가 할 행동들을 미리 정의해 둔다. 그 후 만들어 놓은 server의 responses, 즉 API을 메뉴판처럼 사용자에게 보여주면 된다.

```
// API 예시
// 어떤 사용자가 "https://~/detail"로 GET요청을 하면 이 코드를 실행해 주세요
app.get('/detail', (request, response) => {
    // code to perform particular action (API).
    // To access GET variable use req.query() and req.params() methods.
});
```

Web Server의 API를 성공적으로 작동하기 위해서는 다음이 필요하다:

1. 요청방식 (http request method): 어떤 요청을 할 것인지
2. URI (endpoint): 어떤 자료를 요청할지
3. Parameter: 자료요청에 필요한 추가 정보

예시: `(GET request) https://comic.naver.com/webtoon/detail?id=318995`

1. 요청방식: GET request
2. Endpoint: `https://comic.naver.com/webtoon/detail`
3. Parameter: `id=318995`

Web Server의 경우 `REST API`라는 방법론의 원칙에 따라 API를 작성하면 좋다.

잘 만든 API는 상업적으로 팔 수 있다. API hosting service를 이용하여 정해진 횟수 이상의 데이터 요청이 발생하면, 사용자에게 돈을 지불하게 만들 수 있다.

⭐ 요약:

1. API가 무엇인가?

**API: 한 program에서 다른 program으로 data를 주고 받기 위한 서버의 메뉴판**

2. Web Server에서 API가 무엇인가?

**Web Server에서의 API: 서버 개발자가 사용자에게 어떤 data를 얻기 위해서는 어떤 URI로 http요청을 보내라고 알려주는 서버의 메뉴판**

### 3. REST (Representational State Transfer) APIs

**REST는 HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD (CREATE, READ, UPDATE, DELETE) Operation을 적용하는 것을 의미한다.**

- REST API는 크게 세가지로 구성으로 있다:

1. 자원 (RESOURCE): URI (접근할 대상)
2. 행위 (Verb): HTTP METHOD { GET(조회), POST(생성), PUT(수정), DELELTE(삭제) }
3. 표현 (Representations): Message

- REST API를 설계할 때, 다음의 2가지를 만족해야 한다.

1. **URI는 정보의 자원을 표현해야 한다.**
2. **자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.**

```
1. 회원을 삭제하는 URI
GET /members/delete/1 (x)
DELETE /members/1     (o)

2. 회원정보를 가져오는 URI
GET /members/show/1 (x)
GET /members/1      (o)

3. 회원을 추가하는 URI
GET /members/insert/2 (x)
POST /members/2       (o)
```

URI를 설계할 때 주의할 점:

1. 슬래쉬 구분자(/)는 계층 관계를 나타내는 데 사용

```
http://restapi.example.com/houses/apartments
http://restapi.example.com/animals/mammals/whales
```

2. URI 마지막 문자로 슬래시(/)를 포함하지 않는다. URI에 포함되는 모든 글자는 리소스의 유일한 식별자로 사용되어야 하며 URI가 다르다는 것은 리소스가 다르다는 것이고, 역으로 리소스가 다르면 URI도 달라져야 합니다. REST API는 분명한 URI를 만들어 통신을 해야 하기 때문에 혼동을 주지 않도록 URI 경로의 마지막에는 슬래시(/)를 사용하지 않습니다.

```
http://restapi.example.com/houses/apartments/ (X)
http://restapi.example.com/houses/apartments  (0)
```

3. 하이픈 (hyphen: -)은 URI 가독성을 높이는데 사용한다. URI를 쉽게 읽고 해석하기 위해, 불가피하게 긴 URI경로를 사용하게 된다면 하이픈 (-)을 사용해 가독성을 높인다.

4. 밑줄 (\_)은 URI에 사용하지 않는다. 글꼴에 따라 다르긴 하지만 밑줄은 보기 어렵거나 밑줄 때문에 문자가 가려지기도 합니다. 가독성을 위해 밑줄 대신 하이픈(-)을 사용하는 것이 좋습니다.

5. URI 경로에는 소문자가 적합하다. URI 경로에 대문자 사용은 피하도록 해야 합니다. 대소문자에 따라 다른 리소스로 인식하게 되기 때문입니다. RFC 3986 (URI 문법 형식)은 URI 스키마와 호스트를 제외하고는 대소문자를 구별하도록 규정하기 때문이지요.

6. 파일 확장자는 URI에 포함시키지 않는다.

```
http://restapi.example.com/members/soccer/345/photo.jpg (X)

// REST API에서는 메시지 바디 내용의 포맷을 나타내기 위한 파일 확장자를 URI 안에 포함시키지 않습니다.
// Accept header를 사용하도록 합시다.
GET / members/soccer/345/photo HTTP/1.1 Host: restapi.example.com Accept: image/jpg
```

Below is a table summarizing recommended return values of the primary HTTP methods in combination with the resource URIs:

| HTTP Verb | CRUD   | Entire Collection (e.g. /customers) | Specific Item (e.g. /customers/{id})                                       |
| --------- | ------ | ----------------------------------- | -------------------------------------------------------------------------- |
| POST      | Create | 201 (Created)                       | 404 (Not Found), 409 (Conflict) if resource already exists..               |
| GET       | READ   | 200 (OK)                            | 404 (Not Found), if ID not found or invalid.                               |
| PUT/PATCH | UPDATE | 405 (Method Not Allowed)            | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
| DELETE    | DELETE | 405 (Method Not Allowed)            | 200 (OK). 404 (Not Found), if ID not found or invalid.                     |

Postman is great program to build an RESTful web services.

- Postman POST요청 사용법:

1. POST의 Header에서 `Content-Type:application/json`을 선택한다.
2. POST의 Body에서 `raw` 선택 후, Post하고자 하는 데이터를 JSON 형식으로 입력한다.

또는

1. POST의 Body에서 `x-www-form-urlencoded` 선택 후, Post하고자 하는 데이터를 key, value pair로 입력한다.

![POST1](./img/postman1.png)

![POST2](./img/postman2.png)

⭐ 요약:

1. REST API가 무엇인가?

**REST API는 Web 통신에서 사용자로부터 http요청을 받을 URI를 설계할 때 지켜야 되는 방법론을 기반으로 만든 API를 의미한다.**

2. REST API를 왜 사용하는가?

**REST API를 사용하면, 사용자는 URI 주소만 가지고도 내가 무슨 Data를 다루고 있는지 쉽게 알 수 있다.**

### 4. What is Node.js?

**Node.js는 Javascript runtime environment이다.**

Javascript는 HTML에 종속된 programming language이다. 즉, 1 + 1과 같은 연산을 보다 **HTML을 조작**하기 위해서 만들어진 script 언어이다.

- `HTML (HyperText Markup Language)`: 웹페이지에 글쓰고, 그림을 넣은 언어로, 프로그래밍언어가 아니기 때문에 정적인 (static: 안움직이는) 웹사이트만 보여줄 수 있다.
- Javascript가 HTML을 조작하여 웹페이지를 동적 (dynamic)으로 바꿔준다. 예): 버튼을 클릭하면 어떤 동작이 실행됨.

Javascript는 Chrome, Edge와 같은 browser가 해석한다. 각 browser마다 Javascript를 해석하는 방법이 다른데, 그 중 Chrome이 만든 `V8`이라는 javascript 해석엔진이 너무 유용해 Chrome browser안에서만 사용하기에는 아까워서 `Node.js`라는 이름을 가지고 browser와 독립되서 나왔다.

즉, `Node.js` 자체로는 프로그래밍 언어가 아니라 Javascript를 실행하게 해주는 실행 환경을 의미한다. `Node.js`덕분에 Javascript를 browser밖에서 Programming Language처럼 사용할 수 있게 되었다.

Node.js로 할 수 있는 대표적인 것은 **Web Server를 만드는 것**이다. Node.js를 사용하면 Web Server를 쉽게 만들 수 있다. 왜 하필 Node.js를 이용하여 Server를 만드는 것이 좋냐하면, Node.js의 **Non-blocking I/O** 특징 때문이다.

- `Node.js`의 특징:

1. **Non-blocking I/O**
2. **Event-driven**

`Non-blocking I/O` operations allow a single process to serve multiple requests at the same time. Instead of the process being blocked and waiting for I/O operations to complete, the I/O operations are delegated to the system, so that the process can execute the next piece of code. 즉, Non-blocking I/O은 Server가 버거운 요청을 받아도, 그 요청이 끝날 때까지 기다리지 않고 뒤의 code들을 실행해서 더 빨리 끝나는 요청을 먼저 처리한다.

```
예시: 사용자의 요청에 따라 영화를 예매하주는 서버
1. 일반 프로그래밍 언어로 만든 서버
사용자가 티켓한장, 두장과 같이 적은 수을 요청하면 문제가 없지만,
사용자가 시간이 오래걸리는 요청, 티겟 200장을 예매하면, 서버는 그 요청을 다 완료할 때까지 다른 작업을 하지 못하게 된다.
이렇게 되면, 티겟 200장 예매한 사람 뒤에 있는 티켓 1장을 예매한 사람 역시 티켓 200장이 예매가 완료될 때 까지 서버를 기다려야 한다.

2. Node.js로 만든 서버
사용자가 시간이 오래걸리는 요청, 티겟 200장을 예매해도 서버는 무거운 요청을 다 완료할 때까지 기다리지 않고,
티겟 200장 예매한 사람 뒤에 있는 티켓 1장을 예매한 사람 먼저 처리를 한 다음에 티켓 200장을 처리한다.
```

`Node.js`는 이벤트를 적극 활용하여 처리가 빠른 것 부터 실행하기 때문에, 요청이 매우 많이 오는 채팅 프로그램 서버나, SNS Web server를 만들 때 적극 선호됩니다. 요즘에는 다른 프로그래밍 언어들도 Node.js방식으로 서버를 짤 수 있기 때문에 요즘은 장점이 희석되긴 했지만, 코드가 매우 짧고 쉽다는 극강의 장점 덕분에 서버 개발 입문자에게 선호도가 높습니다. 하지만, 만약 필요한 서버가 웹 서버가 아니라면, Node.js보다는 Python과 C같은 언어들을 사용하는 것이 좋다.

`Node.js`를 설치하는 이유는? `npm (node package manager)`과 `Javascript`를 사용하기 위해서 node.js를 설치해야한다. `npm`은 `npm.js`에 등록된 package들을 내 프로젝트의 dependencies (packages)로 설치하는 것을 도와준다. 내 프로젝트에 dependencies를 설치하면 다른 프로그래머들이 작성한 유용한 code들을 가져다가 내 프로젝트에 사용할 수 있다.

⭐ 요약:

1. Node.js가 무엇인가?

**Node.js: Browser내에서만 사용가능한 Javascript를 밖에서도 사용가능하게 만든 Javascript 실행환경**

2. Node.js를 왜 사용하는가?

**Node.js는 Web Server를 만드는 데 특화되어 있다. Node.js는 다른 프로그래밍 언어와 다르게 Non-blocking I/O의 특징을 가져, 시간이 오래걸리는 code들을 기다리지 않고, 다음 code를 실행한다. 그럼으로, 요청이 매우 많이 오는 프로그램들은 Node.js를 이용하여 web server를 만들면 된다.**

### 5. Express.js를 이용하여 실제 Server 만들기

`Express.js`는 the most popular Node web framework으로, 아주 간단하게 web server를 만들 수 있도록 도와주는 package이다.

- 환경설정:

1. Node.js 설치: 구글에 Node.js 검색 후, 가장 최신버전 설치
2. VSCode 설치: 구글에 VSCode 검색 후, 가장 최신버전 설치
3. Terminal을 열어 project folder 생성 후, VSCode로 열기

```
> $ mkdir projectName
> $ cd projectName
> $ code .
```

`package.json` 생성 (이 프로젝트가 사용하는 dependencies을 모아둔 파일)

> `npm init`

이러면, `node_modules`란 folder가 생성되는 데, 이 folder에는 다운 받은 packages의 실제 source code가 담겨있다.

`Express.js`을 이 project내에 설치

> `npm i express`

4. `server.js`, `app.js` files을 생성 후, Express.js 가져오기

- `server.js` file

```
const app = require("./app"); // import app from './app.js'

const PORT = 5000;
app.listen(PORT, () => console.log(`Server started on PORT ${PORT}`));

// app.listen(서버를 띄울 port number, 서버를 띄운 후 실행할 코드)
// 8080 port에 웹서버를 생성 후, 서버가 잘 생성이 되면 "Listening on 8080"을 출력한다.
// 여기서 port란: Copmuter에는 외부와 Network 통신을 하기 위해 60000개의 구멍이 존재하고, 각각의 구멍이 하나의 port가 된다.
// 8080 port는 8080 구멍으로 들어오는 통신에만 반응한다.
```

- `app.js` file

```
const express = require('express'); // import Express.js framework
const app = express();

// Bodyparser Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

module.export = app; // export app
```

5. Server를 실행하기: Terminal에 `node server.js`을 입력

6. 내 컴퓨터의 5000 port에 진입하기

Browser에서 `http://localhost:5000`에 GET 요청을 보내면, 내 컴퓨터의 5000 port에 접근할 수 있다.

7. Get 요청에 응답할 code 작성하기

```
// 사용자가 '/pet'으로 Get 요청을 보내면, pet과 관련된 안내문을 띄우기
app.get('/pet', function (req, res) {
  res.send("This is pet page")
  // 또는
  res.status(200).json({ message: "This is pet page" });
});

// Browser에서 `http://localhost:5000/pet`에 Get 요청을 보내면, "This is pet page"라는 문구를 확인할 수 있다.
```

이는 내 컴퓨터의 5000 port이므로, 다른 컴퓨터로 위의 localhost URI를 검색하면, 그 컴퓨터의 5000 port에 접근하기 때문에 이 서버에는 접근할 수 없다.

8. Nodemon.js library로 코드 수정시 서버 재시작을 자동화하기

우리가 코드를 수정하면, 수정할 때마다 서버를 `CTRL + C`로 종료하고 `node server.js`로 서버를 다시 시작해야 한다. 그럼으로 Nodemon.js library로 코드 수정시 서버 재시작을 자동화한다.

nodemon은 개발할 때만 사용할 dependency이기 때문에, -D를 붙혀 실제 production에서는 설치하지 않는다.

> `npm i -D nodemon`

- `package.json` file

```
// package.json의 scripts에 다음의 코드를 추가한다.
"scripts": {
  "start": "node server.js",
  "server": "nodemon server.js"
},
```

- **start**: start the server. but need to restart the server after every server-side change.
- **server**: start the server. nodemon continuously watch the server, and we won't have to keep updating it. server는 개발할 때만 사용할 command이다. 실제 production에서는 nodemon이 필요하지 않다.

To use these command, type:

> `npm start`

> `npm run server`

우리는 이제 `node server.js` 대신 `npm start`로 웹서버를 실행시킬 수 있고, `npm run server`로 nodemon을 이용하여 server를 개발할 수 있다.

9. GET요청시 HTML file을 주는 code 작성하기

사용자가 '/'으로 GET요청시, index.html file 보여주기

```
var path = require("path"); // __dirname을 사용하기 위해, include path module

app.get('/', function (req, res) {
    res.sendFile(__dirname + "/index.html"); // __dirname은 current directory를 반환한다.
});

// Browser에서 `http://localhost:5000`에 Get 요청을 보내면, `index.html` file을 확인할 수 있다.
```

10. Node.js의 CommonJS module을 ES6 module로 변경하기 (Optional)

Node.js는 CommonJS module의 syntax을 채용하였다. 그래서, 다른 files을 불러오거나 내보낼 때 (import/export), CommonJS syntax인 `const module_name = require('module_path')`와 `module.export = "module_name"`을 사용한다. 우리는 `import`와 `export` keywords가 편하기 때문에 ES6 module로 변경 할 것이다.

In order to enable Node support for ES modules we need to tweak the `package.json` file. In the `package.json` file add `"type": "module"` to the root of the file.

```
// package.json에 "type": "module" 추가하기
{
  "name": "index",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js",
    "server": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
  "dependencies": {
    "express": "~4.16.1",
  } "devDependencies" : {
    "nodemon": "~2.0.15"
  }
}
```

Then run the following command to update changes to package.json

> `npm i`

Once we have updated our package file we have to make the relevant changes to our app's code as follows:

```
import express from 'express';

const app = express();
const PORT = 5000;

app.get('/',(req,res) => {
  res.send('ES6 is the Node way to go');
})

app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}!`);
})
```

Callback function을 정의하는 세가지 방법:

1. Arrow function으로 함수의 이름 없이 함수를 정의
2. `function` keyword를 사용해 regular function을 정의
3. 함수를 따로 정의해 그 함수의 이름을 parameter로 전달

```
// arrow function
app.get('/', (req,res) => {
  res.send('ES6 is the Node way to go');
})

// regular function
app.get('/', function (req,res) {
  res.send('ES6 is the Node way to go');
})

// function을 parameter로 전달
const getGoals = (req, res) => {
  try {
    res.status(200).json({ message: "Get goal" });
  } catch (err) {
    console.error(err.message);
  }
};

app.get('/', getGoals)
```

자세한 Express.js 사용법은 official documentation을 참고한다.

⭐ 요약:

1. Express.js가 무엇이고, 왜 사용하는가?

**Express.js는 Javascript web framework로 web server를 아주 쉽고 간편하게 만들게 해준다.**

2. 컴퓨터에서 port가 무엇인지?

**ports는 computer가 외부와 네트워크로 소통할 수 있는 구멍들을 의미하고, localhost:${port}를 browser에 검색하면 내 컴퓨터의 특정 port에 접근할 수 있다.**

### 6. Server 운영 방식에 차이 이해하기

우리가 해외로 파견을 나가 작업을 해야할 때, 큰 회사의 호텔을 이용하거나, 건물을 빌려 사용할 수 있다.

호텔을 이용하면, 빨래, 청소, 식사등 많은 것을 호텔 측에서 해주기 때문에, 나는 내가 할 작업에만 집중할 수 있다. 작업을 같이하는 인원에 변동이 생겨도, 호텔의 방을 더 빌리거나, 줄일 수 있기 때문에 인원수에 맞게 이용할 수 있다. 호텔이 보안에 모든 것을 관리하기 때문에 보안에 민감한 작업팀에게는 맞지 않다.

건물을 빌리면, 빨래, 청소, 식사등 많은 것을 직접해야 하기 때문에, 내가 할 작업에만 집중할 수 없다. 작업을 같이하는 인원에 변동이 생기면, 인원수에 맞게 새로운 건물을 빌려야 한다. 대신, 내가 모든 것을 관리하기 때문에 보안 문제에 더 안전하게 대처할 수 있다.

회사가 server를 운영하는 방식인 `On-premise`방식과 `Cloud computing service` 방식을 각 각
건물을 빌리는 것과 호텔을 이용하는 것에 비유할 수 있다.

1. **On-premise** 방식:
   회사가 집적 물리적인 computer를 사서, 그 computer를 server로 만든다.
   이 방법은 computer를 직접 사야함으로 Cloud Computing service보다 더 많은 돈이 요구된다.
   black friday와 같이, 특정날에 사용자가 많아져 server를 늘리려면, 새로운 computer를 또 사야하고
   이 시즌이 지나면 그 computer는 다시 사용되지 않는다.
   server를 사용자 수에 맞게 scale-up, scale-down하기 쉽지 않아 자원에 낭비가 생긴다.
   대신, 회사가 집적 관리하기 떄문에 보안 문제에 더 안전하다.

2. **Cloud Computing Service** 방식:
   위에서 호텔이 여려 방을 제공한다고 했는데,
   cloud computing에서는 virtualization을 이용하여 한 물리적 computer에 여러대의 가상 computer를 만들 수 있다
   (virtualBox에 ubuntu를 설치하는 것을 생각하면 된다).
   대기업에서 제공하는 Cloud computing service를 이용하면, 회사는 물리적인 computer 자원을 사지않고 저렴한 가격에 server를 운용할 수 있다.
   black friday와 같이, 특정날에 사용자가 많아지면, server를 늘리는 데 아주 적합하다.
   server를 사용자 수에 맞게 scale-up, scale-down하기 쉽기 때문에, 자원에 낭비가 없고, 내가 사용한 만큼만 돈을 지불하면 된다 (pay-as-you-use).

```
Amazon사의 AWS (Amazon web services),
Microsoft사의 Azure,
Google사의 GCP (Google cloud platform)등이 cloud computing service를 제공하는 대표적인 사이트이다.
```

각 방식의 장점 요약:

- On-premise: security
- Cloud Computing service: money, scale-up & down, fast set up

Cloud Computing service가 어디까지 service해주는 가에 따라 service를 세 가지로 나눌 수 있다.

1. `Iaas (Infrastructure as a service)`: AWS EC2 가상 머신,
2. `Paas (platform as a service)`: AWS Elastic Beanstalk,
3. `Saas (Software as a service)`: youtube, evernote, dropbox, Amazon Web Services (AWS)

예로, brainless machine을 생각할 수 있다. 기존에 machine을 만드려먼 그 machine에 들어갈 비싼 computer 부품들을
직접사서 조립해야 했지만, 이젠 machine이 network에 연결만 되어 있으면 cloud Computing service의 computer를 가져다
사용하면 된다. 이런 cloud computing service의 엄청난 장점 덕분에 대세로 떠오르고 있다.

- 기존 machine: 실제 computer 부품 구매하여 제품내에 설치하고 비용은 200만원으로 비싸다.
- Brainless machine: network를 사용하여 더 좋은 computer를 더 싸게 이용하고 비용은 50만원으로 더 저렴하다.

⭐ 요약:

1. Cloud Computing Services가 무엇인가?

**Cloud Computing Services는 내 컴퓨터가 아닌 각 Cloud computing service의 데이터베이스에 있는 computer들로 Server를 운영하기 때문에, 내가 직접 컴퓨터를 안사도 인터넷만 있으면 더 싼 가격에 더 좋은 컴퓨터로 나의 Server를 운영할 수 있다.**

2. Cloud Computing Services를 왜 사용하는가?

**Cloud Computing Services로 Server를 운영하면 money, scale-up & down, fast set up에 엄청난 강점이 존재한다.**

### 7. CORS (Cross-Origin Resource Sharing) 이해하기

#### CORS가 무엇인가?

**CORS는 다른 출처간에 resource를 공유할 수 있도록, browser내에서 다른 URI사이의 API등의 데이터 접근이 가능하도록 허용하는 것을 의미한다.**

`교차 출처 리소스 공유(Cross-Origin Resource Sharing, CORS)`는 추가 HTTP Header를 사용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제입니다.

CORS란 내 주소에서 다른 주소로 API로 데이터를 받아오기 위해 **Frontend에서** HTTP request를 보냈을 때 발생하는 에러를 없에기 위한 것이다. Postman이나 backend에서 다른 주소로 http요청을 하면 잘 작동하는 데, 웹브라우저에서 다른 주소로 http요청을 하면 CORS 문제로 막히게 된다.

이는 크롬, 엣지같은 browser가 내가 data를 얻기위해 방문하는 웹사이트를 믿지 못하기 때문에 발생하는 에러이다. Browser로 내가 웹사이트에 login한 사이트들은 다음번에 이 사이트를 방문하면, log-in한 것이 유지되고 있는 경우가 많다. 이는 browser가 token등의 로그인 정보를 cookie로 저장해서, 그 사이트를 다시 접속하면, 그 http request에다가 로그인 정보가 있는 cookie를 같이 보내, 웹사이트가 내가 로그인이 되어있다는 것을 알게하기 때문에 가능하다.

그럼으로, 브라우저에서는 보안적인 이유로 `cross-origin` HTTP 요청들을 제한한다. 그래서 `cross-origin` 요청을 하려면 서버의 동의가 필요합니다. 만약 서버가 동의한다면 브라우저에서는 요청을 허락하고, 동의하지 않는다면 브라우저에서 거절합니다.

이러한 허락을 구하고 거절하는 메커니즘을 HTTP-header를 이용해서 가능한데, 이를 `CORS(Cross-Origin Resource Sharing)`라고 부릅니다.

그래서 브라우저에서 `cross-origin` 요청을 안전하게 할 수 있도록 하는 메커니즘입니다.

`cross-origin`이란 다음 중 한 가지라도 다른 경우를 말합니다:

- **Protocal** (scheme): http와 https는 프로토콜이 다르다.
- **Domain**: `domain.com`과 `other-domain.com`은 다르다.
- **port**: 8080포트와 3000포트는 다르다.

```
https://naver.com/id=3:3000

Scheme(Protocol) : https
Domain : naver.com
port : 3000
```

즉, Origin이란 출처를 의미하며 `Protocol + Host + Port` 를 합친 것을 말한다. Origin이 같으면 CORS가 필요하지 않고, 에러는 발생하지 않는다.

#### CORS가 왜 필요한가?

CORS가 없이 모든 곳에서 데이터를 요청할 수 있게 되면, 다른 사이트에서 원래 사이트를 흉내낼 수 있게 됩니다. 악성웹사이트들은 악성사이트로 나를 유인하여 내 크롬에 저장된 일반 웹사이트에 대한 인증정보를 훔쳐 그 웹사이트를 내 개인정보를 이용하여 접속하면, 내 아이디로 다른 사이트에 로그인이 가능하다. 그래서 이를 막기위해 broswer는 `SOP (Same-Origin Policy)`, 동일 출처 정책,으로 동일한 Origin사이에서만 API등의 data 접근이 가능하고, 다른 cross origin으로의 요청을 막는 것을 의미한다.

원래는 Browser는 서로 다른 출처끼리의 요청을 주고받는 건 금지되어있다. 하지만, 웹 생태계가 다양해 지면서, 여러 서비스들간에 보다 자유롭게 데이터가 주고 받아질 필요가 생기면서 합의된 출처들간에 데이터를 주고받는 것을 합법적으로 허용하기 위해 CORS가 등징했다. CORS를 사용하려면 요청을 받는 backend쪽에서 이걸 허락할 다른 출처들을 미리 명시해 두면 된다.

- 예시: 음식점 홈페이지에서 Google map API로 데이터를 요청한다. 다른 주소로의 요청이니까 `Cross-Origin API`이다. Broswer는 다른 주소로의 요청에는 Origin이라는 HEADER를 추가해서 보낸다. Header의 Origin 항목에는 요청하는 쪽의 scheme (Protocol), domain, port가 담겨있다. 이 요청을 받은 Google map API는 답장 HEADER에 지정된 `Access-Control-Allow-Origin` 정보를 실어서 보낸다. 만약 음식점 홈페이지 URI가 CORS에 등록된 상태면, 답장 HEADER에 이 URI도 들어있다. 크롬이 Origin애서 보낸 출처값이 Googlde Map server의 답장 HEADER에 담긴 `Access-Control-Allow-Origin`에 똑같이 있으면 안전한 웹사이트로 간주하고, response data를 받아온다. 만약 없다면, 크롬은 "data를 받으려면 CORS를 사용하던지 해라"라는 error를 발생시킨다.

#### CORS는 어떻게 동작하는가?

- `Simple requests`인 경우

1. 서버로 요청을 합니다.
2. 서버의 응답이 왔을 때 브라우저가 요청한 Origin과 응답한 헤더 `Access-Control-Request-Headers`의 값을 비교하여 유효한 요청이라면 리소스를 응답합니다.
3. 만약 유효하지 않은 요청이라면 브라우저에서 이를 막고 에러가 발생합니다.

- Simple requests란?

1. HTTP method가 GET, HEAD, POST 중 하나이면서
2. 자동으로 설정되는 헤더는 제외하고, 설정할 수 있는 다음 헤더들만 변경하면서

```
Accept
Accept-Language
Content-Language
```

3. `Content-Type`이 다음과 같은 경우

```
application/x-www-form-urlencoded
multipart/form-data
text/plain
```

Simple requqets라고 부릅니다. 이 요청은 추가적으로 확인하지 않고 바로 본 요청을 보냅니다.

- `preflight` 요청일 경우

Origin헤더에 현재 요청하는 origin과,` Access-Control-Request-Method` Header에 요청하는 HTTP method와 `Access-Control-Request-Headers` 요청 시 사용할 헤더를 OPTIONS 메서드로 서버로 요청합니다. 이때 내용물은 없이 헤더만 전송합니다. 브라우저가 서버에서 응답한 헤더를 보고 유효한 요청인지 확인합니다. 만약 유효하지 않은 요청이라면 요청은 중단되고 에러가 발생합니다. 만약 유효한 요청이라면 원래 요청으로 보내려던 요청을 다시 요청하여 리소스를 응답받습니다.

- preflight 요청이란?

사용자 인증정보가 담긴 token이 담긴 요청에 대해서는 token이 나쁜용도로 사용될 수 있기 때문에 더욱 엄격하다. 요청을 보내는 쪽에서는 요청의 옵션에 `credential = true`로 설정해야 되고, 요청을 받는 쪽에서는 아무 출처나 다 허용하는 `와일드 카드 (*)`가 아니라 보내는 쪽의 출처와 웹페이지 주소를 정확히 명시한 다음 `Access-Control-Allow-Credential = true`로 설정해야지만 한다. PUT이나 DELETE 요청은 서버 데이터에 직접 영향을 주기 때문에 `Preflight` 요청이란 걸 먼저 보내서 요청이 안전한 지 확인하고, 그 후에 본격적으로 요청을 보낼 수 있다. Simple requests가 아닌 cross-origin요청은 모두 preflight 요청을 하게 되는데, 실제 요청을 보내는 것이 안전한지 확인하기 위해 먼저 OPTIONS 메서드를 사용하여 cross-origin HTTP 요청을 보냅니다. 이렇게 하는 이유는 사용자 데이터에 영향을 미칠 수 있는 요청이므로 사전에 확인 후 본 요청을 보냅니다.

- 요청 헤더 목록

```
Origin
Access-Control-Request-Method: preflight요청 시 실제 요청에서 어떤 method를 사용할 것인지 서버에게 알리기 위해 사용됩니다.
Access-Control-Request-Headers: preflight요청 시 실제 요청에서 어떤 header를 사용할 것인지 서버에게 알리기 위해 사용됩니다.
```

- 응답 헤더 목록

```
Access-Control-Allow-Origin: 브라우저가 해당 origin이 자원에 접근할 수 있도록 허용합니다. 혹은 와일드 카드 (*)는 credentials이 없는 요청에 한해서 모든 origin에서 접근이 가능하도록 허용합니다.
Access-Control-Expose-Headers:  브라우저가 액세스할 수 있는 서버 화이트리스트 헤더를 허용합니다.
Access-Control-Max-Age: 얼마나 오랫동안 preflight요청이 캐싱 될 수 있는지를 나타낸다.
Access-Control-Allow-Credentials:
- Credentials가 true 일 때 요청에 대한 응답이 노출될 수 있는지를 나타냅니다.
- preflight요청에 대한 응답의 일부로 사용되는 경우 실제 자격 증명을 사용하여 실제 요청을 수행할 수 있는지를 나타냅니다.
- 간단한 GET 요청은 preflight되지 않으므로 자격 증명이 있는 리소스를 요청하면 헤더가 리소스와 함께 반환되지 않으면 브라우저에서 응답을 무시하고 웹 콘텐츠로 반환하지 않습니다.
Access-Control-Allow-Methods: preflight요청에 대한 응답으로 허용되는 메서드들을 나타냅니다.
Access-Control-Allow-Headers: preflight요청에 대한 응답으로 실제 요청 시 사용할 수 있는 HTTP 헤더를 나타냅니다.
```

⭐ 요약:

1. CORS (Cross-Origin Resource Sharing)가 무엇인가?

**CORS는 다른 출처간에 resource를 공유할 수 있도록, web browser내에서 다른 URI사이에 데이터를 주고 받는 것을 합법적으로 허용하는 것을 의미한다.**
즉, 서로 다른 Origin간에 자원을 공유하는 것을 가능하게 해주며 기본적으로 차단되어있습니다.

2. SOP (Same-Origin Policy)가 무엇인가?

**Web browser의 동일 출처 정책,으로 동일한 URI사이에서만 API등의 data 접근이 가능하도록, 다른 URI의 data접근을 막는 것을 의미한다.** Web browser는 default값으로 SOP를 유지한다.

### 8. Express.js에서 CORS 사용하기

Installation is done using the npm install command:

> $ `npm i express cors`

- Simple Usage in Express.js (Enable All CORS Requests)

```
var express = require('express')
var cors = require('cors')
var app = express()

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors())

app.get('/products/:id', (req, res, next) => {
  res.json({msg: 'This is CORS-enabled for all origins!'})
})

app.listen(80, function () {
  console.log('CORS-enabled web server listening on port 80')
})
```

- Configuring CORS

```
var express = require('express')
var cors = require('cors')
var app = express()

var corsOptions = {
  origin: 'http://example.com',
  optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}

app.get('/products/:id', cors(corsOptions), function (req, res, next) {
  res.json({msg: 'This is CORS-enabled for only example.com.'})
})

app.listen(80, function () {
  console.log('CORS-enabled web server listening on port 80')
})
```

자세한 사용법은 구글에 express cors 검색 후 공식문서를 확인한다.

### 9. AJAX 이해하기

`Ajax` is a set of web development techniques that uses various web technologies on the client-side to create **asynchronous web applications**. With Ajax, web applications can send and retrieve data from a server asynchronously without interfering with the display and behaviour of the existing page. Ajax는 Asynchronous JavaScript And XML의 약자로 서버와 비동기적으로 데이터를 주고받는 자바스크립트 기술을 의미한다. Ajax를 사용하면 새로고침없이 서버에게 GET요청을 할 수 있다.

- 장점: 새로고침이 없기 때문에, 페이지들간에 부드러운 이동이 가능하다.

Ajax는 서버랑 비동기적으로 통신할 때 사용하는 기술이므로 Ajax를 이해하기 위해서는 서버에 대한 이해가 먼저 필요하다. 서버는 유저가 데이터를 요구하면 데이터를 보내주는 프로그램이다.

웹서버에게 데이터를 요구하는 방법:

1. 원하는 데이터의 URL (서버개발자가 만든 API를 통해 얻을 수 있다.)
2. 그 URL로 GET request 보내기

#### 데이터 URL에 GET request 보내기

원하는 데이터의 URL에 GET request를 보내는 데에는 여러가지 방법이 있다:

1. Browser에 URL를 입력

2. HTML `form` tag로 GET요청

`form` tag내의 `button`을 누르면, action의 URL로 GET요청이 실행된다.

- `index.html` file

```
<form action="example.com" method="GET">
  <button type="submit">GET request</button>
</form>
```

위의 방법들로 GET요청을 보내면, browser가 새로고침된다. 새로고침되는 게 싫다면 AJAX로 GET요청을 보내면 된다.

#### Ajax로 GET요청 보내기

Ajax로 GET요청을 보내는 방법:

1. javascript의 built-in 함수인 `fetch()` function 사용: native JavaScript

최신 javascript는 `fetch()`를 사용하여 Ajax로 GET요청을 보낸다.

`https://example.github.io/price.json` URL에 GET요청 보내기

```
// Promise ver
const 함수 = fetch("https://example.github.io/price.json")
  .then((res) => {
    if (!res) {
      throw new Error("Data not found");
    }
    return res.json();
  })
  .then((result) => {
    console.log(result);
  })
  .catch((err) => {
    console.log(err.message);
  });

// Async/Await ver
const 함수 = async () => {
  try {
    const res = await fetch("https://example.github.io/price.json");
    if (!res) {
      throw new Error("Data not found");
    }
    const result = await res.json();
    console.log(result);
  } catch (error) {
    console.log(err.message);
  }
};
```

위에서 보다 싶이, native javascript만 사용하면 데이터 하나를 가져오는 데 많은 코드를 작성해야 한다.

2. 외부 library 사용: `Axios`의 `axios.get()`, `Jquery`의 `$.ajax()`

- React나 Vue 개발환경에서는 자주 `Axios` library를 설치해서 사용한다.
- Axios 환경설정: npm으로 Axios 설치 or CDN 추가

> `npm i axios`

또는, HTML에 다음 script tag 추가

`<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.25.0/axios.min.js" integrity="sha512-/Q6t3CASm04EliI1QyIDAA/nDo9R8FQ/BULoUFyN4n/BDdyIxeH7u++Z+eobdmr11gG5D/6nPFyDlnisDwhpYA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>`

- Axios 사용법

```
const axios = require('axios');

// Promise ver
const 함수 = axios
  .get("https://example.github.io/price.json")
  .then((result) => {
    console.log(result.data);
  })
  .catch((err) => {
    console.log(err.message);
  });

// Async/Await ver
const 함수 = async () => {
  try {
    const result = await axios.get("https://example.github.io/price.json");
    const data = await result.data();
    console.log(data);
  } catch (error) {
    console.log(err.message);
  }
};

// axios API
// Send a POST request
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
});

// GET request for remote image in node.js
axios({
  method: 'get', // default
  url: 'http://bit.ly/2mTM3nY',
  responseType: 'stream',
  headers: {
	  'Access-Control-Allow-Origin': '*',
	},
})
  .then(function (response) {
    response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
  });
```

Axios는 우리가 Postman에서 서버에 http request를 보내는 것과 동일한 일을 수행한다.

Axios로 GET요청시 CORS관련 에러를 자주 보게 된다. 이는 browser에서 보안때문에 내 주소와 다른 주소로는 ajax 요청이 불가능해 생기는 에러이다. 이럴 경우 다음의 코드를 추가한다.

```
headers: {
	  'Access-Control-Allow-Origin': '*',
},

또는

CORS 정책 관련 기능을 끈다.

//  Express.js의 경우
const cors = require('cors');
app.use(cors());
```


## 2. [ExpressJs](https://expressjs.com/)

### What is Express.js?

Express.js는 Javascript Back-end Framework로, Web Server을 만들 때 사용한다.

## 3. [FlaskPy](https://flask.palletsprojects.com) (Python)

### What is Flask?

`Flask` is a micro web framework written in Python. Flask는 Python으로 구동되는 Web Framework로, 간단하게 기능을 설명하면 내가 만든 program에 web server를 구동시켜주는 편한 코드 모음이라고 할 수 있다. 다른 python으로 작성된 web framework인 `Django` 보다 코드가 가볍기때문에 간단한 API서버 구축에 적합하다. By default, Flask runs on port 5000 in development mode.

### Setup flask Project

Install Flask module

> $ `pip install Flask`

Create flask application working directory

> $ `mkdir flaskapp`

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
Web context를 전부 모은 directory를 `Web Application Server`라고 부른다.

위의 tree 구조에서:
  - Web Application Server = `flaskWeb`
  - Web context = `newFlaskApp`, `flaskapp`
  - `templates` folder는 HTML files을 모아두는 곳이다.
  - `static` folder는 정적이라는 의미로 서비스를 운영하는 데 변하지 않는 것
    - server에 요청하면 연산이 없이 바로 나가는 것들, images, css, js등이 해당된다.

여기서 중요한 점은 `flask`를 사용할 때 `"templates"`, `"static"`이라는 폴더명을 변경해선 안된다. `flask`는 framework이기 때문에 `flask`가 요구하는 틀을 따라야지만 제대로 작동한다.

## 4. [Postgresql](https://www.postgresql.org/docs/)

Postgresql는 relational database의 대표주자이다.

## 5. [Mongodb](https://www.mongodb.com/)

### What is Mongodb

MongoDB is a source-available cross-platform document-oriented database program. MongoDB is Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. NoSQL은 Not Only SQL, SQL 뿐만 아니다라는 의미를 지니고있다. 즉, SQL을 사용하는 관계형 데이터베이스가 아닌 데이터베이스를 의미한다. 대표적인 관계형 데이터베이스로는 MySQL, Oracle, PostgreSQL이 있고, NoSQL 진영에는 이 포스트에서 다루는 MongoDB와 Redis, HBase 등이 있다.

### Collections이 무엇인지

If you aren't failiar with nosql, think `Collectoins` as `Table of row and column` in sql.
In nosql, you have collection of Document.

Document is just json object.

### Mongodb 개발환경

We need a MongoDB URL to be able to connect to.

- Go to Mongodb website (Mongodb Atlas) and create database
- Mongodb Atlas: cloud baesd
- Mongodb compass: local computer based
- MongoDB URL (MongoDB Atlas): https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=1217adtest_pmcopy_control&utm_source=google&utm_campaign=gs_americas_united_states_search_core_brand_atlas_desktop&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624338&adgroup=115749704063&gclid=Cj0KCQiAxc6PBhCEARIsAH8Hff0GkAMWkv-SOoaFSdMgxQaEshcIGIyDHAaSqp-B-yPgW03BbW9DxxQaAhi8EALw_wcB

```
Create Project => Create Database => Cluster Tier: M0 Sandbox (Free) => Cloud Provider: AWS
Set User name & User password => Network access IP Address => Connect => "Connet your application" => DRIVER: Node.js => Get mongoDBURI
```

"Connect using MongoDB Compass" => Get mongoDBURI => 이 mongodbURI을 mongo compass에 복사하면, 로컬 컴퓨터에서 mongodb를 이용할 수 있다.

"Connet your application" => DRIVER: Node.js => Get mongoDBURI => 이 mongodbURI을 code에 복사하면, project에서 mongodb를 이용할 수 있다.

- add `MONGO_URI` to `.env` file

`MONGO_URI = mongodb+srv://Shin:<password>@cluster0.sjhvl.mongodb.net/<myfirstDatabase>?retryWrites=true&w=majority`

## 6. [RocketRs](https://rocket.rs/) (Rust)

Rocket is a web framework for Rust that makes it simple to write fast, secure web applications without sacrificing flexibility, usability, or type safety.

Rocket은 Rust 프로그래밍언어로 작성된 서버 사이드 웹 framework이다. Rust는 C,C++과 같은 low-level programming language로 사람보다는 기계에 가깝게 코딩을 한다.

![low-high](img/lowhigh.png)

Rust와 C, C++는 Javascript, python과는 다르게 memory를 관리해주는 garbage collector (GC)가 없기 때문에, 변수를 선언할 때 memory에 변수를 저장할 공간을 직접 요청하고, 더이상 이용하지 않는 변수는 memory에서 free해주어야 한다. GC가 없기 때문에 아주 빠르고, 안전하다.

Rust의 compiler `rustc`는 기계가 읽을 수 있는 a binary code를 생성하고, 코드의 문제를 발견 시 compiler error를 발생시켜 코드의 어디가 왜 문제이고 어떻게 작성해야 하는지 까지 알려준다. 이는 Rust로 code를 작성하는 큰 이유 중 하나이다.

예시: `hello.rs` file

```
// This is a comment, and is ignored by the compiler
// You can test this code by clicking the "Run" button over there ->
// or if you prefer to use your keyboard, you can use the "Ctrl + Enter" shortcut

// This code is editable, feel free to hack it!
// You can always return to the original code by clicking the "Reset" button ->

// This is the main function
fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    println!("Hello World!");
}
```

- A binary can be generated using the Rust compiler: `rustc`.
- `println!` is a macro that prints text to the console.

> `$ rustc hello.rs`

`rustc` will produce a hello binary that can be executed.

```
$ ./hello
Hello World!
```

## % 부록2: Amazon사의 cloud service인 AWS (Amazon Web Service) 사용하기 %

1. AWS IAM - User를 생성하고, create access key를 사용하여, API에 접근하기

2. AWS S3 - bucket을 만들어 파일 저장하기

3. AWS SES (Simple Email Service) - email 보내기

4. AWS EC2 가상환경 - virtualBox와 같이 가상 환경을 제공

5. AWS Lambda - 함수

6. AWS Elastic Beanstalk - 간단히 코드를 배포할 때 사용

## % 부록3: Docker 이해하기 %

local computer에 다운되어 있는 environment와 server computer에 다운되어 있는 environment가 다르면, local에서 작성된 code는 server에서 호환성 문제로 작동이 안될 수도 있다. 이 문제를 해결하기 위해 container라는 개념이 등장하였고, Docker가 container를 제공하는 가장 큰 platform이다.

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
