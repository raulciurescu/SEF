import React, { useEffect, useRef, useState } from "react";
import axios from "./api/axios";

const Reservation = () => {
    const nameRef = useRef();
    const phoneRef = useRef();
    const dateRef = useRef();
    const timeRef = useRef();

    const [name, setName] = useState("");
    const [phone, setPhone] = useState("");
    const [date, setDate] = useState("");
    const [time, setTime] = useState("");
    const [success, setSuccess] = useState(false);
    const [errMsg, setErrMsg] = useState("");
    
    useEffect(() => {   
        nameRef.current && nameRef.current.focus();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [name, phone, date, time]);

    

    const handleReservation = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post(
                "/ClientReservation",
                {
                    name: name,
                    phone: phone,
                    date: date,
                    time: time,
                    status: "Pending"
                }
            );
            setSuccess(true);
            console.log(response.data.message);
            setName("");
            setPhone("");
            setDate("");
            setTime("");
        } catch (err) {
            if (err.response) {
                setErrMsg("Reservation failed. Please try again.");
            }
            if (name === "") {
                nameRef.current && nameRef.current.focus();
            } else if (phone === "") {
                phoneRef.current && phoneRef.current.focus();
            } else if (date === "") {
                dateRef.current && dateRef.current.focus();
            } else if (time === "") {
                timeRef.current && timeRef.current.focus();
            }
        }
    };

    return (
        <div>
            <h1 className="header">Restaurant's Management</h1>
            <div className="title"></div>
            <h2 className="title">Reservation Form</h2>
            <form onSubmit={handleReservation} className="content">
                <div>
                    <label>Name:</label>
                    <input type="text" ref={nameRef} value={name} onChange={(event) => setName(event.target.value)} required />
                </div>
                <br/>
                <div>
                    <label>Phone:</label>
                    <input type="text" ref={phoneRef} value={phone} onChange={(event) => setPhone(event.target.value)} required />
                </div>
                <br/>
                <div>
                    <label>Date:</label>
                    <input type="text" ref={dateRef} value={date} onChange={(event) => setDate(event.target.value)} required />
                </div>
                <br/>
                <div>
                    <label>Time:</label>
                    <input type="text" ref={timeRef} value={time} onChange={(event) => setTime(event.target.value)} required />
                </div>  
                <br/>
                <button className="checkout-btn" type="submit" >Make Reservation</button>
                {errMsg && <p className="errmsg">{errMsg}</p>}
                {success && <h1>See you!</h1>}
            </form>
        </div>
    );
};

export default Reservation;