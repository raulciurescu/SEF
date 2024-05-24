import React, { useRef, useState, useEffect } from "react";
import axios from "./api/axios";
import { Link } from "react-router-dom";

const ManagerHome = () => {

    return (
            <>
                {(
                    <section>
                    <h1 className="header">Restaurant's Management</h1>
                        <div className="title">
                            <h2>Manager Home</h2>
                            <br />
                            <br />
                            <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/Menu"}>
                                Menu  
                            </button> 
                            <br/>
                            <br/>
                            <button className="checkout-btn" type="submit" onClick={() => window.location.href = "/Staff"}>
                                Staff
                            </button>
                        </div>
                </section>
                    )}
            </>
    )
}

export default ManagerHome;