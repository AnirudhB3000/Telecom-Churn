import React from "react";
import { Churn } from "../Churn";
import { Routes, Route } from "react-router";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-custom" style={{ backgroundColor: '#192236'}}>
    <a className="navbar-brand" href="../" style={{ color: '#ADEFD1FF' }}>
    <img src="/logo4.png" width="30" height="30" alt="Logo" style={{marginRight: '4px', marginLeft: '4px'}}/>
      Telecom Churn
    </a>
    <button
      className="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNavDropdown"
      aria-controls="navbarNavDropdown"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span className="navbar-toggler-icon"></span>
    </button>

    <div className="collapse navbar-collapse" id="navbarNavDropdown">
      <ul className="navbar-nav">
        {}
        <li className="nav-item">
          <Link className="nav-link" to="/churn" style={{ color: '#E3B448' }}>
            Churn
          </Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link" to="/review" style={{ color: '#E3B448' }}>
            Review
          </Link>
        </li>
        {}
      </ul>
    </div>
  </nav>)
}
export default Navbar