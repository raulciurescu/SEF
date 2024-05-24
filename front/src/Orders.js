import React, { useRef, useState, useEffect } from "react";
import axios from "./api/axios";
import { Link } from "react-router-dom";

const ORDERS_URL = "/Orders";   

const Orders = () => {
    const StaffIDRef = useRef();
    const OrderIDRef = useRef();
    const OrderProductsRef = useRef();
    const OrderStatusRef = useRef();
    const OrderPriceRef = useRef();

    const [StaffID, setStaffID] = useState("");
    const [OrderID, setOrderID] = useState("");
    const [OrderProducts, setOrderProducts] = useState("");
    const [OrderStatus, setOrderStatus] = useState("");
    const [OrderPrice, setOrderPrice] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [success, setSuccess] = useState(false);
    const [ordersItems, setOrdersItems] = useState([]);
    const [MyOrders, setMyOrders] = useState([]);   

    useEffect(() => {
        StaffIDRef.current && StaffIDRef.current.focus();
        handleDisplay();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [StaffID, OrderID, OrderProducts, OrderStatus, OrderPrice]);

    const handleDisplay = async () => {
        try {
            const response = await axios.get(ORDERS_URL);
            setOrdersItems(response.data);
        } catch (err) {
            console.log(err);
        }
    };  

    const handleTakeOrder = async (order) => {
        const StaffID = localStorage.getItem("StaffID"); // Retrieve StaffID from local storage
        if (!StaffID) {
            console.log("StaffID not found in local storage");
            return;
        }

        try {
            await axios.put(`/Orders/${order.OrderID}`, { OrderStatus: "In Progress", StaffID: StaffID });

            setOrdersItems(prevOrders => prevOrders.filter(item => item.OrderID !== order.OrderID));
            setMyOrders(prevMyOrders => [...prevMyOrders, { ...order, OrderStatus: "In Progress", StaffID: StaffID }]);
        } catch (err) {
            console.log(err);
        }
    };

    return (
            <section>
                <h1 className="header">Restaurant's Management</h1>
                <div className="title">
                <h2>All Orders</h2>
                <br /> 
                <br />
                <table className = "table">
                    <thead>
                        <tr>
                            <th>StaffID</th>
                            <th>OrderID</th>
                            <th>OrderProducts</th>
                            <th>OrderStatus</th>
                            <th>OrderPrice</th>
                        </tr>
                    </thead>
                    <tbody>
                        {ordersItems.map((item, index) => (
                            <tr key={item.OrderID}>
                                <td>{item.StaffID}</td>
                                <td>{item.OrderID}</td>
                                <td>{item.OrderProducts}</td>
                                <td>{item.OrderStatus}</td>
                                <td>{item.OrderPrice}</td>
                                <td>
                                     <button className="checkout-btn" onClick={() => handleTakeOrder(item)}>Take</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>

                <h2>My Orders</h2>
                <br />
                <br />
                <table className="table">
                    <thead>
                        <tr>
                            <th>StaffID</th>
                            <th>OrderID</th>
                            <th>OrderProducts</th>
                            <th>OrderStatus</th>
                            <th>OrderPrice</th>
                        </tr>
                    </thead>
                    <tbody>
                        {MyOrders.map((item) => (
                            <tr key={item.OrderID}>
                                <td>{item.StaffID}</td>
                                <td>{item.OrderID}</td>
                                <td>{item.OrderProducts}</td>
                                <td>{item.OrderStatus}</td>
                                <td>{item.OrderPrice}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>

            </div>
        </section>
    )
}

export default Orders;