import React, { useRef, useState, useEffect } from "react";
import axios from "./api/axios";
import { Link } from "react-router-dom";

const STAFF_URL = "/Staff";

const Staff = () => {
    const StaffIDRef = useRef();
    const StaffNameRef = useRef();
    const StaffEmailRef = useRef();
    const StaffPasswordRef = useRef();

    const [StaffID, setStaffID] = useState("");
    const [StaffName, setStaffName] = useState("");
    const [StaffEmail, setStaffEmail] = useState("");
    const [StaffPassword, setStaffPassword] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [success, setSuccess] = useState(false);
    const [showAddForm, setShowAddButton] = useState(false);
    const [Staff, setStaff] = useState([]);

    useEffect(() => {
        handleDisplay(); // Fetch staff members when component mounts
    }, []);

    useEffect(() => {
        StaffIDRef.current && StaffIDRef.current.focus();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [StaffID, StaffName, StaffEmail, StaffPassword]);

    const handleAdd = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(
                STAFF_URL,
                {
                    StaffID: StaffID,
                    StaffName: StaffName,
                    StaffEmail: StaffEmail,
                    StaffPassword: StaffPassword,
                }
            );
            setSuccess(true);
            console.log(response.data.message);
            setStaffID("");
            setStaffName("");
            setStaffEmail("");
            setStaffPassword("");
            setShowAddButton(false);
            handleDisplay();
        } catch (err) {
            if (err.response) {
                if(err.response.status === 409){
                    setErrMsg('User already exists');
                }else{
                    setErrMsg('Registration failed');
                }    
            }
            if(StaffID === ""){
                StaffIDRef.current.focus();
            }else if(StaffName === ""){
                StaffNameRef.current.focus();
            }else if(StaffEmail === ""){
                StaffEmailRef.current.focus();
            }else{
                StaffPasswordRef.current.focus();
            }
        }
    }
    
    const handleDisplay = async () => { 
        try {
            const response = await axios.get(STAFF_URL);
            setStaff(response.data);
        } catch (err) {
            console.log(err);
        }
    }

    const handleDelete = async (StaffID) => {
        try {
            const response = await axios.delete(`/Staff1/${StaffID}`);
            console.log(response.data.message);
            handleDisplay();
        } catch (err) {
            console.log(err);
        }
    }
    

    return (
        <section>            
            <h1 className="header">Restaurant's Management</h1>
            <h2 className="title">Employee Register</h2>
            <button className="checkout-btn" onClick={() => setShowAddButton(true)}>Hire</button>
            {showAddForm && (
                <div>
                <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
                    {errMsg}
                </p>
                <form className="content" onSubmit={handleAdd}>
                <br/>
                <label htmlFor="StaffID"> StaffID: </label>
                <input
                    type="text"
                    id="StaffID"
                    ref={StaffIDRef}
                    value={StaffID}
                    onChange={(event) => setStaffID(event.target.value)}
                    required
                />
                <br />
                <br />
                <label htmlFor="StaffName"> Name: </label>
                <input
                    type="text"
                    id="StaffName"
                    ref={StaffNameRef}
                    value={StaffName}
                    onChange={(event) => setStaffName(event.target.value)}
                    required
                />
                <br />  
                <br />
                <label htmlFor="StaffEmail"> E-mail: </label>
                <input
                    type="text"
                    id="StaffEmail"
                    ref={StaffEmailRef}
                    value={StaffEmail}
                    onChange={(event) => setStaffEmail(event.target.value)}
                    required
                />
                <br />
                <br />
                <label htmlFor="StaffPassword"> Password: </label>
                <input
                    type="password"
                    id="StaffPassword"
                    ref={StaffPasswordRef}
                    value={StaffPassword}
                    onChange={(event) => setStaffPassword(event.target.value)}
                    required
                />
                <br />
                <br />
                <button className="checkout-btn" type="submit">
                    Add Employee
                </button>
                </form>
            </div>   
            )}
            <br /> 
            <br />
            <table className = "table">
                <thead>
                    <tr>
                        <th>Staff ID</th>
                        <th>Staff Name</th>
                        <th>Staff E-mail</th>
                        <th>Staff Password</th>
                        <th>Fire</th>
                    </tr>
                </thead>
                <tbody>
                    {Staff.map((employee, index) => (
                        <tr key={employee.StaffID}>
                            <td>{employee.StaffID}</td>
                            <td>{employee.StaffName}</td>
                            <td>{employee.StaffEmail}</td>
                            <td>{employee.StaffPassword}</td>
                            <td>
                                <button className="checkout-btn" onClick={() => handleDelete(employee.StaffID)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </section>
    )
}

export default Staff;