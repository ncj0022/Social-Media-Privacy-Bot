import React from 'react';
import ReactDOM from 'react-dom';
import "bootstrap/dist/css/bootstrap.min.css";

import TweetBotNav from './components/tweetBotNav.component';
import InteractiveGame from './components/interactive-tweet.component';


ReactDOM.render(
  <React.StrictMode>
    <InteractiveGame />
  </React.StrictMode>,
  document.getElementById('interactiveTweet')
);
/*
ReactDOM.render(
  <React.StrictMode>
    <GetByProfile />
  </React.StrictMode>,
  document.getElementById('getByProfile')
);
*/
ReactDOM.render(
  <React.StrictMode>
    <TweetBotNav /> 
  </React.StrictMode>,
  document.getElementById('navbar')
);// put this back later on

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
