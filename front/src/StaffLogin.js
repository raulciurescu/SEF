import React, { useRef, useState, useEffect, useContext } from "react";
import AuthContext from "./context/AuthProvider";
import { Link } from "react-router-dom";
import axios from "./api/axios";
const LOGIN_URL = "/auth";

const StaffLogin = () => {
    const { setAuth } = useContext(AuthContext);
    const nameInputRef = useRef();
    const passwordInputRef = useRef();

    const [name, setName] = useState("");
    const [pwd, setPwd] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        nameInputRef.current.focus();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [name, pwd]);

    const handleSubmit = async (e) => {
        e.preventDefault(); 
        try {
            const response = await axios.post(LOGIN_URL,
                JSON.stringify({name, pwd }),
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                    withCredentials: true,
                }
            );
            console.log(JSON.stringify(response?.data));
            const accessToken = response?.data?.accessToken;
            const roles = response?.data?.roles;
            setAuth({name, pwd, roles, accessToken });
            setName("");
            setPwd("");
            setSuccess(true);    
        } catch (err) {
            if (!err.response) {
                setErrMsg("No server response");
            } else if (err.response.status === 401) {
                setErrMsg("Invalid credentials");
            } else if (err.response.status === 400) {
                setErrMsg("Missing credentials");
            } else {
                setErrMsg("Login failed. Please try again.");
            }
            if (name === "") {
                nameInputRef.current.focus();
            } else {
                passwordInputRef.current.focus();
            }
        }
    }

    return (
        <>  
            {success ? (
                <section>
                    <h1>Sign In Successful</h1>
                    <br />
                    <p>
                        <a href="#">Go to home</a>
                    </p>
                </section>
            ) : (
                <section>
                    <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1 className="header">Restaurant's Management</h1>
                    <br/>
                    <div className="title">
                        <h2>Staff Login</h2>
                        <br />
                        <form className="content" onSubmit={handleSubmit}>
                            <label htmlFor="name"> Name: </label> 
                            <input
                                type="text"
                                id="name"
                                autoComplete="off"
                                onChange={(e) => setName(e.target.value)}
                                value={name}
                                required
                                ref={nameInputRef}
                            />
                            <br />
                            <br />
                            <label htmlFor="password"> Password: </label>
                            <input
                                type="password"
                                id="password"
                                onChange={(e) => setPwd(e.target.value)}
                                value={pwd}
                                required
                                ref={passwordInputRef}
                            />
                            <br />
                            <br />
                            <button className="button" type="submit">Login</button> 
                        </form>
                    </div>    
                </section>
            )}
        </>
    );
}

export default StaffLogin;
