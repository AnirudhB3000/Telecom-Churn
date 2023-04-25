import React,{Component} from "react";
import {NavLink,Link} from 'react-router-dom';
import {Navbar,Nav} from 'react-bootstrap';
import BuggyCounter from './BuggyCounter';
import MyErrorBoundary from './MyErrorBoundary';

export class Navigation extends Component{
    render(){
        return(
           <Navbar bg="dark" expand="lg">
            <Navbar.Toggle aria-controls="basic-navbar-nav"/>
            <Navbar.Collapse id="basic-navbar-nav">
                <nav>
                    <NavLink className="d-incline p-2 bg-dark text white" to="/">
                        Home
                    </NavLink>
                    <NavLink className="d-incline p-2 bg-dark text-white" to="/churn">
                        Churn 
                    </NavLink>
                    <NavLink className="d-incline p-2 bg-dark text-white" to="/reviews">
                        Review
                    </NavLink>
                </nav>
            </Navbar.Collapse>
           
           </Navbar>
           
        )
    }
}