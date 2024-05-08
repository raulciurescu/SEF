import React from "react";
import { BrowserRouter as Router, Link } from "react-router-dom";

function Dashboard() {
  return (
    <div>
      <h1 className="header">Restaurant's Management</h1>
      <div className="content">
        <br/>
        <h2>Add Employee</h2>
        <div>
          <Link to="/AddStaff">
            <button className="button">Add employee</button>
          </Link>
        </div>
        <br />
        <h3 className="text">~or~</h3>
        <h2>Add new dish to menu</h2>
        <div>
          <Link to="/StaffLogin">
            <button className="button">Add dish</button>
          </Link>
        </div>
        <br />
      </div>
    </div>
  );
}

export default Dashboard;