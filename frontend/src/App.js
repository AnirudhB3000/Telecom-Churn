// import './App.css';
// import 'bootstrap/dist/css/bootstrap.min.css';
// import {Home} from './Home';
// import {Churn} from './Churn';
// import {Navigation} from './Navigation';
// import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';
// import BuggyCounter from './BuggyCounter';
// import MyErrorBoundary from './MyErrorBoundary';
// import { Switch } from "react-router";

// function App() {
//   return (
//     <Route>
//     <div className="container">
//      <h3 className="m-3 d-flex justify-content-center">
//        React JS Tutorial
//      </h3>

//      <Navigation/>

//      <Switch>
//        <Route path='/' component={Home} exact/>
//        <Route path='/churn' component={Churn}/>
//        {/* <Route path='/employee' component={Employee}/> */}
//      </Switch>
//     </div>
//     </Route>
//   );
// }

// export default App;

import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Home} from './Home';
import Churn from './Churn';
import Review from './Review';
import {Navigation} from './Navigation';
import {BrowserRouter as Router,  Link, Routes, Route} from 'react-router-dom';
import BuggyCounter from './BuggyCounter';
import MyErrorBoundary from './MyErrorBoundary';
import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from "./Navigation/Navbar.js";
function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/churn" element={<Churn />} />
        <Route path="/review" element={<Review />} />
      </Routes>
    </Router>
  );
}
export default App;