import React, { useEffect, useState } from "react";

const Popup = (props) => {
    const { name , target } = props;
    const [isShowed, setIsShowed] = useState(false);
    const [legacies, setLegacies] = useState(null);

    const onClickShowInfoHandler = () => setIsShowed(!isShowed);

    // set legacies from endpoint
    useEffect(() => {
        // endpoint here
        

    });

    return (
        <>
            <button
                className="btn btn-outline-secondary col"
                type="button"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasWithBothOptions"
                aria-controls="offcanvasWithBothOptions"
                onClick={onClickShowInfoHandler}
                style={{
                    minWidth: "100px",
                    maxWidth: "200px",
                    marginLeft: "250px",
                }}
            >
                Show {name}
            </button>
            {isShowed ? (
                <>
                    <div
                        className="offcanvas offcanvas-start show"
                        data-bs-scroll="true"
                        tabIndex={-1}
                        id="offcanvasWithBothOptions"
                        aria-labelledby="offcanvasWithBothOptionsLabel"
                        aria-modal="true"
                        role="dialog"
                        style={{ minWidth: "35vw" }}
                    >
                        <div
                            className="offcanvas-header text-center"
                            style={{
                                borderBottom: "1px gray solid",
                                marginBottom: "10px",
                            }}
                        >
                            <h5
                                className="offcanvas-title h3"
                                id="offcanvasWithBothOptionsLabel"
                            >
                                {name}
                            </h5>
                            <button
                                type="button"
                                className="btn-close"
                                data-bs-dismiss="offcanvas"
                                aria-label="Close"
                                onClick={onClickShowInfoHandler}
                            />
                        </div>

                        <div className="offcanvas-body">
                            {legacies ? (
                                // when legacies is null before loading endpoint
                                legacies.length === 0 ? (
                                    //*// When endpoint return empty list (no legacies)
                                    <div
                                        className="alert alert-warning"
                                        role="alert"
                                    >
                                        No {name} Found
                                    </div>
                                ) : null //*// set map loop here for show all tweets  -- TweetsCards Here --
                            ) : (
                                // When loading endpoint data
                                <div className="container text-center mt-5">
                                    <div
                                        className="spinner-border"
                                        role="status"
                                        style={{
                                            minWidth: "80px",
                                            minHeight: "80px",
                                        }}
                                    >
                                        <span className="visually-hidden">
                                            Loading...
                                        </span>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                    <div
                        className="offcanvas-backdrop fade show"
                        onClick={onClickShowInfoHandler}
                    />
                </>
            ) : null}
        </>
    );
};

export default Popup;
