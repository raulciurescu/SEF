import React, { useRef, useState, useEffect } from "react";
import axios from "./api/axios";
import { Link } from "react-router-dom";

const MENUE_URL = "/Menu";  

const Menu = () => {
    const categoryRef = useRef();    
    const productNameRef = useRef();
    const DescriptionRef = useRef();
    const priceRef = useRef();

    const [Category, setCategory] = useState("");
    const [ProductName, setProductName] = useState("");
    const [Description, setDescription] = useState("");
    const [Price, setPrice] = useState("");
    const [errMsg, setErrMsg] = useState("");
    const [success, setSuccess] = useState(false);
    const [showAddForm, setShowAddForm] = useState(false);
    const [menuItems, setMenuItems] = useState([]);

    useEffect(() => {
        categoryRef.current && categoryRef.current.focus();
    }, []);

    useEffect(() => {
        setErrMsg("");
    }, [Category, ProductName, Description, Price]);

    useEffect(() => {
        handleDisplay();
    }, []); 

    const handleDisplay = async () => {
        try {
            const response = await axios.get(MENUE_URL);
            setMenuItems(response.data); 
        } catch (err) {
            console.log(err);
        }
    };

    const handleAdd = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post(
                MENUE_URL,
                {
                    Category: Category,
                    ProductName: ProductName,
                    Description: Description,
                    Price: Price,
                }
            );
            setSuccess(true);
            console.log(response.data.message);
            setCategory("");
            setProductName("");
            setDescription("");
            setPrice("");
            setSuccess(true);
            setShowAddForm(false);
            handleDisplay();
        } catch (err) { 

            if (err.response) {
                    setErrMsg("Add failed. Please try again.");
                }
            if (Category === "") {
                categoryRef.current && categoryRef.current.focus();
            } else if (ProductName === "") {
                productNameRef.current && productNameRef.current.focus();
            } else if (Price === "") {
                priceRef.current && priceRef.current.focus();
            }
        }
    };

    const handleDelete = async (id) => {
        try {
            const response = await axios.delete(`/Menu1/${id}`);
            console.log(response.data.message);
            handleDisplay();
        } catch (err) {
            console.log(err);
        }
    }

    return (
            <section>
                <h1 className="header">Restaurant's Management</h1>
                <div className="title">
                <h2>Menu</h2>
                <button className="button" onClick={() => setShowAddForm(true)}>+</button>
                {showAddForm && (
                    <div>
                        <p className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">
                            {errMsg}
                        </p>
                        <form className="content" onSubmit={handleAdd}>
                        <br/>
                        <label htmlFor="category"> Category: </label>
                        <input
                            type="text"
                            id="category"
                            ref={categoryRef}
                            value={Category}
                            onChange={(event) => setCategory(event.target.value)}
                            required
                        />
                        <br />
                        <br />
                        <label htmlFor="productName"> Product Name: </label>
                        <input
                            type="text"
                            id="productName"
                            ref={productNameRef}
                            value={ProductName}
                            onChange={(event) => setProductName(event.target.value)}
                            required
                        />
                        <br />  
                        <br />
                        <label htmlFor="Description"> Description: </label>
                        <input
                            type="text"
                            id="Description"
                            ref={DescriptionRef}
                            value={Description}
                            onChange={(event) => setDescription(event.target.value)}
                        />
                        <br />
                        <br />
                        <label htmlFor="price"> Price: </label>
                        <input
                            type="text"
                            id="price"
                            ref={priceRef}
                            value={Price}
                            onChange={(event) => setPrice(event.target.value)}
                            required
                        />
                        <br />
                        <br />
                        <button className="button" type="submit">
                            Add Dish
                        </button>
                        </form>
                    </div>   
                )}
                <br /> 
                <br />
                <table className = "table">
                    <thead>
                        <tr>
                            <th>Category</th>
                            <th>Product Name</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Remove</th>
                        </tr>
                    </thead>
                    <tbody>
                        {menuItems.map((item, index) => (
                            <tr key={item._id}>
                                <td>{item.Category}</td>
                                <td>{item.ProductName}</td>
                                <td>{item.Description}</td>
                                <td>{item.Price}</td>
                                <td>
                                    <button className="button" onClick={() => handleDelete(item._id)}>-</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>

            </div>
        </section>
    );
};



export default Menu;