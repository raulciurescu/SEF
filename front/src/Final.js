import React from "react";
import { useLocation } from 'react-router-dom';
import './App.css';

const Final = () => {
  const location = useLocation();
  const { orderStatus } = location.state || { orderStatus: "unknown" };

  return (
    <div className="final-container">
      <h1 className="header">Restaurant's Management</h1>
      <h2 className= "title">Thank you for your order!</h2>
      <div className= "content">
        <p>Enjoy your meal</p>
        <p>And</p>
        <p>Have a nice day!</p>
        <p>Your order is: {orderStatus}</p>
      </div>
    </div>
  );
};

export default Final;