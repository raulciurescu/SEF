import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./Login";
import ManagerHome from "./ManagerHome";
import StaffHome from "./StaffHome";
import Staff from "./Staff";
import Menu from "./Menu";
import Client from "./Client";
import PlaceOrder from "./PlaceOrder";
import ClientReservation from "./ClientReservation";
import Reservations from "./Reservations"
import Orders from "./Orders";
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
        <Route path = "/Client" element={<Client/>} />
        <Route path = "/PlaceOrder" element={<PlaceOrder/>} />
        <Route path = "/ClientReservation" element={<ClientReservation/>} />
        <Route path = "/Reservations" element={<Reservations/>} />
        <Route path = "/Orders" element={<Orders/>} />
      </Routes>
    </div>
  );
}

export default App;