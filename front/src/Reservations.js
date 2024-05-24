import React, { useState, useEffect } from "react";
import axios from "./api/axios";

const RES_URL = "/Reservations";
const UPDATE_RES_URL = "/UpdateReservation";

const Reservations = () => {
    const [resItems, setResItems] = useState([]);
    const [errMsg, setErrMsg] = useState("");
    const [refresh, setRefresh] = useState(false); // State to trigger data refresh

    useEffect(() => {
        const fetchReservations = async () => {
            try {
                const response = await axios.get(RES_URL);
                setResItems(response.data);
            } catch (error) {
                setErrMsg("Failed to fetch reservations");
                console.error(error);
            }
        };

        fetchReservations();
    }, [refresh]); // Refetch data when 'refresh' state changes

    const handleConfirm = async (id) => {
        try {
            await axios.put(`${RES_URL}/${id}`, {
                ReservationStatus: "Confirmed"
            });
            // Trigger a data refresh after updating the status
            setRefresh(prev => !prev);
        } catch (error) {
            setErrMsg("Failed to update reservation status");
            console.error(error);
        }
    };

    return (
        <section>
            <h1 className="header">Restaurant's Management</h1>
            <div className="title">
                <h2>Reservations</h2>
                <br /> 
                <br />
                {errMsg && <p className="errmsg">{errMsg}</p>}
                <table className="table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Phone</th>
                            <th>Date</th>
                            <th>Time</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {resItems.map((item) => (
                            <tr key={item._id}>
                                <td>{item.ReservationName}</td>
                                <td>{item.ReservationPhone}</td>
                                <td>{item.ReservationDate}</td>
                                <td>{item.ReservationTime}</td>
                                <td>{item.ReservationStatus}</td>
                                <td>
                                    <button
                                        className="button"
                                        onClick={() => handleConfirm(item._id)}
                                        disabled={item.ReservationStatus === "Confirmed"}
                                    >
                                        ✓
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </section>
    );
};

export default Reservations;