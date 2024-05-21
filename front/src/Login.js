import React, { useRef, useState, useEffect } from "react";
import { Link, useNavigate , Redirect} from "react-router-dom";
import axios from "./api/axios";

let path = "/ManagerHome";

const Login = () => {
  const emailInputRef = useRef();
  const passwordInputRef = useRef();

  const navigate = useNavigate();

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

  const handleLogin = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(
        "/Login",
        {
          email: email,
          pwd: pwd,
        }
      );
      setSuccess(true);
      console.log(response.data.message);
      console.log(response.data);
      setEmail("");
      setPwd("");

      if (response.data.message === "Manager") {
        path = "/ManagerHome";
      } else if (response.data.message === "Staff") {
        path = "/StaffHome";
      }
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
      } else {
        passwordInputRef.current.focus();
      }
    }
  };

  if(success){
    window.location.href = path;
  }
  return (
    <section>
      <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
        {errMsg}
      </p>
      <h1 className="header">Restaurant's Management</h1>
      <div className="title">
        <h2>Log In</h2>
        <form className="content" onSubmit={handleLogin}>
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
          <button className="button" type="submit">
            Login
          </button>
          
        </form>
      </div>
    </section>
  );
};

export default Login;
