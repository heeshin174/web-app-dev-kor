# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## React JS

React is a free and open-source front-end JavaScript library for building user interfaces based on UI components.
It is maintained by Meta and a community of individual developers and companies.
React can be used as a base in the development of single-page or mobile applications (SPA).
SPA는 어떤 부분의 데이터가 바뀔때마다 안바뀌는 부분까지 모든 데이터를 가져오는 기존에 사이트들의 문제점을 보안하기 위해 나온 것으로
새로고침없이 바뀌는 부분만 데이터를 로딩한다.

## 📚 Materials/References:

⭐ Youtube Lecture Link -https://www.youtube.com/watch?v=GDa8kZLNhJ4
⭐ Rapid Application Programming Interface (API) - https://rapidapi.com/
⭐ Travel Advisor API - https://rapidapi.com/apidojo/api/travel-advisor?utm_source=youtube.com%2FJavaScriptMastery&utm_medium=DevRel&utm_campaign=DevRel
⭐ Open Weather Map API - https://rapidapi.com/community/api/open-weather-map?utm_source=youtube.com%2FJavaScriptMastery&utm_medium=DevRel&utm_campaign=DevRel
⭐ GitHub Code - https://github.com/adrianhajdin/project_travel_advisor
Styles & Other Code: https://gist.github.com/adrianhajdin/ede527249054b7abbdf4e3a9fac95b5e
If you get: "This page can't load Google Maps correctly." and "For development purposes only." that means that you have to enter your billing details. Google requires that to verify your identity and distinguish actual people from robots. You'll be getting free $200 worth of API requests indefinitely, and you will NOT be charged.
Google Cloud (Maps JavaScript API) in API library - https://console.cloud.google.com/
⭐ Matrerial Ui - https://mui.com/getting-started/installation/

## Matrerial Ui

Material-UI is simply a library that allows us to import and use different components to create a user interface in our React applications. This saves a significant amount of time since the developers do not need to write everything from scratch.

Material-Ui에서는 자주 사용되는 기능/디자인들을 Component/API로 제공해 줘서, React로 개발을 할 때 다양한 UI를 쉽게 만들 수 있다. 기능적인 UI를 제공해 주면서도 내 프로젝트에 맞게 커스터마이징할 수 있다는 게 굉장히 매력적이다.

`import { CssBaseline } from '@material-ui/core';` normalize the style
`import { AppBar, Toolbar, Typography, InputBase, Box } from "@material-ui/core";`
Typography - Every single text element (p tag)
Box - div tag

## ES7+ React/Redux/React-Native snippets in VSCode extension

extends `ES7+ React/Redux/React-Native snippets` in VSCode and type `rafce` to use arrow function.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### install all the dependencies thouugh out the process of building our application

1. install `node.js`
2. > npx create-react-app
3. > npm install @material-ui/core @material-ui/icons @material-ui/lab @react-google-maps/api axios google-map-react
