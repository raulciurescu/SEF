import React, { useState, useEffect } from "react";
import axios from "./api/axios";
import './App.css'; 


const Client = () => {
  return (
    <section>
      <h1 className="header">Restaurant's Management</h1>
      <br />
      <div className="title">
        <h2>Client</h2>
        <br />
        <div>
          <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/PlaceOrder" }>Place Oder</button>
          <br/>
          <br/>
          <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/ClientReservation" }>Make Reservation</button>
        </div>
      </div>
    </section>
  );
};

export default Client;
