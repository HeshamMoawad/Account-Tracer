import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import LineInfo from "./LineInfo/LineInfo";

import logo from "../../../assets/facebook.png";

const AnalyticsPage = () => {
    const { handle } = useParams();
    const [isExist, setIsExist] = useState(false);

    // for chack exist handle
    useEffect(() => {
        // endpoint here
    });

    // fetch account info
    useEffect(() => {
        // endpoint here
    });

    return (
        <div className="container text-left ">
            <div className="row">
                <div
                    className="card mx-auto shadow-lg"
                    style={{ minWidth: "400px" }}
                >
                    <div className="card-body">
                        <div className="container text-center">
                            {isExist ? (
                                <img className="img-fluid" src={logo} alt="" />
                            ) : null}
                            <h1 className="card-title h1">
                                {isExist ? handle : "Not Found " + handle}
                            </h1>
                            <br />
                        </div>
                        <div className="container">
                            <LineInfo
                                title="Tweets"
                                value={null}
                                hasButton={true}
                                key={Math.random()}
                            />
                            <LineInfo
                                title="Replies"
                                value={null}
                                hasButton={true}
                                key={Math.random()}
                            />
                            <LineInfo
                                title="Follow"
                                value={null}
                                key={Math.random()}
                            />
                            <LineInfo
                                title="UnFollow"
                                value={null}
                                key={Math.random()}
                            />
                            <LineInfo
                                title="Messages"
                                value={null}
                                key={Math.random()}
                            />
                            <LineInfo
                                title="Tweets & Replies"
                                value={null}
                                key={Math.random()}
                            />
                        </div>

                        {/* <div className="container text-center">
              <button className="btn btn-secondary">Refresh</button>
            </div> */}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AnalyticsPage;
