import React, { useState, useEffect } from "react";
import axios from "./api/axios";
import { useLocation, useNavigate } from 'react-router-dom';
import './PlaceOrderStyle.css';

/**
 * Renders the Place Order component.
 * 
 * @returns {JSX.Element} The rendered Place Order component.
 */
const PlaceOrder = () => {
  const [menuItems, setMenuItems] = useState([]);
  const [myOrder, setMyOrder] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);
  const navigate = useNavigate();
  const location = useLocation();
  const { selectedItems, initialTotalPrice } = location.state || { selectedItems: [], initialTotalPrice: 0 };

  useEffect(() => {
    fetchMenu();
  }, []);
  

  const fetchMenu = async () => {
    try {
      const response = await axios.get("/Menu");
      setMenuItems(response.data.map(item => ({ ...item, quantity: 0 }))); // Default quantity 0
    } catch (error) {
      console.error("Error fetching menu:", error);
    }
  };

  const handleAdd = (item) => {
    // Check if the item already exists in myOrder
    const existingItemIndex = myOrder.findIndex(orderItem => orderItem._id === item._id);
  
    if (existingItemIndex !== -1) {
      // If the item exists, update its quantity
      const updatedOrder = [...myOrder];
      updatedOrder[existingItemIndex] = {
        ...updatedOrder[existingItemIndex],
        quantity: updatedOrder[existingItemIndex].quantity + 1
      };
      setMyOrder(updatedOrder);
      setTotalPrice(totalPrice + parseFloat(item.Price));
    } else {
      // If the item doesn't exist, add it to myOrder with quantity 1
      const updatedOrder = [...myOrder, { ...item, quantity: 1 }];
      setMyOrder(updatedOrder);
      setTotalPrice(totalPrice + parseFloat(item.Price));
    }

    const updatedMenuItems = menuItems.map(menuItem => {
        if (menuItem._id === item._id) {
          return { ...menuItem, quantity: menuItem.quantity + 1 };
        }
        return menuItem;
      });
      setMenuItems(updatedMenuItems);
  };
  

  const handleDecrease = (item) => {
    const existingItem = myOrder.find(orderItem => orderItem._id === item._id);
    console.log(existingItem);
    if (existingItem) {
      if (existingItem.quantity > 1) {
        setMyOrder(myOrder.map(orderItem => 
          orderItem._id === item._id ? { ...orderItem, quantity: orderItem.quantity - 1 } : orderItem
        ));
        setTotalPrice(totalPrice - parseFloat(item.Price));
      } else {
        setMyOrder(myOrder.filter(orderItem => orderItem._id !== item._id));
        setTotalPrice(totalPrice - parseFloat(item.Price));
      }
    }

    const updatedMenuItems = menuItems.map(menuItem => {
        if (menuItem._id === item._id && menuItem.quantity > 0) {
          return { ...menuItem, quantity: menuItem.quantity - 1 };
        }
        return menuItem;
      });
      setMenuItems(updatedMenuItems);
  };

  const orderId = "OrderID";

  function generateRandomString(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
  }
  
  const randomOrderID = generateRandomString(8);

  const handleConfirmOrder = async () => {
    try {
      const orderProducts = myOrder.map(item => item.ProductName);
      
      
      const orderData = {
        StaffID: "",
        OrderID: randomOrderID, 
        OrederProducts: orderProducts.join(", "), 
        OrderStatus: "Placed",
        OrderPrice: totalPrice.toFixed(2),
      };
  
      
      await axios.post("/table_Orders", orderData);  
  
      
      navigate('/Final', { state: { orderStatus: "Placed" } });
  
      setMyOrder([]);
      setTotalPrice(0);
    } catch (error) {
      console.error("Error confirming order:", error);
      alert("Failed to confirm order. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Place Order</h2>
      <div className="menu-container">
        {menuItems.map((item) => (
            <div key={item._id} className="menu-item">
                <div>
                    <h3>{item.Category}</h3>
                    <p>{item.ProductName}</p>
                    <p>{item.Description}</p>
                    <p>Price: {item.Price}</p>
                </div>
                <div className="item-quantity">
                    <button onClick={() => handleDecrease(item)}>&lt;</button>
                    <input type="text" value={item.quantity} readOnly />
                    <button onClick={() => handleAdd(item)}>&gt;</button>
                    <button onClick={() => handleAdd(item)}>Add</button>
                </div>
            </div>
        ))}
      </div>
      <div className="order-container">
        <h2>My Order</h2>
        {myOrder.length === 0 ? (
          <p className="empty-order">Your order is empty</p>
        ) : (
          <ul>
            {myOrder.map((item) => (
              <li key={item._id} className="order-item">
                <span>{item.ProductName} - ${item.Price} x {item.quantity}</span>
              </li>
            ))}
          </ul>
        )}
        <p className="total-price">Total Price: ${totalPrice.toFixed(2)}</p>
        <button className="confirm-button" onClick={handleConfirmOrder}>Confirm Order</button> 
      </div>
    </div>
  );
};

export default PlaceOrder;