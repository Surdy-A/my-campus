import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {Route, Switch, HashRouter} from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import indexRoutes from './routes/index';
ReactDOM.render(

  
  <HashRouter>
    <Switch>
      {indexRoutes.map((prop, key) => {
        return <Route path={prop.path} key={key} component={prop.component} />
      })}
    </Switch>
  </HashRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
