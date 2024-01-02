import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import LineInfo from "./LineInfo/LineInfo";
import "./AnalyticsPage.css";
// import logo from "../../../assets/facebook.png";

const AnalyticsPage = () => {
    const { handle } = useParams();
    const [account, setAccount] = useState({
        name : "Test",
        handle : "@test" ,
        profileImgURL : "https://pbs.twimg.com/profile_images/1676507105057021953/_Q05LEcB_400x400.jpg" ,
        follow : 0 ,
        unfollow : 0 ,
        tweets : 0 ,
        replies : 0 ,
        messages : 0 ,
    });

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
                            {account ? (
                                <>
                                    <img
                                        className="img-fluid"
                                        src={account.profileImgURL}
                                        alt=""
                                        id="account-img-as-logo"
                                    />
                                    <h1 className="card-title h1" id="name">
                                        {account.name}
                                    </h1>
                                    <h2 className="card-title h3" id="handle">
                                        {account.handle}
                                    </h2>
                                </>
                            ) : (
                                <h2 className="card-title h3" id="handle">
                                    Not Found {handle}
                                </h2>
                            )}
                        </div>
                        {account ? (
                            <div className="container" id="analytics-container">
                                <LineInfo
                                    title="Tweets"
                                    value={account.tweets}
                                    hasButton={true}
                                    target = {account.handle}
                                    key={Math.random()}
                                />
                                <LineInfo
                                    title="Replies"
                                    value={account.replies}
                                    hasButton={true}
                                    target = {account.handle}
                                    key={Math.random()}
                                />
                                <LineInfo
                                    title="Follow"
                                    value={account.follow}
                                    key={Math.random()}
                                />
                                <LineInfo
                                    title="UnFollow"
                                    value={account.unfollow}
                                    key={Math.random()}
                                />
                                <LineInfo
                                    title="Messages"
                                    value={account.messages}
                                    key={Math.random()}
                                />
                                <LineInfo
                                    title="Tweets & Replies"
                                    value={account.follow + account.unfollow}
                                    key={Math.random()}
                                />
                            </div>
                        ) : null}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AnalyticsPage;
