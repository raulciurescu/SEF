



const StaffHome = () => {

    return (
            <>
                {(
                    <section>
                        
                        <br />
                            <div className="title">
                                <h2>Staff Home</h2>
                                <br />
                                <br />
                                <button className="button" type="submit" onClick={() => window.location.href = "/MyOrders"}>
                                    My Orders
                                </button> 
                                <br/>
                                <br/>
                                <button className="button" type="submit" onClick={() => window.location.href = "/AllOrders"}>
                                    All Orders
                                </button>
                            </div>
                    </section>
                    )}
            </>
    )
}

export default StaffHome;