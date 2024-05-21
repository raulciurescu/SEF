import React, { useEffect } from "react";
import { BrowserRouter as Router, Link } from "react-router-dom";

function HomePage() {
  return (
    <div>
      <h1 className="header">Restaurant's Management</h1>
      <div className="content">
        <br/>
        <h2>Manager</h2>
        <div>
          <Link to="/ManagerRegister">
            <button className="button">Sign in</button>
          </Link>
        </div>
        <br />
        <h3 className="text">~or~</h3>
        <h2>Staff</h2>
        <div>
          <Link to="/StaffLogin">
            <button className="button">Sign in</button>
          </Link>
        </div>
        <br />
      </div>
    </div>
  );
}

export default HomePage;