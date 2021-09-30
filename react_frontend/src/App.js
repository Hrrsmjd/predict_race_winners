import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import './App.css';
import Navbar from './apps/Navbar';
import Notebook from './apps/Notebook';
import HowTo from './apps/HowTo';
import Predict from './apps/Predict';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Switch>
          <Route path='/' exact component={Notebook}></Route>
          <Route path='/howto' component={HowTo}></Route>
          <Route path='/predict' component={Predict}></Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
