import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";
import ManagerHome from "./ManagerHome";
import StaffHome from "./StaffHome";
import Staff from "./Staff";
import Menu from "./Menu";
import MyOrders from "./MyOrders";
import AllOrders from "./AllOrders";
import "./App.css";


function App() {
  return (
    <div className="App">
      <Routes >
        <Route exact path="/" element={<Login/>} />
        <Route path = "/ManagerHome" element={<ManagerHome/>} />
        <Route path = "/StaffHome" element={<StaffHome/>} />
        <Route path = "/Staff" element={<Staff/>} />
        <Route path = "/Menu" element={<Menu/>} />
        <Route path = "/MyOrders" element={<MyOrders/>} />
        <Route path = "/AllOrders" element={<AllOrders/>} />
      </Routes>
    </div>
  );
}

export default App;