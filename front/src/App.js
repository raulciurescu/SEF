import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./HomePage";
import ManagerRegister from "./ManagerRegister";
import StaffLogin from "./StaffLogin";
import StaffRegister from "./StaffRegister";
import ManagerLogin from "./ManagerLogin";
import DashBoard from "./Dashboard";
import "./App.css";


function App() {
  return (
    <div className="App">
      <Routes >
        <Route exact path="/" element={<HomePage />} />
        <Route path="/ManagerRegister" element={<ManagerRegister />} />
        <Route path="/StaffLogin" element={<StaffLogin />} />
        <Route path= "/ManagerLogin" element={<ManagerLogin />} />
      </Routes>
    </div>
  );
}

export default App;