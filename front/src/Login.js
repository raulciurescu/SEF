/* eslint-disable no-restricted-globals */
import React, { useRef, useState, useEffect, useContext } from "react";
import AuthContext from "./context/AuthProvider";
import { Link , useNavigate } from "react-router-dom";
import axios from "./api/axios";

/* eslint-enable no-restricted-globals */

const LOGIN_URL = "/Login";
let path = "/Dashboard";

const Login = () => {
  const { setAuth } = useContext(AuthContext);
  const emailInputRef = useRef();
  const passwordInputRef = useRef();
  const navigate = useNavigate(); // Use useHistory hook

  const [email, setEmail] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    emailInputRef.current.focus();
  }, []);

  useEffect(() => {
    setErrMsg("");
  }, [email, pwd]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = axios.post(
        LOGIN_URL,{
          email: email, 
          pwd: pwd
        }
      );
      console.log("Response from backend:", (await response).data.message);
      if(response.data.message === "Staff"){
        path = "/DashboardStaff";
        navigate("/DashboardStaff");
      }else if(response.data.message === "Manager"){
        path = "/Dashboard";
        navigate("/Dashboard");
      }
      setEmail("");
      setPwd("");
      setSuccess(true);
    } catch (err) {
      if (err.response) {
        if (err.response.status === 401) {
          setErrMsg("Invalid credentials");
        } else if (err.response.status === 400) {
          setErrMsg("Missing credentials");
        } else {
          setErrMsg("Login failed. Please try again.");
        }
      } 
      if (email === "") {
        emailInputRef.current.focus();
      } else if(pwd === ""){
        passwordInputRef.current.focus();
      }
    }
  };
  
  if (success) {
    return (
      <section>
        <h1 className="header">Restaurant's Management</h1>
        <h2 className="title">Sign In Successful</h2>
        <br />
        <Link to={path}>
          <button className="button">Go to Dashboard</button>
        </Link>
      </section>
    );
  }

  return (
    <>
      {(
        <section>
          <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
            {errMsg}
          </p>
          <h1 className="header">Restaurant's Management</h1>
          <br />
          <div className="title">
            <h2>Login</h2>
            <br />
            <form className="content" onSubmit={handleSubmit}>
              <br />
              <label htmlFor="email"> E-mail: </label>
              <input
                type="text"
                id="email"
                autoComplete="off"
                onChange={(e) => setEmail(e.target.value)}
                value={email}
                required
                ref={emailInputRef}
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
              <button className="button">
                Login
              </button>
            </form>
          </div>
        </section>
      )}
    </>
  );
};

export default Login;
