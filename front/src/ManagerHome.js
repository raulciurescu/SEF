


const ManagerHome = () => {

        return (
                <>
                    {(
                        <section>
                        
                        <br />
                            <div className="title">
                                <h2>Manager Home</h2>
                                <br />
                                <br />
                                <button className="button" type="submit" onClick={() => window.location.href = "/Menu"}>
                                    Menu  
                                </button> 
                                <br/>
                                <br/>
                                <button className="button" type="submit" onClick={() => window.location.href = "/Staff"}>
                                    Staff
                                </button>
                            </div>
                    </section>
                        )}
                </>
        )
}

export default ManagerHome;