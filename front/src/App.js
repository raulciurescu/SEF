import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./HomePage";
import Login from "./Login";
import StaffLogin from "./StaffLogin";
import StaffRegister from "./StaffRegister";
import ManagerLogin from "./ManagerLogin";
import DashBoard from "./Dashboard";
import "./App.css";


function App() {
  return (
    <div className="App">
      <Routes>
        <>
        <Route exact path="/" element={<Login />} />
        <Route path="/Dashboard" element={<DashBoard />} />
        {/* <Route path="/StaffLogin" element={<StaffLogin />} />
        <Route path="/ManagerLogin" element={<ManagerLogin />} />
        <Route path="/StaffRegister" element={<StaffRegister />} /> */}
        </> 
      </Routes>
    </div>
  );
}

export default App;