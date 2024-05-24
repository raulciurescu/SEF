import React, { useRef, useState, useEffect } from "react";
import axios from "./api/axios";
import { Link } from "react-router-dom";

const StaffHome = () => {

    return (
            <>
                {(
                    <section>
                    <h1 className="header">Restaurant's Management</h1>
                        <div className="title">
                            <h2>Staff Home</h2>
                            <br />
                            <br />
                            <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/Orders"}>
                                Orders  
                            </button> 
                            <br/>
                            <br/>
                            <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/Reservations"}>
                                Reservations
                            </button>
                        </div>
                </section>
                    )}
            </>
    )
}

export default StaffHome;